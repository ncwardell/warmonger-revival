---
title: "Black Skeleton Archer"
type: "monster"
id: 665
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 665", "client: Quest.cdb kill objectives (quests 724, 1011)"]
name_key: "UnitName_665"
category: 1
class_mask: 1
kill_group: 10027
model: 15
model_name: "MOB_Seleton02_02"
model_path: "character/npc/monster/mob_seleton02/mob_seleton02_02.mo"
scale: 0.8
radius: 0.8
projectile: 583
sounds: [4070113, 4070113, 4070014, 4070014, 4070014, 4070003]
quest_targets:
  - {"quest": 724, "need": 1, "group": 10027}
  - {"quest": 1011, "need": 1, "group": 10027}
quest_drops:
  - {"quest": 724, "item": 2573, "rate": 10, "need": 1}
  - {"quest": 1011, "item": 2673, "rate": 10, "need": 1}
spawn_fields: [128]
---
<!-- generated:start -->
<!-- generated-keys: title=c7cccf type=9bbc46 id=af7166 sources=569555 name_key=b7dc72 category=356a19 class_mask=356a19 kill_group=b9cc0a model=f1abd6 model_name=86156e model_path=2b81db scale=480262 radius=480262 projectile=9c676e sounds=89c031 quest_targets=23d085 quest_drops=44ad55 spawn_fields=c9e1d0 -->
|  |  |
|---|---|
| **Unit id** | `665` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10027` with [[wiki/monsters/664-black-skeleton-warrior\|Black Skeleton Warrior]] |
| **Model** | ObjectList `15` MOB_Seleton02_02 (`character/npc/monster/mob_seleton02/mob_seleton02_02.mo`) |
| **Scale** | 0.8 (second scale / radius 0.8) |
| **Projectile?** | `u32@bc` = 583 (archers carry one; meaning *inferred*) |

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

- [[wiki/quests/724-find-lost-item|Find lost item]]: collect 1 × [[wiki/items/2573-toy-ring|Toy Ring]] (drops at 10% while the quest is active) in [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] — via kill group `10027` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1011-skull-cemetery-hunting|Skull Cemetery : Hunting]]: collect 1 × [[wiki/items/2673-toy-ring|Toy Ring]] (drops at 10% while the quest is active) in [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] — via kill group `10027` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] — quest map of [[wiki/quests/724-find-lost-item|Find lost item]], [[wiki/quests/1011-skull-cemetery-hunting|Skull Cemetery : Hunting]]

### Other units with this name

[[wiki/monsters/714-black-skeleton-archer|Black Skeleton Archer (714)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070113 | `Unit/UE4070113.wav` |
| 2 | 0 | 4070113 | `Unit/UE4070113.wav` |
| 3 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 4 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 5 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 6 | 0 | 4070003 | `Unit/UE4070003.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 2.7 |
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
