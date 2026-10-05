---
title: "The land of Greed"
type: "field"
id: 111
status: "stub"
missing: ["spawn_points", "npcs"]
sources: ["client: SceneList.cdb id 111", "client: Quest.cdb map1..3", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 111", "client: Quest.cdb (quests and objectives in field 111)", "client: Trigger.cdb field 111"]
name_key: "FieldName_111"
kind: "field"
scene_type: 5
max_users: 100
group: 12
neighbours: [103, 107]
nation: "Armia"
nation_copies: {"Arslan": 108, "Erion": 109, "Armia": 111}
zones: [116]
segments: ["ZP04_10"]
gates:
  - {"gate": 1107, "x": 1225.76, "z": 2761.94, "to_gate": 1124, "to_field": 107, "label": "FieldName_111"}
  - {"gate": 1137, "x": 1080.11, "z": 2620.79, "to_gate": 1142, "to_field": 113, "label": "FieldName_111"}
connections:
  - {"to": 107, "gate": 1107, "to_gate": 1124}
  - {"to": 113, "gate": 1137, "to_gate": 1142}
npcs: []
monsters: [721, 722, 723, 724, 826, 10001, 10002]
spawn_points: []
triggers:
  - {"id": 11105, "type": 3, "shape": 4, "x": 1216.22, "z": 2753.61, "name_key": "UnitName_241", "model": 187}
---
<!-- generated:start -->
<!-- generated-keys: title=4cdb69 type=7a94db id=6216f8 sources=f9f686 name_key=d9cad3 kind=7a94db scene_type=ac3478 max_users=310b86 group=7b5200 neighbours=a1f6d8 nation=b0e09b nation_copies=a918d5 zones=9b2ee1 segments=217b74 gates=ea660d connections=8ef7c8 npcs=97d170 monsters=63b507 spawn_points=97d170 triggers=d100a2 -->
|  |  |
|---|---|
|  | ![minimap of zone 116](wiki/assets/zones/116.png) |
| **Field id** | `111` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 12 (SceneList last column) |
| **Nation** | Armia |
| **Nation copies** | Arslan [[wiki/fields/108-the-land-of-greed\|Arslan (108)]], Erion [[wiki/fields/109-the-land-of-greed\|Erion (109)]], Armia **111** |
| **Zones** | [[wiki/zones/116-abyss-lv3-111-the-land-of-greed\|Abyss LV3 111 (The land of Greed)]] |
| **Terrain segments** | `ZP04_10` |
| **Name key** | `FieldName_111` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1107 | 1225.76, 2761.94 | [[wiki/fields/107-place-for-scattered-troops\|Place for Scattered troops]] | 1124 | FieldName_111 |
| 1137 | 1080.11, 2620.79 | [[wiki/fields/113-the-avenue-of-spirit\|The avenue of spirit]] | 1142 | FieldName_111 |

Entered from: [[wiki/fields/107-place-for-scattered-troops|Place for Scattered troops]] (gate 1124 → 1107), [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] (gate 1142 → 1137)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/103-place-for-scattered-troops|Place for Scattered troops]], [[wiki/fields/107-place-for-scattered-troops|Place for Scattered troops]]

### NPCs

None known yet.

### Monsters

| monster | unit | why it is listed |
|---|---|---|
| [[wiki/monsters/721-fragile-tow-warrior\|Fragile Tow Warrior]] | 721 | kill objective of quest [[wiki/quests/80-support-the-abyss-expedition\|80]], [[wiki/quests/81-support-the-abyss-expedition\|81]], [[wiki/quests/82-support-the-abyss-expedition\|82]], [[wiki/quests/749-kill-monster-of-the-land-of-greed\|749]], [[wiki/quests/1101-the-land-of-greed-kill-monster\|1101]] (kill group 10001, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/722-fragile-tow-sorcerer\|Fragile Tow Sorcerer]] | 722 | kill objective of quest [[wiki/quests/80-support-the-abyss-expedition\|80]], [[wiki/quests/81-support-the-abyss-expedition\|81]], [[wiki/quests/82-support-the-abyss-expedition\|82]], [[wiki/quests/749-kill-monster-of-the-land-of-greed\|749]], [[wiki/quests/1101-the-land-of-greed-kill-monster\|1101]] (kill group 10001, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/723-fragile-elite-tow-warrior\|Fragile Elite Tow Warrior]] | 723 | kill objective of quest [[wiki/quests/80-support-the-abyss-expedition\|80]], [[wiki/quests/81-support-the-abyss-expedition\|81]], [[wiki/quests/82-support-the-abyss-expedition\|82]], [[wiki/quests/749-kill-monster-of-the-land-of-greed\|749]], [[wiki/quests/1101-the-land-of-greed-kill-monster\|1101]] (kill group 10002, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/724-fragile-elite-tow-sorcerer\|Fragile Elite Tow Sorcerer]] | 724 | kill objective of quest [[wiki/quests/80-support-the-abyss-expedition\|80]], [[wiki/quests/81-support-the-abyss-expedition\|81]], [[wiki/quests/82-support-the-abyss-expedition\|82]], [[wiki/quests/749-kill-monster-of-the-land-of-greed\|749]], [[wiki/quests/1101-the-land-of-greed-kill-monster\|1101]] (kill group 10002, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/826-tow-chief\|Tow Chief]] | 826 | kill objective of quest [[wiki/quests/80-support-the-abyss-expedition\|80]], [[wiki/quests/81-support-the-abyss-expedition\|81]], [[wiki/quests/82-support-the-abyss-expedition\|82]]; monster page (`spawns` / `spawn_fields`) |
| unit 10001 (not in UnitDB) | 10001 | hand-entered |
| unit 10002 (not in UnitDB) | 10002 | hand-entered |

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Client-placed objects (`Trigger`)

Talk devices (shape 4) and gathering nodes (type 0, shape 5: the item is what gathering gives). The server can load these as they are; the video check in [[gameplay/video-dungeon-run|Nas Village dungeon run]] §5 matched them within 5 units.

| trigger | kind | name | gives | at (x, z) | type | model |
|---|---|---|---|---|---|---|
| [[wiki/nodes/11105-scout-leader\|11105]] | talk/device | Scout Leader |  | 1216.22, 2753.61 | 3 | 187 |

### Quests in this field

[[wiki/quests/80-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/81-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/82-support-the-abyss-expedition|Support the Abyss expedition]]

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP04_10 | yes | yes |

### Mentioned in

- [[gameplay/server-rules#Added from the source hunt (see ((gameplay/sources/Sources and gaps)))|Server rules checklist § Added from the source hunt (see ((gameplay/sources/Sources and gaps)))]]
- [[gameplay/abyss-map|Abyss map and portal graph]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] (by name)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] (by name)
- [[gameplay/warmonger-forum|Warmonger forum (2018)]] (by name)
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
