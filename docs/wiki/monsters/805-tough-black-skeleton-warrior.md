---
title: "Tough Black Skeleton Warrior"
type: "monster"
id: 805
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 805", "docs: [[gameplay/dungeon-drops]] (boss of field 804)"]
name_key: "UnitName_805"
category: 1
class_mask: 1
model: 14
model_name: "MOB_Seleton01_02"
model_path: "character/npc/monster/mob_seleton01/mob_seleton01_02.mo"
scale: 0.8
radius: 0.8
sounds: [4070000, 4070000, 3060040, 3060040, 3060040, 4070003]
boss_of: [804]
spawn_fields: [804]
---
<!-- generated:start -->
<!-- generated-keys: title=a82688 type=9bbc46 id=f890d7 sources=1f4c28 name_key=95442d category=356a19 class_mask=356a19 model=fa35e1 model_name=b177e0 model_path=3f540c scale=480262 radius=480262 sounds=6dfede boss_of=8775bb spawn_fields=8775bb -->
|  |  |
|---|---|
| **Unit id** | `805` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `14` MOB_Seleton01_02 (`character/npc/monster/mob_seleton01/mob_seleton01_02.mo`) |
| **Scale** | 0.8 (second scale / radius 0.8) |
| **Boss of** | Field 804 |

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

- Field 804 — boss ([[gameplay/dungeon-drops]])

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
