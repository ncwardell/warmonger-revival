---
title: "The Slime is mine"
type: "quest"
id: 2
status: "complete"
missing: []
sources: ["client: Quest.cdb id 2", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 630", "client: QuestTalk.cdb id 632"]
name_key: "Quest_Title_631"
kind: 0
kind_name: "Main"
giver: {"npc": 201}
turn_in: {"npc": 239}
offer_maps: [89, 93, 97]
turn_in_maps: [89, 93, 97]
bit: 2
requires_bit: 1
prev: [1, 1501]
next: [3]
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit": 604, "count": 3, "item": 2550, "rate": 100, "maps": [89, 93, 97], "text_key": "Quest_QuickText_631_1"}
  - {"n": 2, "type": 0, "what": "report", "maps": [89, 93, 97], "text_key": "Quest_QuickText_G_FLOYD"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1320, "shown": 1200}
  - {"type": 1, "what": "item", "item": 403, "count": 1, "pick": "fixed"}
offer_talk: 630
complete_talk: 632
---
<!-- generated:start -->
<!-- generated-keys: title=494589 type=eb5b2b id=da4b92 sources=679091 name_key=54b21d kind=b6589f kind_name=b3f808 giver=444e6c turn_in=9d96c7 offer_maps=6e2020 turn_in_maps=6e2020 bit=da4b92 requires_bit=356a19 prev=ef8166 next=f1e31d stages=a80fa1 objectives=dd2911 rewards=33dd9c offer_talk=2c9bae complete_talk=e7ee3e -->
|  |  |
|---|---|
|  | ![The Slime is mine](wiki/assets/npcs/201.png) |
| **Quest id** | `2` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/201-shaia\|Shaia]] |
| **Turn in** | [[wiki/npcs/239-floyd\|Floyd]] |
| **Offered on** | Arslan: [[wiki/fields/89-training-ground\|Training Ground]] (89) · Erion: [[wiki/fields/93-training-ground\|Training Ground]] (93) · Armia: [[wiki/fields/97-training-ground\|Training Ground]] (97) |
| **Completion bit** | 2 |
| **Requires bit** | 1 |
| **Current server** | enabled in `server/quests.py` |

### Chain

- **After:** [[wiki/quests/1-on-to-a-promising-start|On to a promising start]], [[wiki/quests/1501-basic-function-move-character|Basic function - Move character]]
- **Next:** [[wiki/quests/3-the-task-at-hand|The task at hand]]

### Objectives

1. Collect [[wiki/items/2550-slime-mucus|Slime Mucus]] × 3 from [[wiki/monsters/604-slime|Slime]] (drop 100%) — tracker: “Slime mucus obtained (0/3)”
2. Report (tracker line; done by turning the quest in) — tracker: “Bring them to Floyd”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 1,320 exp (shown in game as 1,200); [[wiki/items/403-gloves-of-life|Gloves of Life]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 630)

Speaker: [[wiki/npcs/201-shaia|Shaia]]

> **Shaia:** Why are you always late?  
> **Shaia:** Gather a couple of Slime Mucus from the Slimes around here and hurry up. You are already late as it is.  
> **You:** Why should the best fighter in the world gather slime mucus?  
> **Shaia:** The best fighter in the world? Hahaha.<br>At least you have a good sense of humour.<br>You have a long way to go before you can call yourself that.<br>Now stop fooling around and get going, Biologist Floyd needs them for her research.  
> **You:** But... but.... never mind. I'll get the job done!<br>Don't you worry Shaia, the Slimes won't know what hit them!  
> *(accept / continue)*

#### Completion (QuestTalk 632)

Speaker: [[wiki/npcs/239-floyd|Floyd]]

> **Floyd:** There you are, I already thought about sending out a rescue party!<br>But I'm glad you finally made it and brought me the slime mucus.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 1 at [4:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=260s); step 2 at [6:45](https://www.youtube.com/watch?v=s04CSN16w1s&t=405s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 3 at [4:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=240s); step 5 at [7:06](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=426s)
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
