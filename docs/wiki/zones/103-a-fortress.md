---
title: "A Fortress"
type: "zone"
id: 103
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 103", "doc: gameplay/npc-locations §2 (Fortress = ZoneDB 103-105, one per nation)", "client + video: [[gameplay/npc-locations]] §2-§3 (three Fortress copies, segment origins, one shared layout)"]
name_kr: "A_요새"
terrain: "A_Town_01"
bounds: {"x0": 1792, "z0": 1536, "x1": 2047, "z1": 1791}
size: [256, 256]
segments: ["ZP07_06"]
fields: [120]
minimap: "map/minimap/minimap_z103_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=100fa9 type=c899cd id=934385 sources=e7cab0 name_kr=c3fc7a terrain=c4ee09 bounds=051649 size=a1cfbb segments=1e0c0b fields=6c3da9 minimap=de71e5 -->
|  |  |
|---|---|
|  | ![minimap of A Fortress](wiki/assets/zones/103.png) |
| **Zone id** | `103` |
| **ZoneDB name** | A_요새 (English gloss: A Fortress) |
| **Terrain name** | `A_Town_01` |
| **Rectangle** | x 1792–2047, z 1536–1791 (256 × 256 units) |
| **Fields** | [[wiki/fields/120-fortress\|Fortress]] |
| **Minimap** | `map/minimap/minimap_z103_00.dds` |
| **Fog map** | `map/fogmap/Fog_z103.dds` |
| **Lighting** | `Setting/weather/A_Town_01.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP07_06 | yes | yes |

### Mentioned in

- [[gameplay/npc-locations#2. How coordinates were derived|NPC and point-of-interest locations § 2. How coordinates were derived]]
<!-- generated:end -->

## Notes

- One of the three Fortress copies (field 120), segment origin (1792, 1536). All three share one layout, so the Fortress NPC positions in [[gameplay/npc-locations|NPC locations]] §3 carry over by adding the origin difference; the Village maps use the same navmesh ([[gameplay/npc-locations|NPC locations]] §2). *client + video*

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
