---
title: "Demon Hunter Officer"
type: "monster"
id: 860
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 860"]
name_key: "UnitName_860"
category: 1
class_mask: 1
model: 95
model_name: "MOB_Demon_01"
model_path: "character/npc/monster/mob_demon/mob_demon_01.mo"
scale: 2.5
radius: 1
projectile: 853
sounds: [4070066, 4070066, 4070067, 4070067, 4070067, 4070068]
---
<!-- generated:start -->
<!-- generated-keys: title=c57128 type=9bbc46 id=301377 sources=4aa70a name_key=ff715a category=356a19 class_mask=356a19 model=8e63fd model_name=b1dcd3 model_path=6bdcd6 scale=555a5c radius=356a19 projectile=43d6ee sounds=546542 -->
|  |  |
|---|---|
| **Unit id** | `860` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `95` MOB_Demon_01 (`character/npc/monster/mob_demon/mob_demon_01.mo`) |
| **Scale** | 2.5 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 853 (archers carry one; meaning *inferred*) |

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
