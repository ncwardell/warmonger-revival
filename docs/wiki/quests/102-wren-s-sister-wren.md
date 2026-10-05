---
title: "Wren's sister Wren?"
type: "quest"
id: 102
status: "complete"
missing: []
sources: ["client: Quest.cdb id 102", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 670", "client: QuestTalk.cdb id 679"]
name_key: "Quest_Title_649"
kind: 1
kind_name: "Sub"
giver: {"npc": 238}
turn_in: {"auto": true}
offer_maps: [88, 92, 96]
bit: 42
requires_bit: 9
automatic: true
prev: [10]
next: []
prerequisites:
  - {"type": 6, "what": "item", "item": 2563, "count": 1}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 204, "talk": 670, "maps": [0, 120, 120], "text_key": "Quest_QuickText_649_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 67200, "shown": 56000}
  - {"type": 1, "what": "item", "item": 601, "count": 20, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 20, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 700, "count": 10, "pick": "fixed"}
offer_talk: 679
---
<!-- generated:start -->
<!-- generated-keys: title=15b5f9 type=eb5b2b id=c8306a sources=1e3f9a name_key=471be1 kind=356a19 kind_name=0bac50 giver=8c8154 turn_in=847ad4 offer_maps=46bf0f bit=92cfce requires_bit=0ade7c automatic=5ffe53 prev=e9310b next=97d170 prerequisites=70ddc4 stages=30caa7 objectives=468dd5 rewards=45cdcf offer_talk=eac681 -->
|  |  |
|---|---|
|  | ![Wren's sister Wren?](wiki/assets/npcs/238.png) |
| **Quest id** | `102` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/238-wren\|Wren]] |
| **Turn in** | automatic |
| **Offered on** | Arslan: [[wiki/fields/88-training-camp\|Training Camp]] (88) · Erion: [[wiki/fields/92-training-camp\|Training Camp]] (92) · Armia: [[wiki/fields/96-training-camp\|Training Camp]] (96) |
| **Completion bit** | 42 |
| **Requires bit** | 9 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/10-find-the-secret-document|Find the Secret Document]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/2563-hawker-letter\|Hawker letter]] |

### Objectives

1. Talk to [[wiki/npcs/204-wren|Wren]] (dialogue 670) — tracker: “Meet Wren in the fort.” — on Arslan: — · Erion: [[wiki/fields/120-fortress|Fortress]] (120) · Armia: [[wiki/fields/120-fortress|Fortress]] (120)

### Rewards

- **Basic reward:** 67,200 exp (shown in game as 56,000); [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 20; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 20; [[wiki/items/700-crystal-blue|Crystal : Blue]] × 10

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 679)

Speaker: [[wiki/npcs/238-wren|Wren]]

> **Wren:** Are you going to the Fortress? May I ask a favour of you?  
> **Wren:** Please deliver this letter to Wren. She is waiting for it.<br>Don't look at me like that, she is my twin sister and has the same name.<br>You can't chose the name you're born with, am I right?  
> *(accept / continue)*

#### Objective 1 (QuestTalk 670)

Speaker: [[wiki/npcs/204-wren|Wren]]

> **Wren:** What is this?  
> **You:** I was asked to deliver this to you.  
> **Wren:** Really? Thank you.. I was waiting for this letter.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: step 22 at [20:20](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1220s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 14 at [37:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=2222s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 28 at [30:50](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1850s)
<!-- generated:end -->

## Notes

Wren (238) asks the player to carry the Hawker letter (2563, the quest's start item) to her twin Wren (204) in the Fortress; tracker "Meet Wren in the fort" ([37:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=2220s), [30:50](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1850s), [20:20](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1220s)). Done at about 40:05 in the first-session video. Panel: 56,000 exp, 20 Blue and 20 Red Passion Fragments [D], 10 Crystal: Blue ([[gameplay/video-early-quests]] step 14). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-early-quests]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
