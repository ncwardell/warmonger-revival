---
title: "New arena (Battle Arena)"
type: "zone"
id: 148
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 148", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: [[gameplay/arena-ranking-rewards]] (Battle Arena zones)"]
name_kr: "New_arena"
terrain: "new_arena"
bounds: {"x0": 256, "z0": 1920, "x1": 479, "z1": 2015}
size: [224, 96]
segments: ["ZP01_07"]
fields: [140]
minimap: "map/minimap/minimap_z148_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=b6f614 type=c899cd id=536fb6 sources=167eca name_kr=52177e terrain=2932d6 bounds=e175b8 size=770ba9 segments=63c97d fields=3833c5 minimap=6bd532 -->
|  |  |
|---|---|
|  | ![minimap of New arena (Battle Arena)](../assets/zones/148.png) |
| **Zone id** | `148` |
| **ZoneDB name** | New_arena (English gloss: New arena (Battle Arena)) |
| **Terrain name** | `new_arena` |
| **Rectangle** | x 256–479, z 1920–2015 (224 × 96 units) |
| **Fields** | [[wiki/fields/140-battle-arena\|Battle Arena]] |
| **Minimap** | `map/minimap/minimap_z148_00.dds` |
| **Fog map** | `map/fogmap/Fog_z148.dds` |
| **Lighting** | `Setting/weather/new_arena.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP01_07 | yes | yes |

### Overlapping zones

[[wiki/zones/3-dungeon|Dungeon]], [[wiki/zones/11-instance-dungeon-1f|Instance dungeon 1F]], [[wiki/zones/147-field-26-test|Field 26 test]]

### Mentioned in

- [[gameplay/arena-ranking-rewards#Client cross-reference|Battle Arena monthly ranking rewards § Client cross-reference]]
<!-- generated:end -->

## Notes

- One of the two zones the client gives the Battle Arena, with ZoneDB 5 `Battle_Arena_01` ([[gameplay/arena-ranking-rewards|Arena ranking rewards]]). *client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
