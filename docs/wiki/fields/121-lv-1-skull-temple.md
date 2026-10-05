---
title: "[Lv 1] Skull Temple"
type: "field"
id: 121
status: "partial"
missing: ["spawn_points"]
sources: ["client: SceneList.cdb id 121", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 121", "client: Quest.cdb (quests and objectives in field 121)", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 121", "image: [[gameplay/maps-and-dungeons]] §2 (minimap layout from the dungeons guide screenshots)", "notes: [[gameplay/patch-history]] (WM 0615 unlock level 20; WM 0402/0404 open time and respawn)"]
name_key: "FieldName_121"
kind: "dungeon"
scene_type: 3
max_users: 5
group: 31
zones: [133]
segments: ["ZP02_07"]
gates:
  - {"gate": 1210, "x": 599.64, "z": 1819.22, "to_gate": 0, "to_field": 0, "label": "FieldName_121"}
connections:
  - {"to": null, "gate": 1210, "kind": "exit"}
npcs: []
monsters: [81, 640, 641, 642, 643, 672, 10010, 804, 1501, 10009, 10013]
spawn_points: []
triggers:
  - {"id": 12101, "type": 0, "shape": 5, "x": 632.91, "z": 1809.01, "name_key": "UnitName_1005", "item": 802, "model": 1085}
  - {"id": 12102, "type": 0, "shape": 5, "x": 661.81, "z": 1826.7, "name_key": "UnitName_1000", "item": 812, "model": 1082}
  - {"id": 12103, "type": 0, "shape": 5, "x": 723.41, "z": 1862.06, "name_key": "UnitName_1005", "item": 802, "model": 1085}
  - {"id": 12104, "type": 0, "shape": 5, "x": 726.5, "z": 1883.99, "name_key": "UnitName_1000", "item": 812, "model": 1082}
  - {"id": 12105, "type": 0, "shape": 5, "x": 636.02, "z": 1922.59, "name_key": "UnitName_1005", "item": 802, "model": 1085}
  - {"id": 12106, "type": 0, "shape": 5, "x": 623.87, "z": 1936.47, "name_key": "UnitName_1000", "item": 812, "model": 1082}
  - {"id": 12107, "type": 0, "shape": 5, "x": 588.26, "z": 2018.08, "name_key": "UnitName_1005", "item": 802, "model": 1085}
  - {"id": 12108, "type": 0, "shape": 5, "x": 601.43, "z": 2015.79, "name_key": "UnitName_1000", "item": 812, "model": 1082}
dungeon: 121
---
<!-- generated:start -->
<!-- generated-keys: title=5cdb46 type=7a94db id=8bd795 sources=2d08d4 name_key=030599 kind=3e3f38 scene_type=77de68 max_users=ac3478 group=632667 zones=77bb32 segments=312458 gates=258554 connections=79a21f npcs=97d170 monsters=f56e9f spawn_points=97d170 triggers=834094 dungeon=8bd795 -->
|  |  |
|---|---|
|  | ![minimap of zone 133](wiki/assets/zones/133.png) |
|  | ![(Lv 1) Skull Temple](wiki/assets/dungeons/121.png) |
| **Field id** | `121` |
| **Kind** | dungeon (SceneList type 3; name *inferred*) |
| **Max users** | 5 (SceneList, column meaning *guessed*) |
| **Region group** | 31 (SceneList last column) |
| **Zones** | [[wiki/zones/133-underworld-01-lv-1-skull-temple\|Underworld 01 ((Lv 1) Skull Temple)]] |
| **Terrain segments** | `ZP02_07` |
| **Dungeon** | [[wiki/dungeons/121-lv-1-skull-temple\|dungeon page]] |
| **Name key** | `FieldName_121` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1210 | 599.64, 1819.22 | entrance / exit (leaving returns you to the field you came from) | — | FieldName_121 |

### NPCs

None known yet.

### Monsters

| monster | unit | why it is listed |
|---|---|---|
| [[wiki/npcs/81-transmission-equipment\|Transmission equipment]] | 81 | kill objective of quest [[wiki/quests/15-repel-the-skeleton-invasion\|15]] |
| [[wiki/monsters/640-skeleton-warrior\|Skeleton Warrior]] | 640 | kill objective of quest [[wiki/quests/727-the-necessary-materials\|727]], [[wiki/quests/1006-skull-temple-hunting\|1006]] (kill group 10009, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/641-skeleton-archer\|Skeleton Archer]] | 641 | kill objective of quest [[wiki/quests/727-the-necessary-materials\|727]], [[wiki/quests/1006-skull-temple-hunting\|1006]] (kill group 10009, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/642-elite-skeleton-warrior\|Elite Skeleton Warrior]] | 642 | kill objective of quest [[wiki/quests/727-the-necessary-materials\|727]], [[wiki/quests/1006-skull-temple-hunting\|1006]] (kill group 10010, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/643-elite-skeleton-archer\|Elite Skeleton Archer]] | 643 | kill objective of quest [[wiki/quests/727-the-necessary-materials\|727]], [[wiki/quests/1006-skull-temple-hunting\|1006]] (kill group 10010, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/672-king-deathhead\|King Deathhead]] | 672 | kill objective of quest [[wiki/quests/761-killed-boss-of-border-area-no-1\|761]], [[wiki/quests/768-group-border-area-hard-mode\|768]], [[wiki/quests/1008-skull-temple-boss-hunting\|1008]] (kill group 10013, UnitDB i32@80); boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| Object 10010 | 10010 | kill objective of quest [[wiki/quests/727-the-necessary-materials\|727]], [[wiki/quests/1006-skull-temple-hunting\|1006]] |
| [[wiki/monsters/804-tough-king-deathhead\|Tough King Deathhead]] | 804 | boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/1501-king-deathhead\|King Deathhead]] | 1501 | monster page (`spawns` / `spawn_fields`) |
| unit 10009 (not in UnitDB) | 10009 | hand-entered |
| unit 10013 (not in UnitDB) | 10013 | hand-entered |

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Client-placed objects (`Trigger`)

Talk devices (shape 4) and gathering nodes (type 0, shape 5: the item is what gathering gives). The server can load these as they are; the video check in [[gameplay/video-dungeon-run|Nas Village dungeon run]] §5 matched them within 5 units.

| trigger | kind | name | gives | at (x, z) | type | model |
|---|---|---|---|---|---|---|
| [[wiki/nodes/12101-garnet\|12101]] | node | Garnet | [[wiki/items/802-garnet\|Garnet]] | 632.91, 1809.01 | 0 | 1085 |
| [[wiki/nodes/12102-red-bloodstone\|12102]] | node | Red Bloodstone | [[wiki/items/812-red-bloodstone\|Red bloodstone]] | 661.81, 1826.7 | 0 | 1082 |
| [[wiki/nodes/12103-garnet\|12103]] | node | Garnet | [[wiki/items/802-garnet\|Garnet]] | 723.41, 1862.06 | 0 | 1085 |
| [[wiki/nodes/12104-red-bloodstone\|12104]] | node | Red Bloodstone | [[wiki/items/812-red-bloodstone\|Red bloodstone]] | 726.5, 1883.99 | 0 | 1082 |
| [[wiki/nodes/12105-garnet\|12105]] | node | Garnet | [[wiki/items/802-garnet\|Garnet]] | 636.02, 1922.59 | 0 | 1085 |
| [[wiki/nodes/12106-red-bloodstone\|12106]] | node | Red Bloodstone | [[wiki/items/812-red-bloodstone\|Red bloodstone]] | 623.87, 1936.47 | 0 | 1082 |
| [[wiki/nodes/12107-garnet\|12107]] | node | Garnet | [[wiki/items/802-garnet\|Garnet]] | 588.26, 2018.08 | 0 | 1085 |
| [[wiki/nodes/12108-red-bloodstone\|12108]] | node | Red Bloodstone | [[wiki/items/812-red-bloodstone\|Red bloodstone]] | 601.43, 2015.79 | 0 | 1082 |

### Dungeon

Entry cost, rewards, boss and schedule: [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]].

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP02_07 | yes | yes |

### Mentioned in

- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
<!-- generated:end -->

## Notes

- Minimap layout (Skull Temple): an S-shaped chain of chambers from the entry (bottom) to the marker (top-left); mineral nodes only ([[gameplay/maps-and-dungeons|Maps and dungeons]] §2). Legend: framed box = entry portal, yellow four-arrow marker = probably the boss / exit, green leaves = herb nodes, blue diamonds = mineral nodes, pink stars = probably elite spawns. *image*
- Unlock level 20 (WM 0615, [[gameplay/patch-history|Patch history]]). *notes*

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
