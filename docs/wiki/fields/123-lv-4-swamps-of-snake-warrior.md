---
title: "[Lv 4] Swamps of Snake Warrior"
type: "field"
id: 123
status: "stub"
missing: ["spawn_points"]
sources: ["client: SceneList.cdb id 123", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 123", "client: Quest.cdb (quests and objectives in field 123)", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 123"]
name_key: "FieldName_123"
kind: "dungeon"
scene_type: 3
max_users: 5
group: 35
zones: [137]
segments: ["ZP06_07"]
gates:
  - {"gate": 1233, "x": 1594.22, "z": 2005.18, "to_gate": 0, "to_field": 0, "label": "FieldName_123"}
  - {"gate": 1234, "x": 1712.34, "z": 1905.4, "to_gate": 1235, "to_field": 0, "label": "FiledPortal"}
  - {"gate": 1235, "x": 1731.77, "z": 1847.19, "to_gate": 1234, "to_field": 0, "label": "FiledPortal"}
connections:
  - {"to": null, "gate": 1233, "kind": "exit"}
npcs: []
monsters: [81, 646, 647, 648, 649, 675, 710, 711, 736, 1213, 10011, 10012, 10016]
spawn_points: []
triggers:
  - {"id": 12316, "type": 16, "shape": 4, "x": 1602.55, "z": 2004.82, "name_key": "UnitName_400", "model": 391}
  - {"id": 12317, "type": 17, "shape": 4, "x": 1627.73, "z": 1905.95, "name_key": "UnitName_400", "model": 391}
  - {"id": 12318, "type": 18, "shape": 4, "x": 1623.19, "z": 1867.09, "name_key": "UnitName_2591", "model": 2049}
  - {"id": 12301, "type": 0, "shape": 5, "x": 1644.9, "z": 1997.93, "name_key": "UnitName_1004", "item": 816, "model": 1087}
  - {"id": 12302, "type": 0, "shape": 5, "x": 1654.42, "z": 2006.56, "name_key": "UnitName_1012", "item": 826, "model": 3015}
  - {"id": 12303, "type": 0, "shape": 5, "x": 1737.61, "z": 2006.99, "name_key": "UnitName_1013", "item": 828, "model": 3016}
  - {"id": 12304, "type": 0, "shape": 5, "x": 1745.8, "z": 2008.49, "name_key": "UnitName_1004", "item": 816, "model": 1087}
  - {"id": 12305, "type": 0, "shape": 5, "x": 1695.53, "z": 1935.74, "name_key": "UnitName_1012", "item": 826, "model": 3015}
  - {"id": 12306, "type": 0, "shape": 5, "x": 1719.23, "z": 1923.95, "name_key": "UnitName_1013", "item": 828, "model": 3016}
  - {"id": 12307, "type": 0, "shape": 5, "x": 1716.36, "z": 1858.44, "name_key": "UnitName_1012", "item": 826, "model": 3015}
  - {"id": 12308, "type": 0, "shape": 5, "x": 1716.99, "z": 1823.16, "name_key": "UnitName_1013", "item": 828, "model": 3016}
  - {"id": 12309, "type": 0, "shape": 5, "x": 1647.26, "z": 1888.52, "name_key": "UnitName_1004", "item": 816, "model": 1087}
  - {"id": 12310, "type": 0, "shape": 5, "x": 1635.59, "z": 1905.26, "name_key": "UnitName_1012", "item": 826, "model": 3015}
  - {"id": 12311, "type": 0, "shape": 5, "x": 1612.69, "z": 1848.22, "name_key": "UnitName_1004", "item": 816, "model": 1087}
  - {"id": 12312, "type": 0, "shape": 5, "x": 1580.39, "z": 1854.04, "name_key": "UnitName_1012", "item": 826, "model": 3015}
dungeon: 123
---
<!-- generated:start -->
<!-- generated-keys: title=e5603a type=7a94db id=40bd00 sources=e76e5b name_key=b1037d kind=3e3f38 scene_type=77de68 max_users=ac3478 group=972a67 zones=65d3cb segments=ad9609 gates=7c17cd connections=6c6c57 npcs=97d170 monsters=da9811 spawn_points=97d170 triggers=95810a dungeon=40bd00 -->
|  |  |
|---|---|
|  | ![minimap of zone 137](wiki/assets/zones/137.png) |
|  | ![(Lv 4) Swamps of Snake Warrior](wiki/assets/dungeons/123.png) |
| **Field id** | `123` |
| **Kind** | dungeon (SceneList type 3; name *inferred*) |
| **Max users** | 5 (SceneList, column meaning *guessed*) |
| **Region group** | 35 (SceneList last column) |
| **Zones** | [[wiki/zones/137-field-dungeon-03-lizardman-lv-4-swamps-of-snake-warrior\|Field dungeon 03(lizardman) ((Lv 4) Swamps of Snake Warrior)]] |
| **Terrain segments** | `ZP06_07` |
| **Dungeon** | [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior\|dungeon page]] |
| **Name key** | `FieldName_123` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1233 | 1594.22, 2005.18 | entrance / exit (leaving returns you to the field you came from) | — | FieldName_123 |
| 1234 | 1712.34, 1905.4 | portal to gate 1235 in this field | 1235 | FiledPortal |
| 1235 | 1731.77, 1847.19 | portal to gate 1234 in this field | 1234 | FiledPortal |

### NPCs

None known yet.

### Monsters

| monster | unit | why it is listed |
|---|---|---|
| [[wiki/npcs/81-transmission-equipment\|Transmission equipment]] | 81 | kill objective of quest [[wiki/quests/784-swamps-of-the-snake-warrior\|784]] |
| [[wiki/monsters/646-lizard-swordsman\|Lizard Swordsman]] | 646 | kill objective of quest [[wiki/quests/32-swamps-of-snake-warrior\|32]], [[wiki/quests/733-weapon-appropriation\|733]], [[wiki/quests/1021-swamps-of-the-snake-warrior-hunting\|1021]] (kill group 10011, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/647-lizard-swordsman\|Lizard Swordsman]] | 647 | kill objective of quest [[wiki/quests/32-swamps-of-snake-warrior\|32]], [[wiki/quests/733-weapon-appropriation\|733]], [[wiki/quests/1021-swamps-of-the-snake-warrior-hunting\|1021]] (kill group 10011, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/648-elite-lizard-swordsman\|Elite Lizard Swordsman]] | 648 | kill objective of quest [[wiki/quests/32-swamps-of-snake-warrior\|32]], [[wiki/quests/733-weapon-appropriation\|733]], [[wiki/quests/1021-swamps-of-the-snake-warrior-hunting\|1021]] (kill group 10012, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/649-elite-lizard-lancer\|Elite Lizard Lancer]] | 649 | kill objective of quest [[wiki/quests/32-swamps-of-snake-warrior\|32]], [[wiki/quests/733-weapon-appropriation\|733]], [[wiki/quests/1021-swamps-of-the-snake-warrior-hunting\|1021]] (kill group 10012, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/675-slayer-komodo\|Slayer Komodo]] | 675 | kill objective of quest [[wiki/quests/757-group-border-area-hard-mode\|757]], [[wiki/quests/762-killed-boss-of-border-area-no-2\|762]], [[wiki/quests/1023-swamps-of-the-snake-warrior-boss-hunting\|1023]] (kill group 10016, UnitDB i32@80); boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/710-chepa-warrior-officer\|Chepa Warrior Officer]] | 710 | kill objective of quest [[wiki/quests/757-group-border-area-hard-mode\|757]], [[wiki/quests/762-killed-boss-of-border-area-no-2\|762]], [[wiki/quests/1023-swamps-of-the-snake-warrior-boss-hunting\|1023]] (kill group 10016, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/711-chepa-archer-officer\|Chepa Archer Officer]] | 711 | kill objective of quest [[wiki/quests/757-group-border-area-hard-mode\|757]], [[wiki/quests/762-killed-boss-of-border-area-no-2\|762]], [[wiki/quests/1023-swamps-of-the-snake-warrior-boss-hunting\|1023]] (kill group 10016, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/736-slayer-komodo\|Slayer Komodo]] | 736 | boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/1213-slayer-komodo\|Slayer Komodo]] | 1213 | boss ([[gameplay/maps-and-dungeons#2. Border-area (normal/hard) dungeons\|Maps and dungeons]]); monster page (`spawns` / `spawn_fields`) |
| unit 10011 (not in UnitDB) | 10011 | hand-entered |
| unit 10012 (not in UnitDB) | 10012 | hand-entered |
| unit 10016 (not in UnitDB) | 10016 | hand-entered |

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Client-placed objects (`Trigger`)

Talk devices (shape 4) and gathering nodes (type 0, shape 5: the item is what gathering gives). The server can load these as they are; the video check in [[gameplay/video-dungeon-run|Nas Village dungeon run]] §5 matched them within 5 units.

| trigger | kind | name | gives | at (x, z) | type | model |
|---|---|---|---|---|---|---|
| [[wiki/nodes/12316-a-doubtful-character\|12316]] | talk/device | A Doubtful character |  | 1602.55, 2004.82 | 16 | 391 |
| [[wiki/nodes/12317-a-doubtful-character\|12317]] | talk/device | A Doubtful character |  | 1627.73, 1905.95 | 17 | 391 |
| [[wiki/nodes/12318-swamp-mushroom\|12318]] | talk/device | Swamp mushroom |  | 1623.19, 1867.09 | 18 | 2049 |
| [[wiki/nodes/12301-onyx\|12301]] | node | Onyx | [[wiki/items/816-onyx\|Onyx]] | 1644.9, 1997.93 | 0 | 1087 |
| [[wiki/nodes/12302-borage\|12302]] | node | Borage | [[wiki/items/826-borage\|Borage]] | 1654.42, 2006.56 | 0 | 3015 |
| [[wiki/nodes/12303-spartium\|12303]] | node | Spartium | [[wiki/items/828-spartium\|Spartium]] | 1737.61, 2006.99 | 0 | 3016 |
| [[wiki/nodes/12304-onyx\|12304]] | node | Onyx | [[wiki/items/816-onyx\|Onyx]] | 1745.8, 2008.49 | 0 | 1087 |
| [[wiki/nodes/12305-borage\|12305]] | node | Borage | [[wiki/items/826-borage\|Borage]] | 1695.53, 1935.74 | 0 | 3015 |
| [[wiki/nodes/12306-spartium\|12306]] | node | Spartium | [[wiki/items/828-spartium\|Spartium]] | 1719.23, 1923.95 | 0 | 3016 |
| [[wiki/nodes/12307-borage\|12307]] | node | Borage | [[wiki/items/826-borage\|Borage]] | 1716.36, 1858.44 | 0 | 3015 |
| [[wiki/nodes/12308-spartium\|12308]] | node | Spartium | [[wiki/items/828-spartium\|Spartium]] | 1716.99, 1823.16 | 0 | 3016 |
| [[wiki/nodes/12309-onyx\|12309]] | node | Onyx | [[wiki/items/816-onyx\|Onyx]] | 1647.26, 1888.52 | 0 | 1087 |
| [[wiki/nodes/12310-borage\|12310]] | node | Borage | [[wiki/items/826-borage\|Borage]] | 1635.59, 1905.26 | 0 | 3015 |
| [[wiki/nodes/12311-onyx\|12311]] | node | Onyx | [[wiki/items/816-onyx\|Onyx]] | 1612.69, 1848.22 | 0 | 1087 |
| [[wiki/nodes/12312-borage\|12312]] | node | Borage | [[wiki/items/826-borage\|Borage]] | 1580.39, 1854.04 | 0 | 3015 |

### Dungeon

Entry cost, rewards, boss and schedule: [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]].

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP06_07 | yes | yes |

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
