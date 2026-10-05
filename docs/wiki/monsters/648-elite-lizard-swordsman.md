---
title: "Elite Lizard Swordsman"
type: "monster"
id: 648
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 648", "client: Quest.cdb kill objectives (quests 32, 733, 1021)"]
name_key: "UnitName_648"
category: 1
class_mask: 1
kill_group: 10012
model: 71
model_name: "MOB_Lizardman_01"
model_path: "character/npc/monster/mob_lizardman/mob_lizardman_01.mo"
scale: 2
radius: 1
sounds: [4070000, 4070000, 4070013, 4070013, 4070013]
quest_targets:
  - {"quest": 32, "need": 5, "group": 10012}
  - {"quest": 733, "need": 5, "group": 10012}
  - {"quest": 1021, "need": 5, "group": 10012}
quest_drops:
  - {"quest": 733, "item": 2579, "rate": 100, "need": 5}
  - {"quest": 1021, "item": 2679, "rate": 100, "need": 5}
spawn_fields: [123]
---
<!-- generated:start -->
<!-- generated-keys: title=7cbc85 type=9bbc46 id=4de62d sources=61967a name_key=0c2054 category=356a19 class_mask=356a19 kill_group=fcf3e8 model=d02560 model_name=39ab4b model_path=21b985 scale=da4b92 radius=356a19 sounds=904c2a quest_targets=e5c76e quest_drops=7e4036 spawn_fields=4feada -->
|  |  |
|---|---|
| **Unit id** | `648` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10012` with [[wiki/monsters/649-elite-lizard-lancer\|Elite Lizard Lancer]] |
| **Model** | ObjectList `71` MOB_Lizardman_01 (`character/npc/monster/mob_lizardman/mob_lizardman_01.mo`) |
| **Scale** | 2 (second scale / radius 1) |

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

- [[wiki/quests/32-swamps-of-snake-warrior|Swamps of Snake Warrior]]: kill 5 in [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] — via kill group `10012` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/733-weapon-appropriation|Weapon appropriation]]: collect 5 × [[wiki/items/2579-lizard-knife|Lizard knife]] (drops at 100% while the quest is active) in [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] — via kill group `10012` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1021-swamps-of-the-snake-warrior-hunting|Swamps of the Snake Warrior : Hunting]]: collect 5 × [[wiki/items/2679-lizard-knife|Lizard knife]] (drops at 100% while the quest is active) in [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] — via kill group `10012` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] — quest map of [[wiki/quests/32-swamps-of-snake-warrior|Swamps of Snake Warrior]], [[wiki/quests/733-weapon-appropriation|Weapon appropriation]], [[wiki/quests/1021-swamps-of-the-snake-warrior-hunting|Swamps of the Snake Warrior : Hunting]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 2 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 3 | 12 | 4070013 | `Unit/UE4070013.wav` |
| 4 | 12 | 4070013 | `Unit/UE4070013.wav` |
| 5 | 0 | 4070013 | `Unit/UE4070013.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 3 |
| f32@10c | 0.5 |
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
