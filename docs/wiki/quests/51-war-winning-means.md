---
title: "War - Winning means"
type: "quest"
id: 51
status: "complete"
missing: []
sources: ["client: Quest.cdb id 51", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 907", "client: QuestTalk.cdb id 909"]
name_key: "Quest_Title_51"
kind: 0
kind_name: "Main"
giver: {"npc": 208}
turn_in: {"npc": 208}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 127
requires_bit: 126
prev: [50]
next: [53, 696]
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "unit": 5, "count": 1, "text_key": "Quest_QuickText_51_0"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_51_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 2000000, "shown": 1818182}
  - {"type": 1, "what": "item", "item": 7002, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 7012, "count": 1, "pick": "choose"}
offer_talk: 907
complete_talk: 909
---
<!-- generated:start -->
<!-- generated-keys: title=79c38d type=eb5b2b id=b7eb6c sources=2b5675 name_key=a35645 kind=b6589f kind_name=b3f808 giver=58f603 turn_in=58f603 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=008451 requires_bit=114d4e prev=d59264 next=5be15f stages=a80fa1 objectives=432e82 rewards=b1b0e8 offer_talk=bd7c80 complete_talk=ed665f -->
|  |  |
|---|---|
|  | ![War - Winning means](../assets/npcs/208.png) |
| **Quest id** | `51` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/208-bell-thain\|Bell Thain]] |
| **Turn in** | [[wiki/npcs/208-bell-thain\|Bell Thain]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 127 |
| **Requires bit** | 126 |

### Chain

- **After:** [[wiki/quests/50-war-winning-means|War - Winning means]]
- **Next:** [[wiki/quests/53-safety-factor-management|Safety factor Management]], [[wiki/quests/696-occupation-of-monster-invasion-area|Occupation of Monster Invasion Area]]

### Objectives

1. Kill Warrior (Male) × 1 — tracker: “Destroy Nexus of enemy (0/1)”
2. Report (tracker line; done by turning the quest in) — tracker: “Meeting Balten”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 2,000,000 exp (shown in game as 1,818,182)
- **Choose one:** [[wiki/items/7002-attack-rune|Attack Rune]] *or* [[wiki/items/7012-ability-power-rune|Ability Power Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 907)

Speaker: [[wiki/npcs/208-bell-thain|Bell Thain]]

> **Bell Thain:** Have not you gone to war yet? Let's go quickly!  
> *(accept / continue)*

#### Completion (QuestTalk 909)

Speaker: [[wiki/npcs/208-bell-thain|Bell Thain]]

> **Bell Thain:** Did you learn well? Could you go ahead and try it?  
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
