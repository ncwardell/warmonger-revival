---
title: "Lizard Swordsman Officer"
type: "monster"
id: 854
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 854"]
name_key: "UnitName_854"
category: 1
class_mask: 1
model: 71
model_name: "MOB_Lizardman_01"
model_path: "character/npc/monster/mob_lizardman/mob_lizardman_01.mo"
scale: 2.5
radius: 1
sounds: [4070013, 4070013, 4070015, 4070015, 4070015, 4070016]
---
<!-- generated:start -->
<!-- generated-keys: title=b5b675 type=9bbc46 id=cbc34d sources=85cc9c name_key=0dc878 category=356a19 class_mask=356a19 model=d02560 model_name=39ab4b model_path=21b985 scale=555a5c radius=356a19 sounds=e18342 -->
|  |  |
|---|---|
| **Unit id** | `854` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `71` MOB_Lizardman_01 (`character/npc/monster/mob_lizardman/mob_lizardman_01.mo`) |
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
| 1 | 0 | 4070013 | `Unit/UE4070013.wav` |
| 2 | 0 | 4070013 | `Unit/UE4070013.wav` |
| 3 | 12 | 4070015 | `Unit/UE4070015.wav` |
| 4 | 12 | 4070015 | `Unit/UE4070015.wav` |
| 5 | 0 | 4070015 | `Unit/UE4070015.wav` |
| 6 | 0 | 4070016 | `Unit/UE4070016.wav` |

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
