---
title: "Skeleton Warrior Officer"
type: "monster"
id: 686
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 686"]
name_key: "UnitName_686"
category: 1
class_mask: 1
model: 41
model_name: "MOB_Skeleton_Elilte_01"
model_path: "character/npc/monster/mob_seleton_elite_01/mob_seleton_elite_01.mo"
scale: 1.5
radius: 1
sounds: [4070000, 4070000, 5000006, 5000006, 5000006, 4070003]
---
<!-- generated:start -->
<!-- generated-keys: title=d0e2f3 type=9bbc46 id=cea647 sources=876149 name_key=462785 category=356a19 class_mask=356a19 model=761f22 model_name=a307db model_path=eb5090 scale=aa8f28 radius=356a19 sounds=dddd70 -->
|  |  |
|---|---|
| **Unit id** | `686` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `41` MOB_Skeleton_Elilte_01 (`character/npc/monster/mob_seleton_elite_01/mob_seleton_elite_01.mo`) |
| **Scale** | 1.5 (second scale / radius 1) |

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

[[wiki/monsters/704-skeleton-warrior-officer|Skeleton Warrior Officer (704)]], [[wiki/monsters/851-skeleton-warrior-officer|Skeleton Warrior Officer (851)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 2 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 3 | 0 | 5000006 | `effect/EW5000006.wav` |
| 4 | 0 | 5000006 | `effect/EW5000006.wav` |
| 5 | 0 | 5000006 | `effect/EW5000006.wav` |
| 6 | 0 | 4070003 | `Unit/UE4070003.wav` |

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen at [35:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2120s) *(name match)*: Skeleton Warrior Officer (quest boss) · 2000 · +0 · 35:20

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
