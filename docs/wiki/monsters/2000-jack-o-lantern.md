---
title: "Jack O' Lantern"
type: "monster"
id: 2000
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 2000", "client: Quest.cdb kill objectives (quests 901, 902, 903)"]
name_key: "UnitName_2000"
category: 1
class_mask: 1
model: 357
model_name: "NPC_Evil002_0_1_0_01_01"
model_path: "character/npc/monster/npc_evil/npc_evil003.mo"
scale: 1.5
radius: 1
sounds: [4000004, 4000004, 4020004, 4020004, 4030004, 4040004]
quest_targets:
  - {"quest": 901, "need": 20}
  - {"quest": 902, "need": 20}
  - {"quest": 903, "need": 20}
quest_drops:
  - {"quest": 901, "item": 2549, "rate": 100, "need": 20}
  - {"quest": 902, "item": 2549, "rate": 100, "need": 20}
  - {"quest": 903, "item": 2549, "rate": 100, "need": 20}
---
<!-- generated:start -->
<!-- generated-keys: title=1051d5 type=9bbc46 id=a4ac91 sources=d42cf4 name_key=0c97ff category=356a19 class_mask=356a19 model=869700 model_name=cfa6d8 model_path=ed75c8 scale=aa8f28 radius=356a19 sounds=2135c0 quest_targets=548fc0 quest_drops=f5194c -->
|  |  |
|---|---|
| **Unit id** | `2000` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `357` NPC_Evil002_0_1_0_01_01 (`character/npc/monster/npc_evil/npc_evil003.mo`) |
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

### Quests

- [[wiki/quests/901-trick-or-treat|Trick or Treat!!]]: collect 20 × [[wiki/items/2549-jack-s-pumpkin|Jack's Pumpkin]] (drops at 100% while the quest is active)
- [[wiki/quests/902-trick-or-treat|Trick or Treat!!]]: collect 20 × [[wiki/items/2549-jack-s-pumpkin|Jack's Pumpkin]] (drops at 100% while the quest is active)
- [[wiki/quests/903-trick-or-treat|Trick or Treat!!]]: collect 20 × [[wiki/items/2549-jack-s-pumpkin|Jack's Pumpkin]] (drops at 100% while the quest is active)

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4000004 | `voice/UV4000004.wav` |
| 2 | 0 | 4000004 | `voice/UV4000004.wav` |
| 3 | 0 | 4020004 | not in sound.csv |
| 4 | 0 | 4020004 | not in sound.csv |
| 5 | 0 | 4030004 | not in sound.csv |
| 6 | 0 | 4040004 | not in sound.csv |

### Seen in

- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]] § 2016-10-27: Halloween ((t453); costumes (t355)): WM / client: unit 2000 "Jack O' Lantern", item 763 "Scroll of Transform: [Jack]", item 1056 Halloween reward box, costumes 2043–2045 and item 2549 "Jack's Pump…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 4.5 |
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
