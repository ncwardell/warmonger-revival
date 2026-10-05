---
title: "Tough Elite Lizard Lancer"
type: "monster"
id: 738
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 738"]
name_key: "UnitName_738"
category: 1
class_mask: 1
model: 72
model_name: "MOB_Lizardman_02"
model_path: "character/npc/monster/mob_lizardman/mob_lizardman_02.mo"
scale: 2
radius: 1
projectile: 808
sounds: [4070015, 4070015, 4070014, 4070014, 4070014]
---
<!-- generated:start -->
<!-- generated-keys: title=843002 type=9bbc46 id=641e2c sources=fd8abf name_key=217952 category=356a19 class_mask=356a19 model=c09763 model_name=f9e294 model_path=2c38fa scale=da4b92 radius=356a19 projectile=38afd2 sounds=364564 -->
|  |  |
|---|---|
| **Unit id** | `738` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `72` MOB_Lizardman_02 (`character/npc/monster/mob_lizardman/mob_lizardman_02.mo`) |
| **Scale** | 2 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 808 (archers carry one; meaning *inferred*) |

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
| 1 | 0 | 4070015 | `Unit/UE4070015.wav` |
| 2 | 0 | 4070015 | `Unit/UE4070015.wav` |
| 3 | 12 | 4070014 | `Unit/UE4070014.wav` |
| 4 | 12 | 4070014 | `Unit/UE4070014.wav` |
| 5 | 0 | 4070014 | `Unit/UE4070014.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 3 |
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
