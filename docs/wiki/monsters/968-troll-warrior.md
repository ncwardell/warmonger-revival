---
title: "Troll Warrior"
type: "monster"
id: 968
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 968"]
name_key: "UnitName_968"
category: 1
class_mask: 1
model: 285
model_name: "MOB_Troll_Wasteland_01"
model_path: "character/npc/monster/mob_troll_01/mob_troll_01.mo"
scale: 2
radius: 1
sounds: [4070112, 4070112, 4070010, 4070010, 4070010, 4070011]
---
<!-- generated:start -->
<!-- generated-keys: title=ef45c4 type=9bbc46 id=b3bf21 sources=3f8f40 name_key=20ae37 category=356a19 class_mask=356a19 model=367ac6 model_name=b22331 model_path=cc4083 scale=da4b92 radius=356a19 sounds=e898d3 -->
|  |  |
|---|---|
| **Unit id** | `968` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `285` MOB_Troll_Wasteland_01 (`character/npc/monster/mob_troll_01/mob_troll_01.mo`) |
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

### Other units with this name

[[wiki/monsters/969-troll-warrior|Troll Warrior (969)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070112 | `Unit/UE4070112.wav` |
| 2 | 0 | 4070112 | `Unit/UE4070112.wav` |
| 3 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 4 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 5 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 6 | 0 | 4070011 | `Unit/UE4070011.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@8c | 111 |
| u8@91 | 15 |
| f32@c0 | 2.7 |
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
