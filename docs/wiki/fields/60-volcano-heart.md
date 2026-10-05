---
title: "Volcano Heart"
type: "field"
id: 60
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 60", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 60"]
name_key: "FieldName_60"
kind: "land"
scene_type: 2
max_users: 30
group: 6
scene_c4: 2
neighbours: [48, 59, 63]
zones: [77]
segments: ["ZP20_04"]
worldmap_rect: [1219, 461, 1302, 539]
gates:
  - {"gate": 582, "x": 5178.04, "z": 1179.69, "to_gate": 700, "to_field": 48, "label": "FieldName_60"}
  - {"gate": 691, "x": 5233.7, "z": 1102.5, "to_gate": 701, "to_field": 59, "label": "FieldName_60"}
  - {"gate": 730, "x": 5287.37, "z": 1206.32, "to_gate": 702, "to_field": 63, "label": "FieldName_60"}
connections:
  - {"to": 48, "gate": 582, "to_gate": 700}
  - {"to": 59, "gate": 691, "to_gate": 701}
  - {"to": 63, "gate": 730, "to_gate": 702}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=0068b9 type=7a94db id=e6c3dd sources=cf7484 name_key=8e5e22 kind=8e3535 scene_type=da4b92 max_users=22d200 group=c1dfd9 scene_c4=da4b92 neighbours=819225 zones=4c5ce1 segments=28a847 worldmap_rect=d3bf3f gates=1e51da connections=3b22c0 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 77](wiki/assets/zones/77.png) |
| **Field id** | `60` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 6 (SceneList last column) |
| **Zones** | [[wiki/zones/77-field-60-volcano-heart\|Field 60 (Volcano Heart)]] |
| **Terrain segments** | `ZP20_04` |
| **World-map rectangle** | `[1219, 461, 1302, 539]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_60` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 582 | 5178.04, 1179.69 | [[wiki/fields/48-ashes-ruin\|Ashes Ruin]] | 700 | FieldName_60 |
| 691 | 5233.7, 1102.5 | [[wiki/fields/59-fire-spirit\|Fire Spirit]] | 701 | FieldName_60 |
| 730 | 5287.37, 1206.32 | [[wiki/fields/63-cracked-earth\|Cracked Earth]] | 702 | FieldName_60 |

Entered from: [[wiki/fields/48-ashes-ruin|Ashes Ruin]] (gate 700 → 582), [[wiki/fields/59-fire-spirit|Fire Spirit]] (gate 701 → 691), [[wiki/fields/63-cracked-earth|Cracked Earth]] (gate 702 → 730)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/48-ashes-ruin|Ashes Ruin]], [[wiki/fields/59-fire-spirit|Fire Spirit]], [[wiki/fields/63-cracked-earth|Cracked Earth]]

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
| ZP20_04 | yes | yes |
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
