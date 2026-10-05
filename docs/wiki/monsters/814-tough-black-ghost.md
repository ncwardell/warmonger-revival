---
title: "Tough Black Ghost"
type: "monster"
id: 814
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 814"]
name_key: "UnitName_814"
category: 1
class_mask: 1
model: 274
model_name: "NPC_Evil001"
model_path: "character/npc/monster/NPC_Evil/NPC_Evil001.mo"
scale: 1.5
radius: 1
sounds: [4000004, 4000004, 4000004, 4000004, 4000004, 4000004]
---
<!-- generated:start -->
<!-- generated-keys: title=f6fd75 type=9bbc46 id=c9264f sources=bbc948 name_key=b68880 category=356a19 class_mask=356a19 model=431bf3 model_name=07adc2 model_path=e26f4d scale=aa8f28 radius=356a19 sounds=2db6a5 -->
|  |  |
|---|---|
| **Unit id** | `814` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `274` NPC_Evil001 (`character/npc/monster/NPC_Evil/NPC_Evil001.mo`) |
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

[[wiki/monsters/603-tough-black-ghost|Tough Black Ghost (603)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4000004 | `voice/UV4000004.wav` |
| 2 | 0 | 4000004 | `voice/UV4000004.wav` |
| 3 | 0 | 4000004 | `voice/UV4000004.wav` |
| 4 | 0 | 4000004 | `voice/UV4000004.wav` |
| 5 | 0 | 4000004 | `voice/UV4000004.wav` |
| 6 | 0 | 4000004 | `voice/UV4000004.wav` |

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
