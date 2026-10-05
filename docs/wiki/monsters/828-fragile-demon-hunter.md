---
title: "Fragile Demon Hunter"
type: "monster"
id: 828
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 828", "client: Quest.cdb kill objectives (quests 751, 1103)"]
name_key: "UnitName_828"
category: 1
class_mask: 1
kill_group: 10033
model: 95
model_name: "MOB_Demon_01"
model_path: "character/npc/monster/mob_demon/mob_demon_01.mo"
scale: 1.3
radius: 1
projectile: 853
sounds: [4070068, 4070068, 4070066, 4070066, 4070067, 4070068]
quest_targets:
  - {"quest": 751, "need": 50, "group": 10033}
  - {"quest": 1103, "need": 50, "group": 10033}
spawn_fields: [114]
---
<!-- generated:start -->
<!-- generated-keys: title=df941c type=9bbc46 id=0da8cb sources=df3a24 name_key=39b9c3 category=356a19 class_mask=356a19 kill_group=4f4cb1 model=8e63fd model_name=b1dcd3 model_path=6bdcd6 scale=2afe7d radius=356a19 projectile=43d6ee sounds=d5afbf quest_targets=dca187 spawn_fields=6c4502 -->
|  |  |
|---|---|
| **Unit id** | `828` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10033` |
| **Model** | ObjectList `95` MOB_Demon_01 (`character/npc/monster/mob_demon/mob_demon_01.mo`) |
| **Scale** | 1.3 (second scale / radius 1) |
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

### Quests

- [[wiki/quests/751-kill-monster-of-the-way-go-to-devildom|Kill monster of The way go to devildom]]: kill 50 in [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]] — via kill group `10033` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1103-the-way-go-to-devildom-kill-monster|The Way go to devildom : Kill monster]]: kill 50 in [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]] — via kill group `10033` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]] — quest map of [[wiki/quests/751-kill-monster-of-the-way-go-to-devildom|Kill monster of The way go to devildom]], [[wiki/quests/1103-the-way-go-to-devildom-kill-monster|The Way go to devildom : Kill monster]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070068 | `Unit/UE4070068.wav` |
| 2 | 0 | 4070068 | `Unit/UE4070068.wav` |
| 3 | 0 | 4070066 | `Unit/UE4070066.wav` |
| 4 | 0 | 4070066 | `Unit/UE4070066.wav` |
| 5 | 0 | 4070067 | `Unit/UE4070067.wav` |
| 6 | 0 | 4070068 | `Unit/UE4070068.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 6 |
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
