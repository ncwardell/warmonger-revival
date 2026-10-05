---
title: "Group - Border Area Hard Mode"
type: "quest"
id: 759
status: "complete"
missing: []
sources: ["client: Quest.cdb id 759", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 749", "client: QuestTalk.cdb id 750"]
name_key: "Quest_Title_752"
kind: 1
kind_name: "Sub"
level: {"min": 24}
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 107
requires_bit: 67
prev: [762]
next: [758, 1029]
prerequisites:
  - {"type": 4, "what": "level", "min": 24}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 124, "maps": [124, 124, 124], "text_key": "Quest_QuickText_752_0"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10017, "units": [676], "count": 1, "maps": [124, 124, 124], "text_key": "Quest_QuickText_752_1"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 2000000, "shown": 1666667}
  - {"type": 1, "what": "item", "item": 688, "count": 8, "pick": "fixed"}
offer_talk: 749
complete_talk: 750
---
<!-- generated:start -->
<!-- generated-keys: title=e203c4 type=eb5b2b id=dcdee6 sources=90fece name_key=49a481 kind=356a19 kind_name=0bac50 level=a3b082 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=524e05 requires_bit=4d89d2 prev=f425d7 next=6cebaf prerequisites=0ab6f2 stages=30caa7 objectives=ab665d rewards=ba725a offer_talk=01055f complete_talk=404c73 -->
|  |  |
|---|---|
|  | ![Group - Border Area Hard Mode](wiki/assets/npcs/200.png) |
| **Quest id** | `759` |
| **Kind** | Sub (kind 1) |
| **Level** | 24+ |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 107 |
| **Requires bit** | 67 |

### Chain

- **After:** [[wiki/quests/762-killed-boss-of-border-area-no-2|killed boss of Border area No.2]]
- **Next:** [[wiki/quests/758-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/1029-ghost-fortress-boss-hunting|Ghost Fortress : Boss Hunting]]

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 24+ |

### Objectives

1. Go to [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124) — tracker: “Go to the Ghost Fortress” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
2. Kill any unit of kill group 10017 ([[wiki/monsters/676-great-summoner-spectre|Great Summoner Spectre]]) × 1 — tracker: “Kill Great Summoner Specter (0/1)” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
3. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

- **Basic reward:** 2,000,000 exp (shown in game as 1,666,667); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 8

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 749)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** The monster king lives in the border area. Can you go and kill him?  
> *(accept / continue)*

#### Completion (QuestTalk 750)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Thank you so much.<br>The village is safe again.  
> *(accept / continue)*

### Mentioned in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]]
- [[gameplay/progression-and-economy|Progression and economy]]
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
