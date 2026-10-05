---
title: "Tough Skeleton Archer"
type: "monster"
id: 801
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 801"]
name_key: "UnitName_801"
category: 1
class_mask: 1
model: 11
model_name: "MOB_Seleton02"
model_path: "character/npc/monster/mob_seleton02/mob_seleton02.mo"
scale: 0.8
radius: 0.8
projectile: 583
sounds: [4070113, 4070113, 3060040, 3060040, 3060040, 4070003]
---
<!-- generated:start -->
<!-- generated-keys: title=2b73f9 type=9bbc46 id=549843 sources=c5d6ce name_key=944805 category=356a19 class_mask=356a19 model=17ba07 model_name=519469 model_path=c36c5c scale=480262 radius=480262 projectile=9c676e sounds=b4d854 -->
|  |  |
|---|---|
| **Unit id** | `801` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `11` MOB_Seleton02 (`character/npc/monster/mob_seleton02/mob_seleton02.mo`) |
| **Scale** | 0.8 (second scale / radius 0.8) |
| **Projectile?** | `u32@bc` = 583 (archers carry one; meaning *inferred*) |

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
| 1 | 0 | 4070113 | `Unit/UE4070113.wav` |
| 2 | 0 | 4070113 | `Unit/UE4070113.wav` |
| 3 | 0 | 3060040 | `effect/ES3060040.wav` |
| 4 | 0 | 3060040 | `effect/ES3060040.wav` |
| 5 | 0 | 3060040 | `effect/ES3060040.wav` |
| 6 | 0 | 4070003 | `Unit/UE4070003.wav` |

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
