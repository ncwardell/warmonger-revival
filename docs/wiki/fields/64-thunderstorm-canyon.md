---
title: "Thunderstorm Canyon"
type: "field"
id: 64
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 64", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 64"]
name_key: "FieldName_64"
kind: "land"
scene_type: 2
max_users: 30
group: 5
scene_c4: 2
neighbours: [63, 59, 71]
zones: [81]
segments: ["ZP04_05"]
worldmap_rect: [1396, 452, 1447, 528]
gates:
  - {"gate": 692, "x": 1186.27, "z": 1358.1, "to_gate": 740, "to_field": 59, "label": "FieldName_64"}
  - {"gate": 731, "x": 1071.51, "z": 1462.19, "to_gate": 741, "to_field": 63, "label": "FieldName_64"}
  - {"gate": 810, "x": 1189.79, "z": 1473.66, "to_gate": 742, "to_field": 71, "label": "FieldName_64"}
connections:
  - {"to": 59, "gate": 692, "to_gate": 740}
  - {"to": 63, "gate": 731, "to_gate": 741}
  - {"to": 71, "gate": 810, "to_gate": 742}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=2fa6ad type=7a94db id=c66c65 sources=48819c name_key=56af4f kind=8e3535 scene_type=da4b92 max_users=22d200 group=ac3478 scene_c4=da4b92 neighbours=066fc2 zones=350acf segments=d3c589 worldmap_rect=b99f9b gates=321c86 connections=f708ad npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 81](../assets/zones/81.png) |
| **Field id** | `64` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 5 (SceneList last column) |
| **Zones** | [[wiki/zones/81-field-64-thunderstorm-canyon\|Field 64 (Thunderstorm Canyon)]] |
| **Terrain segments** | `ZP04_05` |
| **World-map rectangle** | `[1396, 452, 1447, 528]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_64` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 692 | 1186.27, 1358.1 | [[wiki/fields/59-fire-spirit\|Fire Spirit]] | 740 | FieldName_64 |
| 731 | 1071.51, 1462.19 | [[wiki/fields/63-cracked-earth\|Cracked Earth]] | 741 | FieldName_64 |
| 810 | 1189.79, 1473.66 | [[wiki/fields/71-thunderstorm-door\|Thunderstorm door]] | 742 | FieldName_64 |

Entered from: [[wiki/fields/59-fire-spirit|Fire Spirit]] (gate 740 → 692), [[wiki/fields/63-cracked-earth|Cracked Earth]] (gate 741 → 731), [[wiki/fields/71-thunderstorm-door|Thunderstorm door]] (gate 742 → 810)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/63-cracked-earth|Cracked Earth]], [[wiki/fields/59-fire-spirit|Fire Spirit]], [[wiki/fields/71-thunderstorm-door|Thunderstorm door]]

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
| ZP04_05 | yes | yes |
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
