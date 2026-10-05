---
title: "Village"
type: "field"
id: 87
status: "stub"
missing: ["npcs", "connections"]
sources: ["client: SceneList.cdb id 87", "doc: gameplay/npc-locations §2", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 87"]
name_key: "FieldName_87"
kind: "town"
scene_type: 1
max_users: 100
group: 13
nation: "Arslan"
nation_copies: {"Arslan": 87, "Erion": 91, "Armia": 95}
zones: [102]
segments: ["ZP10_01"]
gates:
  - {"gate": 0, "x": 2688.83, "z": 382.86, "to_gate": 0, "to_field": 87, "label": "FieldName_87"}
connections: []
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=93abca type=7a94db id=e62d7f sources=9a0e58 name_key=230a99 kind=da9544 scene_type=356a19 max_users=310b86 group=bd307a nation=a20b0f nation_copies=b9e49f zones=187cfc segments=030709 gates=ee4d64 connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 102](../assets/zones/102.png) |
| **Field id** | `87` |
| **Kind** | town (SceneList type 1; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 13 (SceneList last column) |
| **Nation** | Arslan |
| **Nation copies** | Arslan **87**, Erion [[wiki/fields/91-village\|Erion (91)]], Armia [[wiki/fields/95-village\|Armia (95)]] |
| **Zones** | [[wiki/zones/102-town-a-village\|Town A (Village)]] |
| **Terrain segments** | `ZP10_01` |
| **Name key** | `FieldName_87` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 0 | 2688.83, 382.86 | arrival / spawn point only | — | FieldName_87 |

Entered from: [[wiki/fields/88-training-camp|Training Camp]] (gate 1201 → ?), [[wiki/fields/92-training-camp|Training Camp]] (gate 1204 → ?), [[wiki/fields/96-training-camp|Training Camp]] (gate 1207 → ?)

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
| ZP10_01 | yes | yes |

### Mentioned in

- [[gameplay/npc-locations#1. What the client data contains (and what it does not)|NPC and point-of-interest locations § 1. What the client data contains (and what it does not)]]
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
