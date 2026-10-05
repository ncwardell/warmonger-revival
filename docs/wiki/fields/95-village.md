---
title: "Village"
type: "field"
id: 95
status: "stub"
missing: ["npcs", "connections"]
sources: ["client: SceneList.cdb id 95", "doc: gameplay/npc-locations §2", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 95"]
name_key: "FieldName_95"
kind: "town"
scene_type: 1
max_users: 100
group: 13
nation: "Armia"
nation_copies: {"Arslan": 87, "Erion": 91, "Armia": 95}
zones: [6]
segments: ["ZP20_01"]
gates:
  - {"gate": 2, "x": 5245.8, "z": 337.38, "to_gate": 2, "to_field": 95, "label": "FieldName_95"}
connections: []
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=93abca type=7a94db id=8e63fd sources=ecdc58 name_key=27124f kind=da9544 scene_type=356a19 max_users=310b86 group=bd307a nation=b0e09b nation_copies=b9e49f zones=4a0a63 segments=9a8e10 gates=e8dad6 connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 6](wiki/assets/zones/6.png) |
| **Field id** | `95` |
| **Kind** | town (SceneList type 1; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 13 (SceneList last column) |
| **Nation** | Armia |
| **Nation copies** | Arslan [[wiki/fields/87-village\|Arslan (87)]], Erion [[wiki/fields/91-village\|Erion (91)]], Armia **95** |
| **Zones** | [[wiki/zones/6-town-c-village\|Town C (Village)]] |
| **Terrain segments** | `ZP20_01` |
| **Name key** | `FieldName_95` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 2 | 5245.8, 337.38 | arrival / spawn point only | 2 | FieldName_95 |

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
| ZP20_01 | yes | yes |

### Mentioned in

- [[gameplay/maps-and-dungeons#1. The world (Gaia)|Maps and dungeons § 1. The world (Gaia)]]
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
