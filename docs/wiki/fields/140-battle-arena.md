---
title: "Battle Arena"
type: "field"
id: 140
status: "complete"
missing: []
sources: ["client: SceneList.cdb id 140", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 140"]
name_key: "FieldName_140"
kind: "arena"
scene_type: 4
max_users: 10
group: 0
zones: [148]
segments: ["ZP01_07"]
gates:
  - {"gate": 1401, "x": 448.07, "z": 1990.04, "x2": 427.03, "z2": 1990.11, "to_gate": 1401, "to_field": 140, "label": "FieldName_140"}
  - {"gate": 1402, "x": 286.34, "z": 1990.42, "x2": 307.31, "z2": 1990.22, "to_gate": 1402, "to_field": 140, "label": "FieldName_140"}
connections: []
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=3ff156 type=7a94db id=c28aca sources=0df286 name_key=764d56 kind=c9882f scene_type=1b6453 max_users=b1d578 group=b6589f zones=a5c262 segments=63c97d gates=33ff5e connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 148](wiki/assets/zones/148.png) |
| **Field id** | `140` |
| **Kind** | arena (SceneList type 4; name *inferred*) |
| **Max users** | 10 (SceneList, column meaning *guessed*) |
| **Region group** | 0 (SceneList last column) |
| **Zones** | [[wiki/zones/148-new-arena-battle-arena\|New arena (Battle Arena)]] |
| **Terrain segments** | `ZP01_07` |
| **Name key** | `FieldName_140` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1401 | 448.07, 1990.04 | arrival / spawn point only | 1401 | FieldName_140 |
| 1402 | 286.34, 1990.42 | arrival / spawn point only | 1402 | FieldName_140 |

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
| ZP01_07 | yes | yes |

### Mentioned in

- [[gameplay/pvp-and-matches#3. Queued battles and arenas|PvP, land wars and matches § 3. Queued battles and arenas]]
- [[gameplay/arena-ranking-rewards|Battle Arena monthly ranking rewards]] (by name)
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] (by name)
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]] (by name)
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/patch-history|Patch notes and other sources]] (by name)
- [[gameplay/server-rules|Server rules checklist]] (by name)
- [[gameplay/skull-artifact-set|Skull artifact set tooltips (Crush Online, Feb 2017)]] (by name)
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
