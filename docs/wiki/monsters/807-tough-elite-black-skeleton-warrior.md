---
title: "Tough Elite Black Skeleton Warrior"
type: "monster"
id: 807
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 807", "docs: [[gameplay/dungeon-drops]] (boss of field 806)"]
name_key: "UnitName_807"
category: 3
class_mask: 1
model: 42
model_name: "MOB_Skeleton_Elilte_01_02"
model_path: "character/npc/monster/mob_seleton_elite_01/mob_seleton_elite_01_02.mo"
scale: 1.2
radius: 1
sounds: [4070000, 4070000, 3060040, 3060040, 3060040, 4070003]
boss_of: [806]
spawn_fields: [806]
---
<!-- generated:start -->
<!-- generated-keys: title=81b0f5 type=9bbc46 id=425ac6 sources=b8f4c7 name_key=35ef4c category=77de68 class_mask=356a19 model=92cfce model_name=2038a8 model_path=8e1010 scale=8114b9 radius=356a19 sounds=6dfede boss_of=b34dfb spawn_fields=b34dfb -->
|  |  |
|---|---|
| **Unit id** | `807` |
| **Category** | elite / named variant (inferred) (`category@8a` = 3) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `42` MOB_Skeleton_Elilte_01_02 (`character/npc/monster/mob_seleton_elite_01/mob_seleton_elite_01_02.mo`) |
| **Scale** | 1.2 (second scale / radius 1) |
| **Boss of** | Field 806 |

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

- Field 806 — boss ([[gameplay/dungeon-drops]])

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

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen *(name match)*: Kill messages ("X was destroyed") in quest order: Slime → Chepa Warrior / Chepa Archer (Training Ground circle, many killed for exp) → Bee, Cobra → Chepa Warri…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 4 |
| f32@10c | 0.5 |
<!-- generated:end -->

## Notes

- Seen in the Mist Lake (31) war map with its archer partner, after 1:43:10 in the charmanmugen video, where server staff were changing monster stats live (video, [[gameplay/video-early-quests]] §5).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/video-early-quests]] §5

## Open questions

- The generated `boss_of` [806] is wrong: 806 is the item code of Emerald in [[gameplay/dungeon-drops]] §1, not a field.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
