---
title: "Stepping up your game"
type: "quest"
id: 24
status: "stub"
missing: ["next"]
sources: ["client: Quest.cdb id 24", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 718", "client: QuestTalk.cdb id 719"]
name_key: "Quest_Title_696"
kind: 0
kind_name: "Main"
classes: ["Punisher"]
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 23
requires_bit: 21
prev: [21]
next: []
prerequisites:
  - {"type": 1, "what": "class", "classes": ["Punisher"], "mask": 2}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 7, "what": "reach_level", "level": 25, "text_key": "Quest_QuickText_696_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 770000, "shown": 700000}
  - {"type": 1, "what": "item", "item": 2000, "count": 1, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 7122, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 7132, "count": 1, "pick": "choose"}
offer_talk: 718
complete_talk: 719
---
<!-- generated:start -->
<!-- generated-keys: title=53c716 type=eb5b2b id=4d134b sources=7d00c1 name_key=6fa184 kind=b6589f kind_name=b3f808 classes=51f98f giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=d435a6 requires_bit=472b07 prev=6c9878 next=97d170 prerequisites=288542 stages=30caa7 objectives=b904e0 rewards=91cd22 offer_talk=395ea6 complete_talk=839501 -->
|  |  |
|---|---|
|  | ![Stepping up your game](wiki/assets/npcs/200.png) |
| **Quest id** | `24` |
| **Kind** | Main (kind 0) |
| **Classes** | Punisher |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 23 |
| **Requires bit** | 21 |

### Chain

- **After:** [[wiki/quests/21-group-ancient-ghosts|(Group) Ancient Ghosts]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 23 with:** [[wiki/quests/23-stepping-up-your-game|Stepping up your game]], [[wiki/quests/25-stepping-up-your-game|Stepping up your game]] (completing one closes the others)

### Requirements

| type | meaning | value |
|---|---|---|
| 1 | class | Punisher (mask 2) |

### Objectives

1. Reach level 25 — tracker: “Achieve Character Level 25”

### Rewards

- **Basic reward:** 770,000 exp (shown in game as 700,000); [[wiki/items/2000-haple-set|Haple Set]]
- **Choose one:** [[wiki/items/7122-life-steal-rune|Life Steal Rune]] *or* [[wiki/items/7132-spell-vamp-rune|Spell Vamp Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 718)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Welcome, you still need more training and better equipment before you can <br>face the real threat.  
> **Freya:** Your next task will be to become stronger! So keep on training and report back to me when you are done.  
> *(accept / continue)*

#### Completion (QuestTalk 719)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Long time, no see. I can feel that you are more stronger than before.  
> **You:** Of course, I put in a lot of effort and countless hours!  
> **Freya:** I can feel your power. take this new Gear as a token of appreciation.. <br>Just few part has left to set all.  
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
