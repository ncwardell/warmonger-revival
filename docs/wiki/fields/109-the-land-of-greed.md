---
title: "The land of Greed"
type: "field"
id: 109
status: "partial"
missing: ["spawn_points", "npcs"]
sources: ["client: SceneList.cdb id 109", "client: Quest.cdb map1..3", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 109", "client: Quest.cdb (quests and objectives in field 109)", "client: Trigger.cdb field 109", "client + image: [[gameplay/abyss-map]] Portal table, Routes and Markers (unlabelled portals image-measured ±5 units)", "video: [[gameplay/video-early-quests]] §1-§3 and §6 (Land of Greed quests, Scout Leader, Gem Stone: Blue drops), video"]
name_key: "FieldName_109"
kind: "field"
scene_type: 5
max_users: 100
group: 12
nation: "Erion"
nation_copies: {"Arslan": 108, "Erion": 109, "Armia": 111}
zones: [114]
segments: ["ZP02_10"]
gates:
  - {"gate": 1114, "x": 701.93, "z": 2624.07, "to_gate": 1126, "to_field": 106, "label": "FieldName_109"}
  - {"gate": 1125, "x": 567.67, "z": 2620.55, "to_gate": 1131, "to_field": 105, "label": "FieldName_109"}
  - {"gate": 1135, "x": 711.35, "z": 2760.44, "to_gate": 1138, "to_field": 113, "label": "FieldName_109"}
connections:
  - {"to": 106, "gate": 1114, "to_gate": 1126}
  - {"to": 105, "gate": 1125, "to_gate": 1131}
  - {"to": 113, "gate": 1135, "to_gate": 1138}
  - {"to": 102, "gate": null, "to_gate": null, "at": [574, 2758], "to_at": [451, 2365], "source": "image"}
npcs: []
monsters: [721, 722, 723, 724, 826, 10001, 10002]
spawn_points: []
triggers:
  - {"id": 10904, "type": 3, "shape": 4, "x": 575.82, "z": 2629.17, "name_key": "UnitName_241", "model": 187}
---
<!-- generated:start -->
<!-- generated-keys: title=4cdb69 type=7a94db id=a1422e sources=c67f22 name_key=dc9240 kind=7a94db scene_type=ac3478 max_users=310b86 group=7b5200 nation=069950 nation_copies=a918d5 zones=6c4502 segments=8c2f3b gates=cc4947 connections=e341c9 npcs=97d170 monsters=63b507 spawn_points=97d170 triggers=fae5dc -->
|  |  |
|---|---|
|  | ![minimap of zone 114](wiki/assets/zones/114.png) |
| **Field id** | `109` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 12 (SceneList last column) |
| **Nation** | Erion |
| **Nation copies** | Arslan [[wiki/fields/108-the-land-of-greed\|Arslan (108)]], Erion **109**, Armia [[wiki/fields/111-the-land-of-greed\|Armia (111)]] |
| **Zones** | [[wiki/zones/114-abyss-lv3-109-the-land-of-greed\|Abyss LV3 109 (The land of Greed)]] |
| **Terrain segments** | `ZP02_10` |
| **Name key** | `FieldName_109` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1114 | 701.93, 2624.07 | [[wiki/fields/106-the-avenue-of-spirit\|The avenue of spirit]] | 1126 | FieldName_109 |
| 1125 | 567.67, 2620.55 | [[wiki/fields/105-place-for-scattered-troops\|Place for Scattered troops]] | 1131 | FieldName_109 |
| 1135 | 711.35, 2760.44 | [[wiki/fields/113-the-avenue-of-spirit\|The avenue of spirit]] | 1138 | FieldName_109 |

Other connections (hand-entered): to 102, gate None, to_gate None, at [574, 2758], to_at [451, 2365], source image

Entered from: [[wiki/fields/105-place-for-scattered-troops|Place for Scattered troops]] (gate 1131 → 1125), [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] (gate 1138 → 1135)

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
| [[wiki/nodes/10904-scout-leader\|10904]] | talk/device | Scout Leader |  | 575.82, 2629.17 | 3 | 187 |

### Quests in this field

[[wiki/quests/80-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/81-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/82-support-the-abyss-expedition|Support the Abyss expedition]]

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP02_10 | yes | yes |

### Mentioned in

- [[gameplay/abyss-map#Fields and layout|Abyss map and portal graph § Fields and layout]]
- [[gameplay/server-rules#Added from the source hunt (see ((gameplay/sources/Sources and gaps)))|Server rules checklist § Added from the source hunt (see ((gameplay/sources/Sources and gaps)))]]
- [[gameplay/video-character-creation-and-tutorial#After the tutorial (Fortress, from 22:00)|Video notes: character creation and tutorial (ZonderCoRe, June 2018) § After the tutorial (Fortress, from 22:00)]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] (by name)
- [[gameplay/warmonger-forum|Warmonger forum (2018)]] (by name)
<!-- generated:end -->

## Notes

- Abyss level 3. The three Land of Greed copies join the nations' level-2 fields (108 links 103, 105, 107; 109 links 102, 105, 106; 111 links 103, 104, 107), so players of different nations meet here ([[gameplay/abyss-map|Abyss map]] Routes). *image*
- Portals: top-left (about 574, 2758) → 102; top-right 1135 → 113; bottom-left 1125 → 105; bottom-right 1114 → 106 ([[gameplay/abyss-map|Abyss map]]). *client + image*
- The Erion player of the June 2018 video farmed Tows here from about 31:00 to the end ([[gameplay/video-character-creation-and-tutorial|character-creation video]] §3). *video*
- Gem Stone: Blue drops in the Land of Greed ([[gameplay/video-early-quests|first-session video]] §6). *video*
- Abyss rules from the 2018 patches: lower drop rate, kills do not count for the daily kill quest, 5 s immunity after moving, and later a non-PK area ([[gameplay/patch-history|Patch history]], WM 0329/0404/0511). The ES guide says Abyss monsters stop giving loot at level 30 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §1). *guide*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/abyss-map|Abyss map]], [[gameplay/video-early-quests|first-session video]], [[gameplay/patch-history|Patch history]].

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
