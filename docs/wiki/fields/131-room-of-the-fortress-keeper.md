---
title: "Room of the Fortress Keeper"
type: "field"
id: 131
status: "partial"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 131", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 131", "guide: [[gameplay/classes-and-legions]] §4 (floor 2 hero-only boss; guardian Crusader Cherubim 825; fit of fields 130/131 to the two floors is a guess)", "client: [[gameplay/video-fort-war]] §2 (gates 1301, 1304/1305/1307)"]
name_key: "FieldName_131"
kind: "dungeon"
scene_type: 3
max_users: 30
group: 0
zones: [139]
segments: ["ZP02_15"]
gates:
  - {"gate": 1301, "x": 546.46, "z": 3867.4, "to_gate": 1301, "to_field": 131, "label": "FieldName_131"}
  - {"gate": 1304, "x": 677.7, "z": 4046.48, "to_gate": 1305, "to_field": 131, "label": "FieldName_131"}
  - {"gate": 1305, "x": 663.87, "z": 4028.04, "to_gate": 1304, "to_field": 131, "label": "FieldName_131"}
  - {"gate": 1307, "x": 669.46, "z": 4037.68, "to_gate": 0, "to_field": 131, "label": "FieldName_131"}
connections:
  - {"to": null, "gate": 1301, "kind": "exit"}
  - {"to": null, "gate": 1304, "kind": "exit"}
  - {"to": null, "gate": 1305, "kind": "exit"}
  - {"to": null, "gate": 1307, "kind": "exit"}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=22c229 type=7a94db id=e794a8 sources=24e66a name_key=989f34 kind=3e3f38 scene_type=77de68 max_users=22d200 group=b6589f zones=9bbca3 segments=e7de41 gates=ff5923 connections=c63150 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 139](wiki/assets/zones/139.png) |
| **Field id** | `131` |
| **Kind** | dungeon (SceneList type 3; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 0 (SceneList last column) |
| **Zones** | [[wiki/zones/139-room-of-the-fortress-keeper\|Room of the Fortress Keeper]] |
| **Terrain segments** | `ZP02_15` |
| **Name key** | `FieldName_131` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1301 | 546.46, 3867.4 | entrance / exit (leaving returns you to the field you came from) | 1301 | FieldName_131 |
| 1304 | 677.7, 4046.48 | entrance / exit (leaving returns you to the field you came from) | 1305 | FieldName_131 |
| 1305 | 663.87, 4028.04 | entrance / exit (leaving returns you to the field you came from) | 1304 | FieldName_131 |
| 1307 | 669.46, 4037.68 | entrance / exit (leaving returns you to the field you came from) | — | FieldName_131 |

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
| ZP02_15 | yes | yes |

### Mentioned in

- [[gameplay/video-fort-war#Video notes: fortress war series (ZonderCoRe)|Video notes: fortress war series (ZonderCoRe) § Video notes: fortress war series (ZonderCoRe)]]
- [[gameplay/video-fort-war#Room of Core (field 130 "Room of Core", ZoneDB 138 `코어실`, rectangle x 256–511, z 3840–4095)|Video notes: fortress war series (ZonderCoRe) § Room of Core (field 130 "Room of Core", ZoneDB 138 `코어실`, rectangle x 256–511, z 3840–4095)]]
- [[gameplay/video-fort-war#5. Still open|Video notes: fortress war series (ZonderCoRe) § 5. Still open]]
- [[gameplay/classes-and-legions|Classes, nations and legions]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
<!-- generated:end -->

## Notes

- Probably floor 2 of a fort siege, the guardian's room: the guides describe a very strong boss that needs heroes, and the fort guardian **Crusader Cherubim** (UnitDB 825); killing it removes one fort shield and pays part of the fort's taxes to the winners ([[gameplay/classes-and-legions|Classes and legions]] §4, fit to this field *guess*). *guide*
- Gates 1301 at (546.46, 3867.4) and 1304 / 1305 / 1307 near (664-678, 4028-4046); no video reaches this room ([[gameplay/video-fort-war|fort-war video notes]] §2). *client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

- Layout and the guardian's HP; whether 825 is the only boss here ([[gameplay/video-fort-war|fort-war video notes]] §5).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
