---
title: "Sinking Nest (Crystal)"
type: "field"
id: 133
status: "partial"
missing: []
sources: ["client: SceneList.cdb id 133", "doc: gameplay/video-dungeon-run §1 (Nas Village Entrance geometry = ZoneDB 126; guess)", "video: [[gameplay/video-dungeon-run]] §1-§3 (Nas Village Entrance = field 133; pack positions video-measured ±4 units; 5-7 monsters per pack; packs back after 90-100 s with a 3-player party; midpoints derived from the measured ranges)", "client: [[gameplay/video-dungeon-run]] §2 (the Nas units 688-691, 1219, 1220; which of them spawn in this run is a guess)", "client + video: [[gameplay/video-dungeon-run]] §1 (entry / exit point = Teleport_List gate 1200 at (1332.13, 2866.99))"]
manual: ["status"]
name_key: "FieldName_133"
kind: "event_dungeon"
scene_type: 6
max_users: 100
group: 41
zones: [126]
segments: ["ZP05_11"]
connections:
  - {"to": null, "gate": 1200, "kind": "exit", "source": "video + client (gate row belongs to field 119)"}
npcs: []
monsters: [688, 689, 690, 691, 1219, 1220]
spawn_points:
  - {"unit": null, "x": 1362, "z": 2887, "count": null, "respawn_s": null, "pack": 1, "x_range": [1352, 1372], "z_range": [2884, 2890], "seen": "5-7 Nas warriors/archers, back after 90-100 s"}
  - {"unit": null, "x": 1382.5, "z": 2893.5, "count": null, "respawn_s": null, "pack": 2, "x_range": [1377, 1388], "z_range": [2890, 2897], "seen": "5-7"}
  - {"unit": null, "x": 1413.5, "z": 2911.5, "count": null, "respawn_s": null, "pack": 3, "x_range": [1408, 1419], "z_range": [2908, 2915], "seen": "5-7"}
  - {"unit": null, "x": 1453.5, "z": 2932, "count": null, "respawn_s": null, "pack": 4, "x_range": [1449, 1458], "z_range": [2929, 2935], "seen": "5-7"}
  - {"unit": null, "x": 1463.5, "z": 2940, "count": null, "respawn_s": null, "pack": 5, "x_range": [1460, 1467], "z_range": [2938, 2942], "seen": "5-7"}
  - {"unit": null, "x": 1480, "z": 2954.5, "count": null, "respawn_s": null, "pack": 6, "x_range": [1478, 1482], "z_range": [2951, 2958], "seen": "5-7, dead end"}
dungeon: 133
---
<!-- generated:start -->
<!-- generated-keys: title=7f851f type=7a94db id=d30f79 sources=93d02e name_key=9c77e6 kind=884439 scene_type=c1dfd9 max_users=310b86 group=761f22 zones=d9b420 segments=5a389d connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 dungeon=d30f79 -->
|  |  |
|---|---|
|  | ![minimap of zone 126](../assets/zones/126.png) |
|  | ![Sinking Nest (Crystal)](../assets/dungeons/133.png) |
| **Field id** | `133` |
| **Kind** | event dungeon (SceneList type 6; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 41 (SceneList last column) |
| **Zones** | [[wiki/zones/126-battlefield-tutorial-sinking-nest\|Battlefield tutorial (Sinking Nest)]] |
| **Terrain segments** | `ZP05_11` |
| **Dungeon** | [[wiki/dungeons/133-sinking-nest-crystal\|dungeon page]] |
| **Name key** | `FieldName_133` |

### Gates and connections

No `Teleport_List` row: the client places no gate here.

### NPCs

None known yet.

### Monsters

None known yet.

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Dungeon

Entry cost, rewards, boss and schedule: [[wiki/dungeons/133-sinking-nest-crystal|Sinking Nest (Crystal)]].

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP05_11 | yes | yes |

### Mentioned in

- [[gameplay/patch-history#Dungeons and world|Patch notes and other sources § Dungeons and world]]
- [[gameplay/server-rules#Added from the Warmonger forum and videos (round 2)|Server rules checklist § Added from the Warmonger forum and videos (round 2)]]
- [[gameplay/video-dungeon-run#2. Pack positions (field 133)|Video notes: Nas Village dungeon run (ZonderCoRe) § 2. Pack positions (field 133)]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
<!-- generated:end -->

## Notes

- This is the event dungeon players called **Nas Village (Entrance)**: `DungeonAdmission` row 133 advertises exactly the crystals and gem stones Nas drops, and its geometry is ZoneDB 126, the only minimap with a diagonal chain of six round chambers ([[gameplay/video-dungeon-run|dungeon-run video notes]] §1). *client + video*
- Entry / exit point: gate 1200 at (1332.13, 2866.99); in the June 2018 run the party entered from a stone portal ring in Raging Wind (57) at about (4452, 1070) and returned there when the dungeon finished ([[gameplay/video-dungeon-run|dungeon-run video notes]] §1, §7). *video*
- Packs: six stops along a 160-unit chain from the portal (south-west) to a dead end (north-east), with about 5-7 humanoid warriors and archers each. The client's Nas units are 688 Nas Warrior, 689 Nas Archer, 690/691 Elite, 1219/1220 Superior; which of them spawn is not shown ([[gameplay/video-dungeon-run|dungeon-run video notes]] §2). *video + client*
- Drops seen: Faded Passion fragments / Piece / Pattern, Crystal Blue/Yellow/Red/Black, one Medal: Bronze; no gear and no boss ([[gameplay/video-dungeon-run|dungeon-run video notes]] §4). Guides call Nas the best place for crystals and gold ([[gameplay/maps-and-dungeons|Maps and dungeons]] §3). *video + guide*
- WM 0124 refocused Sinking Nest on crystals and gem stones with a 3-hour limit; it is a "Mysterious World" tab reached through the fortress gate ([[gameplay/patch-history|Patch history]]; [[gameplay/events-and-schedules|Events and schedules]] §9). Entry 4 Dimensional Energy (client). *notes + client*

## Behaviour

- With a 3-player party in Hard mode a cleared pack refilled in about 90-100 s; one lap took 95-105 s. The run ended with "Dungeon finished / Exiting the dungeon initiated" about 11 min 13 s after entry, with no timer on screen ([[gameplay/video-dungeon-run|dungeon-run video notes]] §3). *video*

## Sources

- [[gameplay/video-dungeon-run|dungeon-run video notes]], [[gameplay/maps-and-dungeons|Maps and dungeons]], [[gameplay/patch-history|Patch history]], [[gameplay/events-and-schedules|Events and schedules]].

## Open questions

- `spawn_points` records only the pack positions: which Nas unit stands in which pack, the exact count and the respawn time a server should use are not known (the videos give 5-7 and 90-100 s for a 3-player party).
- Why the dungeon closed after about 11 minutes (an event window ending is a guess).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
