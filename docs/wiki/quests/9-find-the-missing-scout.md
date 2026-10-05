---
title: "Find the missing Scout"
type: "quest"
id: 9
status: "complete"
missing: []
sources: ["client: Quest.cdb id 9", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 639", "client: QuestTalk.cdb id 640", "client: QuestTalk.cdb id 641"]
name_key: "Quest_Title_635"
kind: 0
kind_name: "Main"
giver: {"npc": 198}
turn_in: {"auto": true}
offer_maps: [88, 92, 96]
bit: 8
requires_bit: 99
automatic: true
prev: [7]
next: [10]
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 215, "talk": 640, "maps": [88, 92, 96], "text_key": "Quest_QuickText_635_1"}
  - {"n": 2, "type": 5, "what": "gadget", "gadget": 1, "talk": 641, "maps": [99, 100, 101], "text_key": "Quest_QuickText_635_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 11440, "shown": 10400}
  - {"type": 1, "what": "item", "item": 885, "count": 100, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 889, "count": 100, "pick": "choose"}
offer_talk: 639
---
<!-- generated:start -->
<!-- generated-keys: title=ae7acb type=eb5b2b id=0ade7c sources=6f7e86 name_key=df0b89 kind=b6589f kind_name=b3f808 giver=f8f324 turn_in=847ad4 offer_maps=46bf0f bit=fe5dbb requires_bit=9a79be automatic=5ffe53 prev=bd703d next=e9310b stages=a80fa1 objectives=498e98 rewards=474386 offer_talk=40e0ce -->
|  |  |
|---|---|
|  | ![Find the missing Scout](wiki/assets/npcs/198.png) |
| **Quest id** | `9` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/198-frei\|Frei]] |
| **Turn in** | automatic |
| **Offered on** | Arslan: [[wiki/fields/88-training-camp\|Training Camp]] (88) · Erion: [[wiki/fields/92-training-camp\|Training Camp]] (92) · Armia: [[wiki/fields/96-training-camp\|Training Camp]] (96) |
| **Completion bit** | 8 |
| **Requires bit** | 99 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/7-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]]
- **Next:** [[wiki/quests/10-find-the-secret-document|Find the Secret Document]]

### Objectives

1. Talk to [[wiki/npcs/215-guard|Guard]] (dialogue 640) — tracker: “Talk to the Guard”
2. Talk to [[wiki/nodes/9901-scout|Scout]] / [[wiki/nodes/10001-scout|Scout]] / [[wiki/nodes/10101-scout|Scout]] (gadget 1) (dialogue 641) — tracker: “Find the Scout in Corpse incineration.” — on Arslan: [[wiki/fields/99-corpse-incineration|Corpse incineration]] (99) · Erion: [[wiki/fields/100-corpse-incineration|Corpse incineration]] (100) · Armia: [[wiki/fields/101-corpse-incineration|Corpse incineration]] (101)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 11,440 exp (shown in game as 10,400)
- **Choose one:** [[wiki/items/885-potion-of-health-c|Potion of Health (C)]] × 100 *or* [[wiki/items/889-potion-of-mana-c|Potion of Mana (C)]] × 100

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 639)

Speaker: [[wiki/npcs/198-frei|Frei]]

> **Frei:** I'm awaiting the arrival of one of our scouts, but he is long overdue.<br>He carries important information.  
> **Frei:** I have no other scouts at my disposal, can you go to the Abyss and look for him?  
> **Frei:** This is your first real mission for our nation.<br>The information is crucial for all our safety.<br>I hope you will be able to find the scout and you both come back well.  
> **Frei:** The Guard will tell you how to get to the Abyss.<br>May the gods bless you.  
> *(accept / continue)*

#### Objective 1 (QuestTalk 640)

Speaker: [[wiki/npcs/215-guard|Guard]]

> **Guard:** So you are the one that has to go into the Abyss?<br>The Abyss is a real maze,<br>I'm glad it's not me they are sending out to find the missing scout.  
> **Guard:** The Abyss is what connects all of Gaia.  
> **Guard:** Use this portal to get into the Abyss.  
> *(accept / continue)*

#### Objective 2 (QuestTalk 641)

Speaker: [[wiki/nodes/9901-scout|Scout]] / [[wiki/nodes/10001-scout|Scout]] / [[wiki/nodes/10101-scout|Scout]] (gadget 1)

> **Scout:** Oh I'm glad someone found me. Did the Oracle send you?  
> **Scout:** I got attacked by a skeleton and lost the document.  
> **Scout:** I can tell you where to find those monsters, please recover the document and bring it <br>back to Frei.  
> **You:** Don't you worry. I will get the job done!  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: step 16 at [15:30](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=930s); step 20 at [18:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1090s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 9 at [21:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=1300s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 20 at [23:45](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1425s); step 23 at [26:45](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1605s)
<!-- generated:end -->

## Notes

From Frei: a scout carrying important information is overdue; talk to the Guard (215) at the Corpse incineration gate in the south of the camp, then find the Scout in Corpse incineration ([21:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=1295s), [23:45](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1425s)). The Guard's dialogue is QuestTalk 640 ([24:02](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1442s)). The Scout is the quest gadget at Trigger 9901 (465.27, 2259.45 in field 99) ([[gameplay/video-tutorial-walkthrough]] steps 21–23). Panel: 10,400 exp, then 100× Potion of Health [C] (885) or 100× Potion of Mana [C] (889). Done at [26:15](https://www.youtube.com/watch?v=s04CSN16w1s&t=1575s), [26:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1590s) and [18:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1090s). *video*

## Behaviour

Finding the Scout completes this quest and starts quest 10 and side quest 107 together ([[gameplay/video-tutorial-walkthrough]] step 23, [[gameplay/video-character-creation-and-tutorial]] §3 step 20). *video*

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-tutorial-walkthrough]]
- [[gameplay/video-character-creation-and-tutorial]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
