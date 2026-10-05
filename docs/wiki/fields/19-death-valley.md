---
title: "Death Valley"
type: "field"
id: 19
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 19", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 19"]
name_key: "FieldName_19"
kind: "land"
scene_type: 2
max_users: 30
group: 7
scene_c4: 2
neighbours: [18, 14, 24]
zones: [44]
segments: ["ZP19_02"]
worldmap_rect: [789, 435, 833, 490]
gates:
  - {"gate": 242, "x": 5037.32, "z": 666.98, "to_gate": 290, "to_field": 14, "label": "FieldName_19"}
  - {"gate": 281, "x": 4911.55, "z": 567.72, "to_gate": 291, "to_field": 18, "label": "FieldName_19"}
  - {"gate": 340, "x": 5040.19, "z": 571.17, "to_gate": 292, "to_field": 24, "label": "FieldName_19"}
connections:
  - {"to": 14, "gate": 242, "to_gate": 290}
  - {"to": 18, "gate": 281, "to_gate": 291}
  - {"to": 24, "gate": 340, "to_gate": 292}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=e0656e type=7a94db id=b3f0c7 sources=223e9f name_key=103568 kind=8e3535 scene_type=da4b92 max_users=22d200 group=902ba3 scene_c4=da4b92 neighbours=e60d7c zones=7aed3f segments=4e87a8 worldmap_rect=3d84b6 gates=a36a68 connections=b8d981 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 44](../assets/zones/44.png) |
| **Field id** | `19` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 7 (SceneList last column) |
| **Zones** | [[wiki/zones/44-field-19-death-valley\|Field 19 (Death Valley)]] |
| **Terrain segments** | `ZP19_02` |
| **World-map rectangle** | `[789, 435, 833, 490]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_19` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 242 | 5037.32, 666.98 | [[wiki/fields/14-eternal-river-upper-region\|Eternal River - Upper Region]] | 290 | FieldName_19 |
| 281 | 4911.55, 567.72 | [[wiki/fields/18-eternal-river-lower-region\|Eternal River - Lower Region]] | 291 | FieldName_19 |
| 340 | 5040.19, 571.17 | [[wiki/fields/24-silent-garden\|Silent Garden]] | 292 | FieldName_19 |

Entered from: [[wiki/fields/14-eternal-river-upper-region|Eternal River - Upper Region]] (gate 290 → 242), [[wiki/fields/18-eternal-river-lower-region|Eternal River - Lower Region]] (gate 291 → 281), [[wiki/fields/24-silent-garden|Silent Garden]] (gate 292 → 340)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/18-eternal-river-lower-region|Eternal River - Lower Region]], [[wiki/fields/14-eternal-river-upper-region|Eternal River - Upper Region]], [[wiki/fields/24-silent-garden|Silent Garden]]

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
| ZP19_02 | yes | yes |

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
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
