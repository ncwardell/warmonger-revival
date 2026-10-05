#!/usr/bin/env python3
"""Warmonger navmesh (map/navi/ZPxx_zz_00.nav) reader and walkability test.

The client uses PathEngine (error prefix "P.E.ERROR", a mesh federation of
21 x 21 tiles). Each .nav file is ONE federation tile = one 256-unit terrain
segment ZPxx_zz.

File layout (all little-endian):

  +0x00 u32 100            format/version tag (naviSystem.cfg starts the same)
  +0x04 u32 file size
  +0x08 u32 checksum       also stored in the matching Map/ZPxx_zz_00.zp header
                           (zp +0x164); the client compares them after loading
  +0x0c u32 tilesX = 21, +0x10 u32 tilesY = 21, +0x14 u32 1, +0x18 u32 0,
  +0x1c u32 1 (tiles per file side)
  +0x20 u32 0x24 = header size, then 3 chunk records {u32 size, u32 offset}:
        chunk 0 at 0x3c  = the ground mesh (PathEngine tokenised XML, below)
        chunk 1, chunk 2 = PathEngine preprocess blobs (not decoded; not needed)

Chunk 0 is PathEngine "tok" (tokenised XML):
  element-name table: NUL-terminated strings, ended by an empty string
      (mesh, mesh3D, verts, vert, tris, tri, tiledCPFaceIndexTranslator2, ...)
  attribute table: {u8 type, NUL-terminated name}..., ended by a 0 byte.
      type 3 = s16, type 4 = s8 (only these occur in the mesh part)
  body: element = u8 (1-based element index), then {u8 1-based attr index,
      value}... ended by 0, then children, then 0 closes the element.
      An 0xFF token starts a raw buffer (startFacePerTile/collapsedBuffer);
      the reader stops there: everything needed is before it.

  <mesh majorRelease=5 minorRelease=27>
    <mesh3D>
      <verts> <vert x y z/>...   (s16, PathEngine units)
      <tris>  <tri edge0StartVert edge1StartVert edge2StartVert
                   [edgeNConnection] [edgeNStartZ] [sectionID] [surfaceType]
                   [userData]/>...
    <tiledCPFaceIndexTranslator2 federationTileIndex startX startY tileSize
                                 beginTileX beginTileY endTileX ...>

Coordinate mapping (from the client, FUN_0048d666 -> FUN_00452d26):
  PathEngine x = world x * 100, PathEngine y = world z * 100,
  PathEngine z (height) = world y * 100   (constant 100.0 at 0x7267d0)
  tile index = x/25600 + (y/25600)*21  (FUN_00452746; tileSize = 25600)
  vertex coords are relative to the tile CENTRE (FUN_004528bd -> tile
  centre), i.e. world = seg*256 + 128 + v/100.

The client's "is the player on the navmesh" test (FUN_00452d26) is
mesh->positionFor3DPoint(x, y, height*100 + 50): it succeeds when a mesh
face lies under the point at or below 0.5 units above the player. The
player's height comes from the terrain heightmap (Map/ZPxx_zz_00.zp: 129x129
u16 grid, 2 units per cell, h = v * 1024/65535; offset at zp +0x178), which
this tool also reads (terrain_height) when the .zp is extracted.

Usage:
  navmesh.py check <x> <z>            walkable? (face height, terrain height,
                                      distance to the nearest mesh edge)
  navmesh.py sample <segX> <segZ> [step]   walkable points on a grid (+edge dist)
  navmesh.py info <segX> <segZ>       mesh bounds and counts
Files are read from $NAVDIR (default $WARMONGER_DATA/map/map/navi) and
$ZPDIR (default $WARMONGER_DATA/map/map; WARMONGER_DATA defaults to ./data);
extract them with
  tools/jpk.py extract Data/map.jpk data/map 'map/navi/ZP05_01*'
"""
import os
import struct
import sys

SEG = 256
SCALE = 100
EDGE_EPS = 0.05  # points closer than this to a boundary edge count as off-mesh
DATA = os.environ.get("WARMONGER_DATA", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data"))
NAVDIR = os.environ.get("NAVDIR", os.path.join(DATA, "map", "map", "navi"))
ZPDIR = os.environ.get("ZPDIR", os.path.join(DATA, "map", "map"))
_cache = {}


def parse_nav(data):
    """Return (verts [(x,y,z)], tris [dict], tile dict) from a .nav file."""
    hdr = struct.unpack_from("<9I", data, 0)
    if hdr[0] != 100:
        raise ValueError("not a navmesh (tag %d)" % hdr[0])
    size, off = struct.unpack_from("<II", data, 0x24)
    p, end = off, off + size

    def cstr(p):
        e = data.index(b"\0", p)
        return data[p:e].decode("latin1"), e + 1

    elements, attrs = [], []
    while data[p]:
        s, p = cstr(p)
        elements.append(s)
    p += 1
    while data[p]:
        t = data[p]
        s, p = cstr(p + 1)
        attrs.append((t, s))
    p += 1
    fmt = {3: ("<h", 2), 4: ("<b", 1)}
    verts, tris, tile, depth = [], [], {}, 0
    while p < end:
        e = data[p]
        p += 1
        if e == 0:
            depth -= 1
            if depth <= 0:
                break
            continue
        if e > len(elements):  # 0xFF raw buffer: nothing after it is needed
            break
        name, a = elements[e - 1], {}
        while True:
            k = data[p]
            p += 1
            if not k:
                break
            t, an = attrs[k - 1]
            f, n = fmt[t]
            a[an] = struct.unpack_from(f, data, p)[0]
            p += n
        depth += 1
        if name == "vert":
            verts.append((a["x"], a["y"], a["z"]))
        elif name == "tri":
            tris.append(a)
        elif name.startswith("tiledCPFaceIndexTranslator"):
            tile = a
    return verts, tris, tile


def load(sx, sz):
    key = (sx, sz)
    if key not in _cache:
        fn = os.path.join(NAVDIR, "ZP%02d_%02d_00.nav" % (sx, sz))
        if not os.path.exists(fn):
            _cache[key] = None
        else:
            v, t, tile = parse_nav(open(fn, "rb").read())
            faces = []
            for f in t:
                a, b, c = (v[f["edge%dStartVert" % i]] for i in range(3))
                faces.append((a, b, c, f))
            _cache[key] = (v, faces, tile)
    return _cache[key]


def terrain_height(x, z):
    """Bilinear terrain height (world units) from the .zp heightmap, or None."""
    sx, sz = int(x // SEG), int(z // SEG)
    fn = os.path.join(ZPDIR, "ZP%02d_%02d_00.zp" % (sx, sz))
    if not os.path.exists(fn):
        return None
    d = open(fn, "rb").read()
    off = struct.unpack_from("<I", d, 0x178)[0]
    g = struct.unpack_from("<16641H", d, off)
    lx, lz = (x - sx * SEG) / 2, (z - sz * SEG) / 2
    ix, iz = min(int(lx), 127), min(int(lz), 127)
    fx, fz = lx - ix, lz - iz
    h = lambda i, j: g[j * 129 + i] * 1024 / 65535
    return ((h(ix, iz) * (1 - fx) + h(ix + 1, iz) * fx) * (1 - fz)
            + (h(ix, iz + 1) * (1 - fx) + h(ix + 1, iz + 1) * fx) * fz)


def faces_at(x, z):
    """Mesh faces under world (x, z): list of (height, face attrs)."""
    sx, sz = int(x // SEG), int(z // SEG)
    m = load(sx, sz)
    if m is None:
        return None
    _, faces, _ = m
    px = (x - (sx * SEG + SEG / 2)) * SCALE
    py = (z - (sz * SEG + SEG / 2)) * SCALE
    out = []
    for a, b, c, f in faces:
        d1 = (b[0] - a[0]) * (py - a[1]) - (b[1] - a[1]) * (px - a[0])
        d2 = (c[0] - b[0]) * (py - b[1]) - (c[1] - b[1]) * (px - b[0])
        d3 = (a[0] - c[0]) * (py - c[1]) - (a[1] - c[1]) * (px - c[0])
        if (d1 >= 0 and d2 >= 0 and d3 >= 0) or (d1 <= 0 and d2 <= 0 and d3 <= 0):
            den = (b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1])
            if den == 0:
                continue
            w1 = ((b[1] - c[1]) * (px - c[0]) + (c[0] - b[0]) * (py - c[1])) / den
            w2 = ((c[1] - a[1]) * (px - c[0]) + (a[0] - c[0]) * (py - c[1])) / den
            h = (w1 * a[2] + w2 * b[2] + (1 - w1 - w2) * c[2]) / SCALE
            out.append((h, f))
    return out


def walkable(x, z, y=None):
    """True if the client's positionFor3DPoint test would pass at (x, z).

    y defaults to the terrain height (what the client gives the player).
    A point lying on a boundary edge/vertex (e.g. the old tutorial spawn
    (1424, 416), which is a corner of a hole in the mesh) is reported as NOT
    walkable: PathEngine's point-in-face test is not inclusive there.
    """
    fs = faces_at(x, z)
    if not fs:
        return False
    if edge_distance(x, z) < EDGE_EPS:
        return False  # exactly on the mesh boundary: PathEngine may reject it
    if y is None:
        y = terrain_height(x, z)
    if y is None:
        return True
    return any(h <= y + 0.5 + 0.01 for h, _ in fs)


def boundary(sx, sz):
    """Mesh boundary edges (edges used by only one face), in world units."""
    m = load(sx, sz)
    key = ("edges", sx, sz)
    if key not in _cache:
        v, faces, _ = m
        cnt = {}
        for a, b, c, f in faces:
            ids = [f["edge%dStartVert" % i] for i in range(3)]
            for i in range(3):
                e = tuple(sorted((ids[i], ids[(i + 1) % 3])))
                cnt[e] = cnt.get(e, 0) + 1
        cx, cz = sx * SEG + SEG / 2, sz * SEG + SEG / 2
        w = lambda p: (cx + v[p][0] / SCALE, cz + v[p][1] / SCALE)
        _cache[key] = [(w(i), w(j)) for (i, j), n in cnt.items() if n == 1]
    return _cache[key]


def edge_distance(x, z):
    """Distance (world units) from (x, z) to the nearest navmesh boundary edge."""
    best = float("inf")
    for (ax, az), (bx, bz) in boundary(int(x // SEG), int(z // SEG)):
        dx, dz = bx - ax, bz - az
        L = dx * dx + dz * dz
        t = 0 if L == 0 else max(0, min(1, ((x - ax) * dx + (z - az) * dz) / L))
        px, pz = ax + t * dx - x, az + t * dz - z
        best = min(best, (px * px + pz * pz) ** 0.5)
    return best


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd = argv[1]
    if cmd == "check":
        x, z = float(argv[2]), float(argv[3])
        fs = faces_at(x, z)
        th = terrain_height(x, z)
        if fs is None:
            print("(%.2f, %.2f): no navmesh file for segment ZP%02d_%02d -> NOT walkable"
                  % (x, z, x // SEG, z // SEG))
            return 1
        ok = walkable(x, z)
        if not ok and fs and edge_distance(x, z) < EDGE_EPS:
            print("  (point lies exactly on a mesh boundary edge/vertex)")
        print("(%.2f, %.2f) seg ZP%02d_%02d: %s" % (x, z, x // SEG, z // SEG,
                                                    "WALKABLE" if ok else "NOT walkable"))
        for h, f in fs:
            print("  face height %.2f section %s" % (h, f.get("sectionID", 0)))
        if th is not None:
            print("  terrain height %.2f" % th)
        if ok:
            print("  nearest mesh edge %.2f units away" % edge_distance(x, z))
        return 0 if ok else 1
    if cmd in ("sample", "info"):
        sx, sz = int(argv[2]), int(argv[3])
        m = load(sx, sz)
        if m is None:
            print("no navmesh for ZP%02d_%02d" % (sx, sz))
            return 1
        v, faces, tile = m
        cx, cz = sx * SEG + SEG / 2, sz * SEG + SEG / 2
        xs, ys = [p[0] for p in v], [p[1] for p in v]
        print("ZP%02d_%02d: %d verts, %d faces, tile %s" % (sx, sz, len(v), len(faces), tile))
        print("world bounds x %.1f..%.1f z %.1f..%.1f" % (
            cx + min(xs) / SCALE, cx + max(xs) / SCALE, cz + min(ys) / SCALE, cz + max(ys) / SCALE))
        if cmd == "info":
            return 0
        step = float(argv[4]) if len(argv) > 4 else 8
        z = sz * SEG + step / 2
        while z < (sz + 1) * SEG:
            x = sx * SEG + step / 2
            while x < (sx + 1) * SEG:
                if walkable(x, z):
                    print("%.1f %.1f  edge %.1f" % (x, z, edge_distance(x, z)))
                x += step
            z += step
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
