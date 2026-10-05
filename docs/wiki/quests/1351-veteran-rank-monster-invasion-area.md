---
title: "[Veteran Rank] Monster Invasion Area"
type: "quest"
id: 1351
status: "stub"
missing: ["objectives", "rewards"]
sources: ["client: Quest.cdb id 1351", "client: NoticeQuest.cdb id 49", "client: QuestTalk.cdb id 720", "client: QuestTalk.cdb id 915"]
name_key: "Quest_Title_1351"
kind: 6
kind_name: "War"
giver: {"board": 49}
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
  - {"n": 2, "type": 15, "what": null, "a": 4, "b": 3, "text_key": "Quest_QuickText_1351_1"}
  - {"n": 5, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards: null
rewards_client:
  - {"type": 1, "what": "item", "item": 601, "count": 80, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 611, "count": 40, "pick": "choose"}
  - {"type": 5, "what": null, "a": 300}
  - {"type": 2, "what": "exp", "amount": 20000}
complete_talk: 720
board:
  - {"row": 49, "tab": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=6e1a28 type=eb5b2b id=0311e1 sources=b093bc name_key=0415dc kind=c1dfd9 kind_name=5432ef giver=bfafc9 turn_in=1caac0 turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 prerequisites=6ffc47 stages=a80fa1 objectives=2be88c objectives_client=af7e17 rewards=2be88c rewards_client=488115 complete_talk=aeaa8a board=51c42d -->
|  |  |
|---|---|
| **Quest id** | `1351` |
| **Kind** | War (kind 6) |
| **Giver** | quest board (NoticeQuest row 49) |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Quest board** | row 49, War tab |

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
2. Type 15 — monster-area war / occupation?; values a=4, b=3 — tracker: “Occupation of Monster Invasion Area”
5. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

> [!warning] Not all reward types are decoded
> The rows below are the client's (`rewards_client`). Write the server-ready list into `rewards:` once the unclear ones are understood.

- **Basic reward:** 20,000 exp
- **Choose one:** [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 80 *or* [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 40
- Type 5 — fame?; values a=300

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
