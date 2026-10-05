---
title: "Lypiz"
type: "monster"
id: 695
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 695"]
name_key: "UnitName_695"
category: 1
class_mask: 1
model: 431
model_name: "MOB_Dragon_01_0_1_0_01_01"
model_path: "character/npc/monster/mob_dragon/mob_dragon_01.mo"
scale: 1.8
radius: 1
projectile: 1216
sounds: [4070501, 4070501, 4070502, 4070502, 4070502, 4070503]
---
<!-- generated:start -->
<!-- generated-keys: title=c09ff2 type=9bbc46 id=00a691 sources=b77438 name_key=2e66ee category=356a19 class_mask=356a19 model=6c0ac7 model_name=88c23f model_path=5f7da0 scale=93ec1d radius=356a19 projectile=e81695 sounds=04d425 -->
|  |  |
|---|---|
| **Unit id** | `695` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `431` MOB_Dragon_01_0_1_0_01_01 (`character/npc/monster/mob_dragon/mob_dragon_01.mo`) |
| **Scale** | 1.8 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 1216 (archers carry one; meaning *inferred*) |

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
| 1 | 0 | 4070501 | `Unit/UE4070501.wav` |
| 2 | 0 | 4070501 | `Unit/UE4070501.wav` |
| 3 | 926 | 4070502 | `Unit/UE4070502.wav` |
| 4 | 926 | 4070502 | `Unit/UE4070502.wav` |
| 5 | 0 | 4070502 | `Unit/UE4070502.wav` |
| 6 | 0 | 4070503 | `Unit/UE4070503.wav` |

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
