---
title: "Cobra"
type: "monster"
id: 732
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 732", "client: Quest.cdb kill objectives (quests 3)"]
name_key: "UnitName_732"
category: 1
class_mask: 1
model: 58
model_name: "MOB_Cobra_01"
model_path: "character/npc/monster/mob_cobra_01/mob_cobra_01.mo"
scale: 1.3
radius: 1
sounds: [4070028, 4070028, 4070028, 4070030]
quest_targets:
  - {"quest": 3, "need": 5}
quest_drops:
  - {"quest": 3, "item": 2551, "rate": 100, "need": 5}
spawn_fields: [89, 93, 97]
---
<!-- generated:start -->
<!-- generated-keys: title=3fcd0e type=9bbc46 id=9deb86 sources=953a9c name_key=874cf3 category=356a19 class_mask=356a19 model=667be5 model_name=49c4fc model_path=0e0cbd scale=2afe7d radius=356a19 sounds=6db17f quest_targets=a48a0d quest_drops=ff7442 spawn_fields=6e2020 -->
|  |  |
|---|---|
| **Unit id** | `732` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `58` MOB_Cobra_01 (`character/npc/monster/mob_cobra_01/mob_cobra_01.mo`) |
| **Scale** | 1.3 (second scale / radius 1) |

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

- [[wiki/quests/3-the-task-at-hand|The task at hand]]: collect 5 × [[wiki/items/2551-snake-leather|Snake Leather]] (drops at 100% while the quest is active) in [[wiki/fields/89-training-ground|Training Ground]], [[wiki/fields/93-training-ground|Training Ground]], [[wiki/fields/97-training-ground|Training Ground]]

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/89-training-ground|Training Ground]] — quest map of [[wiki/quests/3-the-task-at-hand|The task at hand]]
- [[wiki/fields/93-training-ground|Training Ground]] — quest map of [[wiki/quests/3-the-task-at-hand|The task at hand]]
- [[wiki/fields/97-training-ground|Training Ground]] — quest map of [[wiki/quests/3-the-task-at-hand|The task at hand]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 3 | 12 | 4070028 | `Unit/UE4070028.wav` |
| 4 | 12 | 4070028 | `Unit/UE4070028.wav` |
| 5 | 0 | 4070028 | `Unit/UE4070028.wav` |
| 6 | 0 | 4070030 | `Unit/UE4070030.wav` |

### Current server

What `server/` does now (our choices, not original data):

- `server/world.py` MONSTERS: 2 spawned near the tutorial centre, level 2, HP 120
- `server/loot.py` EXTRA_DROPS: [[wiki/items/839-wild-herb|Wild herb]] 10% × 1–1; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] 5% × 1–1

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § Training Ground and Camp (levels 1–11) at [7:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=420s), [12:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=757s): 3. The task at hand (3, Floyd), accepted at 7:00: 5 Bee Needle from Bees (731) and 5 Cobra/Snake Leather from Cobras (732). Turn in to Floyd at 12:35. Reward:…
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps at [8:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=480s), [9:45](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=585s): 6. Bees (731) and Cobras (732) 8:00–9:45. The drops show in chat as Bee Needle (2552) and Snake Leather (2551). The tracker names the second one "Cobra Leather…
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Monsters and damage: Bee / Cobra · 731 / 732 · Training Ground, middle · Bee Needle 2552 / Snake Leather 2551 for Q3; a Bee hit the player for 15
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps at [7:06](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=426s), [7:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=450s) *(name match)*: 5. Floyd (239), Q2 turn-in 7:06. Floyd's line is QuestTalk 632. Reward: 1200 exp and Gloves of Life (403), which gives level 3 (HP 610, MP 750). She offers Q3…
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § Training Ground (field 93) *(name match)*: Objectives: 5 Bee Needle 2552 from Bee 731 and 5 Snake Leather 2551 from Cobra 732, both 100 % drops (the tracker calls the second "Cobra Leather").
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 5. Other facts *(name match)*: Monsters by area: Training Ground: Slime 604, Bee 731, Cobra 732, Chepa Warrior 727, Chepa Archer 728, Chepa officers 710/711 (the officers fight inside a grou…
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen *(name match)*: Kill messages ("X was destroyed") in quest order: Slime → Chepa Warrior / Chepa Archer (Training Ground circle, many killed for exp) → Bee, Cobra → Chepa Warri…

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
