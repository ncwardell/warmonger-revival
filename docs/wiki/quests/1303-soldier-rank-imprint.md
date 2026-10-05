---
title: "[Soldier Rank] Imprint"
type: "quest"
id: 1303
status: "stub"
missing: ["objectives", "rewards"]
sources: ["client: Quest.cdb id 1303", "client: NoticeQuest.cdb id 47", "client: QuestTalk.cdb id 720", "client: QuestTalk.cdb id 915"]
name_key: "Quest_Title_1303"
kind: 6
kind_name: "War"
giver: {"board": 47}
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
  - {"n": 2, "type": 31, "what": null, "a": 3, "b": 5, "text_key": "Quest_QuickText_1303_1"}
  - {"n": 5, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards: null
rewards_client:
  - {"type": 1, "what": "item", "item": 601, "count": 50, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 611, "count": 30, "pick": "choose"}
  - {"type": 5, "what": null, "a": 100}
  - {"type": 2, "what": "exp", "amount": 10000}
complete_talk: 720
board:
  - {"row": 47, "tab": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=6e9e55 type=eb5b2b id=3fc863 sources=5d97e5 name_key=ce0da1 kind=c1dfd9 kind_name=5432ef giver=12a96c turn_in=1caac0 turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 prerequisites=6ffc47 stages=a80fa1 objectives=2be88c objectives_client=944d62 rewards=2be88c rewards_client=420d28 complete_talk=aeaa8a board=5f3df0 -->
|  |  |
|---|---|
| **Quest id** | `1303` |
| **Kind** | War (kind 6) |
| **Giver** | quest board (NoticeQuest row 47) |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Quest board** | row 47, War tab |

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
2. Type 31 — imprint?; values a=3, b=5 — tracker: “Monster area imprint”
5. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

> [!warning] Not all reward types are decoded
> The rows below are the client's (`rewards_client`). Write the server-ready list into `rewards:` once the unclear ones are understood.

- **Basic reward:** 10,000 exp
- **Choose one:** [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 50 *or* [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30
- Type 5 — fame?; values a=100

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
