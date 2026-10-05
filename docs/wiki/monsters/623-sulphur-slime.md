---
title: "Sulphur Slime"
type: "monster"
id: 623
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 623"]
name_key: "UnitName_623"
category: 1
class_mask: 1
model: 67
model_name: "MOB_Slime_01_DrakBlue"
model_path: "character/npc/monster/mob_slime/mob_slime.mo"
scale: 1.3
radius: 1
sounds: [4070007, 4070007, 4070008, 4070008, 4070008, 4070009]
---
<!-- generated:start -->
<!-- generated-keys: title=e7270d type=9bbc46 id=01eebb sources=66356f name_key=1099e4 category=356a19 class_mask=356a19 model=4d89d2 model_name=d091b2 model_path=0cd0f3 scale=2afe7d radius=356a19 sounds=d25fba -->
|  |  |
|---|---|
| **Unit id** | `623` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `67` MOB_Slime_01_DrakBlue (`character/npc/monster/mob_slime/mob_slime.mo`) |
| **Scale** | 1.3 (second scale / radius 1) |

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
| 1 | 0 | 4070007 | `Unit/UE4070007.wav` |
| 2 | 0 | 4070007 | `Unit/UE4070007.wav` |
| 3 | 0 | 4070008 | `Unit/UE4070008.wav` |
| 4 | 0 | 4070008 | `Unit/UE4070008.wav` |
| 5 | 0 | 4070008 | `Unit/UE4070008.wav` |
| 6 | 0 | 4070009 | `Unit/UE4070009.wav` |

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
