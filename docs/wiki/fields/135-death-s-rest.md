---
title: "Death's Rest"
type: "field"
id: 135
status: "partial"
missing: ["spawn_points", "monsters", "connections"]
sources: ["client: SceneList.cdb id 135", "client + video: [[gameplay/video-dungeon-run]] §6 (world-map list value 24 = Event_Dungeon target 135, 80-minute window: The avenue of spirit)", "guide: [[gameplay/maps-and-dungeons]] §2-§3 (seen on Skywing Yard; drops; entry 5 / 20)"]
name_key: "FieldName_112"
kind: "dungeon"
scene_type: 3
max_users: 5
group: 12
connections: []
npcs: []
monsters: []
spawn_points: []
dungeon: 135
---
<!-- generated:start -->
<!-- generated-keys: title=5991de type=7a94db id=40f7c0 sources=723152 name_key=5ed3e6 kind=3e3f38 scene_type=77de68 max_users=ac3478 group=7b5200 connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 dungeon=40f7c0 -->
|  |  |
|---|---|
| **Field id** | `135` |
| **Kind** | dungeon (SceneList type 3; name *inferred*) |
| **Max users** | 5 (SceneList, column meaning *guessed*) |
| **Region group** | 12 (SceneList last column) |
| **Dungeon** | [[wiki/dungeons/135-death-s-rest\|dungeon page]] |
| **Name key** | `FieldName_112` |

### Gates and connections

No `Teleport_List` row: the client places no gate here.

### NPCs

None known yet.

### Monsters

None known yet.

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Dungeon

Entry cost, rewards, boss and schedule: [[wiki/dungeons/135-death-s-rest|Death's Rest]].

### Mentioned in

- [[gameplay/abyss-map|Abyss map and portal graph]] (by name)
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/patch-history|Patch notes and other sources]] (by name)
- [[gameplay/server-rules|Server rules checklist]] (by name)
- [[gameplay/sources|Sources and gaps]] (by name)
<!-- generated:end -->

## Notes

- The event dungeon "The avenue of spirit": the world map's Event Dungeon list shows it with the number 24, which matches `Event_Dungeon` target 135 (80-minute window) ([[gameplay/video-dungeon-run|dungeon-run video notes]] §6). *client + video*
- Seen on Skywing Yard; drops Orange Passion T1, Yellow and Red crystals, T2 Red/Blue Passion ([[gameplay/maps-and-dungeons|Maps and dungeons]] §3). Entry 5 normal / 20 hard in the 2018 table; client `DungeonAdmission` 5 / 15 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §2; [[gameplay/video-dungeon-run|dungeon-run video notes]]). *guide + client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

- FieldNames calls this field "Death's Rest"; the match to The avenue of spirit rests on the world-map list numbers ([[gameplay/video-dungeon-run|dungeon-run video notes]] §6). Monsters and layout unknown.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
