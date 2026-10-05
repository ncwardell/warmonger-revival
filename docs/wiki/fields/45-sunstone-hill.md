---
title: "Sunstone Hill"
type: "field"
id: 45
status: "partial"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 45", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 45", "image: [[gameplay/maps-and-dungeons]] §1; [[gameplay/lords-of-the-land]] §6"]
name_key: "FieldName_45"
kind: "land"
scene_type: 2
max_users: 30
group: 8
neighbours: [39, 44, 49]
zones: [64]
segments: ["ZP05_04"]
worldmap_rect: [1065, 614, 1146, 674]
gates:
  - {"gate": 492, "x": 1385.23, "z": 1073.94, "to_gate": 551, "to_field": 44, "label": "FieldName_45"}
  - {"gate": 541, "x": 1373.6, "z": 1190.92, "to_gate": 550, "to_field": 39, "label": "FieldName_45"}
  - {"gate": 590, "x": 1486.42, "z": 1159.8, "to_gate": 552, "to_field": 49, "label": "FieldName_45"}
connections:
  - {"to": 44, "gate": 492, "to_gate": 551}
  - {"to": 39, "gate": 541, "to_gate": 550}
  - {"to": 49, "gate": 590, "to_gate": 552}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=5a9a0b type=7a94db id=fb6443 sources=cc346c name_key=c156e8 kind=8e3535 scene_type=da4b92 max_users=22d200 group=fe5dbb neighbours=f50a12 zones=85cf27 segments=edd5f4 worldmap_rect=4f9020 gates=b61a32 connections=9be26d npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 64](../assets/zones/64.png) |
| **Field id** | `45` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 8 (SceneList last column) |
| **Zones** | [[wiki/zones/64-field-45-sunstone-hill\|Field 45 (Sunstone Hill)]] |
| **Terrain segments** | `ZP05_04` |
| **World-map rectangle** | `[1065, 614, 1146, 674]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_45` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 492 | 1385.23, 1073.94 | [[wiki/fields/44-sunstone-temple\|Sunstone Temple]] | 551 | FieldName_45 |
| 541 | 1373.6, 1190.92 | [[wiki/fields/39-sunstone-gateway\|Sunstone gateway]] | 550 | FieldName_45 |
| 590 | 1486.42, 1159.8 | [[wiki/fields/49-weltering-flame\|Weltering Flame]] | 552 | FieldName_45 |

Entered from: [[wiki/fields/39-sunstone-gateway|Sunstone gateway]] (gate 550 → 541), [[wiki/fields/44-sunstone-temple|Sunstone Temple]] (gate 551 → 492), [[wiki/fields/49-weltering-flame|Weltering Flame]] (gate 552 → 590)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/39-sunstone-gateway|Sunstone gateway]], [[wiki/fields/44-sunstone-temple|Sunstone Temple]], [[wiki/fields/49-weltering-flame|Weltering Flame]]

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
| ZP05_04 | yes | yes |

### Mentioned in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
<!-- generated:end -->

## Notes

- Part of the grey band between Arslan and Erion in spring 2018 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §1), and the October 2016 Crush map marks a defended fort near it ([[gameplay/lords-of-the-land|Lords of the Land]] §6). *image*

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
