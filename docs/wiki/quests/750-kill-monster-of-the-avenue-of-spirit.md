---
title: "Kill monster of The avenue of spirit"
type: "quest"
id: 750
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 750", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 891"]
name_key: "Quest_Title_663"
kind: 3
kind_name: "Free"
level: {"min": 20, "max": 25}
giver: null
turn_in: {"npc": 207}
turn_in_maps: [120, 120, 120]
bit: 0
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 20, "max": 25}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "unit_group": 10007, "units": [715, 716], "count": 50, "maps": [113, 113, 113], "text_key": "Quest_QuickText_663_1"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10008, "units": [717, 718], "count": 50, "maps": [113, 113, 113], "text_key": "Quest_QuickText_663_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_725_0"}
rewards:
  - {"type": 2, "what": "exp", "amount": 70000, "shown": 70000}
  - {"type": 4, "what": "gold", "amount": 70000}
  - {"type": 1, "what": "item", "item": 601, "count": 60, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 60, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 701, "count": 10, "pick": "fixed"}
complete_talk: 891
---
<!-- generated:start -->
<!-- generated-keys: title=cb9850 type=eb5b2b id=404c73 sources=d214ce name_key=37279b kind=77de68 kind_name=01e781 level=8448b1 giver=2be88c turn_in=7e080a turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 prerequisites=c08948 stages=30caa7 objectives=c4f092 rewards=aa57c8 complete_talk=a0308a -->
|  |  |
|---|---|
| **Quest id** | `750` |
| **Kind** | Free (kind 3) |
| **Level** | 20–25 |
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
| 4 | level | level 20–25 |

### Objectives

1. Kill any unit of kill group 10007 ([[wiki/monsters/715-fragile-black-ghost|Fragile Black Ghost]], [[wiki/monsters/716-fragile-red-ghost|Fragile Red Ghost]]) × 50 — tracker: “Fragile Kill Ghost (0/50)” — on [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] (113)
2. Kill any unit of kill group 10008 ([[wiki/monsters/717-fragile-elite-black-ghost|Fragile Elite Black Ghost]], [[wiki/monsters/718-fragile-elite-red-ghost|Fragile Elite Red Ghost]]) × 50 — tracker: “Fragile Kill Elite Ghost (0/50)” — on [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] (113)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Athan” — on [[wiki/fields/120-fortress|Fortress]] (120)

### Rewards

- **Basic reward:** 70,000 exp; 70,000 gold; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 60; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 60; [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 10

### Dialogue

#### Completion (QuestTalk 891)

Speaker: [[wiki/npcs/207-athan|Athan]]

> **Athan:** Thank you! A case of killing ghosts!  
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
