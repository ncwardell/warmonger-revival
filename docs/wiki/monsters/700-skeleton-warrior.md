---
title: "Skeleton Warrior"
type: "monster"
id: 700
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 700", "client: Quest.cdb kill objectives (quests 101)"]
name_key: "UnitName_700"
category: 1
class_mask: 1
kill_group: 10003
model: 10
model_name: "MOB_Seleton01"
model_path: "character/npc/monster/mob_seleton01/mob_seleton01.mo"
scale: 0.8
radius: 0.8
sounds: [4070000, 4070000, 3060040, 3060040, 3060040, 4070003]
quest_targets:
  - {"quest": 101, "need": 10, "group": 10003}
quest_drops:
  - {"quest": 101, "item": 2571, "rate": 100, "need": 10}
spawn_fields: [99, 100, 101]
---
<!-- generated:start -->
<!-- generated-keys: title=1d8195 type=9bbc46 id=d8e4bb sources=1054a5 name_key=beae27 category=356a19 class_mask=356a19 kill_group=b27b41 model=b1d578 model_name=608f6a model_path=08c0f7 scale=480262 radius=480262 sounds=6dfede quest_targets=c290ae quest_drops=cee252 spawn_fields=0f349c -->
|  |  |
|---|---|
| **Unit id** | `700` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10003` with [[wiki/monsters/701-skeleton-archer\|Skeleton Archer]] |
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

- [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]: collect 10 × [[wiki/items/2571-weak-skeleton-bone|Weak Skeleton bone]] (drops at 100% while the quest is active) in [[wiki/fields/99-corpse-incineration|Corpse incineration]], [[wiki/fields/100-corpse-incineration|Corpse incineration]], [[wiki/fields/101-corpse-incineration|Corpse incineration]] — via kill group `10003` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/99-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]
- [[wiki/fields/100-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]
- [[wiki/fields/101-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]

### Other units with this name

[[wiki/monsters/640-skeleton-warrior|Skeleton Warrior (640)]]

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

- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps at [24:12](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1452s): 22. Portal → Corpse incineration (field 99) 24:12. The player arrives beside a "Training Camp" return portal (gate 1500 at 306.03, 2254.17, *client*). Mobs: Sk…
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Monsters and damage: Skeleton Warrior / Archer, Elite Skeleton Warrior / Archer · 700 / 701, 702 / 703 · Corpse incineration (99) · groups 10003 / 10004; they hit for about 19
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

- Lives in [[wiki/fields/99-corpse-incineration|Corpse incineration (99)]]; kill group 10003 for quest 101 (Weak Skeleton bone) (video + client, [[gameplay/video-tutorial-walkthrough]] step 22 at [24:12](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1452s), step 26).
- Skeletons hit the player (a low-level Guardian) for about 19; the player's basic hits did 109 damage to them (video, [[gameplay/video-tutorial-walkthrough]] § Monsters and damage).

## Behaviour

- Quest items drop at the `Quest.tsv` rate: every kill of a matching monster gave one while the quest was active (video, [[gameplay/video-early-quests]] §6).

## Sources

- [[gameplay/video-tutorial-walkthrough]] steps 22–26 and § Monsters and damage; [[gameplay/video-early-quests]] §2, §5

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
