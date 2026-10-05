---
title: "Wasteland Phyton"
type: "monster"
id: 500
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 500"]
name_key: "UnitName_500"
category: 8
class_mask: 1
model: 98
model_name: "MOB_Python_01"
model_path: "character/npc/monster/mob_python/mob_python.mo"
scale: 1.6
radius: 1
sounds: [4070075, 4070075, 4070110, 4070110, 4070110, 4070078]
---
<!-- generated:start -->
<!-- generated-keys: title=8aae56 type=9bbc46 id=f83a38 sources=abee6c name_key=c74d62 category=fe5dbb class_mask=356a19 model=31bd9b model_name=e3823f model_path=40dea4 scale=469369 radius=356a19 sounds=d18cfe -->
|  |  |
|---|---|
| **Unit id** | `500` |
| **Category** | field monster (inferred: ogres, trolls, bears, phytons) (`category@8a` = 8) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `98` MOB_Python_01 (`character/npc/monster/mob_python/mob_python.mo`) |
| **Scale** | 1.6 (second scale / radius 1) |

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
| 1 | 0 | 4070075 | `Unit/UE4070075.wav` |
| 2 | 0 | 4070075 | `Unit/UE4070075.wav` |
| 3 | 932 | 4070110 | `Unit/UE4070110.wav` |
| 4 | 932 | 4070110 | `Unit/UE4070110.wav` |
| 5 | 0 | 4070110 | `Unit/UE4070110.wav` |
| 6 | 0 | 4070078 | `Unit/UE4070078.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@8c | 101 |
| u8@91 | 15 |
| f32@c0 | 7 |
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
