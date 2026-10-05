---
title: "Farrell's Request"
type: "quest"
id: 16
status: "complete"
missing: []
sources: ["client: Quest.cdb id 16", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 655", "client: QuestTalk.cdb id 656", "client: QuestTalk.cdb id 896"]
name_key: "Quest_Title_642"
kind: 0
kind_name: "Main"
giver: {"npc": 237}
turn_in: {"npc": 237}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 15
requires_bit: 22
prev: [22]
next: [32, 733, 734, 735, 1021, 1022]
stages: [1, 2, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 99, "talk": 896, "maps": [120, 120, 120], "text_key": "Quest_QuickText_Area"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 122, "maps": [122, 122, 122], "text_key": "Quest_QuickText_642_1"}
  - {"n": 3, "type": 1, "what": "collect", "unit": 645, "count": 5, "item": 2566, "rate": 100, "maps": [122, 122, 122], "text_key": "Quest_QuickText_642_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_G_FAREL"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1760000, "shown": 1600000}
  - {"type": 1, "what": "item", "item": 688, "count": 6, "pick": "fixed"}
offer_talk: 655
complete_talk: 656
---
<!-- generated:start -->
<!-- generated-keys: title=af04be type=eb5b2b id=1574bd sources=7fbb45 name_key=290175 kind=b6589f kind_name=b3f808 giver=65eab4 turn_in=65eab4 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=f1abd6 requires_bit=12c6fc prev=5c6c1d next=261072 stages=642aaf objectives=621ff9 rewards=44d999 offer_talk=4dcee7 complete_talk=e30e49 -->
|  |  |
|---|---|
|  | ![Farrell's Request](wiki/assets/npcs/237.png) |
| **Quest id** | `16` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/237-farrell\|Farrell]] |
| **Turn in** | [[wiki/npcs/237-farrell\|Farrell]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 15 |
| **Requires bit** | 22 |

### Chain

- **After:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]
- **Next:** [[wiki/quests/32-swamps-of-snake-warrior|Swamps of Snake Warrior]], [[wiki/quests/733-weapon-appropriation|Weapon appropriation]], [[wiki/quests/734-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/735-collecting-material|Collecting material]], [[wiki/quests/1021-swamps-of-the-snake-warrior-hunting|Swamps of the Snake Warrior : Hunting]], [[wiki/quests/1022-swamps-of-the-snake-warrior-collecting-material|Swamps of the Snake Warrior : Collecting material]]

### Objectives

1. Talk to Dimension Gate (dialogue 896) — tracker: “Go to Dimension Gate”
2. Go to [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122) — tracker: “Go to the Tsunami Lake” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
3. Collect [[wiki/items/2566-crystal-ball|Crystal Ball]] × 5 from [[wiki/monsters/645-elite-fisher|Elite Fisher]] (drop 100%) — tracker: “Acquire Crystal Balls (0/5)” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
4. Report (tracker line; done by turning the quest in) — tracker: “Deliver them to Farrell”

Stages (`flag1..5` = [1, 2, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 1,760,000 exp (shown in game as 1,600,000); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 6

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 655)

Speaker: [[wiki/npcs/237-farrell|Farrell]]

> **Farrell:** The mutants at the Tsunami Lake have powerful Crystal Balls in their possession.  
> **Farrell:** Could you obtain a couple of those for me?  
> **Farrell:** If you manage to do that, I will reward you properly.  
> *(accept / continue)*

#### Objective 1 (QuestTalk 896)

Speaker: NPC

> *(end)*

#### Completion (QuestTalk 656)

Speaker: [[wiki/npcs/237-farrell|Farrell]]

> **You:** Hey Farrell, I got what you asked me for.  
> **Farrell:** Hahaha... You really did it. Take this as a reward  
> *(accept / continue)*
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
