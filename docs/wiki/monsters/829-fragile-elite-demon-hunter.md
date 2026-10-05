---
title: "Fragile Elite Demon Hunter"
type: "monster"
id: 829
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 829", "docs: [[gameplay/dungeon-drops]] (boss of field 828)", "client: Quest.cdb kill objectives (quests 40, 751, 1103)"]
name_key: "UnitName_829"
category: 1
class_mask: 1
kill_group: 10034
model: 95
model_name: "MOB_Demon_01"
model_path: "character/npc/monster/mob_demon/mob_demon_01.mo"
scale: 1.7
radius: 1
projectile: 853
sounds: [4070068, 4070068, 4070066, 4070066, 4070067]
boss_of: [828]
quest_targets:
  - {"quest": 40, "need": 4}
  - {"quest": 751, "need": 50, "group": 10034}
  - {"quest": 1103, "need": 50, "group": 10034}
quest_drops:
  - {"quest": 40, "item": 2548, "rate": 30, "need": 4}
spawn_fields: [114, 828]
---
<!-- generated:start -->
<!-- generated-keys: title=a40f44 type=9bbc46 id=459b50 sources=d904fb name_key=6c97d2 category=356a19 class_mask=356a19 kill_group=6f2cdc model=8e63fd model_name=b1dcd3 model_path=6bdcd6 scale=58e6d3 radius=356a19 projectile=43d6ee sounds=879981 boss_of=a39b6e quest_targets=381282 quest_drops=a5c2af spawn_fields=2c5d83 -->
|  |  |
|---|---|
| **Unit id** | `829` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10034` |
| **Model** | ObjectList `95` MOB_Demon_01 (`character/npc/monster/mob_demon/mob_demon_01.mo`) |
| **Scale** | 1.7 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 853 (archers carry one; meaning *inferred*) |
| **Boss of** | Field 828 |

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

- [[wiki/quests/40-innocence-s-recovery-operation|Innocence's recovery operation]]: collect 4 × [[wiki/items/2548-broken-innocence|Broken Innocence]] (drops at 30% while the quest is active) in [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]]
- [[wiki/quests/751-kill-monster-of-the-way-go-to-devildom|Kill monster of The way go to devildom]]: kill 50 in [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]] — via kill group `10034` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1103-the-way-go-to-devildom-kill-monster|The Way go to devildom : Kill monster]]: kill 50 in [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]] — via kill group `10034` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]] — quest map of [[wiki/quests/40-innocence-s-recovery-operation|Innocence's recovery operation]], [[wiki/quests/751-kill-monster-of-the-way-go-to-devildom|Kill monster of The way go to devildom]], [[wiki/quests/1103-the-way-go-to-devildom-kill-monster|The Way go to devildom : Kill monster]]
- Field 828 — boss ([[gameplay/dungeon-drops]])

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070068 | `Unit/UE4070068.wav` |
| 2 | 0 | 4070068 | `Unit/UE4070068.wav` |
| 3 | 0 | 4070066 | `Unit/UE4070066.wav` |
| 4 | 0 | 4070066 | `Unit/UE4070066.wav` |
| 5 | 0 | 4070067 | `Unit/UE4070067.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 7.5 |
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
