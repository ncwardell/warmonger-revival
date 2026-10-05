---
title: "Evil's Wood"
type: "field"
id: 58
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 58", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 58"]
name_key: "FieldName_58"
kind: "land"
scene_type: 2
max_users: 30
group: 3
neighbours: [53, 57, 65]
zones: [75]
segments: ["ZP18_04"]
worldmap_rect: [1349, 617, 1415, 661]
gates:
  - {"gate": 632, "x": 4655.33, "z": 1164.14, "to_gate": 680, "to_field": 53, "label": "FieldName_58"}
  - {"gate": 633, "x": 4687.1, "z": 1160.43, "to_gate": 635, "to_field": 58, "label": "FieldName_58"}
  - {"gate": 634, "x": 4733.18, "z": 1131.01, "to_gate": 636, "to_field": 58, "label": "FieldName_58"}
  - {"gate": 635, "x": 4832.81, "z": 1180.49, "to_gate": 633, "to_field": 58, "label": "FieldName_58"}
  - {"gate": 636, "x": 4828.45, "z": 1080.64, "to_gate": 634, "to_field": 58, "label": "FieldName_58"}
  - {"gate": 671, "x": 4764.15, "z": 1090.62, "to_gate": 681, "to_field": 57, "label": "FieldName_58"}
  - {"gate": 750, "x": 4757.97, "z": 1195.16, "to_gate": 682, "to_field": 65, "label": "FieldName_58"}
connections:
  - {"to": 53, "gate": 632, "to_gate": 680}
  - {"to": 57, "gate": 671, "to_gate": 681}
  - {"to": 65, "gate": 750, "to_gate": 682}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=49ce15 type=7a94db id=667be5 sources=227061 name_key=39a357 kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 neighbours=6f99c3 zones=0270af segments=eac6aa worldmap_rect=3da94e gates=400499 connections=3542fc npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 75](wiki/assets/zones/75.png) |
| **Field id** | `58` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/75-field-58-evil-s-wood\|Field 58 (Evil's Wood)]] |
| **Terrain segments** | `ZP18_04` |
| **World-map rectangle** | `[1349, 617, 1415, 661]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_58` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 632 | 4655.33, 1164.14 | [[wiki/fields/53-ashcolor-hill\|Ashcolor Hill]] | 680 | FieldName_58 |
| 633 | 4687.1, 1160.43 | portal to gate 635 in this field | 635 | FieldName_58 |
| 634 | 4733.18, 1131.01 | portal to gate 636 in this field | 636 | FieldName_58 |
| 635 | 4832.81, 1180.49 | portal to gate 633 in this field | 633 | FieldName_58 |
| 636 | 4828.45, 1080.64 | portal to gate 634 in this field | 634 | FieldName_58 |
| 671 | 4764.15, 1090.62 | [[wiki/fields/57-raging-wind\|Raging Wind]] | 681 | FieldName_58 |
| 750 | 4757.97, 1195.16 | [[wiki/fields/65-canyon-of-earth\|Canyon of Earth]] | 682 | FieldName_58 |

Entered from: [[wiki/fields/53-ashcolor-hill|Ashcolor Hill]] (gate 680 → 632), [[wiki/fields/57-raging-wind|Raging Wind]] (gate 681 → 671), [[wiki/fields/65-canyon-of-earth|Canyon of Earth]] (gate 682 → 750)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/53-ashcolor-hill|Ashcolor Hill]], [[wiki/fields/57-raging-wind|Raging Wind]], [[wiki/fields/65-canyon-of-earth|Canyon of Earth]]

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
| ZP18_04 | yes | yes |
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
