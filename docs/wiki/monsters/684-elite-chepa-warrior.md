---
title: "Elite Chepa Warrior"
type: "monster"
id: 684
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 684"]
name_key: "UnitName_684"
category: 1
class_mask: 1
model: 30
model_name: "MOB_Chepa01_0_1_0_00_00"
model_path: "character/npc/monster/mob_chepa/mob_chepa01.mo"
scale: 2.5
radius: 1
sounds: [4070000, 4070000, 5000006, 5000006, 5000006, 4070003]
---
<!-- generated:start -->
<!-- generated-keys: title=647312 type=9bbc46 id=a79e9a sources=145346 name_key=31aa8b category=356a19 class_mask=356a19 model=22d200 model_name=67408a model_path=207e1f scale=555a5c radius=356a19 sounds=dddd70 -->
|  |  |
|---|---|
| **Unit id** | `684` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `30` MOB_Chepa01_0_1_0_00_00 (`character/npc/monster/mob_chepa/mob_chepa01.mo`) |
| **Scale** | 2.5 (second scale / radius 1) |

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

### Other units with this name

[[wiki/monsters/670-elite-chepa-warrior|Elite Chepa Warrior (670)]], [[wiki/monsters/708-elite-chepa-warrior|Elite Chepa Warrior (708)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 2 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 3 | 0 | 5000006 | `effect/EW5000006.wav` |
| 4 | 0 | 5000006 | `effect/EW5000006.wav` |
| 5 | 0 | 5000006 | `effect/EW5000006.wav` |
| 6 | 0 | 4070003 | `Unit/UE4070003.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 8 |
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
