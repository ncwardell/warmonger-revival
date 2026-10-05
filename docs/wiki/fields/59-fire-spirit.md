---
title: "Fire Spirit"
type: "field"
id: 59
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 59", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 59"]
name_key: "FieldName_59"
kind: "land"
scene_type: 2
max_users: 30
group: 6
scene_c4: 1
neighbours: [49, 60, 64]
zones: [76]
segments: ["ZP19_04"]
worldmap_rect: [1278, 545, 1370, 611]
gates:
  - {"gate": 592, "x": 4927.15, "z": 1117.26, "to_gate": 690, "to_field": 49, "label": "FieldName_59"}
  - {"gate": 701, "x": 4975.86, "z": 1219.17, "to_gate": 691, "to_field": 60, "label": "FieldName_59"}
  - {"gate": 740, "x": 5045.58, "z": 1111.54, "to_gate": 692, "to_field": 64, "label": "FieldName_59"}
connections:
  - {"to": 49, "gate": 592, "to_gate": 690}
  - {"to": 60, "gate": 701, "to_gate": 691}
  - {"to": 64, "gate": 740, "to_gate": 692}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=362655 type=7a94db id=5a5b0f sources=d1ee08 name_key=8d26d6 kind=8e3535 scene_type=da4b92 max_users=22d200 group=c1dfd9 scene_c4=356a19 neighbours=0e42a9 zones=f6cf0f segments=005fc2 worldmap_rect=eec97d gates=688d9c connections=977f0d npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 76](wiki/assets/zones/76.png) |
| **Field id** | `59` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 6 (SceneList last column) |
| **Zones** | [[wiki/zones/76-field-59-fire-spirit\|Field 59 (Fire Spirit)]] |
| **Terrain segments** | `ZP19_04` |
| **World-map rectangle** | `[1278, 545, 1370, 611]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_59` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 592 | 4927.15, 1117.26 | [[wiki/fields/49-weltering-flame\|Weltering Flame]] | 690 | FieldName_59 |
| 701 | 4975.86, 1219.17 | [[wiki/fields/60-volcano-heart\|Volcano Heart]] | 691 | FieldName_59 |
| 740 | 5045.58, 1111.54 | [[wiki/fields/64-thunderstorm-canyon\|Thunderstorm Canyon]] | 692 | FieldName_59 |

Entered from: [[wiki/fields/49-weltering-flame|Weltering Flame]] (gate 690 → 592), [[wiki/fields/60-volcano-heart|Volcano Heart]] (gate 691 → 701), [[wiki/fields/64-thunderstorm-canyon|Thunderstorm Canyon]] (gate 692 → 740)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/49-weltering-flame|Weltering Flame]], [[wiki/fields/60-volcano-heart|Volcano Heart]], [[wiki/fields/64-thunderstorm-canyon|Thunderstorm Canyon]]

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
| ZP19_04 | yes | yes |
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
