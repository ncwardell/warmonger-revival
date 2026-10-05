---
title: "Superior Zombie"
type: "monster"
id: 1216
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 1216"]
name_key: "UnitName_1216"
category: 1
class_mask: 1
model: 276
model_name: "MOB_Zombi_01"
model_path: "character/npc/monster/mob_zombi_01/mob_zombi_01.mo"
scale: 1.4
radius: 1
sounds: [4070085, 4070085, 3060040, 3060040, 3060040]
---
<!-- generated:start -->
<!-- generated-keys: title=9655cd type=9bbc46 id=e81695 sources=9ecaef name_key=1e1bd6 category=356a19 class_mask=356a19 model=6d3634 model_name=9f5c3a model_path=1d8b30 scale=a26f83 radius=356a19 sounds=9dd31f -->
|  |  |
|---|---|
| **Unit id** | `1216` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `276` MOB_Zombi_01 (`character/npc/monster/mob_zombi_01/mob_zombi_01.mo`) |
| **Scale** | 1.4 (second scale / radius 1) |

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
| 1 | 0 | 4070085 | `Unit/UE4070085.wav` |
| 2 | 0 | 4070085 | `Unit/UE4070085.wav` |
| 3 | 0 | 3060040 | `effect/ES3060040.wav` |
| 4 | 0 | 3060040 | `effect/ES3060040.wav` |
| 5 | 0 | 3060040 | `effect/ES3060040.wav` |

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
