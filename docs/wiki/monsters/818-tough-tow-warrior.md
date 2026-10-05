---
title: "Tough Tow Warrior"
type: "monster"
id: 818
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 818"]
name_key: "UnitName_818"
category: 1
class_mask: 1
model: 17
model_name: "MOB_Orc_Warrior_0_1_0_00_00"
model_path: "character/npc/monster/mob_orc/mob_orc_warrior.mo"
scale: 1.2
radius: 1
sounds: [4070112, 4070112, 4070010, 4070010, 4070010, 4070011]
---
<!-- generated:start -->
<!-- generated-keys: title=4eb846 type=9bbc46 id=37a53d sources=98fd6d name_key=d55ce5 category=356a19 class_mask=356a19 model=0716d9 model_name=cb6e5e model_path=c6d4b3 scale=8114b9 radius=356a19 sounds=e898d3 -->
|  |  |
|---|---|
| **Unit id** | `818` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `17` MOB_Orc_Warrior_0_1_0_00_00 (`character/npc/monster/mob_orc/mob_orc_warrior.mo`) |
| **Scale** | 1.2 (second scale / radius 1) |

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
