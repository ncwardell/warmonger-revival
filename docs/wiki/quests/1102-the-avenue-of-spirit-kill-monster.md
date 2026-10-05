---
title: "The Avenue of spirit : Kill monster"
type: "quest"
id: 1102
status: "partial"
missing: ["giver"]
sources: ["client: Quest.cdb id 1102", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 890", "client: QuestTalk.cdb id 891"]
name_key: "Quest_Title_1102"
kind: 3
kind_name: "Free"
level: {"min": 20}
giver: null
turn_in: {"npc": 207}
turn_in_maps: [120, 120, 120]
bit: 0
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 20}
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 207, "talk": 890, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_Athan"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10007, "units": [715, 716], "count": 50, "maps": [113, 113, 113], "text_key": "Quest_QuickText_1102_1"}
  - {"n": 3, "type": 1, "what": "kill", "unit_group": 10008, "units": [717, 718], "count": 50, "maps": [113, 113, 113], "text_key": "Quest_QuickText_1102_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_B_Athan"}
rewards:
  - {"type": 2, "what": "exp", "amount": 70000, "shown": 70000}
  - {"type": 4, "what": "gold", "amount": 70000}
  - {"type": 1, "what": "item", "item": 601, "count": 60, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 60, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 701, "count": 10, "pick": "fixed"}
complete_talk: 891
---
<!-- generated:start -->
<!-- generated-keys: title=ce9b36 type=eb5b2b id=7c9fe6 sources=d39a30 name_key=7dec1a kind=77de68 kind_name=01e781 level=c59912 giver=2be88c turn_in=7e080a turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 prerequisites=d9dcd6 stages=a80fa1 objectives=e730aa rewards=aa57c8 complete_talk=a0308a -->
|  |  |
|---|---|
| **Quest id** | `1102` |
| **Kind** | Free (kind 3) |
| **Level** | 20+ |
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
| 4 | level | level 20+ |

### Objectives

1. Talk to [[wiki/npcs/207-athan|Athan]] (dialogue 890) — tracker: “Go to Athan” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Kill any unit of kill group 10007 ([[wiki/monsters/715-fragile-black-ghost|Fragile Black Ghost]], [[wiki/monsters/716-fragile-red-ghost|Fragile Red Ghost]]) × 50 — tracker: “Fragile Kill Ghost (0/50)” — on [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] (113)
3. Kill any unit of kill group 10008 ([[wiki/monsters/717-fragile-elite-black-ghost|Fragile Elite Black Ghost]], [[wiki/monsters/718-fragile-elite-red-ghost|Fragile Elite Red Ghost]]) × 50 — tracker: “Fragile Kill Elite Ghost (0/50)” — on [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] (113)
4. Report (tracker line; done by turning the quest in) — tracker: “Return to Athan” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 70,000 exp; 70,000 gold; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 60; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 60; [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 10

### Dialogue

#### Objective 1 (QuestTalk 890)

Speaker: [[wiki/npcs/207-athan|Athan]]

> **Athan:** There are ghosts in Abyss! Can you get rid of the ghosts?  
> *(accept / continue)*

#### Completion (QuestTalk 891)

Speaker: [[wiki/npcs/207-athan|Athan]]

> **Athan:** Thank you! A case of killing ghosts!  
> *(accept / continue)*
<!-- generated:end -->

## Notes

Repeatable ("Free") quest. The WM 0110 patch moved repeatable quests to a "Free Quests" tab on the quest board, and WM 0124 removed that tab again ([[gameplay/patch-history]]). *patch notes* Shares its rewards with 750, the ghost quest Athan offered in the first-session video ([2:22:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=8550s), [[gameplay/video-early-quests]] step 17). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/patch-history]]
- [[gameplay/video-early-quests]]

## Open questions

The client names no giver for this row. Whether it was offered from the quest board or by the NPC of its first "talk" step is not known ([[gameplay/patch-history]] 0110/0124).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
