---
title: "Eternal Lake"
type: "field"
id: 84
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 84", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 84"]
name_key: "FieldName_84"
kind: "land"
scene_type: 2
max_users: 30
group: 7
scene_c4: 1
neighbours: [6, 14]
zones: [98]
segments: ["ZP04_06"]
worldmap_rect: [762, 280, 824, 326]
gates:
  - {"gate": 160, "x": 1187.64, "z": 1710.61, "to_gate": 940, "to_field": 6, "label": "FieldName_84"}
  - {"gate": 240, "x": 1066.88, "z": 1603.03, "to_gate": 941, "to_field": 14, "label": "FieldName_84"}
connections:
  - {"to": 6, "gate": 160, "to_gate": 940}
  - {"to": 14, "gate": 240, "to_gate": 941}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=42a5e7 type=7a94db id=be461a sources=0b8c5d name_key=5fbb94 kind=8e3535 scene_type=da4b92 max_users=22d200 group=902ba3 scene_c4=356a19 neighbours=82abbc zones=c595b3 segments=34f348 worldmap_rect=f1a2f6 gates=8f5d57 connections=605e71 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 98](wiki/assets/zones/98.png) |
| **Field id** | `84` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 7 (SceneList last column) |
| **Zones** | [[wiki/zones/98-field-84-eternal-lake\|Field 84 (Eternal Lake)]] |
| **Terrain segments** | `ZP04_06` |
| **World-map rectangle** | `[762, 280, 824, 326]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_84` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 160 | 1187.64, 1710.61 | [[wiki/fields/6-skywing-yard\|Skywing Yard]] | 940 | FieldName_84 |
| 240 | 1066.88, 1603.03 | [[wiki/fields/14-eternal-river-upper-region\|Eternal River - Upper Region]] | 941 | FieldName_84 |

Entered from: [[wiki/fields/6-skywing-yard|Skywing Yard]] (gate 940 → 160), [[wiki/fields/14-eternal-river-upper-region|Eternal River - Upper Region]] (gate 941 → 240)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/6-skywing-yard|Skywing Yard]], [[wiki/fields/14-eternal-river-upper-region|Eternal River - Upper Region]]

### NPCs

None known yet.

### Monsters

None known yet.

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP04_06 | yes | yes |

### Mentioned in

- [[gameplay/video-fort-war#Eternal River – Upper Region (field 14, ZoneDB 39, rectangle x 3616–3775, z 544–703)|Video notes: fortress war series (ZonderCoRe) § Eternal River – Upper Region (field 14, ZoneDB 39, rectangle x 3616–3775, z 544–703)]]
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]] (by name)
<!-- generated:end -->

## Notes

<!-- hand-written: add what you know, with a source -->

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
