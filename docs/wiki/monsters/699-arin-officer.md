---
title: "Arin Officer"
type: "monster"
id: 699
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 699"]
name_key: "UnitName_699"
category: 1
class_mask: 1
model: 429
model_name: "test_0_1_0_00_00"
model_path: "character/npc/monster/mob_dragon/mob_dragon_elite_01.mo"
scale: 2.8
radius: 1
sounds: [4070504, 4070504, 4070505, 4070505, 4070505, 4070506]
---
<!-- generated:start -->
<!-- generated-keys: title=254075 type=9bbc46 id=8666e1 sources=5f2ada name_key=4a296c category=356a19 class_mask=356a19 model=75988f model_name=f2db30 model_path=612e48 scale=368ca5 radius=356a19 sounds=f184b2 -->
|  |  |
|---|---|
| **Unit id** | `699` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `429` test_0_1_0_00_00 (`character/npc/monster/mob_dragon/mob_dragon_elite_01.mo`) |
| **Scale** | 2.8 (second scale / radius 1) |

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
| 1 | 0 | 4070504 | `Unit/UE4070504.wav` |
| 2 | 0 | 4070504 | `Unit/UE4070504.wav` |
| 3 | 0 | 4070505 | `Unit/UE4070505.wav` |
| 4 | 0 | 4070505 | `Unit/UE4070505.wav` |
| 5 | 0 | 4070505 | `Unit/UE4070505.wav` |
| 6 | 0 | 4070506 | `Unit/UE4070506.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 4 |
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
