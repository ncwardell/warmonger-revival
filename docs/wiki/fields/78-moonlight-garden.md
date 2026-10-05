---
title: "Moonlight Garden"
type: "field"
id: 78
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 78", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 78"]
name_key: "FieldName_78"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 1
scene_c10: 1
neighbours: [86, 81, 83]
zones: [91]
segments: ["ZP18_05"]
worldmap_rect: [1492, 199, 1578, 239]
gates:
  - {"gate": 910, "x": 4673.23, "z": 1431.93, "to_gate": 881, "to_field": 81, "label": "FieldName_78"}
  - {"gate": 931, "x": 4763.49, "z": 1447.18, "to_gate": 882, "to_field": 83, "label": "FieldName_78"}
  - {"gate": 961, "x": 4691.45, "z": 1347.71, "to_gate": 880, "to_field": 86, "label": "FieldName_78"}
connections:
  - {"to": 81, "gate": 910, "to_gate": 881}
  - {"to": 83, "gate": 931, "to_gate": 882}
  - {"to": 86, "gate": 961, "to_gate": 880}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=632426 type=7a94db id=eb4ac3 sources=38c2cc name_key=d670f5 kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=356a19 scene_c10=356a19 neighbours=394b83 zones=bb2d63 segments=25ba0d worldmap_rect=e924f6 gates=fa867a connections=e629b0 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 91](../assets/zones/91.png) |
| **Field id** | `78` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/91-field-78-moonlight-garden\|Field 78 (Moonlight Garden)]] |
| **Terrain segments** | `ZP18_05` |
| **World-map rectangle** | `[1492, 199, 1578, 239]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_78` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 910 | 4673.23, 1431.93 | [[wiki/fields/81-windmist-hill\|Windmist Hill]] | 881 | FieldName_78 |
| 931 | 4763.49, 1447.18 | [[wiki/fields/83-moonlight-plain-east\|Moonlight Plain - East]] | 882 | FieldName_78 |
| 961 | 4691.45, 1347.71 | [[wiki/fields/86-moonlight-temple\|Moonlight Temple]] | 880 | FieldName_78 |

Entered from: [[wiki/fields/81-windmist-hill|Windmist Hill]] (gate 881 → 910), [[wiki/fields/83-moonlight-plain-east|Moonlight Plain - East]] (gate 882 → 931), [[wiki/fields/86-moonlight-temple|Moonlight Temple]] (gate 880 → 961)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/86-moonlight-temple|Moonlight Temple]], [[wiki/fields/81-windmist-hill|Windmist Hill]], [[wiki/fields/83-moonlight-plain-east|Moonlight Plain - East]]

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
| ZP18_05 | yes | yes |
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
