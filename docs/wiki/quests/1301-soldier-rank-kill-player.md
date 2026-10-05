---
title: "[Soldier Rank] Kill Player"
type: "quest"
id: 1301
status: "stub"
missing: ["objectives", "rewards"]
sources: ["client: Quest.cdb id 1301", "client: NoticeQuest.cdb id 45", "client: QuestTalk.cdb id 720", "client: QuestTalk.cdb id 915"]
name_key: "Quest_Title_1301"
kind: 6
kind_name: "War"
giver: {"board": 45}
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
  - {"n": 2, "type": 2, "what": null, "a": 5, "b": 10, "text_key": "Quest_QuickText_1301_1"}
  - {"n": 5, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards: null
rewards_client:
  - {"type": 1, "what": "item", "item": 887, "count": 25, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 891, "count": 25, "pick": "choose"}
  - {"type": 5, "what": null, "a": 200}
  - {"type": 2, "what": "exp", "amount": 10000}
complete_talk: 720
board:
  - {"row": 45, "tab": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=e30b09 type=eb5b2b id=055550 sources=eeb326 name_key=308b99 kind=c1dfd9 kind_name=5432ef giver=88ee98 turn_in=1caac0 turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 prerequisites=6ffc47 stages=a80fa1 objectives=2be88c objectives_client=dbf1f4 rewards=2be88c rewards_client=caa2b6 complete_talk=aeaa8a board=bfa3e3 -->
|  |  |
|---|---|
| **Quest id** | `1301` |
| **Kind** | War (kind 6) |
| **Giver** | quest board (NoticeQuest row 45) |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Quest board** | row 45, War tab |

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
2. Type 2 — kill enemy players?; values a=5, b=10 — tracker: “Destroy the enemy player from the Gaia field”
5. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

> [!warning] Not all reward types are decoded
> The rows below are the client's (`rewards_client`). Write the server-ready list into `rewards:` once the unclear ones are understood.

- **Basic reward:** 10,000 exp
- **Choose one:** [[wiki/items/887-potion-of-health-a|Potion of Health (A)]] × 25 *or* [[wiki/items/891-potion-of-mana-a|Potion of Mana (A)]] × 25
- Type 5 — fame?; values a=200

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
