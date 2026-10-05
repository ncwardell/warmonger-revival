---
title: "Elite Tow Sorcerer"
type: "monster"
id: 661
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 661", "client: Quest.cdb kill objectives (quests 779, 1032)"]
name_key: "UnitName_661"
category: 1
class_mask: 1
kill_group: 10024
model: 18
model_name: "MOB_Orc_Wizard_0_1_0_00_00"
model_path: "character/npc/monster/mob_orc/mob_orc_wizard.mo"
scale: 1.7
radius: 1
projectile: 642
sounds: [4070111, 4070111, 4070012, 4070012, 4070012, 4070011]
quest_targets:
  - {"quest": 779, "need": 5, "group": 10024}
  - {"quest": 1032, "need": 5, "group": 10024}
spawn_fields: [125]
---
<!-- generated:start -->
<!-- generated-keys: title=501765 type=9bbc46 id=28903f sources=c709b3 name_key=8b9604 category=356a19 class_mask=356a19 kill_group=fe762c model=9e6a55 model_name=beb51d model_path=07c67e scale=58e6d3 radius=356a19 projectile=99316d sounds=ab3b33 quest_targets=400f8b spawn_fields=896837 -->
|  |  |
|---|---|
| **Unit id** | `661` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10024` with [[wiki/monsters/660-elite-tow-warrior\|Elite Tow Warrior]] |
| **Model** | ObjectList `18` MOB_Orc_Wizard_0_1_0_00_00 (`character/npc/monster/mob_orc/mob_orc_wizard.mo`) |
| **Scale** | 1.7 (second scale / radius 1) |
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

- [[wiki/quests/779-request-of-dispatch-knight|Request of dispatch knight]]: kill 5 in [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] — via kill group `10024` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1032-tow-canyon-hunting|Tow Canyon : Hunting]]: kill 5 in [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] — via kill group `10024` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] — quest map of [[wiki/quests/779-request-of-dispatch-knight|Request of dispatch knight]], [[wiki/quests/1032-tow-canyon-hunting|Tow Canyon : Hunting]]

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
