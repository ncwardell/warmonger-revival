---
title: "Call Tempest"
type: "quest"
id: 37
status: "complete"
missing: []
sources: ["client: Quest.cdb id 37", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 813", "client: QuestTalk.cdb id 814"]
name_key: "Quest_Title_23"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"npc": 327}
offer_maps: [120, 120, 120]
turn_in_maps: [90, 94, 98]
bit: 37
requires_bit: 85
prev: [783, 784]
next: [38]
prerequisites:
  - {"type": 6, "what": "item", "item": 911, "count": 1}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 13, "what": "use_item", "item": 911, "count": 1, "text_key": "Quest_QuickText_23_1"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_23_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 500000, "shown": 454545}
offer_talk: 813
complete_talk: 814
---
<!-- generated:start -->
<!-- generated-keys: title=47e91a type=eb5b2b id=cb7a1d sources=8572dd name_key=04faf7 kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=922d85 offer_maps=15f2a7 turn_in_maps=18e60d bit=cb7a1d requires_bit=135224 prev=03785d next=429a2a prerequisites=154ad3 stages=30caa7 objectives=10d71d rewards=f79b21 offer_talk=90b930 complete_talk=c9264f -->
|  |  |
|---|---|
|  | ![Call Tempest](wiki/assets/npcs/200.png) |
| **Quest id** | `37` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/327-aenes\|Aenes]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Turned in on** | Arslan: [[wiki/fields/90-castle\|Castle]] (90) · Erion: [[wiki/fields/94-castle\|Castle]] (94) · Armia: [[wiki/fields/98-castle\|Castle]] (98) |
| **Completion bit** | 37 |
| **Requires bit** | 85 |

### Chain

- **After:** [[wiki/quests/783-swamps-of-the-snake-warrior|Swamps of the Snake Warrior]], [[wiki/quests/784-swamps-of-the-snake-warrior|Swamps of the Snake Warrior]]
- **Next:** [[wiki/quests/38-innocence-s-recovery-operation|Innocence's recovery operation]]

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/911-scroll-castle\|Scroll : Castle]] |

### Objectives

1. Use [[wiki/items/911-scroll-castle|Scroll : Castle]] — tracker: “Use castle's scroll”
2. Report (tracker line; done by turning the quest in) — tracker: “Go to castle's the Oracle of Protect”

### Rewards

- **Basic reward:** 500,000 exp (shown in game as 454,545)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 813)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** We Tempest are carrying out sacred duties to defend the world from the evil forces that threaten it. <br> If you go to the Oracle of Protection in the Castle, you may find some more detailed information.  
> *(accept / continue)*  
> *(accept / continue)*

#### Completion (QuestTalk 814)

Speaker: [[wiki/npcs/327-aenes|Aenes]]

> **Aenes:** You are running away from the temple now. Can you go now?  
> *(accept / continue)*  
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
