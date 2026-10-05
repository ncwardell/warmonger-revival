---
title: "Windmist Hill"
type: "field"
id: 81
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 81", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 81"]
name_key: "FieldName_81"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 2
scene_c10: 1
neighbours: [80, 78, 82]
zones: [94]
segments: ["ZP01_06"]
worldmap_rect: [1380, 51, 1566, 114]
gates:
  - {"gate": 881, "x": 370.86, "z": 1592.65, "to_gate": 910, "to_field": 78, "label": "FieldName_81"}
  - {"gate": 902, "x": 305.78, "z": 1693.09, "to_gate": 911, "to_field": 80, "label": "FieldName_81"}
  - {"gate": 920, "x": 423.5, "z": 1690.34, "to_gate": 912, "to_field": 82, "label": "FieldName_81"}
connections:
  - {"to": 78, "gate": 881, "to_gate": 910}
  - {"to": 80, "gate": 902, "to_gate": 911}
  - {"to": 82, "gate": 920, "to_gate": 912}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=6e85fe type=7a94db id=1d513c sources=1cc922 name_key=b1e936 kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=da4b92 scene_c10=356a19 neighbours=6e72c6 zones=f20d03 segments=83ce42 worldmap_rect=805d4a gates=4f2213 connections=9fa1d2 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 94](../assets/zones/94.png) |
| **Field id** | `81` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/94-field-81-windmist-hill\|Field 81 (Windmist Hill)]] |
| **Terrain segments** | `ZP01_06` |
| **World-map rectangle** | `[1380, 51, 1566, 114]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_81` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 881 | 370.86, 1592.65 | [[wiki/fields/78-moonlight-garden\|Moonlight Garden]] | 910 | FieldName_81 |
| 902 | 305.78, 1693.09 | [[wiki/fields/80-windmist-valley\|Windmist Valley]] | 911 | FieldName_81 |
| 920 | 423.5, 1690.34 | [[wiki/fields/82-moonlight-plain-west\|Moonlight Plain - West]] | 912 | FieldName_81 |

Entered from: [[wiki/fields/78-moonlight-garden|Moonlight Garden]] (gate 910 → 881), [[wiki/fields/80-windmist-valley|Windmist Valley]] (gate 911 → 902), [[wiki/fields/82-moonlight-plain-west|Moonlight Plain - West]] (gate 912 → 920)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/80-windmist-valley|Windmist Valley]], [[wiki/fields/78-moonlight-garden|Moonlight Garden]], [[wiki/fields/82-moonlight-plain-west|Moonlight Plain - West]]

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
| ZP01_06 | yes | yes |
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
