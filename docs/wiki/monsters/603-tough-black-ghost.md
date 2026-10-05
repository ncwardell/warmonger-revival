---
title: "Tough Black Ghost"
type: "monster"
id: 603
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 603"]
name_key: "UnitName_814"
category: 9
class_mask: 1
model: 12
model_name: "MOB_Slime_01_Green"
model_path: "character/npc/monster/mob_slime/mob_slime.mo"
scale: 1
radius: 0.7
sounds: [4000005, 4000005, 4020005, 4020005, 4030005, 4040005]
---
<!-- generated:start -->
<!-- generated-keys: title=f6fd75 type=9bbc46 id=8d255e sources=ef8102 name_key=b68880 category=0ade7c class_mask=356a19 model=7b5200 model_name=b5444f model_path=0cd0f3 scale=356a19 radius=717757 sounds=05c963 -->
|  |  |
|---|---|
| **Unit id** | `603` |
| **Category** | special (unknown) (`category@8a` = 9) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `12` MOB_Slime_01_Green (`character/npc/monster/mob_slime/mob_slime.mo`) |
| **Scale** | 1 (second scale / radius 0.7) |

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

[[wiki/monsters/814-tough-black-ghost|Tough Black Ghost (814)]]

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
| f32@c0 | 1.5 |
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
