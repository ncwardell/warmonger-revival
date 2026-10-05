---
title: "Find the Secret Document"
type: "quest"
id: 10
status: "complete"
missing: []
sources: ["client: Quest.cdb id 10", "client: QuestTalk.cdb id 641", "client: QuestTalk.cdb id 642"]
name_key: "Quest_Title_636"
kind: 0
kind_name: "Main"
giver: {"gadget": 1}
turn_in: {"npc": 198}
offer_maps: [99, 100, 101]
turn_in_maps: [88, 92, 96]
bit: 9
requires_bit: 8
prev: [9]
next: [11, 102]
stages: [4, 0, 0, 0, 0]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit": 704, "count": 1, "item": 2565, "rate": 100, "maps": [99, 100, 101], "text_key": "Quest_QuickText_636_1"}
  - {"n": 2, "type": 0, "what": "report", "maps": [88, 92, 96], "text_key": "Quest_QuickText_G_FREI"}
rewards:
  - {"type": 1, "what": "item", "item": 2021, "count": 1, "pick": "class", "class": "Saint"}
  - {"type": 1, "what": "item", "item": 2022, "count": 1, "pick": "class", "class": "Punisher"}
  - {"type": 1, "what": "item", "item": 2023, "count": 1, "pick": "class", "class": "Guardian"}
  - {"type": 1, "what": "item", "item": 399, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 407, "count": 1, "pick": "choose"}
offer_talk: 641
complete_talk: 642
---
<!-- generated:start -->
<!-- generated-keys: title=c90d73 type=eb5b2b id=b1d578 sources=bce37b name_key=44c42c kind=b6589f kind_name=b3f808 giver=bc802c turn_in=f8f324 offer_maps=0f349c turn_in_maps=46bf0f bit=0ade7c requires_bit=fe5dbb prev=7a6055 next=65eca2 stages=603efe objectives=54d601 rewards=4c4335 offer_talk=d2578a complete_talk=99316d -->
|  |  |
|---|---|
| **Quest id** | `10` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/nodes/9901-scout\|Scout]] / [[wiki/nodes/10001-scout\|Scout]] / [[wiki/nodes/10101-scout\|Scout]] (gadget 1) |
| **Turn in** | [[wiki/npcs/198-frei\|Frei]] |
| **Offered on** | Arslan: [[wiki/fields/99-corpse-incineration\|Corpse incineration]] (99) · Erion: [[wiki/fields/100-corpse-incineration\|Corpse incineration]] (100) · Armia: [[wiki/fields/101-corpse-incineration\|Corpse incineration]] (101) |
| **Turned in on** | Arslan: [[wiki/fields/88-training-camp\|Training Camp]] (88) · Erion: [[wiki/fields/92-training-camp\|Training Camp]] (92) · Armia: [[wiki/fields/96-training-camp\|Training Camp]] (96) |
| **Completion bit** | 9 |
| **Requires bit** | 8 |

### Chain

- **After:** [[wiki/quests/9-find-the-missing-scout|Find the missing Scout]]
- **Next:** [[wiki/quests/11-an-urgent-message|An urgent message]], [[wiki/quests/102-wren-s-sister-wren|Wren's sister Wren?]]

### Objectives

1. Collect [[wiki/items/2565-secret-document|Secret document]] from [[wiki/monsters/704-skeleton-warrior-officer|Skeleton Warrior Officer]] (drop 100%) — tracker: “Kill the Leader of the Skeleton Warriors and acquire the document (0/1)”
2. Report (tracker line; done by turning the quest in) — tracker: “Give the document to Frei” — on Arslan: [[wiki/fields/88-training-camp|Training Camp]] (88) · Erion: [[wiki/fields/92-training-camp|Training Camp]] (92) · Armia: [[wiki/fields/96-training-camp|Training Camp]] (96)

Stages (`flag1..5` = [4, 0, 0, 0, 0]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Choose one:** [[wiki/items/399-spell-bracelet|Spell Bracelet]] *or* [[wiki/items/407-bracelet-of-life|Bracelet of Life]]
- **By class:** Saint: [[wiki/items/2021-oracle-set|Oracle Set]]; Punisher: [[wiki/items/2022-oracle-set|Oracle Set]]; Guardian: [[wiki/items/2023-oracle-set|Oracle Set]]

### Dialogue

#### Offer (QuestTalk 641)

Speaker: [[wiki/nodes/9901-scout|Scout]] / [[wiki/nodes/10001-scout|Scout]] / [[wiki/nodes/10101-scout|Scout]] (gadget 1)

> **Scout:** Oh I'm glad someone found me. Did the Oracle send you?  
> **Scout:** I got attacked by a skeleton and lost the document.  
> **Scout:** I can tell you where to find those monsters, please recover the document and bring it <br>back to Frei.  
> **You:** Don't you worry. I will get the job done!  
> *(accept / continue)*

#### Completion (QuestTalk 642)

Speaker: [[wiki/npcs/198-frei|Frei]]

> **You:** This is the secret document you were looking for.  
> **Frei:** I see.. Thank you.. Where is our scout?  
> **You:** He continues to explore the Abyss and will report back to you when he is done.  
> **Frei:** That would be of great help to know the Abyss better.<br>I will give you this Gear for your battle. Thank you<br>When you gather all parts, you will be stronger than now.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: step 20 at [18:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1090s); step 21 at [20:00](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1200s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 11 at [26:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=1580s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 23 at [26:45](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1605s); step 27 at [29:50](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1790s)
<!-- generated:end -->

## Notes

From the Scout (dialogue 641): kill the Skeleton Warrior Officer (704) for the Secret document (2565, 100%) and take it to Frei ([26:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=1580s)). The officer had 2,000 HP and no regeneration ([35:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2120s)). Turned in at [36:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2180s), [29:50](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1790s) and [20:00](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1200s). Rewards: one Oracle Set costume chosen by class (2021/2022/2023) and a choice of Spell Bracelet (399) or Bracelet of Life (407); no exp. At the turn-in the player also receives Scroll: Gaia (912) and the Urgent Letter (2567), the items that start quest 11 ([[gameplay/video-tutorial-walkthrough]] step 27). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-tutorial-walkthrough]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
