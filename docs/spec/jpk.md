---
title: "`.jpk` archives (Data/*.jpk): format and extraction"
---

# `.jpk` archives (Data/*.jpk): format and extraction

Client: Client.exe (32-bit MSVC, image base 0x400000). Addresses are VAs. Tool:
`~/Vaults/Overview/Worklab/WarmongerRevamp/tools/jpk.py` (stdlib only).

## TL;DR

- **A `.jpk` is a Blizzard MPQ archive** (format v1, an old StormLib ~2005 statically linked)
  with the magic renamed: `NPK\x1a` for `MPQ\x1a` and `NPK\x1b` for `MPQ\x1b`. Same hash function,
  crypt table, table encryption, sector layout. This is **not** CryptoAPI/CEncDecrypt and **not**
  the Gilles Vollant unzip code.
- Three changes from stock MPQ:
  1. **Flag bits 0x10000 and 0x20000 are swapped.** `0x20000` = ENCRYPTED, `0x10000` = FIX_KEY.
     Every file in every archive has flags `0x80020200` (exists | encrypted | compressed). The only
     exception is `{attributes}`, which has `0x80000200`.
  2. **The listfile and attributes have curly braces:** `{listfile}` and `{attributes}`, not
     `(listfile)` and `(attributes)`. The table keys still use `(hash table)` and `(block table)`.
  3. **The compression-type byte is remapped** (table at 0x8424e8): `0x01` zlib, `0x02` PKWARE
     explode, `0x08` Huffman, `0x10`/`0x40` ADPCM, `0x80` bzip2. Every compressed sector in all six
     archives uses `0x01` (zlib).
- Every archive has a complete `{listfile}`, so all entries have names: setting 203/203,
  map 488/488, shader 124/124, ui 822/822, model 4809/4809, sound 496/496.
- Extraction was checked against `{attributes}`. For setting.jpk all 201 CRC32s match.

## Header (0x2c bytes, little-endian, at offset 0)

| off | type | field | setting.jpk |
|---|---|---|---|
| 0x00 | char[4] | magic `NPK\x1a` (0x1a4b504e) | |
| 0x04 | u32 | header size, 0x2c (v1) or 0x20 (v0) | 0x2c |
| 0x08 | u32 | archive size | 0x00a857d0 |
| 0x0c | u16 | format version, 0 or 1. Anything else gives error 0x32 | 1 |
| 0x0e | u16 | sector shift: sector size = 0x200 << shift | 3 (4096) |
| 0x10 | u32 | hash table offset | 0x00684b20 |
| 0x14 | u32 | block table offset | 0x00a84b20 |
| 0x18 | u32 | hash table entry count (power of 2) | 0x40000 |
| 0x1c | u32 | block table entry count | 0xcb (203) |
| 0x20 | u64 | hi-block table offset (v1) | 0 |
| 0x28 | u16 | hash table offset, high 16 bits | 0 |
| 0x2a | u16 | block table offset, high 16 bits | 0 |

Offsets are relative to the start of the header. The opener scans every 0x200 bytes for the magic,
and an `NPK\x1b` user-data header can redirect it. In these files the header is at 0.

The hash table always has 0x40000 entries × 16 bytes, i.e. 4 MB. That is the large gap before the
block table in every archive. The block table sits at the very end of the file.

## Tables

Both tables are encrypted with the standard MPQ cipher (see below). The keys are
`HashString("(hash table)", 0x300)` = 0xc3af3770 and `HashString("(block table)", 0x300)` = 0xec83b3a3.

- Hash entry (16 B): `u32 name_a (hash type 1), u32 name_b (type 2), u16 locale, u16 platform,
  u32 block_index`. 0xffffffff means empty (ends a probe), 0xfffffffe means deleted. The slot is
  `hash(name, type 0) & (count-1)`, with linear probing.
- Block entry (16 B): `u32 offset (relative to header), u32 packed_size, u32 file_size, u32 flags`.

## Crypto

The standard MPQ cipher, unchanged:

- Crypt table: 0x500 dwords, seed 0x00100001, `seed = (seed*125+3) % 0x2AAAAB`, built at
  0x8581c8 by `FUN_0067d870`.
- `HashString(name, type)`: `FUN_0067de70` (type 0x300 = file key). It upper-cases with `toupper`
  and does **not** convert `/`, so names must use `\`. The archive wrapper `FUN_0067b800` replaces
  `/` with `\` before every open or lookup.
- Decrypt a dword stream: `FUN_0067dd10(buf, len, key)`. `FUN_0067da20(buf, "name", len)` decrypts
  with `HashString(name, 0x300)` (used for the two tables).
- **File key** = `HashString(basename, 0x300)`, where basename is the part after the last `\`
  (`FUN_0067ca50` and `FUN_0067e180`, using `_strrchr(name, '\\')`). If flag 0x10000 (FIX_KEY) is
  set: `key = (key + block.offset) ^ block.file_size`. No file has that flag.
- **Sector-offset table** (compressed files: `(ceil(size/sector) + 1)` dwords at the block offset)
  is decrypted with `key - 1`. Sector *n* is decrypted with `key + n`.
- **Key recovery without the name:** the first dword of the sector table equals its own byte size.
  `FUN_0067dac0` brute-forces the 256 possible low key bytes from that known plaintext. The client
  uses it as a fallback in the sector reader `FUN_0067ce10` when its first try fails. jpk.py does
  the same, so it could extract even unnamed files.

## Sectors and compression

- Compressed files (flags & 0xff00): sector-offset table, then sectors. A sector shorter than its
  uncompressed length starts with a compression-mask byte. The dispatcher is `FUN_006801c0`, with the
  table `{mask, fn}` at 0x8424e8:

  | mask | fn | method |
  |---|---|---|
  | 0x80 | 0x67ff20 | bzip2 (BZ2_bzDecompress loop) |
  | 0x02 | 0x67fe00 | PKWARE DCL explode (0x3134-byte work buffer) |
  | 0x01 | 0x67fce0 | zlib inflate ("1.2.3") |
  | 0x08 | 0x67fbd0 | Huffman |
  | 0x40 | 0x67fb00 | IMA ADPCM, 2 channels |
  | 0x10 | 0x67fa60 | IMA ADPCM, 1 channel |

  A sector whose packed length equals its plain length is stored raw.
- jpk.py implements 0x01 and 0x80. Only 0x01 occurs in any archive.

## Function map

| VA | role |
|---|---|
| 0x67b4b0 | archive wrapper → open archive (`FUN_0067c290`) |
| 0x67b530 | archive wrapper → open file by name (`FUN_0067ca50`) |
| 0x67b800 | path normaliser: `/` → `\` |
| 0x67c290 | SFileOpenArchive: magic scan, header checks, reads and decrypts hash and block tables |
| 0x67c0d0 | validates table offsets against the file size |
| 0x67ca50 | SFileOpenFile: hash lookup, file key from basename, FIX_KEY |
| 0x67ce10 | read sectors: sector table, key detection, decrypt, decompress |
| 0x67d870 | builds the crypt table (seed 0x100001) |
| 0x67da20 | decrypt with a named key ("(hash table)" / "(block table)") |
| 0x67dac0 | detect the file key from the sector-table known plaintext |
| 0x67dd10 | MPQ decrypt block |
| 0x67de70 | HashString |
| 0x67e180 | add-file path, i.e. the writer (names `{listfile}` 0x80020200 and `{attributes}` 0x80000200) |
| 0x6801c0 | multi-decompression dispatcher |

## Contents of interest

- `setting.jpk`: 203 entries under `setting\` (`.cdb` tables, `.csv`, `.ini`, `ZoneTable.dat`, fonts,
  `weather\NN.dat`, particle txt). Extracted to `data/setting/`.
- `map.jpk`: `map\ZPxx_zz_00.zp` (145 terrain segments), `map\navi\ZPxx_zz_00.nav` (navmesh, 143),
  `map\minimap\minimap_z<zone>_00.dds`, `map\fogmap\Fog_z<zone>.dds`, `map\bookmarks.txt`.
  `<zone>` is the ZoneDB id. Listing: `data/map.list.txt`. Segment and zone analysis:
  `data/terrain-segments.txt`.

## .cdb tables (setting/*.cdb)

There are two encodings:

- **Record tables** (SceneList, Teleport_List, Dungeon, Create_Char…): CP949 ASCII fields, each
  terminated by `\0`, `rows\0 N\0` and then rows × columns. The second header number is **not**
  the column count: SceneList says 14 but has 11 columns, and Teleport_List says 12 but has 11. A
  trailing number follows the rows. The column count has to be inferred per table.
- **CSV tables** (ZoneDB.cdb): plain CP949 CSV `id,name,flags,x0,z0,x1,z1,map`.
- `config/StringAll_Eng.cdb` (outside the jpk): `count\0 N\0`, then records `key\0`,
  UTF-16LE value ending in `\0\0`, then an ASCII flag ending in `\0`.

Readable dumps: `data/tables/{SceneList,Teleport_List,ZoneDB,FieldNames}.tsv`.

## Field (map id) → terrain

- SceneList id = FieldName_N = the server's map/field id. ZoneDB id is a different numbering.
  It is the terrain zone, picked by position and used for minimap and fog.
- Teleport_List gives positions for each field (cols: gate, field, x, z, …, linkGate, linkField,
  label). Its points fall inside the matching ZoneDB rect. Examples:
  - 87 Village (nation A) → (2688.83, 382.86), ZoneDB 102 마을A `A_Town_01`, rect
    x 2592..2783 z 256..479, segment ZP10_01 (zp and nav present).
  - 91 / 95 Village (B / C) → (3963.73, 322.41) ZP15_01 / (5245.8, 337.38) ZP20_01.
  - 88 Training Camp → ~(356, 3502), ZoneDB 128 캠핑장_A, ZP01_13. 92 / 96 → ZP02_13 / ZP03_13.
  - 89 Training Ground → ~(451, 3629), ZoneDB 127 훈련장_A, ZP01_14. 93 / 97 → ZP02_14 / ZP03_14.
  - 90 Castle → (318, 4135), ZoneDB 144 A대도시, ZP01_16.
  - 117 Beginner's Training Ground: no teleport row. Inferred: ZoneDB 2 튜토리얼맵_01 / 107
    튜토리얼존 (tutorial map / zone), rect around (1424, 416), segment ZP05_01 (present).
    Confidence medium.
