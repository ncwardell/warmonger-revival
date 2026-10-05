---
title: "Training Ground B"
type: "zone"
id: 131
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 131", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client + video: [[gameplay/npc-locations]] §2 (segment origins of the three Training Ground copies)"]
name_kr: "훈련장_B"
terrain: "B_training"
bounds: {"x0": 544, "z0": 3616, "x1": 735, "z1": 3807}
size: [192, 192]
segments: ["ZP02_14"]
fields: [93]
minimap: "map/minimap/minimap_z131_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=de60ee type=c899cd id=e794a8 sources=0165d5 name_kr=e54400 terrain=b411f3 bounds=87c110 size=be57ee segments=772a13 fields=a7533a minimap=7c7a3a -->
|  |  |
|---|---|
|  | ![minimap of Training Ground B](../assets/zones/131.png) |
| **Zone id** | `131` |
| **ZoneDB name** | 훈련장_B (English gloss: Training Ground B) |
| **Terrain name** | `B_training` |
| **Rectangle** | x 544–735, z 3616–3807 (192 × 192 units) |
| **Fields** | [[wiki/fields/93-training-ground\|Training Ground]] |
| **Minimap** | `map/minimap/minimap_z131_00.dds` |
| **Fog map** | `map/fogmap/Fog_z131.dds` |
| **Lighting** | `Setting/weather/B_training.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP02_14 | yes | yes |

### Mentioned in

- [[gameplay/npc-locations#2. How coordinates were derived|NPC and point-of-interest locations § 2. How coordinates were derived]]
- [[gameplay/video-character-creation-and-tutorial#4. NPC positions (Erion copy)|Video notes: character creation and tutorial (ZonderCoRe, June 2018) § 4. NPC positions (Erion copy)]]
<!-- generated:end -->

## Notes

- Training Ground of field 93, segment origin (512, 3584); the three copies have identical meshes ([[gameplay/npc-locations|NPC locations]] §2). The June 2018 Erion video measured this minimap at 1.1228 units per pixel ([[gameplay/video-character-creation-and-tutorial|character-creation video]] §4). *client + video*

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
