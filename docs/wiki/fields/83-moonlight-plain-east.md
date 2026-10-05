---
title: "Moonlight Plain - East"
type: "field"
id: 83
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 83", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 83"]
name_key: "FieldName_83"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 2
neighbours: [82, 78, 77]
zones: [96]
segments: ["ZP03_06"]
worldmap_rect: [1632, 202, 1751, 267]
gates:
  - {"gate": 872, "x": 937.44, "z": 1594.71, "to_gate": 930, "to_field": 77, "label": "FieldName_83"}
  - {"gate": 882, "x": 827.37, "z": 1591.73, "to_gate": 931, "to_field": 78, "label": "FieldName_83"}
  - {"gate": 921, "x": 829.14, "z": 1696.12, "to_gate": 932, "to_field": 82, "label": "FieldName_83"}
connections:
  - {"to": 77, "gate": 872, "to_gate": 930}
  - {"to": 78, "gate": 882, "to_gate": 931}
  - {"to": 82, "gate": 921, "to_gate": 932}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=24781e type=7a94db id=7d7116 sources=0f0a22 name_key=95fd6a kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=da4b92 neighbours=573533 zones=65ae82 segments=4906b6 worldmap_rect=787bac gates=8416b3 connections=39e1c4 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 96](wiki/assets/zones/96.png) |
| **Field id** | `83` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/96-field-83-moonlight-plain-east\|Field 83 (Moonlight Plain - East)]] |
| **Terrain segments** | `ZP03_06` |
| **World-map rectangle** | `[1632, 202, 1751, 267]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_83` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 872 | 937.44, 1594.71 | [[wiki/fields/77-sandairvalley\|SandairValley]] | 930 | FieldName_83 |
| 882 | 827.37, 1591.73 | [[wiki/fields/78-moonlight-garden\|Moonlight Garden]] | 931 | FieldName_83 |
| 921 | 829.14, 1696.12 | [[wiki/fields/82-moonlight-plain-west\|Moonlight Plain - West]] | 932 | FieldName_83 |

Entered from: [[wiki/fields/77-sandairvalley|SandairValley]] (gate 930 → 872), [[wiki/fields/78-moonlight-garden|Moonlight Garden]] (gate 931 → 882), [[wiki/fields/82-moonlight-plain-west|Moonlight Plain - West]] (gate 932 → 921)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/82-moonlight-plain-west|Moonlight Plain - West]], [[wiki/fields/78-moonlight-garden|Moonlight Garden]], [[wiki/fields/77-sandairvalley|SandairValley]]

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
| ZP03_06 | yes | yes |
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
