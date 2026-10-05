---
title: "Fire Calling"
type: "field"
id: 61
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 61", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 61"]
name_key: "FieldName_61"
kind: "land"
scene_type: 2
max_users: 30
group: 6
scene_c4: 1
neighbours: [47, 62]
zones: [78]
segments: ["ZP01_05"]
worldmap_rect: [1170, 329, 1236, 393]
gates:
  - {"gate": 572, "x": 328.41, "z": 1361.22, "to_gate": 710, "to_field": 47, "label": "FieldName_61"}
  - {"gate": 720, "x": 429.98, "z": 1450.4, "to_gate": 711, "to_field": 62, "label": "FieldName_61"}
connections:
  - {"to": 47, "gate": 572, "to_gate": 710}
  - {"to": 62, "gate": 720, "to_gate": 711}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=a78565 type=7a94db id=6c1e67 sources=c68853 name_key=39fbea kind=8e3535 scene_type=da4b92 max_users=22d200 group=c1dfd9 scene_c4=356a19 neighbours=a96359 zones=88a276 segments=7294ce worldmap_rect=39c41f gates=1be096 connections=9b6d03 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 78](../assets/zones/78.png) |
| **Field id** | `61` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 6 (SceneList last column) |
| **Zones** | [[wiki/zones/78-field-61-fire-calling\|Field 61 (Fire Calling)]] |
| **Terrain segments** | `ZP01_05` |
| **World-map rectangle** | `[1170, 329, 1236, 393]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_61` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 572 | 328.41, 1361.22 | [[wiki/fields/47-burning-earth\|Burning Earth]] | 710 | FieldName_61 |
| 720 | 429.98, 1450.4 | [[wiki/fields/62-sad-swamp\|Sad Swamp]] | 711 | FieldName_61 |

Entered from: [[wiki/fields/47-burning-earth|Burning Earth]] (gate 710 → 572), [[wiki/fields/62-sad-swamp|Sad Swamp]] (gate 711 → 720)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/47-burning-earth|Burning Earth]], [[wiki/fields/62-sad-swamp|Sad Swamp]]

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
| ZP01_05 | yes | yes |
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
