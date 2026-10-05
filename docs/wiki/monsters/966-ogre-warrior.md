---
title: "Ogre Warrior"
type: "monster"
id: 966
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 966"]
name_key: "UnitName_966"
category: 1
class_mask: 1
model: 293
model_name: "MOB_Oger_Wasteland_01"
model_path: "character/npc/monster/mob_oger/mob_oger_wasteland_01.mo"
scale: 1
radius: 1
sounds: [4070112, 4070112, 4070010, 4070010, 4070010, 4070120]
---
<!-- generated:start -->
<!-- generated-keys: title=7d4d69 type=9bbc46 id=bdf59a sources=e9324f name_key=f09525 category=356a19 class_mask=356a19 model=05580c model_name=2b48c3 model_path=981715 scale=356a19 radius=356a19 sounds=9229d8 -->
|  |  |
|---|---|
| **Unit id** | `966` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `293` MOB_Oger_Wasteland_01 (`character/npc/monster/mob_oger/mob_oger_wasteland_01.mo`) |
| **Scale** | 1 (second scale / radius 1) |

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

[[wiki/monsters/967-ogre-warrior|Ogre Warrior (967)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070112 | `Unit/UE4070112.wav` |
| 2 | 0 | 4070112 | `Unit/UE4070112.wav` |
| 3 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 4 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 5 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 6 | 0 | 4070120 | `Unit/UE4070120.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@8c | 119 |
| u8@91 | 15 |
| f32@c0 | 4.5 |
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
