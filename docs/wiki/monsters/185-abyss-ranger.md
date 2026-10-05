---
title: "Abyss Ranger"
type: "monster"
id: 185
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 185"]
name_key: "UnitName_180"
category: 1
class_mask: 1
model: 94
model_name: "PCDM_Basic_002"
model_path: "character/pc/pcdm/pcdm.mo"
scale: 1.2
radius: 1
sounds: [5000010, 5000010, 5000009, 5000009, 4040003]
---
<!-- generated:start -->
<!-- generated-keys: title=651d0b type=9bbc46 id=cfa2ed sources=064fbb name_key=d841be category=356a19 class_mask=356a19 model=215bb4 model_name=ec2ef8 model_path=215e0e scale=8114b9 radius=356a19 sounds=213fd8 -->
|  |  |
|---|---|
| **Unit id** | `185` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `94` PCDM_Basic_002 (`character/pc/pcdm/pcdm.mo`) |
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

### Other units with this name

[[wiki/monsters/180-abyss-ranger|Abyss Ranger (180)]], [[wiki/monsters/181-abyss-ranger|Abyss Ranger (181)]], [[wiki/monsters/182-abyss-ranger|Abyss Ranger (182)]], [[wiki/monsters/183-abyss-ranger|Abyss Ranger (183)]], [[wiki/monsters/184-abyss-ranger|Abyss Ranger (184)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 5000010 | `effect/EW5000010.wav` |
| 2 | 0 | 5000010 | `effect/EW5000010.wav` |
| 3 | 1033 | 5000009 | `effect/EW5000009.wav` |
| 4 | 1033 | 5000009 | `effect/EW5000009.wav` |
| 6 | 0 | 4040003 | `voice/UV4040003.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 3 |
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
