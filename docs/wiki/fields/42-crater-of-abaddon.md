---
title: "Crater of Abaddon"
type: "field"
id: 42
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 42", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 42"]
name_key: "FieldName_42"
kind: "land"
scene_type: 2
max_users: 30
group: 6
scene_c4: 1
neighbours: [40, 43]
zones: [61]
segments: ["ZP02_04"]
worldmap_rect: [990, 931, 1129, 996]
gates:
  - {"gate": 502, "x": 570.7, "z": 1204.52, "to_gate": 520, "to_field": 40, "label": "FieldName_42"}
  - {"gate": 531, "x": 691.69, "z": 1082.49, "to_gate": 521, "to_field": 43, "label": "FieldName_42"}
connections:
  - {"to": 40, "gate": 502, "to_gate": 520}
  - {"to": 43, "gate": 531, "to_gate": 521}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=1af78d type=7a94db id=92cfce sources=64dbdd name_key=044eb7 kind=8e3535 scene_type=da4b92 max_users=22d200 group=c1dfd9 scene_c4=356a19 neighbours=4ed04a zones=065175 segments=64c884 worldmap_rect=8a4f8a gates=975a43 connections=d39349 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 61](wiki/assets/zones/61.png) |
| **Field id** | `42` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 6 (SceneList last column) |
| **Zones** | [[wiki/zones/61-field-42-crater-of-abaddon\|Field 42 (Crater of Abaddon)]] |
| **Terrain segments** | `ZP02_04` |
| **World-map rectangle** | `[990, 931, 1129, 996]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_42` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 502 | 570.7, 1204.52 | [[wiki/fields/40-angry-river-upper-region\|Angry River - Upper Region]] | 520 | FieldName_42 |
| 531 | 691.69, 1082.49 | [[wiki/fields/43-floor-of-twilight\|Floor of Twilight]] | 521 | FieldName_42 |

Entered from: [[wiki/fields/40-angry-river-upper-region|Angry River - Upper Region]] (gate 520 → 502), [[wiki/fields/43-floor-of-twilight|Floor of Twilight]] (gate 521 → 531)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/40-angry-river-upper-region|Angry River - Upper Region]], [[wiki/fields/43-floor-of-twilight|Floor of Twilight]]

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
| ZP02_04 | yes | yes |

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
