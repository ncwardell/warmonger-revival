---
title: "Enter of Twilight"
type: "field"
id: 41
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 41", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 41"]
name_key: "FieldName_41"
kind: "land"
scene_type: 2
max_users: 30
group: 4
scene_c4: 1
neighbours: [40, 43, 44]
zones: [60]
segments: ["ZP01_04"]
worldmap_rect: [979, 772, 1049, 844]
gates:
  - {"gate": 501, "x": 303.88, "z": 1077.92, "to_gate": 510, "to_field": 40, "label": "FieldName_41"}
  - {"gate": 530, "x": 430.66, "z": 1196.81, "to_gate": 511, "to_field": 43, "label": "FieldName_41"}
  - {"gate": 540, "x": 321.99, "z": 1190.65, "to_gate": 512, "to_field": 44, "label": "FieldName_41"}
connections:
  - {"to": 40, "gate": 501, "to_gate": 510}
  - {"to": 43, "gate": 530, "to_gate": 511}
  - {"to": 44, "gate": 540, "to_gate": 512}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=8f6bfd type=7a94db id=761f22 sources=47ddc6 name_key=40f26b kind=8e3535 scene_type=da4b92 max_users=22d200 group=1b6453 scene_c4=356a19 neighbours=3d2be4 zones=77eeff segments=7a0989 worldmap_rect=81af39 gates=5ca1a0 connections=f23424 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 60](../assets/zones/60.png) |
| **Field id** | `41` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 4 (SceneList last column) |
| **Zones** | [[wiki/zones/60-field-41-enter-of-twilight\|Field 41 (Enter of Twilight)]] |
| **Terrain segments** | `ZP01_04` |
| **World-map rectangle** | `[979, 772, 1049, 844]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_41` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 501 | 303.88, 1077.92 | [[wiki/fields/40-angry-river-upper-region\|Angry River - Upper Region]] | 510 | FieldName_41 |
| 530 | 430.66, 1196.81 | [[wiki/fields/43-floor-of-twilight\|Floor of Twilight]] | 511 | FieldName_41 |
| 540 | 321.99, 1190.65 | [[wiki/fields/44-sunstone-temple\|Sunstone Temple]] | 512 | FieldName_41 |

Entered from: [[wiki/fields/40-angry-river-upper-region|Angry River - Upper Region]] (gate 510 → 501), [[wiki/fields/43-floor-of-twilight|Floor of Twilight]] (gate 511 → 530), [[wiki/fields/44-sunstone-temple|Sunstone Temple]] (gate 512 → 540)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/40-angry-river-upper-region|Angry River - Upper Region]], [[wiki/fields/43-floor-of-twilight|Floor of Twilight]], [[wiki/fields/44-sunstone-temple|Sunstone Temple]]

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
| ZP01_04 | yes | yes |
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
