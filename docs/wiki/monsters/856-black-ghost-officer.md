---
title: "Black Ghost Officer"
type: "monster"
id: 856
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 856"]
name_key: "UnitName_856"
category: 1
class_mask: 1
model: 274
model_name: "NPC_Evil001"
model_path: "character/npc/monster/NPC_Evil/NPC_Evil001.mo"
scale: 2.5
radius: 1
sounds: [4000005, 4000005, 4020005, 4020005, 4030005, 4040005]
---
<!-- generated:start -->
<!-- generated-keys: title=02882d type=9bbc46 id=efe76d sources=c030c5 name_key=91e249 category=356a19 class_mask=356a19 model=431bf3 model_name=07adc2 model_path=e26f4d scale=555a5c radius=356a19 sounds=05c963 -->
|  |  |
|---|---|
| **Unit id** | `856` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `274` NPC_Evil001 (`character/npc/monster/NPC_Evil/NPC_Evil001.mo`) |
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

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4000005 | not in sound.csv |
| 2 | 0 | 4000005 | not in sound.csv |
| 3 | 0 | 4020005 | not in sound.csv |
| 4 | 0 | 4020005 | not in sound.csv |
| 5 | 0 | 4030005 | not in sound.csv |
| 6 | 0 | 4040005 | not in sound.csv |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 5.3 |
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
