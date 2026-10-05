---
title: "Skeleton Warrior"
type: "monster"
id: 640
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 640", "client: Quest.cdb kill objectives (quests 727, 1006)"]
name_key: "UnitName_640"
category: 1
class_mask: 1
kill_group: 10009
model: 10
model_name: "MOB_Seleton01"
model_path: "character/npc/monster/mob_seleton01/mob_seleton01.mo"
scale: 0.8
radius: 0.8
sounds: [4070000, 4070000, 3060040, 3060040, 3060040, 4070003]
quest_targets:
  - {"quest": 727, "need": 10, "group": 10009}
  - {"quest": 1006, "need": 10, "group": 10009}
quest_drops:
  - {"quest": 727, "item": 2555, "rate": 100, "need": 10}
  - {"quest": 1006, "item": 2655, "rate": 100, "need": 10}
spawn_fields: [121]
---
<!-- generated:start -->
<!-- generated-keys: title=1d8195 type=9bbc46 id=a52b27 sources=77a77a name_key=257adb category=356a19 class_mask=356a19 kill_group=e15470 model=b1d578 model_name=608f6a model_path=08c0f7 scale=480262 radius=480262 sounds=6dfede quest_targets=63f5e3 quest_drops=aa667e spawn_fields=a5a5cb -->
|  |  |
|---|---|
| **Unit id** | `640` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10009` with [[wiki/monsters/641-skeleton-archer\|Skeleton Archer]] |
| **Model** | ObjectList `10` MOB_Seleton01 (`character/npc/monster/mob_seleton01/mob_seleton01.mo`) |
| **Scale** | 0.8 (second scale / radius 0.8) |

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

- [[wiki/quests/727-the-necessary-materials|The necessary materials]]: collect 10 × [[wiki/items/2555-skeleton-bone|Skeleton bone]] (drops at 100% while the quest is active) in [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] — via kill group `10009` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1006-skull-temple-hunting|Skull Temple : Hunting]]: collect 10 × [[wiki/items/2655-skeleton-bone|Skeleton bone]] (drops at 100% while the quest is active) in [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] — via kill group `10009` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] — quest map of [[wiki/quests/727-the-necessary-materials|The necessary materials]], [[wiki/quests/1006-skull-temple-hunting|Skull Temple : Hunting]]

### Other units with this name

[[wiki/monsters/700-skeleton-warrior|Skeleton Warrior (700)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 2 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 3 | 0 | 3060040 | `effect/ES3060040.wav` |
| 4 | 0 | 3060040 | `effect/ES3060040.wav` |
| 5 | 0 | 3060040 | `effect/ES3060040.wav` |
| 6 | 0 | 4070003 | `Unit/UE4070003.wav` |

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § Training Camp (field 92) and back at [18:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1090s), [19:20](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1160s) *(name match)*: 20. 18:10 Scout found → quest 9 complete. The Scout (dialogue 641) starts quest 10 "Find the Secret Document": kill Skeleton Warrior Officer 704 for Secret doc…
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § Training Ground and Camp (levels 1–11) at [26:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=1590s), [36:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=2196s) *(name match)*: 12. Hunting Skeletons (107, the Scout, 26:30): kill the Skeleton Warrior Leader and the Skeleton Archer Leader (704/705), then report to Frei at 36:35. Reward:…
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps at [26:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1590s), [26:45](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1605s) *(name match)*: 23. Scout (238, Trigger 9901) 26:30–26:45 (QuestTalk 641). He is glad to be found and asks whether the Oracle sent the player. He lost a document to the skelet…
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
