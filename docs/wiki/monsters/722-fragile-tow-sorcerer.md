---
title: "Fragile Tow Sorcerer"
type: "monster"
id: 722
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 722", "client: Quest.cdb kill objectives (quests 80, 81, 82, 749, 1101)"]
name_key: "UnitName_722"
category: 1
class_mask: 1
kill_group: 10001
model: 18
model_name: "MOB_Orc_Wizard_0_1_0_00_00"
model_path: "character/npc/monster/mob_orc/mob_orc_wizard.mo"
scale: 1.2
radius: 1
projectile: 642
sounds: [4070111, 4070111, 4070012, 4070012, 4070012, 4070011]
quest_targets:
  - {"quest": 80, "need": 10, "group": 10001}
  - {"quest": 81, "need": 10, "group": 10001}
  - {"quest": 82, "need": 10, "group": 10001}
  - {"quest": 749, "need": 50, "group": 10001}
  - {"quest": 1101, "need": 50, "group": 10001}
spawn_fields: [108, 109, 111]
---
<!-- generated:start -->
<!-- generated-keys: title=1b8388 type=9bbc46 id=278e89 sources=3ec9c1 name_key=dad7e5 category=356a19 class_mask=356a19 kill_group=6c447a model=9e6a55 model_name=beb51d model_path=07c67e scale=8114b9 radius=356a19 projectile=99316d sounds=ab3b33 quest_targets=2f1220 spawn_fields=20d88d -->
|  |  |
|---|---|
| **Unit id** | `722` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10001` with [[wiki/monsters/721-fragile-tow-warrior\|Fragile Tow Warrior]] |
| **Model** | ObjectList `18` MOB_Orc_Wizard_0_1_0_00_00 (`character/npc/monster/mob_orc/mob_orc_wizard.mo`) |
| **Scale** | 1.2 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 642 (archers carry one; meaning *inferred*) |

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

- [[wiki/quests/80-support-the-abyss-expedition|Support the Abyss expedition]]: kill 10 in [[wiki/fields/108-the-land-of-greed|The land of Greed]], [[wiki/fields/109-the-land-of-greed|The land of Greed]], [[wiki/fields/111-the-land-of-greed|The land of Greed]] — via kill group `10001` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/81-support-the-abyss-expedition|Support the Abyss expedition]]: kill 10 in [[wiki/fields/108-the-land-of-greed|The land of Greed]], [[wiki/fields/109-the-land-of-greed|The land of Greed]], [[wiki/fields/111-the-land-of-greed|The land of Greed]] — via kill group `10001` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/82-support-the-abyss-expedition|Support the Abyss expedition]]: kill 10 in [[wiki/fields/108-the-land-of-greed|The land of Greed]], [[wiki/fields/109-the-land-of-greed|The land of Greed]], [[wiki/fields/111-the-land-of-greed|The land of Greed]] — via kill group `10001` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/749-kill-monster-of-the-land-of-greed|Kill monster of The land of Greed]]: kill 50 in [[wiki/fields/108-the-land-of-greed|The land of Greed]], [[wiki/fields/109-the-land-of-greed|The land of Greed]], [[wiki/fields/111-the-land-of-greed|The land of Greed]] — via kill group `10001` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1101-the-land-of-greed-kill-monster|The Land of Greed : Kill monster]]: kill 50 in [[wiki/fields/108-the-land-of-greed|The land of Greed]], [[wiki/fields/109-the-land-of-greed|The land of Greed]], [[wiki/fields/111-the-land-of-greed|The land of Greed]] — via kill group `10001` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/108-the-land-of-greed|The land of Greed]] — quest map of [[wiki/quests/80-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/81-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/82-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/749-kill-monster-of-the-land-of-greed|Kill monster of The land of Greed]], [[wiki/quests/1101-the-land-of-greed-kill-monster|The Land of Greed : Kill monster]]
- [[wiki/fields/109-the-land-of-greed|The land of Greed]] — quest map of [[wiki/quests/80-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/81-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/82-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/749-kill-monster-of-the-land-of-greed|Kill monster of The land of Greed]], [[wiki/quests/1101-the-land-of-greed-kill-monster|The Land of Greed : Kill monster]]
- [[wiki/fields/111-the-land-of-greed|The land of Greed]] — quest map of [[wiki/quests/80-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/81-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/82-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/749-kill-monster-of-the-land-of-greed|Kill monster of The land of Greed]], [[wiki/quests/1101-the-land-of-greed-kill-monster|The Land of Greed : Kill monster]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070111 | `Unit/UE4070111.wav` |
| 2 | 0 | 4070111 | `Unit/UE4070111.wav` |
| 3 | 926 | 4070012 | `Unit/UE4070012.wav` |
| 4 | 926 | 4070012 | `Unit/UE4070012.wav` |
| 5 | 0 | 4070012 | `Unit/UE4070012.wav` |
| 6 | 0 | 4070011 | `Unit/UE4070011.wav` |

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
