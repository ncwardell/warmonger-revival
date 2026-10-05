---
title: "Eternal River - Upper Region"
type: "field"
id: 14
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 14", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 14"]
name_key: "FieldName_14"
kind: "land"
scene_type: 2
max_users: 30
group: 7
neighbours: [84, 13, 19]
zones: [39]
segments: ["ZP14_02"]
worldmap_rect: [750, 350, 825, 416]
gates:
  - {"gate": 231, "x": 3648.37, "z": 559.81, "to_gate": 241, "to_field": 13, "label": "FieldName_14"}
  - {"gate": 290, "x": 3759.9, "z": 571.1, "to_gate": 242, "to_field": 19, "label": "FieldName_14"}
  - {"gate": 941, "x": 3760.31, "z": 673.16, "to_gate": 240, "to_field": 84, "label": "FieldName_14"}
connections:
  - {"to": 13, "gate": 231, "to_gate": 241}
  - {"to": 19, "gate": 290, "to_gate": 242}
  - {"to": 84, "gate": 941, "to_gate": 240}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=fe9680 type=7a94db id=fa35e1 sources=6ba324 name_key=0a4289 kind=8e3535 scene_type=da4b92 max_users=22d200 group=902ba3 neighbours=7f5c57 zones=44b878 segments=ed90f2 worldmap_rect=4280cc gates=bbc753 connections=4010b6 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 39](wiki/assets/zones/39.png) |
| **Field id** | `14` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 7 (SceneList last column) |
| **Zones** | [[wiki/zones/39-field-14-eternal-river-upper-region\|Field 14 (Eternal River - Upper Region)]] |
| **Terrain segments** | `ZP14_02` |
| **World-map rectangle** | `[750, 350, 825, 416]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_14` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 231 | 3648.37, 559.81 | [[wiki/fields/13-punish-peak\|Punish Peak]] | 241 | FieldName_14 |
| 290 | 3759.9, 571.1 | [[wiki/fields/19-death-valley\|Death Valley]] | 242 | FieldName_14 |
| 941 | 3760.31, 673.16 | [[wiki/fields/84-eternal-lake\|Eternal Lake]] | 240 | FieldName_14 |

Entered from: [[wiki/fields/13-punish-peak|Punish Peak]] (gate 241 → 231), [[wiki/fields/19-death-valley|Death Valley]] (gate 242 → 290), [[wiki/fields/84-eternal-lake|Eternal Lake]] (gate 240 → 941)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/84-eternal-lake|Eternal Lake]], [[wiki/fields/13-punish-peak|Punish Peak]], [[wiki/fields/19-death-valley|Death Valley]]

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
| ZP14_02 | yes | yes |

### Mentioned in

- [[gameplay/video-fort-war#Structures|Video notes: fortress war series (ZonderCoRe) § Structures]] — at [3:56](https://www.youtube.com/watch?v=7f7QwwUyYBg&t=236s)
- [[gameplay/video-fort-war#Eternal River – Upper Region (field 14, ZoneDB 39, rectangle x 3616–3775, z 544–703)|Video notes: fortress war series (ZonderCoRe) § Eternal River – Upper Region (field 14, ZoneDB 39, rectangle x 3616–3775, z 544–703)]]
- [[gameplay/video-tutorial-walkthrough#Steps|Video notes: tutorial walkthrough (Bravely Forward 2) § Steps]] — at [32:25](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1945s)
- [[gameplay/video-tutorial-walkthrough#Teleports used|Video notes: tutorial walkthrough (Bravely Forward 2) § Teleports used]] — at [32:55](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1975s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] (by name)
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
