---
title: "Tough Elite Fisher Lancer"
type: "monster"
id: 864
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 864"]
name_key: "UnitName_864"
category: 1
class_mask: 1
model: 302
model_name: "MOB_Fisher_02"
model_path: "character/npc/monster/mob_fisher/mob_fisher.mo"
scale: 1.8
radius: 1
sounds: [4070032, 4070032, 4070031, 4070031, 4070032, 4070016]
---
<!-- generated:start -->
<!-- generated-keys: title=fa4013 type=9bbc46 id=de1592 sources=c3a59d name_key=b5adba category=356a19 class_mask=356a19 model=cd0613 model_name=df4447 model_path=0cce97 scale=93ec1d radius=356a19 sounds=c3bdc4 -->
|  |  |
|---|---|
| **Unit id** | `864` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `302` MOB_Fisher_02 (`character/npc/monster/mob_fisher/mob_fisher.mo`) |
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

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070032 | `Unit/UE4070032.wav` |
| 2 | 0 | 4070032 | `Unit/UE4070032.wav` |
| 3 | 0 | 4070031 | `Unit/UE4070031.wav` |
| 4 | 0 | 4070031 | `Unit/UE4070031.wav` |
| 5 | 0 | 4070032 | `Unit/UE4070032.wav` |
| 6 | 0 | 4070016 | `Unit/UE4070016.wav` |

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
