---
title: "[Lv 2] Skull Cemetery"
type: "field"
id: 128
status: "stub"
missing: ["spawn_points"]
sources: ["client: SceneList.cdb id 128", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 128", "client: Quest.cdb (quests and objectives in field 128)", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 128"]
name_key: "FieldName_128"
kind: "dungeon"
scene_type: 3
max_users: 5
group: 34
zones: [150]
segments: ["ZP01_17"]
gates:
  - {"gate": 1280, "x": 345.13, "z": 4427.9, "to_gate": 1280, "to_field": 128, "label": "FieldName_128"}
connections:
  - {"to": null, "gate": 1280, "kind": "exit"}
npcs: []
monsters: [81, 664, 665, 673, 809, 1205, 1504, 10014, 10027]
spawn_points: []
triggers:
  - {"id": 12801, "type": 0, "shape": 5, "x": 341.39, "z": 4491.95, "name_key": "UnitName_1003", "item": 814, "model": 1088}
  - {"id": 12802, "type": 0, "shape": 5, "x": 305.91, "z": 4490.22, "name_key": "UnitName_1002", "item": 804, "model": 1081}
  - {"id": 12803, "type": 0, "shape": 5, "x": 340.82, "z": 4520.01, "name_key": "UnitName_1010", "item": 822, "model": 3013}
  - {"id": 12804, "type": 0, "shape": 5, "x": 342.27, "z": 4552.41, "name_key": "UnitName_1011", "item": 824, "model": 3014}
  - {"id": 12805, "type": 0, "shape": 5, "x": 383.26, "z": 4530.88, "name_key": "UnitName_1003", "item": 814, "model": 1088}
  - {"id": 12806, "type": 0, "shape": 5, "x": 391.79, "z": 4567.36, "name_key": "UnitName_1002", "item": 804, "model": 1081}
  - {"id": 12807, "type": 0, "shape": 5, "x": 437.82, "z": 4553.59, "name_key": "UnitName_1010", "item": 822, "model": 3013}
  - {"id": 12808, "type": 0, "shape": 5, "x": 402.08, "z": 4508.76, "name_key": "UnitName_1011", "item": 824, "model": 3014}
dungeon: 128
---
<!-- generated:start -->
<!-- generated-keys: title=006667 type=7a94db id=b4182b sources=43461d name_key=bd8481 kind=3e3f38 scene_type=77de68 max_users=ac3478 group=f1f836 zones=267f86 segments=b756e9 gates=d091a4 connections=16e011 npcs=97d170 monsters=27b30a spawn_points=97d170 triggers=726a40 dungeon=b4182b -->
|  |  |
|---|---|
|  | ![minimap of zone 150](wiki/assets/zones/150.png) |
|  | ![(Lv 2) Skull Cemetery](wiki/assets/dungeons/128.png) |
| **Field id** | `128` |
| **Kind** | dungeon (SceneList type 3; name *inferred*) |
| **Max users** | 5 (SceneList, column meaning *guessed*) |
| **Region group** | 34 (SceneList last column) |
| **Zones** | [[wiki/zones/150-skull-cemetery-border-area-02-lv-2-skull-cemetery\|Skull cemetery(border area 02) ((Lv 2) Skull Cemetery)]] |
| **Terrain segments** | `ZP01_17` |
| **Dungeon** | [[wiki/dungeons/128-lv-2-skull-cemetery\|dungeon page]] |
| **Name key** | `FieldName_128` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1280 | 345.13, 4427.9 | entrance / exit (leaving returns you to the field you came from) | 1280 | FieldName_128 |

### NPCs

None known yet.

### Monsters

| monster | unit | why it is listed |
|---|---|---|
| [[wiki/npcs/81-transmission-equipment\|Transmission equipment]] | 81 | kill objective of quest [[wiki/quests/22-repel-the-black-skeleton-invasion\|22]] |
| [[wiki/monsters/664-black-skeleton-warrior\|Black Skeleton Warrior]] | 664 | kill objective of quest [[wiki/quests/724-find-lost-item\|724]], [[wiki/quests/1011-skull-cemetery-hunting\|1011]] (kill group 10027, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/665-black-skeleton-archer\|Black Skeleton Archer]] | 665 | kill objective of quest [[wiki/quests/724-find-lost-item\|724]], [[wiki/quests/1011-skull-cemetery-hunting\|1011]] (kill group 10027, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/673-dark-knight-skull\|Dark Knight Skull]] | 673 | kill objective of quest [[wiki/quests/761-killed-boss-of-border-area-no-1\|761]], [[wiki/quests/770-group-border-area-hard-mode\|770]], [[wiki/quests/1013-skull-cemetery-boss-hunting\|1013]] (kill group 10014, UnitDB i32@80); boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/809-dark-knight-skull\|Dark Knight Skull]] | 809 | boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/1205-dark-knight-skull\|Dark Knight Skull]] | 1205 | boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/1504-dark-knight-skull\|Dark Knight Skull]] | 1504 | monster page (`spawns` / `spawn_fields`) |
| unit 10014 (not in UnitDB) | 10014 | hand-entered |
| unit 10027 (not in UnitDB) | 10027 | hand-entered |

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Client-placed objects (`Trigger`)

Talk devices (shape 4) and gathering nodes (type 0, shape 5: the item is what gathering gives). The server can load these as they are; the video check in [[gameplay/video-dungeon-run|Nas Village dungeon run]] §5 matched them within 5 units.

| trigger | kind | name | gives | at (x, z) | type | model |
|---|---|---|---|---|---|---|
| [[wiki/nodes/12801-topaz\|12801]] | node | Topaz | [[wiki/items/814-topaz\|Topaz]] | 341.39, 4491.95 | 0 | 1088 |
| [[wiki/nodes/12802-blue-bloodstone\|12802]] | node | Blue Bloodstone | [[wiki/items/804-blue-bloodstone\|Blue bloodstone]] | 305.91, 4490.22 | 0 | 1081 |
| [[wiki/nodes/12803-rosemary\|12803]] | node | Rosemary | [[wiki/items/822-rosemary\|Rosemary]] | 340.82, 4520.01 | 0 | 3013 |
| [[wiki/nodes/12804-jasmine\|12804]] | node | Jasmine | [[wiki/items/824-jasmine\|Jasmine]] | 342.27, 4552.41 | 0 | 3014 |
| [[wiki/nodes/12805-topaz\|12805]] | node | Topaz | [[wiki/items/814-topaz\|Topaz]] | 383.26, 4530.88 | 0 | 1088 |
| [[wiki/nodes/12806-blue-bloodstone\|12806]] | node | Blue Bloodstone | [[wiki/items/804-blue-bloodstone\|Blue bloodstone]] | 391.79, 4567.36 | 0 | 1081 |
| [[wiki/nodes/12807-rosemary\|12807]] | node | Rosemary | [[wiki/items/822-rosemary\|Rosemary]] | 437.82, 4553.59 | 0 | 3013 |
| [[wiki/nodes/12808-jasmine\|12808]] | node | Jasmine | [[wiki/items/824-jasmine\|Jasmine]] | 402.08, 4508.76 | 0 | 3014 |

### Dungeon

Entry cost, rewards, boss and schedule: [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]].

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP01_17 | yes | yes |

### Mentioned in

- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] (by name)
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
