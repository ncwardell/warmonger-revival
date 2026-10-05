---
title: "Spirit's Temple"
type: "field"
id: 29
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 29", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 29"]
name_key: "FieldName_29"
kind: "land"
scene_type: 2
max_users: 30
group: 9
neighbours: [28, 30]
zones: [52]
segments: ["ZP09_03"]
worldmap_rect: [724, 618, 796, 678]
gates:
  - {"gate": 381, "x": 2363.18, "z": 943.53, "to_gate": 390, "to_field": 28, "label": "FieldName_29"}
  - {"gate": 401, "x": 2469.21, "z": 814.39, "to_gate": 391, "to_field": 30, "label": "FieldName_29"}
connections:
  - {"to": 28, "gate": 381, "to_gate": 390}
  - {"to": 30, "gate": 401, "to_gate": 391}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=2feac9 type=7a94db id=7719a1 sources=f5c4a8 name_key=127d92 kind=8e3535 scene_type=da4b92 max_users=22d200 group=0ade7c neighbours=3f3d80 zones=8ca136 segments=6ffdfe worldmap_rect=d851d8 gates=e646e8 connections=e33e4f npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 52](../assets/zones/52.png) |
| **Field id** | `29` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 9 (SceneList last column) |
| **Zones** | [[wiki/zones/52-field-29-spirit-s-temple\|Field 29 (Spirit's Temple)]] |
| **Terrain segments** | `ZP09_03` |
| **World-map rectangle** | `[724, 618, 796, 678]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_29` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 381 | 2363.18, 943.53 | [[wiki/fields/28-spirit-s-refuge\|Spirit's Refuge]] | 390 | FieldName_29 |
| 401 | 2469.21, 814.39 | [[wiki/fields/30-wind-valley\|Wind Valley]] | 391 | FieldName_29 |

Entered from: [[wiki/fields/28-spirit-s-refuge|Spirit's Refuge]] (gate 390 → 381), [[wiki/fields/30-wind-valley|Wind Valley]] (gate 391 → 401)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/28-spirit-s-refuge|Spirit's Refuge]], [[wiki/fields/30-wind-valley|Wind Valley]]

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
| ZP09_03 | yes | yes |
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
