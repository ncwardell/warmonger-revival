---
title: "Training Camp A"
type: "zone"
id: 128
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 128", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: [[gameplay/npc-locations]] §2 (segment origins; minimap = ZoneDB rectangle check)"]
name_kr: "캠핑장_A"
terrain: "A_campingsite"
bounds: {"x0": 288, "z0": 3392, "x1": 447, "z1": 3551}
size: [160, 160]
segments: ["ZP01_13"]
fields: [88]
minimap: "map/minimap/minimap_z128_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=d95688 type=c899cd id=b4182b sources=35929e name_kr=8a403e terrain=87427b bounds=3cf204 size=114466 segments=e346a8 fields=99bd16 minimap=8f8f95 -->
|  |  |
|---|---|
|  | ![minimap of Training Camp A](../assets/zones/128.png) |
| **Zone id** | `128` |
| **ZoneDB name** | 캠핑장_A (English gloss: Training Camp A) |
| **Terrain name** | `A_campingsite` |
| **Rectangle** | x 288–447, z 3392–3551 (160 × 160 units) |
| **Fields** | [[wiki/fields/88-training-camp\|Training Camp]] |
| **Minimap** | `map/minimap/minimap_z128_00.dds` |
| **Fog map** | `map/fogmap/Fog_z128.dds` |
| **Lighting** | `Setting/weather/A_campingsite.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP01_13 | yes | yes |

### Mentioned in

- [[gameplay/npc-locations#2. How coordinates were derived|NPC and point-of-interest locations § 2. How coordinates were derived]]
<!-- generated:end -->

## Notes

- Training Camp of field 88, segment origin (256, 3328) ([[gameplay/npc-locations|NPC locations]] §2). The minimap mapping was checked by drawing field 88's four gates onto this texture: each lands at the end of one arm ([[gameplay/npc-locations|NPC locations]] §2). *client*

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
