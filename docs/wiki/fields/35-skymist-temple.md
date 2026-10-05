---
title: "Skymist Temple"
type: "field"
id: 35
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 35", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 35"]
name_key: "FieldName_35"
kind: "land"
scene_type: 2
max_users: 30
group: 0
scene_c4: 1
neighbours: [33, 37]
zones: [23]
segments: ["ZP15_03"]
worldmap_rect: [674, 817, 732, 878]
gates:
  - {"gate": 432, "x": 3905.24, "z": 940.23, "to_gate": 450, "to_field": 33, "label": "FieldName_35"}
  - {"gate": 470, "x": 4012.86, "z": 821.91, "to_gate": 451, "to_field": 37, "label": "FieldName_35"}
connections:
  - {"to": 33, "gate": 432, "to_gate": 450}
  - {"to": 37, "gate": 470, "to_gate": 451}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=22b4fe type=7a94db id=972a67 sources=991482 name_key=e18455 kind=8e3535 scene_type=da4b92 max_users=22d200 group=b6589f scene_c4=356a19 neighbours=c75fe9 zones=d5525d segments=41f2f2 worldmap_rect=e87e74 gates=1ecbdd connections=1f2a79 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 23](../assets/zones/23.png) |
| **Field id** | `35` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 0 (SceneList last column) |
| **Zones** | [[wiki/zones/23-field-35-skymist-temple\|Field 35 (Skymist Temple)]] |
| **Terrain segments** | `ZP15_03` |
| **World-map rectangle** | `[674, 817, 732, 878]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_35` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 432 | 3905.24, 940.23 | [[wiki/fields/33-dreamer-s-refuge\|Dreamer's Refuge]] | 450 | FieldName_35 |
| 470 | 4012.86, 821.91 | [[wiki/fields/37-turncoat-place\|Turncoat Place]] | 451 | FieldName_35 |

Entered from: [[wiki/fields/33-dreamer-s-refuge|Dreamer's Refuge]] (gate 450 → 432), [[wiki/fields/37-turncoat-place|Turncoat Place]] (gate 451 → 470)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/33-dreamer-s-refuge|Dreamer's Refuge]], [[wiki/fields/37-turncoat-place|Turncoat Place]]

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
| ZP15_03 | yes | yes |
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
