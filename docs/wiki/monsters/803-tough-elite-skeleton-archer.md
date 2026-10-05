---
title: "Tough Elite Skeleton Archer"
type: "monster"
id: 803
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 803", "docs: [[gameplay/dungeon-drops]] (boss of field 802)"]
name_key: "UnitName_803"
category: 3
class_mask: 1
model: 43
model_name: "MOB_Skeleton_Elilte_02"
model_path: "character/npc/monster/mob_seleton_elite_02/mob_seleton_elite_02.mo"
scale: 1.1
radius: 1
projectile: 583
sounds: [4070113, 4070113, 4070014, 4070014, 4070014, 4070003]
boss_of: [802]
spawn_fields: [802]
---
<!-- generated:start -->
<!-- generated-keys: title=695d21 type=9bbc46 id=9d0008 sources=80ecf0 name_key=c5fce9 category=77de68 class_mask=356a19 model=0286dd model_name=843967 model_path=04ed34 scale=4491f8 radius=356a19 projectile=9c676e sounds=89c031 boss_of=87e390 spawn_fields=87e390 -->
|  |  |
|---|---|
| **Unit id** | `803` |
| **Category** | elite / named variant (inferred) (`category@8a` = 3) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `43` MOB_Skeleton_Elilte_02 (`character/npc/monster/mob_seleton_elite_02/mob_seleton_elite_02.mo`) |
| **Scale** | 1.1 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 583 (archers carry one; meaning *inferred*) |
| **Boss of** | Field 802 |

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

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- Field 802 — boss ([[gameplay/dungeon-drops]])

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070113 | `Unit/UE4070113.wav` |
| 2 | 0 | 4070113 | `Unit/UE4070113.wav` |
| 3 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 4 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 5 | 0 | 4070014 | `Unit/UE4070014.wav` |
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
