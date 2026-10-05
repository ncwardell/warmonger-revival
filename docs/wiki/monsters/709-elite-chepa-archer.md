---
title: "Elite Chepa Archer"
type: "monster"
id: 709
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 709"]
name_key: "UnitName_709"
category: 1
class_mask: 1
model: 31
model_name: "MOB_Chepa02_0_1_0_00_00"
model_path: "character/npc/monster/mob_chepa/mob_chepa02.mo"
scale: 2
radius: 1
projectile: 662
sounds: [4070113, 4070113, 4070014, 4070014, 4070014, 4070016]
---
<!-- generated:start -->
<!-- generated-keys: title=a65389 type=9bbc46 id=29da9b sources=60aa3f name_key=b8446d category=356a19 class_mask=356a19 model=632667 model_name=aae49c model_path=baa448 scale=da4b92 radius=356a19 projectile=091d03 sounds=8b163d -->
|  |  |
|---|---|
| **Unit id** | `709` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `31` MOB_Chepa02_0_1_0_00_00 (`character/npc/monster/mob_chepa/mob_chepa02.mo`) |
| **Scale** | 2 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 662 (archers carry one; meaning *inferred*) |

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

[[wiki/monsters/671-elite-chepa-archer|Elite Chepa Archer (671)]], [[wiki/monsters/685-elite-chepa-archer|Elite Chepa Archer (685)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070113 | `Unit/UE4070113.wav` |
| 2 | 0 | 4070113 | `Unit/UE4070113.wav` |
| 3 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 4 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 5 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 6 | 0 | 4070016 | `Unit/UE4070016.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 2.7 |
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
