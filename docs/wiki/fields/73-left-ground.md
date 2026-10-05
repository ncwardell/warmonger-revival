---
title: "Left Ground"
type: "field"
id: 73
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 73", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 73"]
name_key: "FieldName_73"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 1
neighbours: [62, 72, 74]
zones: [88]
segments: ["ZP13_05"]
worldmap_rect: [1279, 270, 1343, 331]
gates:
  - {"gate": 721, "x": 3400.15, "z": 1348.72, "to_gate": 830, "to_field": 62, "label": "FieldName_73"}
  - {"gate": 821, "x": 3477.51, "z": 1455.12, "to_gate": 831, "to_field": 72, "label": "FieldName_73"}
  - {"gate": 840, "x": 3397.11, "z": 1434.09, "to_gate": 832, "to_field": 74, "label": "FieldName_73"}
connections:
  - {"to": 62, "gate": 721, "to_gate": 830}
  - {"to": 72, "gate": 821, "to_gate": 831}
  - {"to": 74, "gate": 840, "to_gate": 832}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=bbf045 type=7a94db id=35e995 sources=22d096 name_key=c792df kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=356a19 neighbours=43dd8f zones=99bd16 segments=056879 worldmap_rect=4b9e8a gates=d42fb8 connections=4c5fcb npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 88](../assets/zones/88.png) |
| **Field id** | `73` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/88-field-73-left-ground\|Field 73 (Left Ground)]] |
| **Terrain segments** | `ZP13_05` |
| **World-map rectangle** | `[1279, 270, 1343, 331]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_73` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 721 | 3400.15, 1348.72 | [[wiki/fields/62-sad-swamp\|Sad Swamp]] | 830 | FieldName_73 |
| 821 | 3477.51, 1455.12 | [[wiki/fields/72-refuge\|Refuge]] | 831 | FieldName_73 |
| 840 | 3397.11, 1434.09 | [[wiki/fields/74-whistle-hill\|Whistle Hill]] | 832 | FieldName_73 |

Entered from: [[wiki/fields/62-sad-swamp|Sad Swamp]] (gate 830 → 721), [[wiki/fields/72-refuge|Refuge]] (gate 831 → 821), [[wiki/fields/74-whistle-hill|Whistle Hill]] (gate 832 → 840)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/62-sad-swamp|Sad Swamp]], [[wiki/fields/72-refuge|Refuge]], [[wiki/fields/74-whistle-hill|Whistle Hill]]

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
| ZP13_05 | yes | yes |
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
