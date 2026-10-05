---
title: "Group - Border Area Hard Mode"
type: "quest"
id: 758
status: "complete"
missing: []
sources: ["client: Quest.cdb id 758", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 749", "client: QuestTalk.cdb id 750"]
name_key: "Quest_Title_751"
kind: 1
kind_name: "Sub"
level: {"min": 24}
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 106
requires_bit: 107
prev: [759]
next: [760, 1034]
prerequisites:
  - {"type": 4, "what": "level", "min": 24}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 125, "maps": [125, 125, 125], "text_key": "Quest_QuickText_751_0"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10019, "units": [677], "count": 1, "maps": [125, 125, 125], "text_key": "Quest_QuickText_751_1"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 2000000, "shown": 1666667}
  - {"type": 1, "what": "item", "item": 688, "count": 7, "pick": "fixed"}
offer_talk: 749
complete_talk: 750
---
<!-- generated:start -->
<!-- generated-keys: title=e203c4 type=eb5b2b id=82a506 sources=5ec16a name_key=0eab34 kind=356a19 kind_name=0bac50 level=a3b082 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=7224f9 requires_bit=524e05 prev=d54366 next=c7f087 prerequisites=0ab6f2 stages=30caa7 objectives=8e9725 rewards=492b75 offer_talk=01055f complete_talk=404c73 -->
|  |  |
|---|---|
|  | ![Group - Border Area Hard Mode](../assets/npcs/200.png) |
| **Quest id** | `758` |
| **Kind** | Sub (kind 1) |
| **Level** | 24+ |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 106 |
| **Requires bit** | 107 |

### Chain

- **After:** [[wiki/quests/759-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** [[wiki/quests/760-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/1034-tow-canyon-boss-hunting|Tow Canyon : Boss Hunting]]

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 24+ |

### Objectives

1. Go to [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125) — tracker: “Go to the Tow Canyon” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)
2. Kill any unit of kill group 10019 ([[wiki/monsters/677-war-chief-garon|War Chief Garon]]) × 1 — tracker: “Kill War Chief Garon (0/1)” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)
3. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

- **Basic reward:** 2,000,000 exp (shown in game as 1,666,667); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 7

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

A guide screenshot names the chain "Group – Border Area Hard Mode": go to a dungeon, kill its boss, talk to Freya ([[gameplay/progression-and-economy]] §1, *image*).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/progression-and-economy]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
