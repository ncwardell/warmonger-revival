---
title: "Eclipsed Road"
type: "field"
id: 50
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 50", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 50"]
name_key: "FieldName_50"
kind: "land"
scene_type: 2
max_users: 30
group: 4
scene_c4: 1
neighbours: [51, 49, 53]
zones: [68]
segments: ["ZP10_04"]
worldmap_rect: [1160, 679, 1243, 754]
gates:
  - {"gate": 591, "x": 2628.93, "z": 1195.71, "to_gate": 600, "to_field": 49, "label": "FieldName_50"}
  - {"gate": 611, "x": 2705.73, "z": 1094.39, "to_gate": 601, "to_field": 51, "label": "FieldName_50"}
  - {"gate": 630, "x": 2714.45, "z": 1176.7, "to_gate": 602, "to_field": 53, "label": "FieldName_50"}
connections:
  - {"to": 49, "gate": 591, "to_gate": 600}
  - {"to": 51, "gate": 611, "to_gate": 601}
  - {"to": 53, "gate": 630, "to_gate": 602}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=f9f3dc type=7a94db id=e1822d sources=6dade1 name_key=97c33e kind=8e3535 scene_type=da4b92 max_users=22d200 group=1b6453 scene_c4=356a19 neighbours=c13635 zones=52dbed segments=53cb00 worldmap_rect=ec716c gates=7c6770 connections=76ab75 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 68](wiki/assets/zones/68.png) |
| **Field id** | `50` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 4 (SceneList last column) |
| **Zones** | [[wiki/zones/68-field-50-eclipsed-road\|Field 50 (Eclipsed Road)]] |
| **Terrain segments** | `ZP10_04` |
| **World-map rectangle** | `[1160, 679, 1243, 754]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_50` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 591 | 2628.93, 1195.71 | [[wiki/fields/49-weltering-flame\|Weltering Flame]] | 600 | FieldName_50 |
| 611 | 2705.73, 1094.39 | [[wiki/fields/51-sunup-campsite\|Sunup Campsite]] | 601 | FieldName_50 |
| 630 | 2714.45, 1176.7 | [[wiki/fields/53-ashcolor-hill\|Ashcolor Hill]] | 602 | FieldName_50 |

Entered from: [[wiki/fields/49-weltering-flame|Weltering Flame]] (gate 600 → 591), [[wiki/fields/51-sunup-campsite|Sunup Campsite]] (gate 601 → 611), [[wiki/fields/53-ashcolor-hill|Ashcolor Hill]] (gate 602 → 630)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/51-sunup-campsite|Sunup Campsite]], [[wiki/fields/49-weltering-flame|Weltering Flame]], [[wiki/fields/53-ashcolor-hill|Ashcolor Hill]]

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
| ZP10_04 | yes | yes |
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
