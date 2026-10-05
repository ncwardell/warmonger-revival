---
title: "[Lv 3] Tsunami Lake"
type: "field"
id: 122
status: "stub"
missing: ["spawn_points"]
sources: ["client: SceneList.cdb id 122", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 122", "client: Quest.cdb (quests and objectives in field 122)", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 122"]
name_key: "FieldName_122"
kind: "dungeon"
scene_type: 3
max_users: 5
group: 33
zones: [136]
segments: ["ZP05_07"]
gates:
  - {"gate": 1221, "x": 1359.32, "z": 1817.82, "to_gate": 0, "to_field": 0, "label": "FieldName_122"}
  - {"gate": 1222, "x": 1370.09, "z": 1817.36, "to_gate": 1223, "to_field": 122, "label": "FiledPortal"}
  - {"gate": 1223, "x": 1409.82, "z": 1811.05, "to_gate": 1222, "to_field": 122, "label": "FiledPortal"}
  - {"gate": 1224, "x": 1444.93, "z": 1814.95, "to_gate": 1225, "to_field": 122, "label": "FiledPortal"}
  - {"gate": 1225, "x": 1449.26, "z": 1864.46, "to_gate": 1224, "to_field": 122, "label": "FiledPortal"}
  - {"gate": 1226, "x": 1473.48, "z": 1882.41, "to_gate": 1227, "to_field": 122, "label": "FiledPortal"}
  - {"gate": 1227, "x": 1402, "z": 1910.2, "to_gate": 1226, "to_field": 122, "label": "FiledPortal"}
  - {"gate": 1228, "x": 1324.16, "z": 1913.37, "to_gate": 1229, "to_field": 122, "label": "FiledPortal"}
  - {"gate": 1229, "x": 1321.48, "z": 1991.88, "to_gate": 1228, "to_field": 122, "label": "FiledPortal"}
  - {"gate": 1230, "x": 1371.45, "z": 2000.6, "to_gate": 1231, "to_field": 122, "label": "FiledPortal"}
  - {"gate": 1231, "x": 1414.79, "z": 2001.99, "to_gate": 1230, "to_field": 122, "label": "FiledPortal"}
connections:
  - {"to": null, "gate": 1221, "kind": "exit"}
npcs: []
monsters: [644, 645, 674, 727, 728, 733, 1209, 10015]
spawn_points: []
triggers:
  - {"id": 12213, "type": 13, "shape": 4, "x": 1366.02, "z": 1823.75, "name_key": "UnitName_400", "model": 89}
  - {"id": 12214, "type": 14, "shape": 4, "x": 1430.97, "z": 2002.75, "name_key": "UnitName_400", "model": 89}
  - {"id": 12215, "type": 15, "shape": 4, "x": 1469.48, "z": 1990.67, "name_key": "UnitName_2590", "model": 4056}
  - {"id": 12201, "type": 0, "shape": 5, "x": 1422.24, "z": 1825.72, "name_key": "UnitName_1003", "item": 814, "model": 1088}
  - {"id": 12202, "type": 0, "shape": 5, "x": 1424.8, "z": 1805.9, "name_key": "UnitName_1002", "item": 804, "model": 1081}
  - {"id": 12203, "type": 0, "shape": 5, "x": 1467.91, "z": 1853.96, "name_key": "UnitName_1010", "item": 822, "model": 3013}
  - {"id": 12204, "type": 0, "shape": 5, "x": 1457.07, "z": 1895.4, "name_key": "UnitName_1011", "item": 824, "model": 3014}
  - {"id": 12205, "type": 0, "shape": 5, "x": 1395.94, "z": 1899.16, "name_key": "UnitName_1003", "item": 814, "model": 1088}
  - {"id": 12206, "type": 0, "shape": 5, "x": 1376.65, "z": 1922.15, "name_key": "UnitName_1002", "item": 804, "model": 1081}
  - {"id": 12207, "type": 0, "shape": 5, "x": 1338.38, "z": 2001.91, "name_key": "UnitName_1010", "item": 822, "model": 3013}
  - {"id": 12208, "type": 0, "shape": 5, "x": 1351.48, "z": 1971.76, "name_key": "UnitName_1011", "item": 824, "model": 3014}
dungeon: 122
---
<!-- generated:start -->
<!-- generated-keys: title=a1b133 type=7a94db id=05a8ea sources=735be7 name_key=a3dd66 kind=3e3f38 scene_type=77de68 max_users=ac3478 group=b6692e zones=07b8de segments=e56b57 gates=8b343c connections=6fe72f npcs=97d170 monsters=62fe4e spawn_points=97d170 triggers=e049d0 dungeon=05a8ea -->
|  |  |
|---|---|
|  | ![minimap of zone 136](wiki/assets/zones/136.png) |
|  | ![(Lv 3) Tsunami Lake](wiki/assets/dungeons/122.png) |
| **Field id** | `122` |
| **Kind** | dungeon (SceneList type 3; name *inferred*) |
| **Max users** | 5 (SceneList, column meaning *guessed*) |
| **Region group** | 33 (SceneList last column) |
| **Zones** | [[wiki/zones/136-field-dungeon-02-lv-3-tsunami-lake\|Field dungeon 02 ((Lv 3) Tsunami Lake)]] |
| **Terrain segments** | `ZP05_07` |
| **Dungeon** | [[wiki/dungeons/122-lv-3-tsunami-lake\|dungeon page]] |
| **Name key** | `FieldName_122` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1221 | 1359.32, 1817.82 | entrance / exit (leaving returns you to the field you came from) | — | FieldName_122 |
| 1222 | 1370.09, 1817.36 | portal to gate 1223 in this field | 1223 | FiledPortal |
| 1223 | 1409.82, 1811.05 | portal to gate 1222 in this field | 1222 | FiledPortal |
| 1224 | 1444.93, 1814.95 | portal to gate 1225 in this field | 1225 | FiledPortal |
| 1225 | 1449.26, 1864.46 | portal to gate 1224 in this field | 1224 | FiledPortal |
| 1226 | 1473.48, 1882.41 | portal to gate 1227 in this field | 1227 | FiledPortal |
| 1227 | 1402, 1910.2 | portal to gate 1226 in this field | 1226 | FiledPortal |
| 1228 | 1324.16, 1913.37 | portal to gate 1229 in this field | 1229 | FiledPortal |
| 1229 | 1321.48, 1991.88 | portal to gate 1228 in this field | 1228 | FiledPortal |
| 1230 | 1371.45, 2000.6 | portal to gate 1231 in this field | 1231 | FiledPortal |
| 1231 | 1414.79, 2001.99 | portal to gate 1230 in this field | 1230 | FiledPortal |

### NPCs

None known yet.

### Monsters

| monster | unit | why it is listed |
|---|---|---|
| [[wiki/monsters/644-fisher\|Fisher]] | 644 | kill objective of quest [[wiki/quests/732-fisher-s-scales\|732]], [[wiki/quests/782-tsunami-lake\|782]], [[wiki/quests/1016-tsunami-lake-hunting\|1016]]; monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/645-elite-fisher\|Elite Fisher]] | 645 | kill objective of quest [[wiki/quests/16-farrell-s-request\|16]], [[wiki/quests/732-fisher-s-scales\|732]], [[wiki/quests/782-tsunami-lake\|782]], [[wiki/quests/1016-tsunami-lake-hunting\|1016]]; monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/674-tempest-fisher\|Tempest Fisher]] | 674 | kill objective of quest [[wiki/quests/756-group-border-area-hard-mode\|756]], [[wiki/quests/762-killed-boss-of-border-area-no-2\|762]], [[wiki/quests/1018-tsunami-lake-boss-hunting\|1018]] (kill group 10015, UnitDB i32@80); boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/727-chepa-warrior\|Chepa Warrior]] | 727 | kill objective of quest [[wiki/quests/756-group-border-area-hard-mode\|756]], [[wiki/quests/762-killed-boss-of-border-area-no-2\|762]], [[wiki/quests/1018-tsunami-lake-boss-hunting\|1018]] (kill group 10015, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/728-chepa-archer\|Chepa Archer]] | 728 | kill objective of quest [[wiki/quests/756-group-border-area-hard-mode\|756]], [[wiki/quests/762-killed-boss-of-border-area-no-2\|762]], [[wiki/quests/1018-tsunami-lake-boss-hunting\|1018]] (kill group 10015, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/733-tempest-fisher\|Tempest Fisher]] | 733 | boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/1209-tempest-fisher\|Tempest Fisher]] | 1209 | boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| unit 10015 (not in UnitDB) | 10015 | hand-entered |

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Client-placed objects (`Trigger`)

Talk devices (shape 4) and gathering nodes (type 0, shape 5: the item is what gathering gives). The server can load these as they are; the video check in [[gameplay/video-dungeon-run|Nas Village dungeon run]] §5 matched them within 5 units.

| trigger | kind | name | gives | at (x, z) | type | model |
|---|---|---|---|---|---|---|
| [[wiki/nodes/12213-a-doubtful-character\|12213]] | talk/device | A Doubtful character |  | 1366.02, 1823.75 | 13 | 89 |
| [[wiki/nodes/12214-a-doubtful-character\|12214]] | talk/device | A Doubtful character |  | 1430.97, 2002.75 | 14 | 89 |
| [[wiki/nodes/12215-tsunami-lake-flower\|12215]] | talk/device | Tsunami Lake flower |  | 1469.48, 1990.67 | 15 | 4056 |
| [[wiki/nodes/12201-topaz\|12201]] | node | Topaz | [[wiki/items/814-topaz\|Topaz]] | 1422.24, 1825.72 | 0 | 1088 |
| [[wiki/nodes/12202-blue-bloodstone\|12202]] | node | Blue Bloodstone | [[wiki/items/804-blue-bloodstone\|Blue bloodstone]] | 1424.8, 1805.9 | 0 | 1081 |
| [[wiki/nodes/12203-rosemary\|12203]] | node | Rosemary | [[wiki/items/822-rosemary\|Rosemary]] | 1467.91, 1853.96 | 0 | 3013 |
| [[wiki/nodes/12204-jasmine\|12204]] | node | Jasmine | [[wiki/items/824-jasmine\|Jasmine]] | 1457.07, 1895.4 | 0 | 3014 |
| [[wiki/nodes/12205-topaz\|12205]] | node | Topaz | [[wiki/items/814-topaz\|Topaz]] | 1395.94, 1899.16 | 0 | 1088 |
| [[wiki/nodes/12206-blue-bloodstone\|12206]] | node | Blue Bloodstone | [[wiki/items/804-blue-bloodstone\|Blue bloodstone]] | 1376.65, 1922.15 | 0 | 1081 |
| [[wiki/nodes/12207-rosemary\|12207]] | node | Rosemary | [[wiki/items/822-rosemary\|Rosemary]] | 1338.38, 2001.91 | 0 | 3013 |
| [[wiki/nodes/12208-jasmine\|12208]] | node | Jasmine | [[wiki/items/824-jasmine\|Jasmine]] | 1351.48, 1971.76 | 0 | 3014 |

### Dungeon

Entry cost, rewards, boss and schedule: [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]].

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP05_07 | yes | yes |

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
