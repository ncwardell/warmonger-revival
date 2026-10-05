---
title: "Tough Elite Chepa Archer"
type: "monster"
id: 813
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 813", "docs: [[gameplay/dungeon-drops]] (boss of field 812)"]
name_key: "UnitName_813"
category: 3
class_mask: 1
model: 31
model_name: "MOB_Chepa02_0_1_0_00_00"
model_path: "character/npc/monster/mob_chepa/mob_chepa02.mo"
scale: 2
radius: 1
projectile: 662
sounds: [4070113, 4070113, 4070015, 4070015, 4070015, 4070016]
boss_of: [812]
spawn_fields: [812]
---
<!-- generated:start -->
<!-- generated-keys: title=75c523 type=9bbc46 id=90b930 sources=780bf1 name_key=093941 category=77de68 class_mask=356a19 model=632667 model_name=aae49c model_path=baa448 scale=da4b92 radius=356a19 projectile=091d03 sounds=023b89 boss_of=8195d2 spawn_fields=8195d2 -->
|  |  |
|---|---|
| **Unit id** | `813` |
| **Category** | elite / named variant (inferred) (`category@8a` = 3) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `31` MOB_Chepa02_0_1_0_00_00 (`character/npc/monster/mob_chepa/mob_chepa02.mo`) |
| **Scale** | 2 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 662 (archers carry one; meaning *inferred*) |
| **Boss of** | Field 812 |

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

- Field 812 — boss ([[gameplay/dungeon-drops]])

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070113 | `Unit/UE4070113.wav` |
| 2 | 0 | 4070113 | `Unit/UE4070113.wav` |
| 3 | 0 | 4070015 | `Unit/UE4070015.wav` |
| 4 | 0 | 4070015 | `Unit/UE4070015.wav` |
| 5 | 0 | 4070015 | `Unit/UE4070015.wav` |
| 6 | 0 | 4070016 | `Unit/UE4070016.wav` |

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
