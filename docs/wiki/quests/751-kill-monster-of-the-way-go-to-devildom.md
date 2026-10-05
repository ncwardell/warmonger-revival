---
title: "Kill monster of The way go to devildom"
type: "quest"
id: 751
status: "complete"
missing: []
sources: ["client: Quest.cdb id 751", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 893", "notes: [[gameplay/patch-history]] 0329 (three repeatable Abyss quests at Athan; matching them to 749-751, which Athan turns in, is *inferred*)"]
manual: ["giver"]
name_key: "Quest_Title_664"
kind: 3
kind_name: "Free"
level: {"min": 25, "max": 29}
giver: {"npc": 207}
turn_in: {"npc": 207}
turn_in_maps: [120, 120, 120]
bit: 0
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 25, "max": 29}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "unit_group": 10033, "units": [828], "count": 50, "maps": [114, 114, 114], "text_key": "Quest_QuickText_664_1"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10034, "units": [829], "count": 50, "maps": [114, 114, 114], "text_key": "Quest_QuickText_664_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_725_0"}
rewards:
  - {"type": 2, "what": "exp", "amount": 100000, "shown": 100000}
  - {"type": 4, "what": "gold", "amount": 100000}
  - {"type": 1, "what": "item", "item": 601, "count": 70, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 70, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 702, "count": 5, "pick": "fixed"}
complete_talk: 893
---
<!-- generated:start -->
<!-- generated-keys: title=da9596 type=eb5b2b id=758a25 sources=217702 name_key=e9a54b kind=77de68 kind_name=01e781 level=23bb23 turn_in=7e080a turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 prerequisites=66acc7 stages=30caa7 objectives=6fe6bb rewards=62046f complete_talk=20b550 -->
|  |  |
|---|---|
|  | ![Kill monster of The way go to devildom](wiki/assets/npcs/207.png) |
| **Quest id** | `751` |
| **Kind** | Free (kind 3) |
| **Level** | 25–29 |
| **Giver** | [[wiki/npcs/207-athan\|Athan]] |
| **Turn in** | [[wiki/npcs/207-athan\|Athan]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 25–29 |

### Objectives

1. Kill any unit of kill group 10033 ([[wiki/monsters/828-fragile-demon-hunter|Fragile Demon Hunter]]) × 50 — tracker: “Fragile Kill the Demon Hunter (0/50)” — on [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]] (114)
2. Kill any unit of kill group 10034 ([[wiki/monsters/829-fragile-elite-demon-hunter|Fragile Elite Demon Hunter]]) × 50 — tracker: “Fragile Kill the Elite Demon Hunter (0/50)” — on [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]] (114)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Athan” — on [[wiki/fields/120-fortress|Fortress]] (120)

### Rewards

- **Basic reward:** 100,000 exp; 100,000 gold; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 70; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 70; [[wiki/items/702-crystal-red|Crystal : Red]] × 5

### Dialogue

#### Completion (QuestTalk 893)

Speaker: [[wiki/npcs/207-athan|Athan]]

> **Athan:** You! That's what you wanted! I'll do it again next time!  
> *(accept / continue)*
<!-- generated:end -->

## Notes

The WM 0329 patch added three repeatable Abyss quests at Athan ([[gameplay/patch-history]]); with 749 and 750 (seen in video) this is the third, for The way go to devildom. Not seen in a video. *patch notes + inferred*

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
