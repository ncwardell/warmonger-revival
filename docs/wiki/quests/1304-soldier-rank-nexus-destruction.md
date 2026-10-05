---
title: "[Soldier Rank] Nexus Destruction"
type: "quest"
id: 1304
status: "partial"
missing: ["rewards"]
sources: ["client: Quest.cdb id 1304", "client: NoticeQuest.cdb id 48", "client: QuestTalk.cdb id 720", "client: QuestTalk.cdb id 915"]
name_key: "Quest_Title_1304"
kind: 6
kind_name: "War"
giver: {"board": 48}
turn_in: {"npc": 200}
turn_in_maps: [120, 120, 120]
bit: 0
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "a": 30}
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 200, "talk": 915, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_FREYA"}
  - {"n": 2, "type": 1, "what": "kill", "unit": 5, "count": 3, "text_key": "Quest_QuickText_1304_1"}
  - {"n": 5, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards: null
rewards_client:
  - {"type": 1, "what": "item", "item": 601, "count": 50, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 611, "count": 30, "pick": "choose"}
  - {"type": 5, "what": null, "a": 200}
  - {"type": 2, "what": "exp", "amount": 10000}
complete_talk: 720
board:
  - {"row": 48, "tab": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=a47f38 type=eb5b2b id=eba907 sources=ada835 name_key=96d1ad kind=c1dfd9 kind_name=5432ef giver=e00f96 turn_in=1caac0 turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 prerequisites=6ffc47 stages=a80fa1 objectives=b153fb rewards=2be88c rewards_client=ceb7d8 complete_talk=aeaa8a board=c22f63 -->
|  |  |
|---|---|
| **Quest id** | `1304` |
| **Kind** | War (kind 6) |
| **Giver** | quest board (NoticeQuest row 48) |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Quest board** | row 48, War tab |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level ?+ (a = 30, meaning unknown) |

### Objectives

1. Talk to [[wiki/npcs/200-freya|Freya]] (dialogue 915) — tracker: “Go to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Kill Warrior (Male) × 3 — tracker: “Nexus Destruction from PvP (0/3)”
5. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

> [!warning] Not all reward types are decoded
> The rows below are the client's (`rewards_client`). Write the server-ready list into `rewards:` once the unclear ones are understood.

- **Basic reward:** 10,000 exp
- **Choose one:** [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 50 *or* [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30
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

The WM 0110 patch moved mission quests to a "War Quests" tab on the quest board, for level 30 and up ([[gameplay/patch-history]]). *patch notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/patch-history]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
