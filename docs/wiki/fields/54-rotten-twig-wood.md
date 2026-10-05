---
title: "Rotten Twig Wood"
type: "field"
id: 54
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 54", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 54"]
name_key: "FieldName_54"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 1
neighbours: [53, 57, 55]
zones: [72]
segments: ["ZP14_04"]
worldmap_rect: [1261, 726, 1322, 801]
gates:
  - {"gate": 631, "x": 3741.21, "z": 1196.93, "to_gate": 640, "to_field": 53, "label": "FieldName_54"}
  - {"gate": 651, "x": 3660.51, "z": 1089.38, "to_gate": 641, "to_field": 55, "label": "FieldName_54"}
  - {"gate": 670, "x": 3797.9, "z": 1077.48, "to_gate": 642, "to_field": 57, "label": "FieldName_54"}
connections:
  - {"to": 53, "gate": 631, "to_gate": 640}
  - {"to": 55, "gate": 651, "to_gate": 641}
  - {"to": 57, "gate": 670, "to_gate": 642}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=19f3ce type=7a94db id=80e28a sources=b7d278 name_key=16ce14 kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=356a19 neighbours=ebaad5 zones=75527e segments=61df0f worldmap_rect=157ca4 gates=518820 connections=ce8f75 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 72](../assets/zones/72.png) |
| **Field id** | `54` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/72-field-54-rotten-twig-wood\|Field 54 (Rotten Twig Wood)]] |
| **Terrain segments** | `ZP14_04` |
| **World-map rectangle** | `[1261, 726, 1322, 801]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_54` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 631 | 3741.21, 1196.93 | [[wiki/fields/53-ashcolor-hill\|Ashcolor Hill]] | 640 | FieldName_54 |
| 651 | 3660.51, 1089.38 | [[wiki/fields/55-sun-hill\|Sun Hill]] | 641 | FieldName_54 |
| 670 | 3797.9, 1077.48 | [[wiki/fields/57-raging-wind\|Raging Wind]] | 642 | FieldName_54 |

Entered from: [[wiki/fields/53-ashcolor-hill|Ashcolor Hill]] (gate 640 → 631), [[wiki/fields/55-sun-hill|Sun Hill]] (gate 641 → 651), [[wiki/fields/57-raging-wind|Raging Wind]] (gate 642 → 670)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/53-ashcolor-hill|Ashcolor Hill]], [[wiki/fields/57-raging-wind|Raging Wind]], [[wiki/fields/55-sun-hill|Sun Hill]]

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
| ZP14_04 | yes | yes |

### Mentioned in

- [[gameplay/sources|Sources and gaps]] (by name)
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
