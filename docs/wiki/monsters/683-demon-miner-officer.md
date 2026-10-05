---
title: "Demon Miner Officer"
type: "monster"
id: 683
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 683"]
name_key: "UnitName_683"
category: 1
class_mask: 1
model: 348
model_name: "MOB_Demon_01_0_1_0_03_03"
model_path: "character/npc/monster/mob_demon/mob_demon_01.mo"
scale: 2.5
radius: 1
sounds: [4070066, 4070066, 4070067, 4070067, 4070067, 4070068]
---
<!-- generated:start -->
<!-- generated-keys: title=8a8ba7 type=9bbc46 id=4f2706 sources=f140c0 name_key=8e19f5 category=356a19 class_mask=356a19 model=cfd179 model_name=34c465 model_path=6bdcd6 scale=555a5c radius=356a19 sounds=546542 -->
|  |  |
|---|---|
| **Unit id** | `683` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `348` MOB_Demon_01_0_1_0_03_03 (`character/npc/monster/mob_demon/mob_demon_01.mo`) |
| **Scale** | 2.5 (second scale / radius 1) |

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
| 1 | 0 | 4070066 | `Unit/UE4070066.wav` |
| 2 | 0 | 4070066 | `Unit/UE4070066.wav` |
| 3 | 0 | 4070067 | `Unit/UE4070067.wav` |
| 4 | 0 | 4070067 | `Unit/UE4070067.wav` |
| 5 | 0 | 4070067 | `Unit/UE4070067.wav` |
| 6 | 0 | 4070068 | `Unit/UE4070068.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 8 |
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
