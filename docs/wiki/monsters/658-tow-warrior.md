---
title: "Tow Warrior"
type: "monster"
id: 658
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 658", "client: Quest.cdb kill objectives (quests 34, 779, 1032)"]
name_key: "UnitName_658"
category: 1
class_mask: 1
kill_group: 10023
model: 17
model_name: "MOB_Orc_Warrior_0_1_0_00_00"
model_path: "character/npc/monster/mob_orc/mob_orc_warrior.mo"
scale: 1.2
radius: 1
sounds: [4070112, 4070112, 4070010, 4070010, 4070010, 4070011]
quest_targets:
  - {"quest": 34, "need": 1, "group": 10023}
  - {"quest": 779, "need": 15, "group": 10023}
  - {"quest": 1032, "need": 15, "group": 10023}
quest_drops:
  - {"quest": 34, "item": 2582, "rate": 10, "need": 1}
spawn_fields: [125]
---
<!-- generated:start -->
<!-- generated-keys: title=4cda7e type=9bbc46 id=f597ae sources=360929 name_key=3f4fc1 category=356a19 class_mask=356a19 kill_group=490a2b model=0716d9 model_name=cb6e5e model_path=c6d4b3 scale=8114b9 radius=356a19 sounds=e898d3 quest_targets=74ee20 quest_drops=e2b15f spawn_fields=896837 -->
|  |  |
|---|---|
| **Unit id** | `658` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10023` with [[wiki/monsters/659-tow-sorcerer\|Tow Sorcerer]] |
| **Model** | ObjectList `17` MOB_Orc_Warrior_0_1_0_00_00 (`character/npc/monster/mob_orc/mob_orc_warrior.mo`) |
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

### Quests

- [[wiki/quests/34-tow-canyon|Tow Canyon]]: collect 1 × [[wiki/items/2582-innocence-piece|Innocence Piece]] (drops at 10% while the quest is active) in [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] — via kill group `10023` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/779-request-of-dispatch-knight|Request of dispatch knight]]: kill 15 in [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] — via kill group `10023` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1032-tow-canyon-hunting|Tow Canyon : Hunting]]: kill 15 in [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] — via kill group `10023` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] — quest map of [[wiki/quests/34-tow-canyon|Tow Canyon]], [[wiki/quests/779-request-of-dispatch-knight|Request of dispatch knight]], [[wiki/quests/1032-tow-canyon-hunting|Tow Canyon : Hunting]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070112 | `Unit/UE4070112.wav` |
| 2 | 0 | 4070112 | `Unit/UE4070112.wav` |
| 3 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 4 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 5 | 0 | 4070010 | `Unit/UE4070010.wav` |
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
