---
title: "Hill of Gollam"
type: "field"
id: 115
status: "partial"
missing: ["spawn_points", "monsters", "connections"]
sources: ["client: SceneList.cdb id 115", "guide: [[gameplay/maps-and-dungeons]] §2-§3 (Gollam Hill: seen on End of Earth, drops, entry 5 / 10)", "client + video: [[gameplay/video-dungeon-run]] §6 (Event_Dungeon row 115, 180-minute window, value 12 on the world-map list)"]
name_key: "FieldName_115"
kind: "dungeon"
scene_type: 3
max_users: 5
group: 6
connections: []
npcs: []
monsters: []
spawn_points: []
dungeon: 115
---
<!-- generated:start -->
<!-- generated-keys: title=e984f5 type=7a94db id=efa6e4 sources=9dac05 name_key=e7b394 kind=3e3f38 scene_type=77de68 max_users=ac3478 group=c1dfd9 connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 dungeon=efa6e4 -->
|  |  |
|---|---|
| **Field id** | `115` |
| **Kind** | dungeon (SceneList type 3; name *inferred*) |
| **Max users** | 5 (SceneList, column meaning *guessed*) |
| **Region group** | 6 (SceneList last column) |
| **Dungeon** | [[wiki/dungeons/115-hill-of-gollam\|dungeon page]] |
| **Name key** | `FieldName_115` |

### Gates and connections

No `Teleport_List` row: the client places no gate here.

### NPCs

None known yet.

### Monsters

None known yet.

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Dungeon

Entry cost, rewards, boss and schedule: [[wiki/dungeons/115-hill-of-gollam|Hill of Gollam]].

### Mentioned in

- [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost (Dimensional Energy, item 688)]]
- [[gameplay/video-dungeon-run|Video notes: Nas Village dungeon run (ZonderCoRe)]] (by name)
<!-- generated:end -->

## Notes

- Event dungeon "Gollam Hill" (Hill of Gollam). It opened on random lands on a schedule; the guides saw it on End of Earth. Drops named by the guides: Red Bloodstone, Diamond, Garnet, Topaz ([[gameplay/maps-and-dungeons|Maps and dungeons]] §3). *guide*
- Entry: 5 / 10 Dimensional Energy (normal / hard) in the 2018 guides; client `DungeonAdmission` 5 / 5 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §2). *guide + client*
- `Event_Dungeon` gives it a 180-minute window; the world map's Event Dungeon list shows the number 12 next to it, matching that row ([[gameplay/video-dungeon-run|dungeon-run video notes]] §6). *client + video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

- Monsters, layout and entrance gate are unknown.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
