---
title: "Battle preparations"
type: "quest"
id: 13
status: "complete"
missing: []
sources: ["client: Quest.cdb id 13", "client: QuestTalk.cdb id 651", "client: QuestTalk.cdb id 652"]
name_key: "Quest_Title_640"
kind: 0
kind_name: "Main"
level: {"min": 10}
giver: {"npc": 200}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 12
automatic: true
prev: []
next: [14]
prerequisites:
  - {"type": 4, "what": "level", "min": 10}
stages: [2, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 212, "talk": 652, "maps": [120, 120, 120], "text_key": "Quest_QuickText_640_1"}
rewards:
  - {"type": 1, "what": "item", "item": 834, "count": 100, "pick": "fixed"}
  - {"type": 4, "what": "gold", "amount": 30000}
  - {"type": 1, "what": "item", "item": 601, "count": 15, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 15, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 700, "count": 5, "pick": "fixed"}
offer_talk: 651
---
<!-- generated:start -->
<!-- generated-keys: title=229ae6 type=eb5b2b id=bd307a sources=a068a7 name_key=9aafdf kind=b6589f kind_name=b3f808 level=29a79b giver=1caac0 turn_in=847ad4 offer_maps=15f2a7 bit=7b5200 automatic=5ffe53 prev=97d170 next=76cdc5 prerequisites=d04db8 stages=0e4f21 objectives=b63128 rewards=e3a779 offer_talk=93f271 -->
|  |  |
|---|---|
|  | ![Battle preparations](wiki/assets/npcs/200.png) |
| **Quest id** | `13` |
| **Kind** | Main (kind 0) |
| **Level** | 10+ |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 12 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** [[wiki/quests/14-battle-preparations|Battle preparations]]

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 10+ |

### Objectives

1. Talk to [[wiki/npcs/212-cassia|Cassia]] (dialogue 652) — tracker: “Talk to Cassia”

Stages (`flag1..5` = [2, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** [[wiki/items/834-empty-flask-c|Empty Flask (C)]] × 100; 30,000 gold; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 15; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 15; [[wiki/items/700-crystal-blue|Crystal : Blue]] × 5

### Dialogue

#### Offer (QuestTalk 651)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** We have confirmation that an Undead Army is in possession of the Transmission Equipment.  
> **Freya:** They plan to use it for an invasion.<br>You should prepare for battle.  
> **Freya:** It's critical for all our survival to secure the Transmission Equipment. (How they got transmission….)  
> **Freya:** Speak to Cassia, she will make sure that you're ready for this battle.  
> *(accept / continue)*

#### Objective 1 (QuestTalk 652)

Speaker: [[wiki/npcs/212-cassia|Cassia]]

> **Cassia:** I guess you're new here.  
> **Cassia:** Go to Odin or Orwen to create better Gears and consumables.  
> *(end)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: at [22:05](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1325s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 15 at [38:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=2312s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 32 at [33:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=2010s)
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
