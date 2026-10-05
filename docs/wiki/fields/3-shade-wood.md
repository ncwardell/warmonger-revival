---
title: "Shade Wood"
type: "field"
id: 3
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 3", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 3"]
name_key: "FieldName_3"
kind: "land"
scene_type: 2
max_users: 30
group: 1
scene_c4: 1
neighbours: [2, 6, 4]
zones: [32]
segments: ["ZP03_02"]
worldmap_rect: [766, 54, 829, 86]
gates:
  - {"gate": 121, "x": 814.55, "z": 644.79, "to_gate": 130, "to_field": 2, "label": "FieldName_3"}
  - {"gate": 140, "x": 942.68, "z": 677.05, "to_gate": 131, "to_field": 4, "label": "FieldName_3"}
  - {"gate": 161, "x": 866.26, "z": 561.77, "to_gate": 132, "to_field": 6, "label": "FieldName_3"}
connections:
  - {"to": 2, "gate": 121, "to_gate": 130}
  - {"to": 4, "gate": 140, "to_gate": 131}
  - {"to": 6, "gate": 161, "to_gate": 132}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=4e339d type=7a94db id=77de68 sources=f94506 name_key=2c7ba6 kind=8e3535 scene_type=da4b92 max_users=22d200 group=356a19 scene_c4=356a19 neighbours=0ba716 zones=b891b8 segments=a25a66 worldmap_rect=7adad3 gates=10789b connections=733f60 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 32](../assets/zones/32.png) |
| **Field id** | `3` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 1 (SceneList last column) |
| **Zones** | [[wiki/zones/32-field-03-shade-wood\|Field 03 (Shade Wood)]] |
| **Terrain segments** | `ZP03_02` |
| **World-map rectangle** | `[766, 54, 829, 86]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_3` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 121 | 814.55, 644.79 | [[wiki/fields/2-exit-of-shadewood\|Exit of Shadewood]] | 130 | FieldName_3 |
| 140 | 942.68, 677.05 | [[wiki/fields/4-enter-of-shadewood\|Enter of Shadewood]] | 131 | FieldName_3 |
| 161 | 866.26, 561.77 | [[wiki/fields/6-skywing-yard\|Skywing Yard]] | 132 | FieldName_3 |

Entered from: [[wiki/fields/2-exit-of-shadewood|Exit of Shadewood]] (gate 130 → 121), [[wiki/fields/4-enter-of-shadewood|Enter of Shadewood]] (gate 131 → 140), [[wiki/fields/6-skywing-yard|Skywing Yard]] (gate 132 → 161)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/2-exit-of-shadewood|Exit of Shadewood]], [[wiki/fields/6-skywing-yard|Skywing Yard]], [[wiki/fields/4-enter-of-shadewood|Enter of Shadewood]]

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
| ZP03_02 | yes | yes |

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
