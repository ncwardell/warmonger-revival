---
title: "The land of Greed"
type: "field"
id: 108
status: "partial"
missing: ["spawn_points", "npcs"]
sources: ["client: SceneList.cdb id 108", "client: Quest.cdb map1..3", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 108", "client: Quest.cdb (quests and objectives in field 108)", "client: Trigger.cdb field 108", "client + image: [[gameplay/abyss-map]] Portal table, Routes and Markers (unlabelled portals image-measured ±5 units)", "video: [[gameplay/video-early-quests]] §1-§3 and §6 (Land of Greed quests, Scout Leader, Gem Stone: Blue drops), video"]
name_key: "FieldName_108"
kind: "field"
scene_type: 5
max_users: 100
group: 12
nation: "Arslan"
nation_copies: {"Arslan": 108, "Erion": 109, "Armia": 111}
zones: [113]
segments: ["ZP01_10"]
gates:
  - {"gate": 1109, "x": 456.63, "z": 2761.09, "to_gate": 1122, "to_field": 103, "label": "FieldName_108"}
  - {"gate": 1140, "x": 308.96, "z": 2619.52, "to_gate": 1134, "to_field": 113, "label": "FieldName_108"}
connections:
  - {"to": 103, "gate": 1109, "to_gate": 1122}
  - {"to": 113, "gate": 1140, "to_gate": 1134}
  - {"to": 105, "gate": null, "to_gate": null, "at": [318, 2755], "to_at": [1217, 2365], "source": "image"}
  - {"to": 107, "gate": null, "to_gate": null, "at": [445, 2621], "to_at": [1593, 2362], "source": "image"}
npcs: []
monsters: [721, 722, 723, 724, 826, 10001, 10002]
spawn_points: []
triggers:
  - {"id": 10803, "type": 3, "shape": 4, "x": 448.84, "z": 2753.87, "name_key": "UnitName_241", "model": 187}
---
<!-- generated:start -->
<!-- generated-keys: title=4cdb69 type=7a94db id=17503a sources=ec9092 name_key=5694ac kind=7a94db scene_type=ac3478 max_users=310b86 group=7b5200 nation=a20b0f nation_copies=a918d5 zones=85c8ae segments=df8332 gates=482247 connections=929b42 npcs=97d170 monsters=63b507 spawn_points=97d170 triggers=37cac2 -->
|  |  |
|---|---|
|  | ![minimap of zone 113](wiki/assets/zones/113.png) |
| **Field id** | `108` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 12 (SceneList last column) |
| **Nation** | Arslan |
| **Nation copies** | Arslan **108**, Erion [[wiki/fields/109-the-land-of-greed\|Erion (109)]], Armia [[wiki/fields/111-the-land-of-greed\|Armia (111)]] |
| **Zones** | [[wiki/zones/113-abyss-lv3-108-the-land-of-greed\|Abyss LV3 108 (The land of Greed)]] |
| **Terrain segments** | `ZP01_10` |
| **Name key** | `FieldName_108` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1109 | 456.63, 2761.09 | [[wiki/fields/103-place-for-scattered-troops\|Place for Scattered troops]] | 1122 | FieldName_108 |
| 1140 | 308.96, 2619.52 | [[wiki/fields/113-the-avenue-of-spirit\|The avenue of spirit]] | 1134 | FieldName_108 |

Other connections (hand-entered): to 105, gate None, to_gate None, at [318, 2755], to_at [1217, 2365], source image; to 107, gate None, to_gate None, at [445, 2621], to_at [1593, 2362], source image

Entered from: [[wiki/fields/103-place-for-scattered-troops|Place for Scattered troops]] (gate 1122 → 1109), [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] (gate 1134 → 1140)

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
| [[wiki/nodes/10803-scout-leader\|10803]] | talk/device | Scout Leader |  | 448.84, 2753.87 | 3 | 187 |

### Quests in this field

[[wiki/quests/80-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/81-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/82-support-the-abyss-expedition|Support the Abyss expedition]]

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP01_10 | yes | yes |

### Mentioned in

- [[gameplay/server-rules#Added from the source hunt (see ((gameplay/sources/Sources and gaps)))|Server rules checklist § Added from the source hunt (see ((gameplay/sources/Sources and gaps)))]]
- [[gameplay/server-rules#Added from the Warmonger forum and videos (round 2)|Server rules checklist § Added from the Warmonger forum and videos (round 2)]]
- [[gameplay/warmonger-forum#3. Bosses, essences and the Tow quest|Warmonger forum (2018) § 3. Bosses, essences and the Tow quest]]
- [[gameplay/abyss-map|Abyss map and portal graph]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] (by name)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] (by name)
<!-- generated:end -->

## Notes

- Abyss level 3. The three Land of Greed copies join the nations' level-2 fields (108 links 103, 105, 107; 109 links 102, 105, 106; 111 links 103, 104, 107), so players of different nations meet here ([[gameplay/abyss-map|Abyss map]] Routes). *image*
- Portals: top-right 1109 → 103; bottom-left 1140 → 113; top-left (about 318, 2755) → 105; bottom-right (about 445, 2621) → 107 ([[gameplay/abyss-map|Abyss map]]). *client + image*
- Seven open clearings at about (390, 2738), (362, 2713), (332, 2683), (385, 2689), (432, 2693), (404, 2668) and (376, 2637); the centre one (385, 2689) carries a red multi-dot icon, probably a boss or elite group; red dots in three others may be monsters ([[gameplay/abyss-map|Abyss map]] Markers, meanings *guess*). *image*
- The Scout Leader is Trigger 10803; the April 2018 video measured him within 6 units of it ([[gameplay/video-early-quests|first-session video]] §3). Quests 17 and 80-82 "Support the Abyss expedition" are done here: 10 Tow, 10 Elite Tow and the Tow's Chief (826); the repeatable 749 / 1101 asks 50 Tow + 50 Elite Tow ([[gameplay/video-early-quests|first-session video]] §2 items 16-17, 21; [[gameplay/warmonger-forum]] §3). *client + video*
- The ES guide names Tow monsters as the Abyss target for levels 1-25 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §1). *guide*
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
