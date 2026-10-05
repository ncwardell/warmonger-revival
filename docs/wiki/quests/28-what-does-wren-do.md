---
title: "What does Wren do?"
type: "quest"
id: 28
status: "complete"
missing: []
sources: ["client: Quest.cdb id 28", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "client: QuestTalk.cdb id 731"]
name_key: "Quest_Title_656"
kind: 2
kind_name: "Guide"
giver: {"auto": true}
turn_in: {"auto": true}
bit: 75
automatic: true
prev: [5]
next: []
prerequisites:
  - {"type": 6, "what": "item", "item": 1900, "count": 1}
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 238, "talk": 731, "maps": [88, 92, 96], "text_key": "Quest_QuickText_656_1"}
  - {"n": 2, "type": 9, "what": "sell_item", "item": 1900, "count": 1, "text_key": "Quest_QuickText_656_2"}
  - {"n": 3, "type": 10, "what": "buy_item", "item": 906, "count": 1, "text_key": "Quest_QuickText_656_3"}
rewards: []
---
<!-- generated:start -->
<!-- generated-keys: title=5c6c1f type=eb5b2b id=0a57cb sources=8e965f name_key=ee7314 kind=da4b92 kind_name=875cc6 giver=847ad4 turn_in=847ad4 bit=450dde automatic=5ffe53 prev=10ae24 next=97d170 prerequisites=e7bbdf stages=a80fa1 objectives=fc8a5c rewards=97d170 -->
|  |  |
|---|---|
| **Quest id** | `28` |
| **Kind** | Guide (kind 2) |
| **Giver** | automatic |
| **Turn in** | automatic |
| **Completion bit** | 75 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/5-united-problem-solvers|United Problem Solvers]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] |

### Objectives

1. Talk to [[wiki/npcs/238-wren|Wren]] (dialogue 731) — tracker: “Talk to Wren” — on Arslan: [[wiki/fields/88-training-camp|Training Camp]] (88) · Erion: [[wiki/fields/92-training-camp|Training Camp]] (92) · Armia: [[wiki/fields/96-training-camp|Training Camp]] (96)
2. Sell [[wiki/items/1900-faded-passion-fragments|Faded Passion fragments]] — tracker: “Sell a Faded Passion fragments to Wren”
3. Buy [[wiki/items/906-scroll-return|Scroll : Return]] — tracker: “Buy a Return Scroll from Wren”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

None in the client.

### Dialogue

#### Objective 1 (QuestTalk 731)

Speaker: [[wiki/npcs/238-wren|Wren]]

> **Wren:** I'm a merchant, you can purchase and sell stuff here.

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: step 17 at [16:40](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1000s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 6 at [16:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=995s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 10 at [13:35](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=815s); step 11 at [14:20](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=860s)
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
