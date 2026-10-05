---
title: "Thunderstorm door"
type: "field"
id: 71
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 71", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 71"]
name_key: "FieldName_71"
kind: "land"
scene_type: 2
max_users: 30
group: 5
scene_c4: 1
neighbours: [64, 70, 75]
zones: [86]
segments: ["ZP11_05"]
worldmap_rect: [1453, 398, 1574, 490]
gates:
  - {"gate": 742, "x": 2876.61, "z": 1332.58, "to_gate": 810, "to_field": 64, "label": "FieldName_71"}
  - {"gate": 801, "x": 2996.87, "z": 1342.03, "to_gate": 811, "to_field": 70, "label": "FieldName_71"}
  - {"gate": 850, "x": 2960.92, "z": 1449.59, "to_gate": 812, "to_field": 75, "label": "FieldName_71"}
connections:
  - {"to": 64, "gate": 742, "to_gate": 810}
  - {"to": 70, "gate": 801, "to_gate": 811}
  - {"to": 75, "gate": 850, "to_gate": 812}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=37e3d6 type=7a94db id=d02560 sources=5807c7 name_key=eb1009 kind=8e3535 scene_type=da4b92 max_users=22d200 group=ac3478 scene_c4=356a19 neighbours=8e40a1 zones=b56b7b segments=ed9c0b worldmap_rect=d57312 gates=729ebd connections=c9a3da npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 86](../assets/zones/86.png) |
| **Field id** | `71` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 5 (SceneList last column) |
| **Zones** | [[wiki/zones/86-field-71-thunderstorm-door\|Field 71 (Thunderstorm door)]] |
| **Terrain segments** | `ZP11_05` |
| **World-map rectangle** | `[1453, 398, 1574, 490]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_71` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 742 | 2876.61, 1332.58 | [[wiki/fields/64-thunderstorm-canyon\|Thunderstorm Canyon]] | 810 | FieldName_71 |
| 801 | 2996.87, 1342.03 | [[wiki/fields/70-cold-breath\|Cold Breath]] | 811 | FieldName_71 |
| 850 | 2960.92, 1449.59 | [[wiki/fields/75-thunderstorm-ruin-abyss\|Thunderstorm Ruin - Abyss]] | 812 | FieldName_71 |

Entered from: [[wiki/fields/64-thunderstorm-canyon|Thunderstorm Canyon]] (gate 810 → 742), [[wiki/fields/70-cold-breath|Cold Breath]] (gate 811 → 801), [[wiki/fields/75-thunderstorm-ruin-abyss|Thunderstorm Ruin - Abyss]] (gate 812 → 850)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/64-thunderstorm-canyon|Thunderstorm Canyon]], [[wiki/fields/70-cold-breath|Cold Breath]], [[wiki/fields/75-thunderstorm-ruin-abyss|Thunderstorm Ruin - Abyss]]

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
| ZP11_05 | yes | yes |
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
