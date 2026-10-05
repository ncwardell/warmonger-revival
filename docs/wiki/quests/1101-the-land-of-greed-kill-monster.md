---
title: "The Land of Greed : Kill monster"
type: "quest"
id: 1101
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1101", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 888", "client: QuestTalk.cdb id 889"]
name_key: "Quest_Title_1101"
kind: 3
kind_name: "Free"
level: {"min": 15}
giver: null
turn_in: {"npc": 207}
turn_in_maps: [120, 120, 120]
bit: 0
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 15}
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 207, "talk": 888, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_Athan"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10001, "units": [721, 722], "count": 50, "maps": [108, 109, 111], "text_key": "Quest_QuickText_1101_1"}
  - {"n": 3, "type": 1, "what": "kill", "unit_group": 10002, "units": [723, 724], "count": 50, "maps": [108, 109, 111], "text_key": "Quest_QuickText_1101_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_B_Athan"}
rewards:
  - {"type": 2, "what": "exp", "amount": 50000, "shown": 50000}
  - {"type": 4, "what": "gold", "amount": 50000}
  - {"type": 1, "what": "item", "item": 601, "count": 50, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 50, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 700, "count": 20, "pick": "fixed"}
complete_talk: 889
---
<!-- generated:start -->
<!-- generated-keys: title=f8c2f9 type=eb5b2b id=551220 sources=186494 name_key=1757db kind=77de68 kind_name=01e781 level=c5cb62 giver=2be88c turn_in=7e080a turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 prerequisites=4a5c58 stages=a80fa1 objectives=5a4b0c rewards=e04a61 complete_talk=4d7adc -->
|  |  |
|---|---|
| **Quest id** | `1101` |
| **Kind** | Free (kind 3) |
| **Level** | 15+ |
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
| 4 | level | level 15+ |

### Objectives

1. Talk to [[wiki/npcs/207-athan|Athan]] (dialogue 888) — tracker: “Go to Athan” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Kill any unit of kill group 10001 ([[wiki/monsters/721-fragile-tow-warrior|Fragile Tow Warrior]], [[wiki/monsters/722-fragile-tow-sorcerer|Fragile Tow Sorcerer]]) × 50 — tracker: “Fragile Kill Tow (0/50)” — on Arslan: [[wiki/fields/108-the-land-of-greed|The land of Greed]] (108) · Erion: [[wiki/fields/109-the-land-of-greed|The land of Greed]] (109) · Armia: [[wiki/fields/111-the-land-of-greed|The land of Greed]] (111)
3. Kill any unit of kill group 10002 ([[wiki/monsters/723-fragile-elite-tow-warrior|Fragile Elite Tow Warrior]], [[wiki/monsters/724-fragile-elite-tow-sorcerer|Fragile Elite Tow Sorcerer]]) × 50 — tracker: “Fragile Kill Elite Tow (0/50)” — on Arslan: [[wiki/fields/108-the-land-of-greed|The land of Greed]] (108) · Erion: [[wiki/fields/109-the-land-of-greed|The land of Greed]] (109) · Armia: [[wiki/fields/111-the-land-of-greed|The land of Greed]] (111)
4. Report (tracker line; done by turning the quest in) — tracker: “Return to Athan” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 50,000 exp; 50,000 gold; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 50; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 50; [[wiki/items/700-crystal-blue|Crystal : Blue]] × 20

### Dialogue

#### Objective 1 (QuestTalk 888)

Speaker: [[wiki/npcs/207-athan|Athan]]

> **Athan:** Do you know the land of Abyss greed? There are tow monster there! Let me go get it!  
> *(accept / continue)*

#### Completion (QuestTalk 889)

Speaker: [[wiki/npcs/207-athan|Athan]]

> **Athan:** I'll give you this! Can you kill the tow?  
> *(accept / continue)*

### Seen in

- [[gameplay/warmonger-forum|Warmonger forum (2018)]]
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
