---
title: "C Fortress"
type: "zone"
id: 105
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 105", "doc: gameplay/npc-locations §2 (Fortress = ZoneDB 103-105, one per nation)", "client + video: [[gameplay/npc-locations]] §2-§3 (three Fortress copies, segment origins, one shared layout)"]
name_kr: "C_요새"
terrain: "C_Town_01"
bounds: {"x0": 2304, "z0": 1536, "x1": 2559, "z1": 1791}
size: [256, 256]
segments: ["ZP09_06"]
fields: [120]
minimap: "map/minimap/minimap_z105_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=00ac22 type=c899cd id=e114c4 sources=f57dba name_kr=d4ad74 terrain=14c5d4 bounds=3ac08f size=a1cfbb segments=ba85be fields=6c3da9 minimap=8de62d -->
|  |  |
|---|---|
|  | ![minimap of C Fortress](wiki/assets/zones/105.png) |
| **Zone id** | `105` |
| **ZoneDB name** | C_요새 (English gloss: C Fortress) |
| **Terrain name** | `C_Town_01` |
| **Rectangle** | x 2304–2559, z 1536–1791 (256 × 256 units) |
| **Fields** | [[wiki/fields/120-fortress\|Fortress]] |
| **Minimap** | `map/minimap/minimap_z105_00.dds` |
| **Fog map** | `map/fogmap/Fog_z105.dds` |
| **Lighting** | `Setting/weather/C_Town_01.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP09_06 | yes | yes |

### Mentioned in

- [[gameplay/npc-locations#2. How coordinates were derived|NPC and point-of-interest locations § 2. How coordinates were derived]]
<!-- generated:end -->

## Notes

- One of the three Fortress copies (field 120), segment origin (2304, 1536). All three share one layout, so the Fortress NPC positions in [[gameplay/npc-locations|NPC locations]] §3 carry over by adding the origin difference; the Village maps use the same navmesh ([[gameplay/npc-locations|NPC locations]] §2). *client + video*

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
