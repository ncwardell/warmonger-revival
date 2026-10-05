---
title: "Tough Red Ghost"
type: "monster"
id: 815
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 815", "docs: [[gameplay/dungeon-drops]] (boss of field 814)"]
name_key: "UnitName_815"
category: 1
class_mask: 1
model: 16
model_name: "NPC_Evil002_0_1_0_00_00"
model_path: "character/npc/monster/npc_evil/npc_evil002.mo"
scale: 1.5
radius: 1
sounds: [4000004, 4000004, 4020004, 4020004, 4030004, 4040004]
boss_of: [814]
spawn_fields: [814]
---
<!-- generated:start -->
<!-- generated-keys: title=fe0a05 type=9bbc46 id=d528ed sources=ffeffa name_key=e3859d category=356a19 class_mask=356a19 model=1574bd model_name=18b713 model_path=9fb616 scale=aa8f28 radius=356a19 sounds=2135c0 boss_of=6312d1 spawn_fields=6312d1 -->
|  |  |
|---|---|
| **Unit id** | `815` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `16` NPC_Evil002_0_1_0_00_00 (`character/npc/monster/npc_evil/npc_evil002.mo`) |
| **Scale** | 1.5 (second scale / radius 1) |
| **Boss of** | Field 814 |

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

- Field 814 — boss ([[gameplay/dungeon-drops]])

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4000004 | `voice/UV4000004.wav` |
| 2 | 0 | 4000004 | `voice/UV4000004.wav` |
| 3 | 0 | 4020004 | not in sound.csv |
| 4 | 0 | 4020004 | not in sound.csv |
| 5 | 0 | 4030004 | not in sound.csv |
| 6 | 0 | 4040004 | not in sound.csv |

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
