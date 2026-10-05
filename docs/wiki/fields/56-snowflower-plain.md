---
title: "Snowflower Plain"
type: "field"
id: 56
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 56", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 56"]
name_key: "FieldName_56"
kind: "land"
scene_type: 2
max_users: 30
group: 2
scene_c4: 1
neighbours: [55, 67]
zones: [26]
segments: ["ZP16_04"]
worldmap_rect: [1375, 780, 1470, 847]
gates:
  - {"gate": 652, "x": 4144.62, "z": 1083.77, "to_gate": 660, "to_field": 55, "label": "FieldName_56"}
  - {"gate": 770, "x": 4267.24, "z": 1183.93, "to_gate": 661, "to_field": 67, "label": "FieldName_56"}
connections:
  - {"to": 55, "gate": 652, "to_gate": 660}
  - {"to": 67, "gate": 770, "to_gate": 661}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=887d95 type=7a94db id=54ceb9 sources=53e6b0 name_key=cef49b kind=8e3535 scene_type=da4b92 max_users=22d200 group=da4b92 scene_c4=356a19 neighbours=5392ab zones=f36b47 segments=1a4785 worldmap_rect=68d9e8 gates=f56d56 connections=9689cd npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 26](wiki/assets/zones/26.png) |
| **Field id** | `56` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 2 (SceneList last column) |
| **Zones** | [[wiki/zones/26-field-56-snowflower-plain\|Field 56 (Snowflower Plain)]] |
| **Terrain segments** | `ZP16_04` |
| **World-map rectangle** | `[1375, 780, 1470, 847]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_56` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 652 | 4144.62, 1083.77 | [[wiki/fields/55-sun-hill\|Sun Hill]] | 660 | FieldName_56 |
| 770 | 4267.24, 1183.93 | [[wiki/fields/67-icethorn-plain\|Icethorn Plain]] | 661 | FieldName_56 |

Entered from: [[wiki/fields/55-sun-hill|Sun Hill]] (gate 660 → 652), [[wiki/fields/67-icethorn-plain|Icethorn Plain]] (gate 661 → 770)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/55-sun-hill|Sun Hill]], [[wiki/fields/67-icethorn-plain|Icethorn Plain]]

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
| ZP16_04 | yes | yes |
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
