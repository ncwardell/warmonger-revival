---
title: "Totem Pole Peak"
type: "field"
id: 52
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 52", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 52"]
name_key: "FieldName_52"
kind: "land"
scene_type: 2
max_users: 30
group: 4
scene_c4: 1
neighbours: [51, 55]
zones: [70]
segments: ["ZP12_04"]
worldmap_rect: [1202, 796, 1266, 861]
gates:
  - {"gate": 612, "x": 3157.01, "z": 1223.58, "to_gate": 620, "to_field": 51, "label": "FieldName_52"}
  - {"gate": 650, "x": 3223.57, "z": 1106.83, "to_gate": 621, "to_field": 55, "label": "FieldName_52"}
connections:
  - {"to": 51, "gate": 612, "to_gate": 620}
  - {"to": 55, "gate": 650, "to_gate": 621}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=a8e1b0 type=7a94db id=a93349 sources=fe9cc8 name_key=97c415 kind=8e3535 scene_type=da4b92 max_users=22d200 group=1b6453 scene_c4=356a19 neighbours=8e7693 zones=36f14e segments=d79140 worldmap_rect=bdfcd5 gates=49f60b connections=ea7617 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 70](wiki/assets/zones/70.png) |
| **Field id** | `52` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 4 (SceneList last column) |
| **Zones** | [[wiki/zones/70-field-52-totem-pole-peak\|Field 52 (Totem Pole Peak)]] |
| **Terrain segments** | `ZP12_04` |
| **World-map rectangle** | `[1202, 796, 1266, 861]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_52` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 612 | 3157.01, 1223.58 | [[wiki/fields/51-sunup-campsite\|Sunup Campsite]] | 620 | FieldName_52 |
| 650 | 3223.57, 1106.83 | [[wiki/fields/55-sun-hill\|Sun Hill]] | 621 | FieldName_52 |

Entered from: [[wiki/fields/51-sunup-campsite|Sunup Campsite]] (gate 620 → 612), [[wiki/fields/55-sun-hill|Sun Hill]] (gate 621 → 650)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/51-sunup-campsite|Sunup Campsite]], [[wiki/fields/55-sun-hill|Sun Hill]]

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
| ZP12_04 | yes | yes |
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
