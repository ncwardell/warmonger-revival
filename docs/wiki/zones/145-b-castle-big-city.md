---
title: "B Castle (big city)"
type: "zone"
id: 145
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 145", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: [[gameplay/npc-locations]] §2 (Castle copies and segment origins)"]
name_kr: "B대도시"
terrain: "B_big city"
bounds: {"x0": 512, "z0": 4096, "x1": 767, "z1": 4351}
size: [256, 256]
segments: ["ZP02_16"]
fields: [94]
minimap: "map/minimap/minimap_z145_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=13b3c5 type=c899cd id=50336b sources=b44a14 name_kr=0de64f terrain=ff6bd6 bounds=e09423 size=a1cfbb segments=c8d43a fields=f20d03 minimap=64cd15 -->
|  |  |
|---|---|
|  | ![minimap of B Castle (big city)](wiki/assets/zones/145.png) |
| **Zone id** | `145` |
| **ZoneDB name** | B대도시 (English gloss: B Castle (big city)) |
| **Terrain name** | `B_big city` |
| **Rectangle** | x 512–767, z 4096–4351 (256 × 256 units) |
| **Fields** | [[wiki/fields/94-castle\|Castle]] |
| **Minimap** | `map/minimap/minimap_z145_00.dds` |
| **Fog map** | `map/fogmap/Fog_z145.dds` |
| **Lighting** | `Setting/weather/B_big city.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP02_16 | yes | yes |

### Mentioned in

- [[gameplay/npc-locations#2. How coordinates were derived|NPC and point-of-interest locations § 2. How coordinates were derived]]
<!-- generated:end -->

## Notes

- Castle of field 94, segment origin (512, 4096); the three Castle copies have identical meshes ([[gameplay/npc-locations|NPC locations]] §2). *client*

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
