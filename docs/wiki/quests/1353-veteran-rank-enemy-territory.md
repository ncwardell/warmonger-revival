---
title: "[Veteran Rank] Enemy territory"
type: "quest"
id: 1353
status: "stub"
missing: ["objectives", "rewards"]
sources: ["client: Quest.cdb id 1353", "client: NoticeQuest.cdb id 51", "client: QuestTalk.cdb id 720", "client: QuestTalk.cdb id 915"]
name_key: "Quest_Title_1353"
kind: 6
kind_name: "War"
giver: {"board": 51}
turn_in: {"npc": 200}
turn_in_maps: [120, 120, 120]
bit: 0
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "a": 30}
stages: [1, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 4, "what": "talk", "npc": 200, "talk": 915, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_FREYA"}
  - {"n": 2, "type": 15, "what": null, "a": 2, "b": 3, "text_key": "Quest_QuickText_1353_1"}
  - {"n": 5, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards: null
rewards_client:
  - {"type": 1, "what": "item", "item": 601, "count": 80, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 611, "count": 40, "pick": "choose"}
  - {"type": 5, "what": null, "a": 500}
  - {"type": 2, "what": "exp", "amount": 20000}
complete_talk: 720
board:
  - {"row": 51, "tab": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=a146c7 type=eb5b2b id=301f83 sources=7121fd name_key=376d6a kind=c1dfd9 kind_name=5432ef giver=8f4acc turn_in=1caac0 turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 prerequisites=6ffc47 stages=a80fa1 objectives=2be88c objectives_client=06c548 rewards=2be88c rewards_client=e0ce37 complete_talk=aeaa8a board=5184c7 -->
|  |  |
|---|---|
| **Quest id** | `1353` |
| **Kind** | War (kind 6) |
| **Giver** | quest board (NoticeQuest row 51) |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Quest board** | row 51, War tab |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level ?+ (a = 30, meaning unknown) |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Talk to [[wiki/npcs/200-freya|Freya]] (dialogue 915) — tracker: “Go to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Type 15 — monster-area war / occupation?; values a=2, b=3 — tracker: “Conquer Enemy's territory”
5. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

> [!warning] Not all reward types are decoded
> The rows below are the client's (`rewards_client`). Write the server-ready list into `rewards:` once the unclear ones are understood.

- **Basic reward:** 20,000 exp
- **Choose one:** [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 80 *or* [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 40
- Type 5 — fame?; values a=500

### Dialogue

#### Objective 1 (QuestTalk 915)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** I will be waiting for you to perform the mission well!  
> *(accept / continue)*

#### Completion (QuestTalk 720)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Wonderful, you made it, you can start the next one whenever you like.  
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
