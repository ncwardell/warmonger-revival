# Protocol overview

Reverse engineered from the client. Every packet, in both directions, starts with a 16-byte little-endian header:

| Offset | Type | Field |
|---|---|---|
| +0x00 | u16 | total length (the client drops server packets of 16 bytes or less) |
| +0x02 | u16 | magic `0xA53C` |
| +0x04 | u16 | opcode |
| +0x06 | u16 | extra (in world: the sender's unit id) |
| +0x08 | u32 | tick |
| +0x0C | u32 | key: client payload words are sent as `~(word - key)` when non-zero |

The client's config `Data/config/serverlist.sof` is RC4 with a 40-bit key, `MD5("CEncDecrypt Default Password")[:5]` + 11 zero bytes ([[jpk]] covers the archives).

## Pages

- Per-opcode first pass: [[group00]], [[group01]], [[group02]], [[group03]]
- Systems: [[loading]] (world loading), [[world]] (spawning, movement relay), [[movement]], [[combat]], [[skills]], [[monsters]] (incl. AI and loot), [[match]]
- Formats: [[jpk]] (archives), [[navmesh]] (walkable ground)
