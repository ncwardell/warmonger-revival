---
title: "Battle arena"
type: "zone"
id: 5
status: "partial"
missing: ["fields"]
sources: ["client: ZoneDB.cdb id 5", "client: [[gameplay/arena-ranking-rewards]] (Battle Arena zones: ZoneDB 5 Battle_Arena_01 and ZoneDB 148 new_arena)"]
name_kr: "배틀아레나"
terrain: "Battle_Arena_01"
bounds: {"x0": 800, "z0": 320, "x1": 991, "z1": 447}
size: [192, 128]
segments: ["ZP03_01"]
fields: []
minimap: "map/minimap/minimap_z5_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=dd350c type=c899cd id=ac3478 sources=acdf45 name_kr=c99826 terrain=946cf3 bounds=9200db size=681360 segments=3fa0ba fields=97d170 minimap=0d802b -->
|  |  |
|---|---|
|  | ![minimap of Battle arena](wiki/assets/zones/5.png) |
| **Zone id** | `5` |
| **ZoneDB name** | 배틀아레나 (English gloss: Battle arena) |
| **Terrain name** | `Battle_Arena_01` |
| **Rectangle** | x 800–991, z 320–447 (192 × 128 units) |
| **Minimap** | `map/minimap/minimap_z5_00.dds` |
| **Lighting** | `Setting/weather/Battle_Arena_01.dat` |

No field is known to use this zone: no gate or trigger lies inside it. It may be a test, a UI scene or a leftover. Add `fields:` if you know better.

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP03_01 | yes | yes |

### Mentioned in

- [[gameplay/arena-ranking-rewards#Client cross-reference|Battle Arena monthly ranking rewards § Client cross-reference]]
<!-- generated:end -->

## Notes

- The client lists this zone, with ZoneDB 148 `new_arena`, as a Battle Arena zone ([[gameplay/arena-ranking-rewards|Arena ranking rewards]]). No gate or trigger of field 140 lies inside it. *client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

- Whether this was an older Battle Arena map for field 140 (so `fields` should list 140), or unused, is not known.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
