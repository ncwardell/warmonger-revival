---
title: "Floor of Twilight"
type: "field"
id: 43
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 43", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 43"]
name_key: "FieldName_43"
kind: "land"
scene_type: 2
max_users: 30
group: 4
scene_c4: 2
neighbours: [41, 51, 42]
zones: [62]
segments: ["ZP03_04"]
worldmap_rect: [1091, 844, 1228, 948]
gates:
  - {"gate": 511, "x": 864.31, "z": 1191.39, "to_gate": 530, "to_field": 41, "label": "FieldName_43"}
  - {"gate": 521, "x": 874.49, "z": 1070.85, "to_gate": 531, "to_field": 42, "label": "FieldName_43"}
  - {"gate": 610, "x": 976.52, "z": 1160.67, "to_gate": 532, "to_field": 51, "label": "FieldName_43"}
connections:
  - {"to": 41, "gate": 511, "to_gate": 530}
  - {"to": 42, "gate": 521, "to_gate": 531}
  - {"to": 51, "gate": 610, "to_gate": 532}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=2947ec type=7a94db id=0286dd sources=b45585 name_key=4c540b kind=8e3535 scene_type=da4b92 max_users=22d200 group=1b6453 scene_c4=da4b92 neighbours=e69a54 zones=0ff587 segments=cc2f64 worldmap_rect=c2935f gates=ed1af5 connections=6287dc npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 62](wiki/assets/zones/62.png) |
| **Field id** | `43` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 4 (SceneList last column) |
| **Zones** | [[wiki/zones/62-field-43-floor-of-twilight\|Field 43 (Floor of Twilight)]] |
| **Terrain segments** | `ZP03_04` |
| **World-map rectangle** | `[1091, 844, 1228, 948]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_43` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 511 | 864.31, 1191.39 | [[wiki/fields/41-enter-of-twilight\|Enter of Twilight]] | 530 | FieldName_43 |
| 521 | 874.49, 1070.85 | [[wiki/fields/42-crater-of-abaddon\|Crater of Abaddon]] | 531 | FieldName_43 |
| 610 | 976.52, 1160.67 | [[wiki/fields/51-sunup-campsite\|Sunup Campsite]] | 532 | FieldName_43 |

Entered from: [[wiki/fields/41-enter-of-twilight|Enter of Twilight]] (gate 530 → 511), [[wiki/fields/42-crater-of-abaddon|Crater of Abaddon]] (gate 531 → 521), [[wiki/fields/51-sunup-campsite|Sunup Campsite]] (gate 532 → 610)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/41-enter-of-twilight|Enter of Twilight]], [[wiki/fields/51-sunup-campsite|Sunup Campsite]], [[wiki/fields/42-crater-of-abaddon|Crater of Abaddon]]

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
| ZP03_04 | yes | yes |

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
