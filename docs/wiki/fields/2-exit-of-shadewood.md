---
title: "Exit of Shadewood"
type: "field"
id: 2
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 2", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 2"]
name_key: "FieldName_2"
kind: "land"
scene_type: 2
max_users: 30
group: 1
scene_c4: 2
neighbours: [1, 3]
zones: [15]
segments: ["ZP02_02"]
worldmap_rect: [686, 73, 746, 129]
gates:
  - {"gate": 110, "x": 557.36, "z": 570.21, "to_gate": 120, "to_field": 1, "label": "FieldName_2"}
  - {"gate": 130, "x": 690.63, "z": 666.43, "to_gate": 121, "to_field": 3, "label": "FieldName_2"}
connections:
  - {"to": 1, "gate": 110, "to_gate": 120}
  - {"to": 3, "gate": 130, "to_gate": 121}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=feb085 type=7a94db id=da4b92 sources=a3aa2f name_key=f3e3a7 kind=8e3535 scene_type=da4b92 max_users=22d200 group=356a19 scene_c4=da4b92 neighbours=993179 zones=017b8e segments=a92acc worldmap_rect=87addf gates=4c1068 connections=9a17c5 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 15](../assets/zones/15.png) |
| **Field id** | `2` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 1 (SceneList last column) |
| **Zones** | [[wiki/zones/15-field-02-exit-of-shadewood\|Field 02 (Exit of Shadewood)]] |
| **Terrain segments** | `ZP02_02` |
| **World-map rectangle** | `[686, 73, 746, 129]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_2` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 110 | 557.36, 570.21 | [[wiki/fields/1-end-of-earth\|End of Earth]] | 120 | FieldName_2 |
| 130 | 690.63, 666.43 | [[wiki/fields/3-shade-wood\|Shade Wood]] | 121 | FieldName_2 |

Entered from: [[wiki/fields/1-end-of-earth|End of Earth]] (gate 120 → 110), [[wiki/fields/3-shade-wood|Shade Wood]] (gate 121 → 130)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/1-end-of-earth|End of Earth]], [[wiki/fields/3-shade-wood|Shade Wood]]

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
| ZP02_02 | yes | yes |

### Mentioned in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]] (by name)
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
