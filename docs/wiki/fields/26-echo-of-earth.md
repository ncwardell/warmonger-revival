---
title: "Echo of Earth"
type: "field"
id: 26
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 26", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 26"]
name_key: "FieldName_26"
kind: "land"
scene_type: 2
max_users: 30
group: 5
scene_c4: 1
neighbours: [21, 22, 46]
zones: [21]
segments: ["ZP06_03"]
worldmap_rect: [1009, 462, 1096, 511]
gates:
  - {"gate": 311, "x": 1590.31, "z": 958.99, "to_gate": 360, "to_field": 21, "label": "FieldName_26"}
  - {"gate": 321, "x": 1701.76, "z": 976.47, "to_gate": 361, "to_field": 22, "label": "FieldName_26"}
  - {"gate": 560, "x": 1706.74, "z": 847.98, "to_gate": 362, "to_field": 46, "label": "FieldName_26"}
connections:
  - {"to": 21, "gate": 311, "to_gate": 360}
  - {"to": 22, "gate": 321, "to_gate": 361}
  - {"to": 46, "gate": 560, "to_gate": 362}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=a4cabc type=7a94db id=887309 sources=f00ec8 name_key=d5dbe8 kind=8e3535 scene_type=da4b92 max_users=22d200 group=ac3478 scene_c4=356a19 neighbours=9313bd zones=6c9878 segments=49e07e worldmap_rect=48babc gates=91fe45 connections=4e6f7b npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 21](wiki/assets/zones/21.png) |
| **Field id** | `26` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 5 (SceneList last column) |
| **Zones** | [[wiki/zones/21-field-26-echo-of-earth\|Field 26 (Echo of Earth)]] |
| **Terrain segments** | `ZP06_03` |
| **World-map rectangle** | `[1009, 462, 1096, 511]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_26` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 311 | 1590.31, 958.99 | [[wiki/fields/21-vortex-plain\|Vortex Plain]] | 360 | FieldName_26 |
| 321 | 1701.76, 976.47 | [[wiki/fields/22-afterlife-hill\|Afterlife Hill]] | 361 | FieldName_26 |
| 560 | 1706.74, 847.98 | [[wiki/fields/46-spider-nest\|Spider Nest]] | 362 | FieldName_26 |

Entered from: [[wiki/fields/21-vortex-plain|Vortex Plain]] (gate 360 → 311), [[wiki/fields/22-afterlife-hill|Afterlife Hill]] (gate 361 → 321), [[wiki/fields/46-spider-nest|Spider Nest]] (gate 362 → 560)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/21-vortex-plain|Vortex Plain]], [[wiki/fields/22-afterlife-hill|Afterlife Hill]], [[wiki/fields/46-spider-nest|Spider Nest]]

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
| ZP06_03 | yes | yes |

### Mentioned in

- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] (by name)
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
