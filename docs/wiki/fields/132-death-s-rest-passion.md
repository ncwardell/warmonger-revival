---
title: "Death's Rest (Passion)"
type: "field"
id: 132
status: "partial"
missing: ["spawn_points", "monsters", "connections"]
sources: ["client: SceneList.cdb id 132", "notes: [[gameplay/patch-history]] (WM 0110: 'Mysterious World' via the fortress gate, tab Death's Rest (Passion))", "client: [[gameplay/events-and-schedules]] §9 (entry 2 Dimensional Energy)"]
name_key: "FieldName_132"
kind: "event_dungeon"
scene_type: 6
max_users: 100
group: 40
connections: []
npcs: []
monsters: []
spawn_points: []
dungeon: 132
---
<!-- generated:start -->
<!-- generated-keys: title=a78e33 type=7a94db id=91dfde sources=5d89f5 name_key=df500a kind=884439 scene_type=c1dfd9 max_users=310b86 group=af3e13 connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 dungeon=91dfde -->
|  |  |
|---|---|
|  | ![Death's Rest (Passion)](../assets/dungeons/132.png) |
| **Field id** | `132` |
| **Kind** | event dungeon (SceneList type 6; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 40 (SceneList last column) |
| **Dungeon** | [[wiki/dungeons/132-death-s-rest-passion\|dungeon page]] |
| **Name key** | `FieldName_132` |

### Gates and connections

No `Teleport_List` row: the client places no gate here.

### NPCs

None known yet.

### Monsters

None known yet.

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Dungeon

Entry cost, rewards, boss and schedule: [[wiki/dungeons/132-death-s-rest-passion|Death's Rest (Passion)]].

### Mentioned in

- [[gameplay/events-and-schedules#9. Other timers and limits|Events, schedules and PvP rewards § 9. Other timers and limits]]
- [[gameplay/maps-and-dungeons#3. Event / special dungeons|Maps and dungeons § 3. Event / special dungeons]]
- [[gameplay/patch-history#Dungeons and world|Patch notes and other sources § Dungeons and world]]
<!-- generated:end -->

## Notes

- Death's Rest (Passion) is a tab of the "Mysterious World" border area, reached through the fortress gate ([[gameplay/patch-history|Patch history]], WM 0110). Entry costs 2 Dimensional Energy ([[gameplay/events-and-schedules|Events and schedules]] §9). `Event_Dungeon` gives it a 180-minute window ([[gameplay/maps-and-dungeons|Maps and dungeons]] §3). *notes + client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

- [[gameplay/video-dungeon-run|dungeon-run video notes]] §6 guesses that field 132 is Siren Lake (by elimination from the world-map list), while the WM 0110 notes name it Death's Rest (Passion), matching FieldNames. The page keeps the client name.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
