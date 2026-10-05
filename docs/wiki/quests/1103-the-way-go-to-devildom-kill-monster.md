---
title: "The Way go to devildom : Kill monster"
type: "quest"
id: 1103
status: "partial"
missing: ["giver"]
sources: ["client: Quest.cdb id 1103", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 892", "client: QuestTalk.cdb id 893"]
name_key: "Quest_Title_1103"
kind: 3
kind_name: "Free"
level: {"min": 25}
giver: null
turn_in: {"npc": 207}
turn_in_maps: [120, 120, 120]
bit: 0
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 25}
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 207, "talk": 892, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_Athan"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10033, "units": [828], "count": 50, "maps": [114, 114, 114], "text_key": "Quest_QuickText_1103_1"}
  - {"n": 3, "type": 1, "what": "kill", "unit_group": 10034, "units": [829], "count": 50, "maps": [114, 114, 114], "text_key": "Quest_QuickText_1103_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_B_Athan"}
rewards:
  - {"type": 2, "what": "exp", "amount": 100000, "shown": 100000}
  - {"type": 4, "what": "gold", "amount": 100000}
  - {"type": 1, "what": "item", "item": 601, "count": 70, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 70, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 702, "count": 5, "pick": "fixed"}
complete_talk: 893
---
<!-- generated:start -->
<!-- generated-keys: title=fe5ace type=eb5b2b id=e0837d sources=74de58 name_key=1d567a kind=77de68 kind_name=01e781 level=00652f giver=2be88c turn_in=7e080a turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 prerequisites=34d94a stages=a80fa1 objectives=52a89d rewards=62046f complete_talk=20b550 -->
|  |  |
|---|---|
| **Quest id** | `1103` |
| **Kind** | Free (kind 3) |
| **Level** | 25+ |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/207-athan\|Athan]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 25+ |

### Objectives

1. Talk to [[wiki/npcs/207-athan|Athan]] (dialogue 892) — tracker: “Go to Athan” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Kill any unit of kill group 10033 ([[wiki/monsters/828-fragile-demon-hunter|Fragile Demon Hunter]]) × 50 — tracker: “Fragile Kill the Demon Hunter (0/50)” — on [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]] (114)
3. Kill any unit of kill group 10034 ([[wiki/monsters/829-fragile-elite-demon-hunter|Fragile Elite Demon Hunter]]) × 50 — tracker: “Fragile Kill the Elite Demon Hunter (0/50)” — on [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]] (114)
4. Report (tracker line; done by turning the quest in) — tracker: “Return to Athan” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 100,000 exp; 100,000 gold; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 70; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 70; [[wiki/items/702-crystal-red|Crystal : Red]] × 5

### Dialogue

#### Objective 1 (QuestTalk 892)

Speaker: [[wiki/npcs/207-athan|Athan]]

> **Athan:** You! Do not you need a Passion? I will give you Passion if you take my favor! Can you do it?  
> *(accept / continue)*

#### Completion (QuestTalk 893)

Speaker: [[wiki/npcs/207-athan|Athan]]

> **Athan:** You! That's what you wanted! I'll do it again next time!  
> *(accept / continue)*
<!-- generated:end -->

## Notes

Repeatable ("Free") quest. The WM 0110 patch moved repeatable quests to a "Free Quests" tab on the quest board, and WM 0124 removed that tab again ([[gameplay/patch-history]]). *patch notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/patch-history]]

## Open questions

The client names no giver for this row. Whether it was offered from the quest board or by the NPC of its first "talk" step is not known ([[gameplay/patch-history]] 0110/0124).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
