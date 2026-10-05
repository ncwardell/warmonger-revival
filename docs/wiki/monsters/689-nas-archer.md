---
title: "Nas Archer"
type: "monster"
id: 689
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 689"]
name_key: "UnitName_689"
category: 1
class_mask: 1
model: 382
model_name: "MOB_Chepa03_0_1_0_00_00"
model_path: "character/npc/monster/mob_chepa/mob_chepa03.mo"
scale: 1.3
radius: 1
projectile: 1240
sounds: [5000008, 5000008, 5000008, 4070003]
---
<!-- generated:start -->
<!-- generated-keys: title=7c87e7 type=9bbc46 id=53c53c sources=d01503 name_key=9a9c21 category=356a19 class_mask=356a19 model=d0226f model_name=6fc42f model_path=5325b1 scale=2afe7d radius=356a19 projectile=042338 sounds=aab421 -->
|  |  |
|---|---|
| **Unit id** | `689` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `382` MOB_Chepa03_0_1_0_00_00 (`character/npc/monster/mob_chepa/mob_chepa03.mo`) |
| **Scale** | 1.3 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 1240 (archers carry one; meaning *inferred*) |

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
| 3 | 0 | 5000008 | `effect/EW5000008.wav` |
| 4 | 0 | 5000008 | `effect/EW5000008.wav` |
| 5 | 0 | 5000008 | `effect/EW5000008.wav` |
| 6 | 0 | 4070003 | `Unit/UE4070003.wav` |

### Seen in

- [[gameplay/video-dungeon-run|Video notes: Nas Village dungeon run (ZonderCoRe)]] § 2. Pack positions (field 133): Monster types: humanoid warriors with shields and bow archers (v &t=51s). The client has exactly these for Nas: 688 Nas Warrior, 689 Nas Archer, 690 Elite Nas…

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
