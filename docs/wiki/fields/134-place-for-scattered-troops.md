---
title: "Place for Scattered troops"
type: "field"
id: 134
status: "partial"
missing: ["spawn_points", "monsters", "connections"]
sources: ["client: SceneList.cdb id 134", "client + video: [[gameplay/video-dungeon-run]] §6 (world-map list value 21 = Event_Dungeon target 134, 80-minute window: Place for Scattered troops)", "guide: [[gameplay/maps-and-dungeons]] §2-§3 (seen on End of Earth; drops; entry 5 / 20)"]
name_key: "FieldName_103"
kind: "dungeon"
scene_type: 3
max_users: 5
group: 12
connections: []
npcs: []
monsters: []
spawn_points: []
dungeon: 134
---
<!-- generated:start -->
<!-- generated-keys: title=48ad72 type=7a94db id=95e815 sources=da7141 name_key=7bf5b8 kind=3e3f38 scene_type=77de68 max_users=ac3478 group=7b5200 connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 dungeon=95e815 -->
|  |  |
|---|---|
| **Field id** | `134` |
| **Kind** | dungeon (SceneList type 3; name *inferred*) |
| **Max users** | 5 (SceneList, column meaning *guessed*) |
| **Region group** | 12 (SceneList last column) |
| **Dungeon** | [[wiki/dungeons/134-place-for-scattered-troops\|dungeon page]] |
| **Name key** | `FieldName_103` |

### Gates and connections

No `Teleport_List` row: the client places no gate here.

### NPCs

None known yet.

### Monsters

None known yet.

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Dungeon

Entry cost, rewards, boss and schedule: [[wiki/dungeons/134-place-for-scattered-troops|Place for Scattered troops]].

### Mentioned in

- [[gameplay/abyss-map|Abyss map and portal graph]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/server-rules|Server rules checklist]] (by name)
- [[gameplay/video-dungeon-run|Video notes: Nas Village dungeon run (ZonderCoRe)]] (by name)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] (by name)
<!-- generated:end -->

## Notes

- The event dungeon "Place for Scattered troops": the world map's Event Dungeon list shows it with the number 21, which matches `Event_Dungeon` target 134 (80-minute window) ([[gameplay/video-dungeon-run|dungeon-run video notes]] §6). *client + video*
- Seen on End of Earth; drops Orange Passion T1, Yellow and Blue crystals, T2 Red/Blue and T1 Blue Passion ([[gameplay/maps-and-dungeons|Maps and dungeons]] §3). Entry 5 normal / 20 hard in the 2018 table (later 5 + 3 bronze Time Energy); client `DungeonAdmission` 5 / 15 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §2; [[gameplay/video-dungeon-run|dungeon-run video notes]]). *guide + client*
- WM 0412 opened Scattered Troops and Avenue of Spirit to both nations ([[gameplay/patch-history|Patch history]]). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

- Monsters and layout unknown.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
