---
title: "Icethorn Plain"
type: "field"
id: 67
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 67", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 67"]
name_key: "FieldName_67"
kind: "land"
scene_type: 2
max_users: 30
group: 2
scene_c4: 2
neighbours: [56, 66, 68]
zones: [82]
segments: ["ZP07_05"]
worldmap_rect: [1494, 708, 1590, 796]
gates:
  - {"gate": 661, "x": 1969.12, "z": 1347.48, "to_gate": 770, "to_field": 56, "label": "FieldName_67"}
  - {"gate": 761, "x": 1836.13, "z": 1340.33, "to_gate": 771, "to_field": 66, "label": "FieldName_67"}
  - {"gate": 780, "x": 1937.55, "z": 1449.02, "to_gate": 772, "to_field": 68, "label": "FieldName_67"}
connections:
  - {"to": 56, "gate": 661, "to_gate": 770}
  - {"to": 66, "gate": 761, "to_gate": 771}
  - {"to": 68, "gate": 780, "to_gate": 772}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=f881b6 type=7a94db id=4d89d2 sources=88d37d name_key=3b175d kind=8e3535 scene_type=da4b92 max_users=22d200 group=da4b92 scene_c4=da4b92 neighbours=0895c9 zones=272913 segments=2cc94f worldmap_rect=31a93e gates=fbf678 connections=d4a072 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 82](../assets/zones/82.png) |
| **Field id** | `67` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 2 (SceneList last column) |
| **Zones** | [[wiki/zones/82-field-67-icethorn-plain\|Field 67 (Icethorn Plain)]] |
| **Terrain segments** | `ZP07_05` |
| **World-map rectangle** | `[1494, 708, 1590, 796]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_67` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 661 | 1969.12, 1347.48 | [[wiki/fields/56-snowflower-plain\|Snowflower Plain]] | 770 | FieldName_67 |
| 761 | 1836.13, 1340.33 | [[wiki/fields/66-earth-of-abyss\|Earth of Abyss]] | 771 | FieldName_67 |
| 780 | 1937.55, 1449.02 | [[wiki/fields/68-frostwind-east\|Frostwind - East]] | 772 | FieldName_67 |

Entered from: [[wiki/fields/56-snowflower-plain|Snowflower Plain]] (gate 770 → 661), [[wiki/fields/66-earth-of-abyss|Earth of Abyss]] (gate 771 → 761), [[wiki/fields/68-frostwind-east|Frostwind - East]] (gate 772 → 780)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/56-snowflower-plain|Snowflower Plain]], [[wiki/fields/66-earth-of-abyss|Earth of Abyss]], [[wiki/fields/68-frostwind-east|Frostwind - East]]

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
| ZP07_05 | yes | yes |
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
