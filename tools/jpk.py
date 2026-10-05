#!/usr/bin/env python3
"""List and extract the client's Data/*.jpk archives.

A .jpk is a Blizzard MPQ (format v1, StormLib of ~2005) with these tweaks:

  * magic "NPK\\x1a" instead of "MPQ\\x1a" ("NPK\\x1b" = user-data header);
  * block-flag bits 0x10000/0x20000 swapped: 0x20000 = ENCRYPTED,
    0x10000 = FIX_KEY (key = (key + block_offset) ^ file_size);
  * the per-sector compression byte is remapped:
      0x01 zlib   0x02 PKWARE implode   0x08 Huffman   0x80 bzip2
      0x10 / 0x40 IMA-ADPCM (mono / stereo)

Header (0x2c bytes, little-endian): magic, header_size=0x2c, archive_size,
version=1, sector_shift (sector = 0x200 << shift), hash_table_pos,
block_table_pos, hash_table_entries, block_table_entries, then the v1
64-bit extension (hi-block table pos, hash/block pos high words; all zero).

Hash table (16 bytes/entry: name_a, name_b, locale, platform, block_index)
and block table (16 bytes/entry: offset, packed_size, file_size, flags) are
encrypted with the standard MPQ cipher, keys hash("(hash table)") and
hash("(block table)"). A file's key is hash(basename, type 3), basename =
part after the last backslash. Files are split into sectors; a compressed
file starts with a sector-offset table encrypted with key-1, each sector
with key+index.

Names: each archive carries a listfile named "{listfile}" (not
"(listfile)"), which is learnt first and names every entry in the shipped
archives. As a fallback, candidates are hashed (built-in ZP patterns,
strings from --names files, paths inside the archive's text files), and an
unnamed file's key is recovered from its sector-offset table (known
plaintext), as the client does (Client.exe FUN_0067dac0). Unnamed entries
appear as "~unnamed/<block>.bin". Spec: docs/spec/jpk.md.

  jpk.py list <archive> [--names FILE ...]
  jpk.py extract <archive> <outdir> [glob] [--names FILE ...]
"""
import bz2
import fnmatch
import os
import re
import struct
import sys
import zlib

MAGIC = b"NPK\x1a"
F_IMPLODE, F_COMPRESS = 0x100, 0x200
F_FIXKEY, F_ENCRYPTED = 0x10000, 0x20000
F_SINGLE, F_EXISTS = 0x1000000, 0x80000000


def crypt_table():
    table, seed = [0] * 0x500, 0x00100001
    for i in range(256):
        for j in range(5):
            seed = (seed * 125 + 3) % 0x2AAAAB
            hi = (seed & 0xFFFF) << 16
            seed = (seed * 125 + 3) % 0x2AAAAB
            table[i + j * 256] = hi | (seed & 0xFFFF)
    return table


T = crypt_table()


def hash_name(name, kind):
    """MPQ string hash. kind 0=table index, 1/2=name check, 3=file key."""
    s1, s2 = 0x7FED7FED, 0xEEEEEEEE
    for c in name.upper().encode("latin-1"):
        s1 = (T[kind * 256 + c] ^ (s1 + s2)) & 0xFFFFFFFF
        s2 = (c + s1 + s2 + (s2 << 5) + 3) & 0xFFFFFFFF
    return s1


def decrypt(data, key):
    n = len(data) // 4
    words = struct.unpack("<%dI" % n, data[:n * 4])
    out, s2 = [], 0xEEEEEEEE
    for w in words:
        s2 = (s2 + T[0x400 + (key & 0xFF)]) & 0xFFFFFFFF
        p = w ^ ((key + s2) & 0xFFFFFFFF)
        out.append(p)
        key = ((((~key) << 21) + 0x11111111) | (key >> 11)) & 0xFFFFFFFF
        s2 = (p + s2 + (s2 << 5) + 3) & 0xFFFFFFFF
    return struct.pack("<%dI" % n, *out) + data[n * 4:]


def detect_key(enc, first):
    """Recover a sector table's key from its known first dword (the table
    size). Yields file keys (table key + 1), as Client.exe FUN_0067dac0."""
    e0, e1 = struct.unpack_from("<2I", enc)
    for i in range(256):
        key = ((e0 ^ first) - 0xEEEEEEEE - T[0x400 + i]) & 0xFFFFFFFF
        if key & 0xFF != i:
            continue
        d0, d1 = struct.unpack("<2I", decrypt(enc[:8], key))
        if d0 == first and d1 & 0xFFFF0000 == 0:
            yield (key + 1) & 0xFFFFFFFF


class Archive:
    def __init__(self, path):
        self.f = open(path, "rb")
        hdr = self.f.read(0x2C)
        if hdr[:4] != MAGIC:
            sys.exit("%s: not an NPK archive" % path)
        (_, _, self.size, self.version, shift, hpos, bpos,
         hcount, bcount) = struct.unpack_from("<4sIIHHIIII", hdr)
        self.sector = 0x200 << shift
        self.hashes = self.table(hpos, hcount, "(hash table)", "<IIHHI")
        self.blocks = self.table(bpos, bcount, "(block table)", "<IIII")
        self.names = {}  # block index -> name

    def table(self, pos, count, keyname, fmt):
        self.f.seek(pos)
        raw = decrypt(self.f.read(count * 16), hash_name(keyname, 3))
        return [struct.unpack_from(fmt, raw, i * 16) for i in range(count)]

    def lookup(self, name):
        a, b = hash_name(name, 1), hash_name(name, 2)
        n = len(self.hashes)
        i = start = hash_name(name, 0) % n
        while True:
            na, nb, _, _, block = self.hashes[i]
            if block == 0xFFFFFFFF:
                return None
            if na == a and nb == b and block < len(self.blocks):
                return block
            i = (i + 1) % n
            if i == start:
                return None

    def learn(self, candidates):
        """Hash candidate names; record the ones present. Returns new names."""
        known = {(h[0], h[1]) for h in self.hashes if h[4] < len(self.blocks)}
        found = []
        for name in candidates:
            name = name.replace("/", "\\")
            if (hash_name(name, 1), hash_name(name, 2)) not in known:
                continue
            block = self.lookup(name)
            if block is not None and block not in self.names:
                self.names[block] = name
                found.append(name)
        return found

    def read(self, block):
        offset, packed, size, flags = self.blocks[block]
        self.f.seek(offset)
        raw = self.f.read(packed)
        key = None
        if flags & F_ENCRYPTED and block in self.names:
            key = hash_name(self.names[block].rsplit("\\", 1)[-1], 3)
            if flags & F_FIXKEY:
                key = ((key + offset) ^ size) & 0xFFFFFFFF
        if flags & F_SINGLE or not flags & (F_IMPLODE | F_COMPRESS):
            if flags & F_ENCRYPTED and key is None:
                raise ValueError("encrypted uncompressed file needs its name")
            return self.read_plain(raw, size, flags, key)
        count = (size + self.sector - 1) // self.sector + 1
        keys = [key] if key is not None else (
            list(detect_key(raw, count * 4)) if flags & F_ENCRYPTED else [None])
        for k in keys:
            try:
                return self.read_sectors(raw, size, flags, k, count)
            except (ValueError, zlib.error, OSError, EOFError):
                continue
        raise ValueError("could not decode block %d" % block)

    def read_plain(self, raw, size, flags, key):
        if key is not None:
            raw = b"".join(decrypt(raw[i:i + self.sector], key + n)
                           for n, i in enumerate(range(0, len(raw), self.sector)))
        if flags & F_SINGLE and len(raw) < size:
            return decompress(raw, size)
        return raw[:size]

    def read_sectors(self, raw, size, flags, key, count):
        table = raw[:count * 4]
        if key is not None:
            table = decrypt(table, (key - 1) & 0xFFFFFFFF)
        offs = struct.unpack("<%dI" % count, table)
        if offs[0] != count * 4 or offs[-1] > len(raw):
            raise ValueError("bad sector table")
        out = bytearray()
        for n in range(count - 1):
            data = raw[offs[n]:offs[n + 1]]
            if key is not None:
                data = decrypt(data, (key + n) & 0xFFFFFFFF)
            want = min(self.sector, size - len(out))
            out += data if len(data) >= want else decompress(data, want)
        if len(out) != size:
            raise ValueError("size mismatch")
        return bytes(out)


def decompress(data, size):
    kind, body = data[0], data[1:]
    if kind == 0x01:
        return zlib.decompressobj().decompress(body)[:size]
    if kind == 0x80:
        return bz2.BZ2Decompressor().decompress(body)[:size]
    raise ValueError("unsupported compression 0x%02x" % kind)


def strings_in(data):
    """Path-like strings in a blob (ASCII and UTF-16LE)."""
    pat = rb"[\x20-\x7e]{4,260}"
    runs = re.findall(pat, data)
    runs += [r.decode("utf-16-le", "ignore").encode()
             for r in re.findall(rb"(?:[\x20-\x7e]\x00){4,260}", data)]
    out = set()
    for r in runs:
        for tok in re.split(r"[\s\"',;=<>|\t]+", r.decode("latin-1")):
            if "." in tok and len(tok) > 3:
                out.add(tok)
                for i, c in enumerate(tok):  # also every suffix after a slash
                    if c in "/\\":
                        out.add(tok[i + 1:])
    return out


def builtin_names():
    names = ["{attributes}", "{signature}", "(attributes)", "(signature)"]
    for x in range(100):
        for z in range(100):
            base = "ZP%02d_%02d_00" % (x, z)
            names.append("Map\\%s.zp" % base)
            names += ["Map\\navi\\%s.%s" % (base, e) for e in ("nav", "navi", "dat", "bin")]
    for z in range(200):
        names += ["Map\\fogmap\\Fog_z%d.dds" % z, "Map\\minimap\\minimap_z%d_00.dds" % z]
    return names


def with_prefixes(names, archive_path):
    """Archive-relative paths keep their top folder (Setting\\x.cdb), so also
    try every candidate under the archive's own name."""
    top = os.path.splitext(os.path.basename(archive_path))[0]
    out = set()
    for n in names:
        n = n.replace("/", "\\").lstrip("\\")
        out.add(n)
        out.add(top + "\\" + n)
        out.add(top.capitalize() + "\\" + n)
    return out


TEXTY = (".txt", ".csv", ".ini", ".cdb", ".xml", ".lst", ".list", ".panel", ".mo", ".scn")


LISTFILES = ("{listfile}", "(listfile)")


def resolve_names(arc, path, name_files):
    """The archive's own listfile is authoritative (and gives the canonical
    spelling), so learn it first; then guess the rest."""
    for lf in arc.learn(LISTFILES):
        lines = arc.read(arc.lookup(lf)).decode("latin-1").splitlines()
        arc.learn(l.strip() for l in lines if l.strip())
    cands = set(builtin_names())
    for nf in name_files:
        cands |= strings_in(open(nf, "rb").read())
    pending = arc.learn(sorted(with_prefixes(cands, path)))
    scanned = set()
    while pending:  # mine newly named text files for more names
        more = set()
        for block, name in list(arc.names.items()):
            if block in scanned or not name.lower().endswith(TEXTY):
                continue
            scanned.add(block)
            try:
                more |= strings_in(arc.read(block))
            except ValueError:
                pass
        pending = arc.learn(sorted(with_prefixes(more, path)))


def entries(arc):
    """(block, name, offset, packed, size, flags) for every live block.
    Folder spellings vary in case between entries (setting\\ vs Setting\\);
    the first spelling seen wins so extraction yields one tree."""
    folders = {}
    for i, (offset, packed, size, flags) in enumerate(arc.blocks):
        if not flags & F_EXISTS:
            continue
        name = arc.names.get(i, "~unnamed\\%05d.bin" % i)
        parts = name.split("\\")
        for n in range(1, len(parts)):
            parts[n - 1] = folders.setdefault("\\".join(parts[:n]).lower(), parts[n - 1])
        yield i, "\\".join(parts), offset, packed, size, flags


def parse_args(argv):
    names, rest = [], []
    it = iter(argv)
    for a in it:
        if a == "--names":
            names.append(next(it))
        else:
            rest.append(a)
    return rest, names


def main():
    args, name_files = parse_args(sys.argv[1:])
    if len(args) < 2 or args[0] not in ("list", "extract"):
        sys.exit(__doc__)
    arc = Archive(args[1])
    resolve_names(arc, args[1], name_files)
    if args[0] == "list":
        print("# %d entries, %d named, sector %d" % (
            len(arc.blocks), len(arc.names), arc.sector))
        print("# path\tsize\toffset\tpacked\tflags")
        for i, name, offset, packed, size, flags in sorted(entries(arc), key=lambda e: e[1].lower()):
            print("%s\t%d\t0x%08x\t%d\t0x%08x" % (name.replace("\\", "/"), size, offset, packed, flags))
        return
    outdir = args[2]
    glob = args[3] if len(args) > 3 else "*"
    bad = 0
    for i, name, *_ in entries(arc):
        rel = name.replace("\\", "/")
        if not fnmatch.fnmatch(rel.lower(), glob.lower()):
            continue
        try:
            data = arc.read(i)
        except ValueError as e:
            print("skip %s: %s" % (rel, e), file=sys.stderr)
            bad += 1
            continue
        dest = os.path.join(outdir, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as out:
            out.write(data)
    if bad:
        print("%d entries failed" % bad, file=sys.stderr)


if __name__ == "__main__":
    main()
