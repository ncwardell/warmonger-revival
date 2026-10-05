---
title: "[Lv 1] Chepa Village"
type: "field"
id: 127
status: "stub"
missing: ["spawn_points"]
sources: ["client: SceneList.cdb id 127", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 127", "client: Quest.cdb (quests and objectives in field 127)", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 127"]
name_key: "FieldName_127"
kind: "dungeon"
scene_type: 3
max_users: 5
group: 32
zones: [149]
segments: ["ZP04_14"]
gates:
  - {"gate": 1255, "x": 1078.94, "z": 3650.26, "to_gate": 0, "to_field": 127, "label": "FieldName_127"}
connections:
  - {"to": null, "gate": 1255, "kind": "exit"}
npcs: []
monsters: [668, 669, 670, 671, 870, 950, 10000, 10025, 10026]
spawn_points: []
triggers:
  - {"id": 12701, "type": 0, "shape": 5, "x": 1109.42, "z": 3657.94, "name_key": "UnitName_1008", "item": 818, "model": 3011}
  - {"id": 12702, "type": 0, "shape": 5, "x": 1125.25, "z": 3654.3, "name_key": "UnitName_1009", "item": 820, "model": 3012}
  - {"id": 12703, "type": 0, "shape": 5, "x": 1175.44, "z": 3686.5, "name_key": "UnitName_1008", "item": 818, "model": 3011}
  - {"id": 12704, "type": 0, "shape": 5, "x": 1149.42, "z": 3701.81, "name_key": "UnitName_1009", "item": 820, "model": 3012}
  - {"id": 12705, "type": 0, "shape": 5, "x": 1226.65, "z": 3769.81, "name_key": "UnitName_1008", "item": 818, "model": 3011}
  - {"id": 12706, "type": 0, "shape": 5, "x": 1216.1, "z": 3780.88, "name_key": "UnitName_1009", "item": 820, "model": 3012}
  - {"id": 12707, "type": 0, "shape": 5, "x": 1120.21, "z": 3776.86, "name_key": "UnitName_1008", "item": 818, "model": 3011}
  - {"id": 12708, "type": 0, "shape": 5, "x": 1112.15, "z": 3733.51, "name_key": "UnitName_1009", "item": 820, "model": 3012}
dungeon: 127
---
<!-- generated:start -->
<!-- generated-keys: title=a46136 type=7a94db id=008451 sources=7d3941 name_key=d34b84 kind=3e3f38 scene_type=77de68 max_users=ac3478 group=cb4e52 zones=7d2f32 segments=2555d9 gates=c56e49 connections=967275 npcs=97d170 monsters=1b1a6a spawn_points=97d170 triggers=ad87f0 dungeon=008451 -->
|  |  |
|---|---|
|  | ![minimap of zone 149](../assets/zones/149.png) |
|  | ![(Lv 1) Chepa Village](../assets/dungeons/127.png) |
| **Field id** | `127` |
| **Kind** | dungeon (SceneList type 3; name *inferred*) |
| **Max users** | 5 (SceneList, column meaning *guessed*) |
| **Region group** | 32 (SceneList last column) |
| **Zones** | [[wiki/zones/149-training-ground-border-area-lv-1-chepa-village\|Training Ground (border area) ((Lv 1) Chepa Village)]] |
| **Terrain segments** | `ZP04_14` |
| **Dungeon** | [[wiki/dungeons/127-lv-1-chepa-village\|dungeon page]] |
| **Name key** | `FieldName_127` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1255 | 1078.94, 3650.26 | entrance / exit (leaving returns you to the field you came from) | — | FieldName_127 |

### NPCs

None known yet.

### Monsters

| monster | unit | why it is listed |
|---|---|---|
| [[wiki/monsters/668-chepa-warrior\|Chepa Warrior]] | 668 | kill objective of quest [[wiki/quests/30-chepa-village\|30]], [[wiki/quests/736-hunting-for-furs\|736]], [[wiki/quests/1001-chepa-village-hunting\|1001]] (kill group 10025, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/669-chepa-archer\|Chepa Archer]] | 669 | kill objective of quest [[wiki/quests/30-chepa-village\|30]], [[wiki/quests/736-hunting-for-furs\|736]], [[wiki/quests/1001-chepa-village-hunting\|1001]] (kill group 10025, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/670-elite-chepa-warrior\|Elite Chepa Warrior]] | 670 | kill objective of quest [[wiki/quests/30-chepa-village\|30]] (kill group 10026, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/671-elite-chepa-archer\|Elite Chepa Archer]] | 671 | kill objective of quest [[wiki/quests/30-chepa-village\|30]] (kill group 10026, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/870-chepa-sorcerer\|Chepa Sorcerer]] | 870 | kill objective of quest [[wiki/quests/761-killed-boss-of-border-area-no-1\|761]], [[wiki/quests/769-group-border-area-hard-mode\|769]], [[wiki/quests/772-group-border-area-hard-mode\|772]], [[wiki/quests/773-group-border-area-hard-mode\|773]], [[wiki/quests/1003-chepa-village-boss-hunting\|1003]] (kill group 10000, UnitDB i32@80); boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/950-chepa-sorcerer\|Chepa Sorcerer]] | 950 | boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| unit 10000 (not in UnitDB) | 10000 | hand-entered |
| unit 10025 (not in UnitDB) | 10025 | hand-entered |
| unit 10026 (not in UnitDB) | 10026 | hand-entered |

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Client-placed objects (`Trigger`)

Talk devices (shape 4) and gathering nodes (type 0, shape 5: the item is what gathering gives). The server can load these as they are; the video check in [[gameplay/video-dungeon-run|Nas Village dungeon run]] §5 matched them within 5 units.

| trigger | kind | name | gives | at (x, z) | type | model |
|---|---|---|---|---|---|---|
| [[wiki/nodes/12701-lavender\|12701]] | node | Lavender | [[wiki/items/818-lavender\|Lavender]] | 1109.42, 3657.94 | 0 | 3011 |
| [[wiki/nodes/12702-peppermint\|12702]] | node | Peppermint | [[wiki/items/820-peppermint\|Peppermint]] | 1125.25, 3654.3 | 0 | 3012 |
| [[wiki/nodes/12703-lavender\|12703]] | node | Lavender | [[wiki/items/818-lavender\|Lavender]] | 1175.44, 3686.5 | 0 | 3011 |
| [[wiki/nodes/12704-peppermint\|12704]] | node | Peppermint | [[wiki/items/820-peppermint\|Peppermint]] | 1149.42, 3701.81 | 0 | 3012 |
| [[wiki/nodes/12705-lavender\|12705]] | node | Lavender | [[wiki/items/818-lavender\|Lavender]] | 1226.65, 3769.81 | 0 | 3011 |
| [[wiki/nodes/12706-peppermint\|12706]] | node | Peppermint | [[wiki/items/820-peppermint\|Peppermint]] | 1216.1, 3780.88 | 0 | 3012 |
| [[wiki/nodes/12707-lavender\|12707]] | node | Lavender | [[wiki/items/818-lavender\|Lavender]] | 1120.21, 3776.86 | 0 | 3011 |
| [[wiki/nodes/12708-peppermint\|12708]] | node | Peppermint | [[wiki/items/820-peppermint\|Peppermint]] | 1112.15, 3733.51 | 0 | 3012 |

### Dungeon

Entry cost, rewards, boss and schedule: [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]].

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP04_14 | yes | yes |

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
