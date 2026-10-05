---
title: "For the honor"
type: "quest"
id: 109
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 109", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 692", "client: QuestTalk.cdb id 693"]
name_key: "Quest_Title_109"
kind: 1
kind_name: "Sub"
level: {"min": 28}
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 18
requires_bit: 16
prev: [17]
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 28}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 2, "what": null, "a": 5, "b": 3, "maps": [113, 113, 113], "text_key": "Quest_QuickText_109"}
  - {"n": 2, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 600000, "shown": 500000}
  - {"type": 4, "what": "gold", "amount": 50000}
offer_talk: 692
complete_talk: 693
---
<!-- generated:start -->
<!-- generated-keys: title=b3542e type=eb5b2b id=a1422e sources=35e174 name_key=436506 kind=356a19 kind_name=0bac50 level=84a59c giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=9e6a55 requires_bit=1574bd prev=79d296 next=97d170 prerequisites=c3110a stages=30caa7 objectives=2be88c objectives_client=eccde8 rewards=330f70 offer_talk=6d3eeb complete_talk=d69b92 -->
|  |  |
|---|---|
|  | ![For the honor](wiki/assets/npcs/200.png) |
| **Quest id** | `109` |
| **Kind** | Sub (kind 1) |
| **Level** | 28+ |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 18 |
| **Requires bit** | 16 |

### Chain

- **After:** [[wiki/quests/17-support-the-abyss-expedition|Support the Abyss expedition]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 28+ |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 2 — kill enemy players?; values a=5, b=3 — tracker: “Destroy the enemy player from the Gaia field” — on [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] (113)
2. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

- **Basic reward:** 600,000 exp (shown in game as 500,000); 50,000 gold

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 692)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** The Gaia are a war zone with enemy Nations.The war is fierce these days.  
> **Freya:** Kill the enemy Players 3 times for the honor of our nation.  
> *(accept / continue)*

#### Completion (QuestTalk 693)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Thank you for resting their souls, I'm sure they would thank you as well.  
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
