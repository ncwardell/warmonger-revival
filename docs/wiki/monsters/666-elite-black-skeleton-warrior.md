---
title: "Elite Black Skeleton Warrior"
type: "monster"
id: 666
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 666"]
name_key: "UnitName_666"
category: 3
class_mask: 1
kill_group: 10028
model: 42
model_name: "MOB_Skeleton_Elilte_01_02"
model_path: "character/npc/monster/mob_seleton_elite_01/mob_seleton_elite_01_02.mo"
scale: 1.2
radius: 1
sounds: [4070000, 4070000, 3060040, 3060040, 3060040, 4070003]
---
<!-- generated:start -->
<!-- generated-keys: title=e561ce type=9bbc46 id=cd3f0c sources=e28be6 name_key=2b8d16 category=77de68 class_mask=356a19 kill_group=4b48d1 model=92cfce model_name=2038a8 model_path=8e1010 scale=8114b9 radius=356a19 sounds=6dfede -->
|  |  |
|---|---|
| **Unit id** | `666` |
| **Category** | elite / named variant (inferred) (`category@8a` = 3) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10028` with [[wiki/monsters/667-elite-black-skeleton-archer\|Elite Black Skeleton Archer]] |
| **Model** | ObjectList `42` MOB_Skeleton_Elilte_01_02 (`character/npc/monster/mob_seleton_elite_01/mob_seleton_elite_01_02.mo`) |
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
| 1 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 2 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 3 | 0 | 3060040 | `effect/ES3060040.wav` |
| 4 | 0 | 3060040 | `effect/ES3060040.wav` |
| 5 | 0 | 3060040 | `effect/ES3060040.wav` |
| 6 | 0 | 4070003 | `Unit/UE4070003.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 4 |
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
