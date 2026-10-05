---
title: "Ice Phyton"
type: "monster"
id: 502
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 502"]
name_key: "UnitName_502"
category: 8
class_mask: 1
model: 295
model_name: "MOB_Python_Ice_01"
model_path: "character/npc/monster/mob_python/mob_python_ice_01.mo"
scale: 1.6
radius: 1
sounds: [4070075, 4070075, 4070110, 4070110, 4070110, 4070078]
---
<!-- generated:start -->
<!-- generated-keys: title=e03a21 type=9bbc46 id=2f9f70 sources=b2c361 name_key=408e65 category=fe5dbb class_mask=356a19 model=a02b85 model_name=4c5792 model_path=75b850 scale=469369 radius=356a19 sounds=d18cfe -->
|  |  |
|---|---|
| **Unit id** | `502` |
| **Category** | field monster (inferred: ogres, trolls, bears, phytons) (`category@8a` = 8) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `295` MOB_Python_Ice_01 (`character/npc/monster/mob_python/mob_python_ice_01.mo`) |
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

### Other units with this name

[[wiki/monsters/1502-ice-phyton|Ice Phyton (1502)]]

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
