---
title: "B Fortress"
type: "zone"
id: 104
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 104", "doc: gameplay/npc-locations §2 (Fortress = ZoneDB 103-105, one per nation)", "client + video: [[gameplay/npc-locations]] §2-§3 (three Fortress copies, segment origins, one shared layout)"]
name_kr: "B_요새"
terrain: "B_Town_01"
bounds: {"x0": 2048, "z0": 1536, "x1": 2303, "z1": 1791}
size: [256, 256]
segments: ["ZP08_06"]
fields: [120]
minimap: "map/minimap/minimap_z104_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=4ebecd type=c899cd id=78a8ef sources=507b0a name_kr=8b82cb terrain=ddf7e2 bounds=850ab9 size=a1cfbb segments=dff210 fields=6c3da9 minimap=3b9ad4 -->
|  |  |
|---|---|
|  | ![minimap of B Fortress](wiki/assets/zones/104.png) |
| **Zone id** | `104` |
| **ZoneDB name** | B_요새 (English gloss: B Fortress) |
| **Terrain name** | `B_Town_01` |
| **Rectangle** | x 2048–2303, z 1536–1791 (256 × 256 units) |
| **Fields** | [[wiki/fields/120-fortress\|Fortress]] |
| **Minimap** | `map/minimap/minimap_z104_00.dds` |
| **Fog map** | `map/fogmap/Fog_z104.dds` |
| **Lighting** | `Setting/weather/B_Town_01.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP08_06 | yes | yes |

### Mentioned in

- [[gameplay/npc-locations#2. How coordinates were derived|NPC and point-of-interest locations § 2. How coordinates were derived]]
<!-- generated:end -->

## Notes

- One of the three Fortress copies (field 120), segment origin (2048, 1536). All three share one layout, so the Fortress NPC positions in [[gameplay/npc-locations|NPC locations]] §3 carry over by adding the origin difference; the Village maps use the same navmesh ([[gameplay/npc-locations|NPC locations]] §2). *client + video*

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
