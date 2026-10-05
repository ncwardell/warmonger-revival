---
title: "Tough Elite Chepa Warrior"
type: "monster"
id: 812
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 812"]
name_key: "UnitName_812"
category: 3
class_mask: 1
model: 30
model_name: "MOB_Chepa01_0_1_0_00_00"
model_path: "character/npc/monster/mob_chepa/mob_chepa01.mo"
scale: 2
radius: 1
sounds: [4070000, 4070000, 4070013, 4070013, 4070013, 4070016]
---
<!-- generated:start -->
<!-- generated-keys: title=233f2b type=9bbc46 id=872a31 sources=ea67ed name_key=fdffea category=77de68 class_mask=356a19 model=22d200 model_name=67408a model_path=207e1f scale=da4b92 radius=356a19 sounds=14185a -->
|  |  |
|---|---|
| **Unit id** | `812` |
| **Category** | elite / named variant (inferred) (`category@8a` = 3) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `30` MOB_Chepa01_0_1_0_00_00 (`character/npc/monster/mob_chepa/mob_chepa01.mo`) |
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

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 2 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 3 | 0 | 4070013 | `Unit/UE4070013.wav` |
| 4 | 0 | 4070013 | `Unit/UE4070013.wav` |
| 5 | 0 | 4070013 | `Unit/UE4070013.wav` |
| 6 | 0 | 4070016 | `Unit/UE4070016.wav` |

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
