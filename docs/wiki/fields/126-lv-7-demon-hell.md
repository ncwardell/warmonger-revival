---
title: "[Lv 7] Demon Hell"
type: "field"
id: 126
status: "partial"
missing: ["spawn_points"]
sources: ["client: SceneList.cdb id 126", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 126", "client: Quest.cdb (quests and objectives in field 126)", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 126", "image: [[gameplay/maps-and-dungeons]] §2 (minimap layout from the dungeons guide screenshots)", "notes: [[gameplay/patch-history]] (WM 0615 unlock level 26; WM 0402/0404 open time and respawn)"]
name_key: "FieldName_126"
kind: "dungeon"
scene_type: 3
max_users: 5
group: 38
zones: [142]
segments: ["ZP09_07"]
gates:
  - {"gate": 1244, "x": 2510.38, "z": 1986.55, "to_gate": 1244, "to_field": 126, "label": "FieldName_126"}
  - {"gate": 1245, "x": 2506.13, "z": 1981.51, "to_gate": 1246, "to_field": 126, "label": "FiledPortal"}
  - {"gate": 1246, "x": 2477.21, "z": 1949.76, "to_gate": 1245, "to_field": 126, "label": "FiledPortal"}
  - {"gate": 1247, "x": 2505.09, "z": 1907.69, "to_gate": 1248, "to_field": 126, "label": "FiledPortal"}
  - {"gate": 1248, "x": 2490.06, "z": 1861.49, "to_gate": 1247, "to_field": 126, "label": "FiledPortal"}
  - {"gate": 1249, "x": 2443.25, "z": 1832.19, "to_gate": 1250, "to_field": 126, "label": "FiledPortal"}
  - {"gate": 1250, "x": 2505.53, "z": 1820.62, "to_gate": 1249, "to_field": 126, "label": "FiledPortal"}
  - {"gate": 1251, "x": 2365.41, "z": 1894.91, "to_gate": 1252, "to_field": 126, "label": "FiledPortal"}
  - {"gate": 1252, "x": 2413.37, "z": 1864.12, "to_gate": 1251, "to_field": 126, "label": "FiledPortal"}
  - {"gate": 1253, "x": 2374.89, "z": 1969.77, "to_gate": 1254, "to_field": 126, "label": "FiledPortal"}
  - {"gate": 1254, "x": 2422.62, "z": 1924.64, "to_gate": 1253, "to_field": 126, "label": "FiledPortal"}
connections:
  - {"to": null, "gate": 1244, "kind": "exit"}
npcs: []
monsters: [662, 678, 740, 739, 972, 10018, 10031]
spawn_points: []
triggers:
  - {"id": 12601, "type": 0, "shape": 5, "x": 2489.51, "z": 1942.35, "name_key": "UnitName_1006", "item": 810, "model": 1083}
  - {"id": 12602, "type": 0, "shape": 5, "x": 2497.59, "z": 1932.83, "name_key": "UnitName_1012", "item": 826, "model": 3015}
  - {"id": 12603, "type": 0, "shape": 5, "x": 2488.65, "z": 1846.31, "name_key": "UnitName_1013", "item": 828, "model": 3016}
  - {"id": 12604, "type": 0, "shape": 5, "x": 2490.82, "z": 1830.74, "name_key": "UnitName_1006", "item": 810, "model": 1083}
  - {"id": 12605, "type": 0, "shape": 5, "x": 2445.47, "z": 1853.51, "name_key": "UnitName_1012", "item": 826, "model": 3015}
  - {"id": 12606, "type": 0, "shape": 5, "x": 2430.36, "z": 1861.09, "name_key": "UnitName_1013", "item": 828, "model": 3016}
  - {"id": 12607, "type": 0, "shape": 5, "x": 2366.35, "z": 1912.26, "name_key": "UnitName_1012", "item": 826, "model": 3015}
  - {"id": 12608, "type": 0, "shape": 5, "x": 2391.98, "z": 1910.77, "name_key": "UnitName_1013", "item": 828, "model": 3016}
  - {"id": 12609, "type": 0, "shape": 5, "x": 2415.92, "z": 1974.41, "name_key": "UnitName_1006", "item": 810, "model": 1083}
  - {"id": 12610, "type": 0, "shape": 5, "x": 2429.51, "z": 1973.41, "name_key": "UnitName_1013", "item": 828, "model": 3016}
  - {"id": 12611, "type": 0, "shape": 5, "x": 2407.94, "z": 2002.97, "name_key": "UnitName_1006", "item": 810, "model": 1083}
  - {"id": 12612, "type": 0, "shape": 5, "x": 2384.95, "z": 1994.69, "name_key": "UnitName_1013", "item": 828, "model": 3016}
dungeon: 126
---
<!-- generated:start -->
<!-- generated-keys: title=12597b type=7a94db id=114d4e sources=abf528 name_key=97594e kind=3e3f38 scene_type=77de68 max_users=ac3478 group=5b384c zones=0688b1 segments=0dbe49 gates=a3e1d9 connections=c4f889 npcs=97d170 monsters=77c8d6 spawn_points=97d170 triggers=2e9022 dungeon=114d4e -->
|  |  |
|---|---|
|  | ![minimap of zone 142](wiki/assets/zones/142.png) |
|  | ![(Lv 7) Demon Hell](wiki/assets/dungeons/126.png) |
| **Field id** | `126` |
| **Kind** | dungeon (SceneList type 3; name *inferred*) |
| **Max users** | 5 (SceneList, column meaning *guessed*) |
| **Region group** | 38 (SceneList last column) |
| **Zones** | [[wiki/zones/142-field-dungeon-06-demon-lv-7-demon-hell\|Field dungeon 06(demon) ((Lv 7) Demon Hell)]] |
| **Terrain segments** | `ZP09_07` |
| **Dungeon** | [[wiki/dungeons/126-lv-7-demon-hell\|dungeon page]] |
| **Name key** | `FieldName_126` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1244 | 2510.38, 1986.55 | entrance / exit (leaving returns you to the field you came from) | 1244 | FieldName_126 |
| 1245 | 2506.13, 1981.51 | portal to gate 1246 in this field | 1246 | FiledPortal |
| 1246 | 2477.21, 1949.76 | portal to gate 1245 in this field | 1245 | FiledPortal |
| 1247 | 2505.09, 1907.69 | portal to gate 1248 in this field | 1248 | FiledPortal |
| 1248 | 2490.06, 1861.49 | portal to gate 1247 in this field | 1247 | FiledPortal |
| 1249 | 2443.25, 1832.19 | portal to gate 1250 in this field | 1250 | FiledPortal |
| 1250 | 2505.53, 1820.62 | portal to gate 1249 in this field | 1249 | FiledPortal |
| 1251 | 2365.41, 1894.91 | portal to gate 1252 in this field | 1252 | FiledPortal |
| 1252 | 2413.37, 1864.12 | portal to gate 1251 in this field | 1251 | FiledPortal |
| 1253 | 2374.89, 1969.77 | portal to gate 1254 in this field | 1254 | FiledPortal |
| 1254 | 2422.62, 1924.64 | portal to gate 1253 in this field | 1253 | FiledPortal |

### NPCs

None known yet.

### Monsters

| monster | unit | why it is listed |
|---|---|---|
| [[wiki/monsters/662-demon-hunter\|Demon Hunter]] | 662 | kill objective of quest [[wiki/quests/35-demon-hell\|35]], [[wiki/quests/743-demon-hell\|743]], [[wiki/quests/1036-demon-hell-hunting\|1036]] (kill group 10031, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/678-reviatan-shadow\|Reviatan Shadow]] | 678 | kill objective of quest [[wiki/quests/760-group-border-area-hard-mode\|760]], [[wiki/quests/1039-demon-hell-boss-hunting\|1039]] (kill group 10018, UnitDB i32@80); boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/740-reviatan-shadow\|Reviatan Shadow]] | 740 | boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/739-commander-reviatan\|Commander Reviatan]] | 739 | boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/972-reviatan\|Reviatan]] | 972 | monster page (`spawns` / `spawn_fields`) |
| unit 10018 (not in UnitDB) | 10018 | hand-entered |
| unit 10031 (not in UnitDB) | 10031 | hand-entered |

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Client-placed objects (`Trigger`)

Talk devices (shape 4) and gathering nodes (type 0, shape 5: the item is what gathering gives). The server can load these as they are; the video check in [[gameplay/video-dungeon-run|Nas Village dungeon run]] §5 matched them within 5 units.

| trigger | kind | name | gives | at (x, z) | type | model |
|---|---|---|---|---|---|---|
| [[wiki/nodes/12601-diamond\|12601]] | node | Diamond | [[wiki/items/810-diamond\|Diamond]] | 2489.51, 1942.35 | 0 | 1083 |
| [[wiki/nodes/12602-borage\|12602]] | node | Borage | [[wiki/items/826-borage\|Borage]] | 2497.59, 1932.83 | 0 | 3015 |
| [[wiki/nodes/12603-spartium\|12603]] | node | Spartium | [[wiki/items/828-spartium\|Spartium]] | 2488.65, 1846.31 | 0 | 3016 |
| [[wiki/nodes/12604-diamond\|12604]] | node | Diamond | [[wiki/items/810-diamond\|Diamond]] | 2490.82, 1830.74 | 0 | 1083 |
| [[wiki/nodes/12605-borage\|12605]] | node | Borage | [[wiki/items/826-borage\|Borage]] | 2445.47, 1853.51 | 0 | 3015 |
| [[wiki/nodes/12606-spartium\|12606]] | node | Spartium | [[wiki/items/828-spartium\|Spartium]] | 2430.36, 1861.09 | 0 | 3016 |
| [[wiki/nodes/12607-borage\|12607]] | node | Borage | [[wiki/items/826-borage\|Borage]] | 2366.35, 1912.26 | 0 | 3015 |
| [[wiki/nodes/12608-spartium\|12608]] | node | Spartium | [[wiki/items/828-spartium\|Spartium]] | 2391.98, 1910.77 | 0 | 3016 |
| [[wiki/nodes/12609-diamond\|12609]] | node | Diamond | [[wiki/items/810-diamond\|Diamond]] | 2415.92, 1974.41 | 0 | 1083 |
| [[wiki/nodes/12610-spartium\|12610]] | node | Spartium | [[wiki/items/828-spartium\|Spartium]] | 2429.51, 1973.41 | 0 | 3016 |
| [[wiki/nodes/12611-diamond\|12611]] | node | Diamond | [[wiki/items/810-diamond\|Diamond]] | 2407.94, 2002.97 | 0 | 1083 |
| [[wiki/nodes/12612-spartium\|12612]] | node | Spartium | [[wiki/items/828-spartium\|Spartium]] | 2384.95, 1994.69 | 0 | 3016 |

### Dungeon

Entry cost, rewards, boss and schedule: [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]].

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP09_07 | yes | yes |

### Mentioned in

- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] (by name)
<!-- generated:end -->

## Notes

- Minimap layout (Demon Hell): entry top-right; many small islands with pink stars; marker top-left. The boss is shown as two identical figures ([[gameplay/maps-and-dungeons|Maps and dungeons]] §2). Legend: framed box = entry portal, yellow four-arrow marker = probably the boss / exit, green leaves = herb nodes, blue diamonds = mineral nodes, pink stars = probably elite spawns. *image*
- Unlock level 26 (WM 0615, [[gameplay/patch-history|Patch history]]). *notes*

## Behaviour

- Solo, monsters do not respawn; with 2+ party members in hard mode they do. Reported respawn: first after 3-5 min then every minute (3 players), or starting at 9-10 min on the dungeon timer ([[gameplay/maps-and-dungeons|Maps and dungeons]] §2). WM 0404: with more than 2 users monsters respawn after 5 min; WM 0402 cut dungeon open time from 20 to 15 min ([[gameplay/patch-history|Patch history]]). *guides + notes*
- One portal is one instance with at most 5 players; the "Can not enter" option locks it ([[gameplay/maps-and-dungeons|Maps and dungeons]] §1). *guide*

## Sources

- [[gameplay/maps-and-dungeons|Maps and dungeons]], [[gameplay/patch-history|Patch history]].

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
