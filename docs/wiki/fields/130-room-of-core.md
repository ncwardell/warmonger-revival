---
title: "Room of Core"
type: "field"
id: 130
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 130", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 130"]
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
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=052e88 type=7a94db id=2a7541 sources=6ae821 name_key=05bf33 kind=3e3f38 scene_type=77de68 max_users=22d200 group=b6589f zones=76eab3 segments=108ae9 gates=b7d380 connections=c07309 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 138](../assets/zones/138.png) |
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

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

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
