---
title: "Mini Golem"
type: "monster"
id: 615
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 615"]
name_key: "UnitName_615"
category: 1
class_mask: 1
model: 65
model_name: "MOB_Golem_Volcano_01"
model_path: "character/npc/monster/mob_golem/mob_golem_01.mo"
scale: 0.4
radius: 1
projectile: 894
sounds: [4070112, 4070112, 4070010, 4070010, 4070010, 4070119]
---
<!-- generated:start -->
<!-- generated-keys: title=fb6fd2 type=9bbc46 id=2456ca sources=738d06 name_key=f11340 category=356a19 class_mask=356a19 model=2a4593 model_name=75717b model_path=ed16ce scale=015b8d radius=356a19 projectile=1ecaeb sounds=f39c5f -->
|  |  |
|---|---|
| **Unit id** | `615` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `65` MOB_Golem_Volcano_01 (`character/npc/monster/mob_golem/mob_golem_01.mo`) |
| **Scale** | 0.4 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 894 (archers carry one; meaning *inferred*) |

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

[[wiki/monsters/617-mini-golem|Mini Golem (617)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070112 | `Unit/UE4070112.wav` |
| 2 | 0 | 4070112 | `Unit/UE4070112.wav` |
| 3 | 926 | 4070010 | `Unit/UE4070010.wav` |
| 4 | 926 | 4070010 | `Unit/UE4070010.wav` |
| 5 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 6 | 0 | 4070119 | `Unit/UE4070119.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@8c | 104 |
| u8@91 | 15 |
| f32@c0 | 2 |
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
