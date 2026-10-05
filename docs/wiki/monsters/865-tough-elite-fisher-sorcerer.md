---
title: "Tough Elite Fisher Sorcerer"
type: "monster"
id: 865
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 865"]
name_key: "UnitName_865"
category: 1
class_mask: 1
model: 56
model_name: "MOB_Fisher_Elite_01"
model_path: "character/npc/monster/mob_fisher_elite_01/mob_fisher_elite_01.mo"
scale: 1.8
radius: 1
projectile: 769
sounds: [4070034, 4070034, 4070033, 4070033, 4070034]
---
<!-- generated:start -->
<!-- generated-keys: title=bee0c9 type=9bbc46 id=81d51c sources=482063 name_key=058a21 category=356a19 class_mask=356a19 model=54ceb9 model_name=3a50ec model_path=f26884 scale=93ec1d radius=356a19 projectile=98079d sounds=94fe28 -->
|  |  |
|---|---|
| **Unit id** | `865` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `56` MOB_Fisher_Elite_01 (`character/npc/monster/mob_fisher_elite_01/mob_fisher_elite_01.mo`) |
| **Scale** | 1.8 (second scale / radius 1) |
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

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070034 | `Unit/UE4070034.wav` |
| 2 | 0 | 4070034 | `Unit/UE4070034.wav` |
| 3 | 770 | 4070033 | `Unit/UE4070033.wav` |
| 4 | 770 | 4070033 | `Unit/UE4070033.wav` |
| 5 | 0 | 4070034 | `Unit/UE4070034.wav` |

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
