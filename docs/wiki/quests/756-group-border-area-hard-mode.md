---
title: "Group - Border Area Hard Mode"
type: "quest"
id: 756
status: "complete"
missing: []
sources: ["client: Quest.cdb id 756", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 749", "client: QuestTalk.cdb id 750"]
name_key: "Quest_Title_749"
kind: 1
kind_name: "Sub"
level: {"min": 24}
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 104
requires_bit: 63
prev: [761]
next: [757, 1018]
prerequisites:
  - {"type": 4, "what": "level", "min": 24}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 122, "maps": [122, 122, 122], "text_key": "Quest_QuickText_749_0"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10015, "units": [674, 727, 728], "count": 1, "maps": [122, 122, 122], "text_key": "Quest_QuickText_749_1"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1800000, "shown": 1500000}
  - {"type": 1, "what": "item", "item": 688, "count": 5, "pick": "fixed"}
offer_talk: 749
complete_talk: 750
---
<!-- generated:start -->
<!-- generated-keys: title=e203c4 type=eb5b2b id=8989f7 sources=8f5c93 name_key=d251af kind=356a19 kind_name=0bac50 level=a3b082 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=78a8ef requires_bit=a17554 prev=c94718 next=482f6c prerequisites=0ab6f2 stages=30caa7 objectives=fef666 rewards=c9d9e4 offer_talk=01055f complete_talk=404c73 -->
|  |  |
|---|---|
|  | ![Group - Border Area Hard Mode](../assets/npcs/200.png) |
| **Quest id** | `756` |
| **Kind** | Sub (kind 1) |
| **Level** | 24+ |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 104 |
| **Requires bit** | 63 |

### Chain

- **After:** [[wiki/quests/761-killed-boss-of-border-area-no-1|killed boss of Border area No.1]]
- **Next:** [[wiki/quests/757-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/1018-tsunami-lake-boss-hunting|Tsunami Lake : Boss Hunting]]

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 24+ |

### Objectives

1. Go to [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122) — tracker: “Go to the Tsunami Lake” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
2. Kill any unit of kill group 10015 ([[wiki/monsters/674-tempest-fisher|Tempest Fisher]], [[wiki/monsters/727-chepa-warrior|Chepa Warrior]], [[wiki/monsters/728-chepa-archer|Chepa Archer]]) × 1 — tracker: “Kill Tempest Fisher (0/1)” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
3. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

- **Basic reward:** 1,800,000 exp (shown in game as 1,500,000); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 5

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
