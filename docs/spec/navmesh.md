---
title: "Navmesh (map/navi/ZPxx_zz_00.nav) and the tutorial spawn"
---

# Navmesh (map/navi/ZPxx_zz_00.nav) and the tutorial spawn

Tool: `~/Vaults/Overview/Worklab/WarmongerRevamp/tools/navmesh.py` (stdlib only):
`check <x> <z>`, `sample <segX> <segZ> [step]`, `info <segX> <segZ>`. Its docstring repeats
the format below. Extracted files: `data/map/map/navi/ZP05_01_00.nav`,
`ZP10_01_00.nav`, `naviSystem.cfg`, and `data/map/map/ZP05_01_00.zp`, `ZP10_01_00.zp`.

## Result

- **Recommended tutorial spawn: map 117, x = 1427.0, z = 429.0** (ZP05_01, inside zone 2
  tutorial_map_01). The mesh face there is at height 256.03 and the terrain at 256.00. The
  nearest mesh edge is 10.8 units away, the most open spot within 15 units of the old point.
  Alternative inside zone 107 "tutorial zone (01)": (1388, 394), 9.9 units from an edge.
- **Why (1424, 416) is stuck:** it is **exactly a mesh vertex on the boundary**, the corner of a
  16×8-unit hole in the mesh (x 1408..1424, z 410..418, probably an obstacle/prop). Boundary
  edges there: (1424,416)-(1424,418), (1424,416)-(1426,416). A point on the boundary is
  degenerate for PathEngine's point-in-face test. The client's `positionFor3DPoint` returns an
  invalid cell, so `FUN_00452d26` fails and the stuck detector fires. The click target
  (1438, 435) is also exactly on a boundary edge (the east rim of that area). Both look like
  ZoneDB rectangle centres or round numbers, not points designed to be stood on.
- **Village sanity check passes:** (2688.8, 382.9) is on the ZP10_01 mesh, face height 253.87 vs
  terrain 253.88, 12.3 units from the nearest edge.
- **The data defines no tutorial start point.** No row in Teleport_List.cdb (fields 88..101, 119
  only, no 117), Trigger.cdb, SceneList.cdb, Dungeon/DungeonAdmission.cdb or Create_Char.cdb
  has a position in segment ZP05_01 or names field 117 with coordinates. The ZP05_01 .zp lists
  water patches (u16 chunk x,z + f32 level 240..250) but no spawn marker. NPC/start placement
  was presumably server-side. ZoneTable.dat (256 KiB) is not a world walkability grid: it is
  loaded with tag 0x10000 and its byte histogram does not match the zone rectangles. It was not
  decoded further.

Confidence:
- format, scale and centre mapping: high. Mesh heights match the independently decoded terrain
  heightmap to a median of 0.02–0.03 units over hundreds of random points in both segments.
- that (1427, 429) clears the client check: high.
- that the boundary vertex is the whole cause of the stuck state: medium-high. It is the only
  difference found between the two spots, and everything else (tile loaded, checksum, heights)
  is identical in kind to the working Village.

Walkable area of ZP05_01 (2-unit cells, `#` = mesh, P = old spawn (1424,416), T = click (1438,434),
x 1344→1494 left to right, z 456 top → 382 bottom):

```
440 ..#############....................########.................................
434 .#############...................##############T...............##########...
428 .###########.......................#############...............###########..
422 .#.###########....................################..............########....
418 ...........####................#.####.###############..........######.......
416 ............####..............#.###.....P#####.######.........######........
410 ...............####..........####....................######..#######........
400 .................#############....##.....................#########..........
392 ................################.........................########...........
384 ................###############.............................................
```

The whole mesh spans x 1346..1492 and z 382..454. It has 656 vertices and 691 faces and is
small: an island plus walkways.

## Client side

- Loader: `FUN_004a33dc` / load-job step 8 builds `map/navi/ZP%02d_%02d_00.%s` from the piece's
  segment (`piece+0x413c8/ca`). Step 9 hands the buffer to `FUN_004523e5` → `FUN_0050eacc`
  (PathEngine federation tile load). The returned checksum is compared with the value stored
  in the .zp header (zp +0x164 = nav +0x08: 0x56431d70 for ZP05_01, 0x55000b12 for ZP10_01; both
  match).
- Walkability query `FUN_00452d26(x100, z100, y100)`:
  - tile = `FUN_00452746`: `x/tileSize + (z/tileSize)*tilesX` (tileSize 25600, tilesX 21);
  - mesh = `FUN_0045277c(tile)` (slot table at +0x275c, < 10000). No mesh → fail;
  - centre = `FUN_004528bd` (federation vtable +0x14, tile centre);
  - `mesh->positionFor3DPoint({x-cx, z-cz, y+50})` (vtable +0x58). Cell −1 → fail.
- Caller `FUN_0048d666` (stuck detector): the unit position (sector + local) → absolute world
  (`FUN_0049b7f6`: sector*256 + local) → ×100 (`ftol`, constant 100.0 at 0x7267d0) → order
  (x, z, height). On failure it waits about 5 s, sends 0x416 type 1, then waits 30 s.
- Player height: terrain heightmap `FUN_004589aa` → `FUN_00457b98`. It is bilinear on a 129×129
  float grid (2 units/cell) at piece+0x10584, loaded from u16 × 1024/65535 (constant at
  0x727e88). The grid sits at the file offset in zp +0x178 (and a second, identical grid at
  zp +0x14). Holes come from a sorted list (`FUN_00457a3b`); ZP05_01 has none.

## .nav file format

```
+0x00 u32 100 (tag; naviSystem.cfg starts with the same 100, 0x24, 21, 21, 1, 0, 1, 0, 0)
+0x04 u32 file size        +0x08 u32 checksum (copied into the .zp header)
+0x0c u32 tilesX=21  +0x10 u32 tilesY=21  +0x14 u32 1  +0x18 u32 0  +0x1c u32 1
+0x20 u32 0x24 (header size)
+0x24 3 × {u32 size, u32 offset}: chunk0 = ground mesh (tokenised XML) at 0x3c,
      chunk1/chunk2 = PathEngine preprocess (collision/pathfind) blobs, not decoded
```

Chunk 0 is PathEngine tokenised XML:
- element names: C strings, ended by an empty string. Here: mesh, mesh3D, verts, vert, tris,
  tri, tiledCPFaceIndexTranslator2, startFacePerTile, collapsedBuffer, indices;
- attributes: `{u8 type, C string}`, ended by 0. Type 3 = s16 and type 4 = s8. Here:
  majorRelease, minorRelease, x, y, z, sectionID, userData, edge0..2StartVert, surfaceType,
  edge0..2Connection, edge0..2StartZ, federationTileIndex, startX, startY, tileSize,
  beginTileX, beginTileY, endTileX;
- body: `u8 element (1-based)`, `{u8 attr (1-based), value}*`, `0`, children, `0` (close).
  0xFF starts a raw buffer (startFacePerTile…). Everything needed comes before it.

Content: `<mesh majorRelease=5 minorRelease=27><mesh3D><verts><vert x y z/>…</verts><tris><tri
edge0StartVert edge1StartVert edge2StartVert [edgeNConnection] [edgeNStartZ] [sectionID]
[surfaceType] [userData]/>…</tris></mesh3D><tiledCPFaceIndexTranslator2 federationTileIndex=26
startX=0 startY=0 tileSize=25600 beginTileX=5 beginTileY=1 endTileX=6>…`

Coordinates: PathEngine units = world × 100. Vertices are relative to the **tile centre**:
`world x = segX*256 + 128 + vx/100`, `world z = segZ*256 + 128 + vy/100`, `height = vz/100`.
A point is on the mesh when it lies inside a tri's (x, y) triangle. navmesh.py also requires
it to be more than 0.05 units from a boundary edge (an edge used by only one tri).

## Server action (not applied; server/ untouched)

In `server/handlers.py` set `TUTORIAL = (117, 1427.0, 429.0)`. Answer 0x416 type-1 resyncs with
that point too, not with a point on the mesh edge. Check any future hand-picked spawn with
`navmesh.py check x z` and keep it at least about 2 units from an edge (the agent radius).
