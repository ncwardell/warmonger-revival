---
title: "Elite Fisher"
type: "monster"
id: 645
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 645", "client: Quest.cdb kill objectives (quests 16, 732, 782, 1016)"]
name_key: "UnitName_645"
category: 1
class_mask: 1
model: 56
model_name: "MOB_Fisher_Elite_01"
model_path: "character/npc/monster/mob_fisher_elite_01/mob_fisher_elite_01.mo"
scale: 1.7
radius: 1
projectile: 769
sounds: [4070034, 4070034, 4070033, 4070033, 4070033]
quest_targets:
  - {"quest": 16, "need": 5}
  - {"quest": 732, "need": 10}
  - {"quest": 782, "need": 10}
  - {"quest": 1016, "need": 10}
quest_drops:
  - {"quest": 16, "item": 2566, "rate": 100, "need": 5}
  - {"quest": 732, "item": 2576, "rate": 100, "need": 10}
  - {"quest": 1016, "item": 2676, "rate": 100, "need": 10}
spawn_fields: [122]
---
<!-- generated:start -->
<!-- generated-keys: title=255c45 type=9bbc46 id=f7b41d sources=7c4b50 name_key=c3097d category=356a19 class_mask=356a19 model=54ceb9 model_name=3a50ec model_path=f26884 scale=58e6d3 radius=356a19 projectile=98079d sounds=b7daa0 quest_targets=bc9805 quest_drops=e0e43a spawn_fields=d4ee27 -->
|  |  |
|---|---|
| **Unit id** | `645` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `56` MOB_Fisher_Elite_01 (`character/npc/monster/mob_fisher_elite_01/mob_fisher_elite_01.mo`) |
| **Scale** | 1.7 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 769 (archers carry one; meaning *inferred*) |

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

- [[wiki/quests/16-farrell-s-request|Farrell's Request]]: collect 5 × [[wiki/items/2566-crystal-ball|Crystal Ball]] (drops at 100% while the quest is active) in [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]]
- [[wiki/quests/732-fisher-s-scales|Fisher's scales]]: collect 10 × [[wiki/items/2576-elite-fisher-s-scales|Elite Fisher's Scales]] (drops at 100% while the quest is active) in [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]]
- [[wiki/quests/782-tsunami-lake|Tsunami Lake]]: kill 10 in [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]]
- [[wiki/quests/1016-tsunami-lake-hunting|Tsunami Lake : Hunting]]: collect 10 × [[wiki/items/2676-elite-fisher-s-scales|Elite Fisher's Scales]] (drops at 100% while the quest is active) in [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]]

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] — quest map of [[wiki/quests/16-farrell-s-request|Farrell's Request]], [[wiki/quests/732-fisher-s-scales|Fisher's scales]], [[wiki/quests/782-tsunami-lake|Tsunami Lake]], [[wiki/quests/1016-tsunami-lake-hunting|Tsunami Lake : Hunting]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070034 | `Unit/UE4070034.wav` |
| 2 | 0 | 4070034 | `Unit/UE4070034.wav` |
| 3 | 770 | 4070033 | `Unit/UE4070033.wav` |
| 4 | 770 | 4070033 | `Unit/UE4070033.wav` |
| 5 | 0 | 4070033 | `Unit/UE4070033.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 4 |
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
