---
title: "Elite Demon Hunter"
type: "monster"
id: 681
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 681", "client: Quest.cdb kill objectives (quests 746, 1041)"]
name_key: "UnitName_681"
category: 1
class_mask: 1
kill_group: 10036
model: 348
model_name: "MOB_Demon_01_0_1_0_03_03"
model_path: "character/npc/monster/mob_demon/mob_demon_01.mo"
scale: 1.8
radius: 1
sounds: [4070068, 4070068, 4070066, 4070066, 4070067]
quest_targets:
  - {"quest": 746, "need": 5, "group": 10036}
  - {"quest": 1041, "need": 5, "group": 10036}
quest_drops:
  - {"quest": 746, "item": 2581, "rate": 100, "need": 5}
  - {"quest": 1041, "item": 2681, "rate": 100, "need": 5}
spawn_fields: [129]
---
<!-- generated:start -->
<!-- generated-keys: title=23000c type=9bbc46 id=89d79a sources=771394 name_key=01387d category=356a19 class_mask=356a19 kill_group=9cbdc5 model=cfd179 model_name=34c465 model_path=6bdcd6 scale=93ec1d radius=356a19 sounds=879981 quest_targets=6d9fcb quest_drops=4e8036 spawn_fields=0ae2ea -->
|  |  |
|---|---|
| **Unit id** | `681` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10036` with [[wiki/monsters/682-elite-devil-miner\|Elite Devil Miner]] |
| **Model** | ObjectList `348` MOB_Demon_01_0_1_0_03_03 (`character/npc/monster/mob_demon/mob_demon_01.mo`) |
| **Scale** | 1.8 (second scale / radius 1) |

*No image: the client has no 2-D monster art (only the 3-D model).*

### Server stats

None of these is in the client; they were server data. Fill them in the front matter with a source (`drops: [{"item": id, "rate": %, "count": [min, max]}]`, `spawns: [{"field": id, "x": .., "z": .., "count": n, "respawn_s": s}]`).

| field | value |
|---|---|
| hp | **missing** |
| level | **missing** |
| attack | **missing** |
| armor | **missing** |
| magic_resist | **missing** |
| move_speed | **missing** |
| attack_speed | **missing** |
| attack_range | **missing** |
| kill_exp | **missing** |
| kill_gold | **missing** |
| drops | **missing** |
| spawns | **missing** |

### Quests

- [[wiki/quests/746-devil-s-material|Devil's material]]: collect 5 × [[wiki/items/2581-red-demon-hunter-horn|Red Demon Hunter Horn]] (drops at 100% while the quest is active) in [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] — via kill group `10036` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1041-thorn-s-hell-hunting|Thorn's Hell : Hunting]]: collect 5 × [[wiki/items/2681-red-demon-hunter-horn|Red Demon Hunter Horn]] (drops at 100% while the quest is active) in [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] — via kill group `10036` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] — quest map of [[wiki/quests/746-devil-s-material|Devil's material]], [[wiki/quests/1041-thorn-s-hell-hunting|Thorn's Hell : Hunting]]

### Other units with this name

[[wiki/monsters/663-elite-demon-hunter|Elite Demon Hunter (663)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070068 | `Unit/UE4070068.wav` |
| 2 | 0 | 4070068 | `Unit/UE4070068.wav` |
| 3 | 0 | 4070066 | `Unit/UE4070066.wav` |
| 4 | 0 | 4070066 | `Unit/UE4070066.wav` |
| 5 | 0 | 4070067 | `Unit/UE4070067.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 7 |
| f32@10c | 1 |
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
