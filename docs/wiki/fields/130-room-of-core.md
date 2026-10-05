---
title: "Room of Core"
type: "field"
id: 130
status: "partial"
missing: ["monsters"]
sources: ["client: SceneList.cdb id 130", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 130", "video: [[gameplay/video-fort-war]] §2 Room of Core (room centres read off minimap_z138, ±5 units; Entry Core 1047, Invasion Core 1048, Heart of Magic 1049, Anti-Aircraft Defence Equipment 1036 room ±1)", "video: [[gameplay/video-fort-war]] §1, §3 (40:00 siege timer, TP reset, about 14 s respawn at the attackers' Nexus)"]
name_key: "FieldName_130"
kind: "dungeon"
scene_type: 3
max_users: 30
group: 0
zones: [138]
segments: ["ZP01_15"]
gates:
  - {"gate": 1300, "x": 362.79, "z": 3947.06, "to_gate": 1300, "to_field": 130, "label": "FieldName_130"}
  - {"gate": 1302, "x": 473.31, "z": 4058.3, "to_gate": 1303, "to_field": 130, "label": "FieldName_130"}
  - {"gate": 1303, "x": 459.92, "z": 4048.72, "to_gate": 1302, "to_field": 130, "label": "FieldName_130"}
  - {"gate": 1306, "x": 480.01, "z": 4008.33, "to_gate": 0, "to_field": 130, "label": "FieldName_130"}
connections:
  - {"to": null, "gate": 1300, "kind": "exit"}
  - {"to": null, "gate": 1302, "kind": "exit"}
  - {"to": null, "gate": 1303, "kind": "exit"}
  - {"to": null, "gate": 1306, "kind": "exit"}
npcs: []
monsters: []
spawn_points:
  - {"unit": 1047, "x": 364, "z": 3934, "count": 1, "kind": "structure", "note": "Entry Core, ring south-west"}
  - {"unit": 1048, "x": 476, "z": 4001, "count": 1, "kind": "structure", "note": "Invasion Core, ring north-east"}
  - {"unit": 1049, "x": 421, "z": 3971, "count": 1, "kind": "structure", "note": "Heart of Magic, centre room"}
  - {"unit": 1036, "x": 471, "z": 3941, "count": 1, "kind": "structure", "note": "Anti-Aircraft Defence Equipment, ring south-east (room ±1)"}
---
<!-- generated:start -->
<!-- generated-keys: title=052e88 type=7a94db id=2a7541 sources=6ae821 name_key=05bf33 kind=3e3f38 scene_type=77de68 max_users=22d200 group=b6589f zones=76eab3 segments=108ae9 gates=b7d380 connections=c07309 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 138](wiki/assets/zones/138.png) |
| **Field id** | `130` |
| **Kind** | dungeon (SceneList type 3; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 0 (SceneList last column) |
| **Zones** | [[wiki/zones/138-room-of-core\|Room of Core]] |
| **Terrain segments** | `ZP01_15` |
| **Name key** | `FieldName_130` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1300 | 362.79, 3947.06 | entrance / exit (leaving returns you to the field you came from) | 1300 | FieldName_130 |
| 1302 | 473.31, 4058.3 | entrance / exit (leaving returns you to the field you came from) | 1303 | FieldName_130 |
| 1303 | 459.92, 4048.72 | entrance / exit (leaving returns you to the field you came from) | 1302 | FieldName_130 |
| 1306 | 480.01, 4008.33 | entrance / exit (leaving returns you to the field you came from) | — | FieldName_130 |

### NPCs

None known yet.

### Monsters

None known yet.

### Spawn points

| unit | x | z | count | kind | note |
|---|---|---|---|---|---|
| Entry Core | 364 | 3934 | 1 | structure | Entry Core, ring south-west |
| Invasion Core | 476 | 4001 | 1 | structure | Invasion Core, ring north-east |
| Heart of Magic | 421 | 3971 | 1 | structure | Heart of Magic, centre room |
| Anti-Aircraft Defence Equipment | 471 | 3941 | 1 | structure | Anti-Aircraft Defence Equipment, ring south-east (room ±1) |

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP01_15 | yes | yes |

### Mentioned in

- [[gameplay/classes-and-legions#4. Forts (castles)|Classes, nations and legions § 4. Forts (castles)]]
- [[gameplay/server-rules#Added from the Warmonger forum and videos (round 2)|Server rules checklist § Added from the Warmonger forum and videos (round 2)]]
- [[gameplay/video-fort-war#Room of Core (field 130 "Room of Core", ZoneDB 138 `코어실`, rectangle x 256–511, z 3840–4095)|Video notes: fortress war series (ZonderCoRe) § Room of Core (field 130 "Room of Core", ZoneDB 138 `코어실`, rectangle x 256–511, z 3840–4095)]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
<!-- generated:end -->

## Notes

- Floor 1 of a fort siege. Clicking the defenders' nexus after a won land war opens the siege; attackers land beside their own Nexus in the outer south room, about (376, 3869), with a new 40:00 timer and TP reset to 0 / 10,000 ([[gameplay/video-fort-war|fort-war video notes]] §1, §3). *video*
- Layout: a ring of six hexagonal rooms around a closed centre room, three outer rooms to the south-west and one detached room to the north-east. Ring centres: south-west (364, 3934) Entry Core; north-west (361, 3996); north (426, 4031); north-east (476, 4001) Invasion Core; south-east (471, 3941) where the air defence stood; south (419, 3909). Centre room (421, 3971): Heart of Magic. The six cores are UnitDB 1043-1048 (Water, Wind, Earth, Fire, Entry, Invasion) ([[gameplay/video-fort-war|fort-war video notes]] §2). *video + client*
- The detached north-east room (476, 4044) holds gates 1302 ↔ 1303 and a pink star; after the air defence fell a white glow appeared in the outer west room (314, 3954) ([[gameplay/video-fort-war|fort-war video notes]] §2). *video; purposes guessed*

## Behaviour

- Capture Entry, then the ring cores, then Invasion; either side can retake cores. Destroying the Heart of Magic stops the Divine Guard and the guardian's recovery; destroying the air defence opens the way to the guardian's room ([[gameplay/video-fort-war|fort-war video notes]] §3; [[gameplay/classes-and-legions|Classes and legions]] §4). *video + guide*
- Respawn in the siege took about 14 s, at the attackers' Nexus ([[gameplay/video-fort-war|fort-war video notes]] §1). *video*

## Sources

- [[gameplay/video-fort-war|fort-war video notes]], [[gameplay/classes-and-legions|Classes and legions]], [[gameplay/server-rules|Server rules]].

## Open questions

- HP of the cores, Heart of Magic and guardian; what ends the siege (the recorded defeat came 7 min 55 s in); which room holds the portal to field 131 ([[gameplay/video-fort-war|fort-war video notes]] §5). The structures are listed under `spawn_points`; regular monsters are not known.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
