---
title: "Tutorial map 01 (Beginner's Training Ground)"
type: "zone"
id: 2
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 2", "doc: spec/navmesh (tutorial spawn in ZoneDB 2 tutorial_map_01)", "client + video: [[gameplay/npc-locations]] §6; [[gameplay/video-character-creation-and-tutorial]] §6 (never visited in 2018)"]
name_kr: "튜토리얼맵_01"
terrain: "tutorial_map_01"
bounds: {"x0": 1344, "z0": 352, "x1": 1503, "z1": 479}
size: [160, 128]
segments: ["ZP05_01"]
fields: [117]
minimap: "map/minimap/minimap_z2_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=af0209 type=c899cd id=da4b92 sources=67adc5 name_kr=c16487 terrain=a5580a bounds=c2c1ee size=fd526b segments=0fbb4f fields=23ae40 minimap=60c543 -->
|  |  |
|---|---|
|  | ![minimap of Tutorial map 01 (Beginner's Training Ground)](wiki/assets/zones/2.png) |
| **Zone id** | `2` |
| **ZoneDB name** | 튜토리얼맵_01 (English gloss: Tutorial map 01 (Beginner's Training Ground)) |
| **Terrain name** | `tutorial_map_01` |
| **Rectangle** | x 1344–1503, z 352–479 (160 × 128 units) |
| **Fields** | [[wiki/fields/117-beginner-s-training-ground\|Beginner's Training Ground]] |
| **Minimap** | `map/minimap/minimap_z2_00.dds` |
| **Fog map** | `map/fogmap/Fog_z2.dds` |
| **Lighting** | `Setting/weather/tutorial_map_01.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP05_01 | yes | yes |

### Overlapping zones

[[wiki/zones/101-town-c-dummy-shop-street|Town C dummy shop street]], [[wiki/zones/107-tutorial-zone|Tutorial zone]]

### Mentioned in

- [[gameplay/npc-locations#6. Village (87/91/95), Castle (90/94/98), tutorial (117)|NPC and point-of-interest locations § 6. Village (87/91/95), Castle (90/94/98), tutorial (117)]]
<!-- generated:end -->

## Notes

- Map of field 117 (Beginner's Training Ground). No client table places anything here; a safe navmesh spawn point is (1427, 429) ([[gameplay/npc-locations|NPC locations]] §6). The 2018 builds never sent players here: new characters started in the Training Ground ([[gameplay/video-character-creation-and-tutorial|character-creation video]] §6). *client + video*

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
