---
title: "Swamps of the Snake Warrior : Boss Hunting"
type: "quest"
id: 1023
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1023", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 749", "client: QuestTalk.cdb id 750"]
name_key: "Quest_Title_1023"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 200}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 105
prev: [757]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 200, "talk": 749, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_FREYA"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 123, "maps": [123, 123, 123], "text_key": "Quest_QuickText_1023_1"}
  - {"n": 3, "type": 1, "what": "kill", "unit_group": 10016, "units": [675, 710, 711], "count": 1, "maps": [123, 123, 123], "text_key": "Quest_QuickText_1023_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 200000, "shown": 200000}
  - {"type": 1, "what": "item", "item": 601, "count": 50, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 50, "pick": "fixed"}
complete_talk: 750
---
<!-- generated:start -->
<!-- generated-keys: title=05586a type=eb5b2b id=138825 sources=34fde6 name_key=ad35de kind=77de68 kind_name=01e781 giver=2be88c turn_in=1caac0 turn_in_maps=15f2a7 bit=b6589f requires_bit=e114c4 prev=bc8ba7 next=97d170 stages=a80fa1 objectives=d3ffe3 rewards=99c628 complete_talk=404c73 -->
|  |  |
|---|---|
| **Quest id** | `1023` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 105 |

### Chain

- **After:** [[wiki/quests/757-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Talk to [[wiki/npcs/200-freya|Freya]] (dialogue 749) — tracker: “Go to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Go to [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123) — tracker: “Go to the Swamps of the Snake Warrior” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
3. Kill any unit of kill group 10016 ([[wiki/monsters/675-slayer-komodo|Slayer Komodo]], [[wiki/monsters/710-chepa-warrior-officer|Chepa Warrior Officer]], [[wiki/monsters/711-chepa-archer-officer|Chepa Archer Officer]]) × 1 — tracker: “Kill Slayer Komodo (0/1)” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
4. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 200,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 50; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 50

### Dialogue

#### Objective 1 (QuestTalk 749)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** The monster king lives in the border area. Can you go and kill him?  
> *(accept / continue)*

#### Completion (QuestTalk 750)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Thank you so much.<br>The village is safe again.  
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
