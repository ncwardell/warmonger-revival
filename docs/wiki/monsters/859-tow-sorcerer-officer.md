---
title: "Tow Sorcerer Officer"
type: "monster"
id: 859
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 859"]
name_key: "UnitName_859"
category: 1
class_mask: 1
model: 18
model_name: "MOB_Orc_Wizard_0_1_0_00_00"
model_path: "character/npc/monster/mob_orc/mob_orc_wizard.mo"
scale: 2.5
radius: 1
projectile: 642
sounds: [4070012, 4070012, 4070012, 4070012, 4070012, 4070011]
---
<!-- generated:start -->
<!-- generated-keys: title=700a40 type=9bbc46 id=812cd8 sources=903a2e name_key=2c547b category=356a19 class_mask=356a19 model=9e6a55 model_name=beb51d model_path=07c67e scale=555a5c radius=356a19 projectile=99316d sounds=e1c552 -->
|  |  |
|---|---|
| **Unit id** | `859` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `18` MOB_Orc_Wizard_0_1_0_00_00 (`character/npc/monster/mob_orc/mob_orc_wizard.mo`) |
| **Scale** | 2.5 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 642 (archers carry one; meaning *inferred*) |

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

[[wiki/monsters/726-tow-sorcerer-officer|Tow Sorcerer Officer (726)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070012 | `Unit/UE4070012.wav` |
| 2 | 0 | 4070012 | `Unit/UE4070012.wav` |
| 3 | 926 | 4070012 | `Unit/UE4070012.wav` |
| 4 | 926 | 4070012 | `Unit/UE4070012.wav` |
| 5 | 0 | 4070012 | `Unit/UE4070012.wav` |
| 6 | 0 | 4070011 | `Unit/UE4070011.wav` |

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
