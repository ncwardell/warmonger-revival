---
title: "Ghost Fortress : Boss Hunting"
type: "quest"
id: 1029
status: "partial"
missing: ["giver"]
sources: ["client: Quest.cdb id 1029", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 749", "client: QuestTalk.cdb id 750"]
name_key: "Quest_Title_1029"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 200}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 107
prev: [759]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 200, "talk": 749, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_FREYA"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 124, "maps": [124, 124, 124], "text_key": "Quest_QuickText_1029_1"}
  - {"n": 3, "type": 1, "what": "kill", "unit_group": 10017, "units": [676], "count": 1, "maps": [124, 124, 124], "text_key": "Quest_QuickText_1029_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 250000, "shown": 250000}
  - {"type": 1, "what": "item", "item": 601, "count": 60, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 60, "pick": "fixed"}
complete_talk: 750
---
<!-- generated:start -->
<!-- generated-keys: title=46631c type=eb5b2b id=685df1 sources=3896b0 name_key=7c7e1e kind=77de68 kind_name=01e781 giver=2be88c turn_in=1caac0 turn_in_maps=15f2a7 bit=b6589f requires_bit=524e05 prev=d54366 next=97d170 stages=a80fa1 objectives=504449 rewards=14f299 complete_talk=404c73 -->
|  |  |
|---|---|
| **Quest id** | `1029` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 107 |

### Chain

- **After:** [[wiki/quests/759-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Talk to [[wiki/npcs/200-freya|Freya]] (dialogue 749) — tracker: “Go to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Go to [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124) — tracker: “Go to the Ghost Fortress” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
3. Kill any unit of kill group 10017 ([[wiki/monsters/676-great-summoner-spectre|Great Summoner Spectre]]) × 1 — tracker: “Kill Great Summoner Specter (0/1)” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
4. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 250,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 60; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 60

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
