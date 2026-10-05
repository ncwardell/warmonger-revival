---
title: "[Lv 9] Dragon Island"
type: "field"
id: 142
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 142", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 142", "client: Trigger.cdb field 142"]
name_key: "FieldName_142"
kind: "dungeon"
scene_type: 3
max_users: 5
group: 5
zones: [152]
segments: ["ZP08_08"]
gates:
  - {"gate": 1425, "x": 2088.61, "z": 2252.65, "to_gate": 1425, "to_field": 142, "label": "FieldName_142"}
  - {"gate": 1421, "x": 2120.48, "z": 2097.94, "to_gate": 1421, "to_field": 142, "label": "FiledPortal"}
  - {"gate": 1422, "x": 2240.03, "z": 2075.41, "to_gate": 1422, "to_field": 142, "label": "FiledPortal"}
  - {"gate": 1423, "x": 2202.76, "z": 2159.27, "to_gate": 1423, "to_field": 142, "label": "FiledPortal"}
  - {"gate": 1424, "x": 2195.01, "z": 2219.63, "to_gate": 1424, "to_field": 142, "label": "FiledPortal"}
connections:
  - {"to": null, "gate": 1425, "kind": "exit"}
npcs: []
monsters: []
spawn_points: []
triggers:
  - {"id": 14201, "type": 0, "shape": 5, "x": 2100.76, "z": 1973.46, "name_key": "UnitName_1007", "item": 806, "model": 1084}
  - {"id": 14202, "type": 0, "shape": 5, "x": 2140.16, "z": 1971.2, "name_key": "UnitName_1010", "item": 822, "model": 3013}
  - {"id": 14203, "type": 0, "shape": 5, "x": 2106.52, "z": 1893.65, "name_key": "UnitName_1011", "item": 824, "model": 3014}
  - {"id": 14204, "type": 0, "shape": 5, "x": 2100.9, "z": 1870.66, "name_key": "UnitName_1007", "item": 806, "model": 1084}
  - {"id": 14205, "type": 0, "shape": 5, "x": 2222.81, "z": 1839.37, "name_key": "UnitName_1010", "item": 822, "model": 3013}
  - {"id": 14206, "type": 0, "shape": 5, "x": 2255.4, "z": 1836.04, "name_key": "UnitName_1011", "item": 824, "model": 3014}
  - {"id": 14207, "type": 0, "shape": 5, "x": 2230.56, "z": 1894.53, "name_key": "UnitName_1010", "item": 822, "model": 3013}
  - {"id": 14208, "type": 0, "shape": 5, "x": 2196.1, "z": 1894.84, "name_key": "UnitName_1011", "item": 824, "model": 3014}
  - {"id": 14209, "type": 0, "shape": 5, "x": 2221.17, "z": 1956.71, "name_key": "UnitName_1007", "item": 806, "model": 1084}
  - {"id": 14210, "type": 0, "shape": 5, "x": 2241.96, "z": 1971.52, "name_key": "UnitName_1010", "item": 822, "model": 3013}
  - {"id": 14213, "type": 0, "shape": 5, "x": 2218.56, "z": 2007.44, "name_key": "UnitName_1007", "item": 806, "model": 1084}
  - {"id": 14214, "type": 0, "shape": 5, "x": 2193.03, "z": 1986.26, "name_key": "UnitName_1010", "item": 822, "model": 3013}
dungeon: 142
---
<!-- generated:start -->
<!-- generated-keys: title=b263a8 type=7a94db id=2a2b47 sources=97a244 name_key=6226f0 kind=3e3f38 scene_type=77de68 max_users=ac3478 group=ac3478 zones=dd2ee1 segments=ad649d gates=027113 connections=58e82b npcs=97d170 monsters=97d170 spawn_points=97d170 triggers=8a5de7 dungeon=2a2b47 -->
|  |  |
|---|---|
|  | ![minimap of zone 152](../assets/zones/152.png) |
|  | ![(Lv 9) Dragon Island](../assets/dungeons/142.png) |
| **Field id** | `142` |
| **Kind** | dungeon (SceneList type 3; name *inferred*) |
| **Max users** | 5 (SceneList, column meaning *guessed*) |
| **Region group** | 5 (SceneList last column) |
| **Zones** | [[wiki/zones/152-field-dungeon-08-dragon-lv-9-dragon-island\|Field dungeon 08(dragon) ((Lv 9) Dragon Island)]] |
| **Terrain segments** | `ZP08_08` |
| **Dungeon** | [[wiki/dungeons/142-lv-9-dragon-island\|dungeon page]] |
| **Name key** | `FieldName_142` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1425 | 2088.61, 2252.65 | entrance / exit (leaving returns you to the field you came from) | 1425 | FieldName_142 |
| 1421 | 2120.48, 2097.94 | arrival / spawn point only | 1421 | FiledPortal |
| 1422 | 2240.03, 2075.41 | arrival / spawn point only | 1422 | FiledPortal |
| 1423 | 2202.76, 2159.27 | arrival / spawn point only | 1423 | FiledPortal |
| 1424 | 2195.01, 2219.63 | arrival / spawn point only | 1424 | FiledPortal |

### NPCs

None known yet.

### Monsters

None known yet.

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Client-placed objects (`Trigger`)

Talk devices (shape 4) and gathering nodes (type 0, shape 5: the item is what gathering gives). The server can load these as they are; the video check in [[gameplay/video-dungeon-run|Nas Village dungeon run]] §5 matched them within 5 units.

| trigger | kind | name | gives | at (x, z) | type | model |
|---|---|---|---|---|---|---|
| [[wiki/nodes/14201-emerald\|14201]] | node | Emerald | [[wiki/items/806-emerald\|Emerald]] | 2100.76, 1973.46 | 0 | 1084 |
| [[wiki/nodes/14202-rosemary\|14202]] | node | Rosemary | [[wiki/items/822-rosemary\|Rosemary]] | 2140.16, 1971.2 | 0 | 3013 |
| [[wiki/nodes/14203-jasmine\|14203]] | node | Jasmine | [[wiki/items/824-jasmine\|Jasmine]] | 2106.52, 1893.65 | 0 | 3014 |
| [[wiki/nodes/14204-emerald\|14204]] | node | Emerald | [[wiki/items/806-emerald\|Emerald]] | 2100.9, 1870.66 | 0 | 1084 |
| [[wiki/nodes/14205-rosemary\|14205]] | node | Rosemary | [[wiki/items/822-rosemary\|Rosemary]] | 2222.81, 1839.37 | 0 | 3013 |
| [[wiki/nodes/14206-jasmine\|14206]] | node | Jasmine | [[wiki/items/824-jasmine\|Jasmine]] | 2255.4, 1836.04 | 0 | 3014 |
| [[wiki/nodes/14207-rosemary\|14207]] | node | Rosemary | [[wiki/items/822-rosemary\|Rosemary]] | 2230.56, 1894.53 | 0 | 3013 |
| [[wiki/nodes/14208-jasmine\|14208]] | node | Jasmine | [[wiki/items/824-jasmine\|Jasmine]] | 2196.1, 1894.84 | 0 | 3014 |
| [[wiki/nodes/14209-emerald\|14209]] | node | Emerald | [[wiki/items/806-emerald\|Emerald]] | 2221.17, 1956.71 | 0 | 1084 |
| [[wiki/nodes/14210-rosemary\|14210]] | node | Rosemary | [[wiki/items/822-rosemary\|Rosemary]] | 2241.96, 1971.52 | 0 | 3013 |
| [[wiki/nodes/14213-emerald\|14213]] | node | Emerald | [[wiki/items/806-emerald\|Emerald]] | 2218.56, 2007.44 | 0 | 1084 |
| [[wiki/nodes/14214-rosemary\|14214]] | node | Rosemary | [[wiki/items/822-rosemary\|Rosemary]] | 2193.03, 1986.26 | 0 | 3013 |

> [!warning] Trigger positions outside this field
> Some `Trigger` rows of this field lie in [[wiki/zones/141-field-dungeon-05-orc-lv-5-tow-canyon|Field dungeon 05(orc) ((Lv 5) Tow Canyon)]], not in the zone of its gates. That zone belongs to [[wiki/fields/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]]; the rows look copied from it without moving them. The server should not use these positions as they are (*client data; cause unknown*).

### Dungeon

Entry cost, rewards, boss and schedule: [[wiki/dungeons/142-lv-9-dragon-island|(Lv 9) Dragon Island]].

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP08_08 | yes | yes |

### Mentioned in

- [[gameplay/dungeon-drops#2. Where the sheet disagrees with the client|Dungeon drops (ores and herbs) § 2. Where the sheet disagrees with the client]]
- [[gameplay/patch-history#Dungeons and world|Patch notes and other sources § Dungeons and world]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
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
