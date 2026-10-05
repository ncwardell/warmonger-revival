---
title: "Sinking Nest"
type: "field"
id: 119
status: "stub"
missing: ["spawn_points", "monsters", "npcs", "connections"]
sources: ["client: FieldNames.cdb id 119 (no SceneList row)", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 119"]
name_key: "FieldName_119"
kind: null
zones: [126]
segments: ["ZP05_11"]
gates:
  - {"gate": 1200, "x": 1332.13, "z": 2866.99, "to_gate": 1200, "to_field": 119, "label": "FieldName_119"}
connections: []
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=b26388 type=7a94db id=a2e33d sources=07eae8 name_key=fd6c9e kind=2be88c zones=d9b420 segments=5a389d gates=bb4b13 connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 126](../assets/zones/126.png) |
| **Field id** | `119` |
| **Zones** | [[wiki/zones/126-battlefield-tutorial-sinking-nest\|Battlefield tutorial (Sinking Nest)]] |
| **Terrain segments** | `ZP05_11` |
| **Name key** | `FieldName_119` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1200 | 1332.13, 2866.99 | arrival / spawn point only | 1200 | FieldName_119 |

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
| ZP05_11 | yes | yes |

### Mentioned in

- [[gameplay/video-dungeon-run#1. Field id and map|Video notes: Nas Village dungeon run (ZonderCoRe) § 1. Field id and map]]
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/patch-history|Patch notes and other sources]] (by name)
- [[gameplay/server-rules|Server rules checklist]] (by name)
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
