---
title: "Village"
type: "field"
id: 91
status: "partial"
missing: ["npcs", "connections"]
sources: ["client: SceneList.cdb id 91", "doc: gameplay/npc-locations §2", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 91", "client + video: [[gameplay/npc-locations]] §2 and §6 (Village = old copy of the town map; start-point gates only)"]
name_key: "FieldName_91"
kind: "town"
scene_type: 1
max_users: 100
group: 13
nation: "Erion"
nation_copies: {"Arslan": 87, "Erion": 91, "Armia": 95}
zones: [8]
segments: ["ZP15_01"]
gates:
  - {"gate": 1, "x": 3963.73, "z": 322.41, "to_gate": 1, "to_field": 91, "label": "FieldName_91"}
connections: []
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=93abca type=7a94db id=4cd66d sources=d1934e name_key=2dfd3b kind=da9544 scene_type=356a19 max_users=310b86 group=bd307a nation=069950 nation_copies=b9e49f zones=1fb085 segments=f7dc89 gates=30f85c connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 8](../assets/zones/8.png) |
| **Field id** | `91` |
| **Kind** | town (SceneList type 1; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 13 (SceneList last column) |
| **Nation** | Erion |
| **Nation copies** | Arslan [[wiki/fields/87-village\|Arslan (87)]], Erion **91**, Armia [[wiki/fields/95-village\|Armia (95)]] |
| **Zones** | [[wiki/zones/8-town-b-village\|Town B (Village)]] |
| **Terrain segments** | `ZP15_01` |
| **Name key** | `FieldName_91` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1 | 3963.73, 322.41 | arrival / spawn point only | 1 | FieldName_91 |

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
| ZP15_01 | yes | yes |

### Mentioned in

- [[gameplay/maps-and-dungeons#1. The world (Gaia)|Maps and dungeons § 1. The world (Gaia)]]
<!-- generated:end -->

## Notes

- The Village is the old copy of the town map: its segments use the same navmesh as the Fortress. Segment origin of this copy: (3840, 256) ([[gameplay/npc-locations|NPC locations]] §2). *client*
- Its only `Teleport_List` row is gate 1 at (3963.73, 322.41), which links to itself, so it is a spawn point, not a way out. The Arslan start point (2688.83, 382.86) is local (128.8, 126.9), the centre of the Fortress plaza ([[gameplay/npc-locations|NPC locations]] §2, §6). *client*
- In 2018 players went Training Camp → Castle → Fortress; the camp's Village gate had no portal icon ([video](https://www.youtube.com/watch?v=E-87WgbO_vo&t=845s), [[gameplay/npc-locations|NPC locations]] §2). No video shows NPCs here ([[gameplay/npc-locations|NPC locations]] §6). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

- Whether players could reach the Village at all in the 2018 game, and which NPCs (if any) stood here, is unknown; `npcs` and `connections` stay empty until a source turns up.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
