---
title: "Tsunami Lake : Boss Hunting"
type: "quest"
id: 1018
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1018", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 749", "client: QuestTalk.cdb id 750"]
name_key: "Quest_Title_1018"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 200}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 104
prev: [756]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 200, "talk": 749, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_FREYA"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 122, "maps": [122, 122, 122], "text_key": "Quest_QuickText_1018_1"}
  - {"n": 3, "type": 1, "what": "kill", "unit_group": 10015, "units": [674, 727, 728], "count": 1, "maps": [122, 122, 122], "text_key": "Quest_QuickText_1018_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 150000, "shown": 150000}
  - {"type": 1, "what": "item", "item": 601, "count": 50, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 50, "pick": "fixed"}
complete_talk: 750
---
<!-- generated:start -->
<!-- generated-keys: title=85bc69 type=eb5b2b id=cea8be sources=45d621 name_key=29ef87 kind=77de68 kind_name=01e781 giver=2be88c turn_in=1caac0 turn_in_maps=15f2a7 bit=b6589f requires_bit=78a8ef prev=52a532 next=97d170 stages=a80fa1 objectives=b1b953 rewards=7b44a8 complete_talk=404c73 -->
|  |  |
|---|---|
| **Quest id** | `1018` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 104 |

### Chain

- **After:** [[wiki/quests/756-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Talk to [[wiki/npcs/200-freya|Freya]] (dialogue 749) — tracker: “Go to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Go to [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122) — tracker: “Go to the Tsunami Lake” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
3. Kill any unit of kill group 10015 ([[wiki/monsters/674-tempest-fisher|Tempest Fisher]], [[wiki/monsters/727-chepa-warrior|Chepa Warrior]], [[wiki/monsters/728-chepa-archer|Chepa Archer]]) × 1 — tracker: “Kill Tempest Fisher (0/1)” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
4. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 150,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 50; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 50

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
