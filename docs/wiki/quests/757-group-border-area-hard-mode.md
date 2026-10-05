---
title: "Group - Border Area Hard Mode"
type: "quest"
id: 757
status: "complete"
missing: []
sources: ["client: Quest.cdb id 757", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 749", "client: QuestTalk.cdb id 750"]
name_key: "Quest_Title_750"
kind: 1
kind_name: "Sub"
level: {"min": 24}
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 105
requires_bit: 104
prev: [756]
next: [1023]
prerequisites:
  - {"type": 4, "what": "level", "min": 24}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 123, "maps": [123, 123, 123], "text_key": "Quest_QuickText_750_0"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10016, "units": [675, 710, 711], "count": 1, "maps": [123, 123, 123], "text_key": "Quest_QuickText_750_1"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1800000, "shown": 1500000}
  - {"type": 1, "what": "item", "item": 688, "count": 6, "pick": "fixed"}
offer_talk: 749
complete_talk: 750
---
<!-- generated:start -->
<!-- generated-keys: title=e203c4 type=eb5b2b id=d64ce8 sources=b1297a name_key=308d4f kind=356a19 kind_name=0bac50 level=a3b082 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=e114c4 requires_bit=78a8ef prev=52a532 next=634124 prerequisites=0ab6f2 stages=30caa7 objectives=cd9584 rewards=08b487 offer_talk=01055f complete_talk=404c73 -->
|  |  |
|---|---|
|  | ![Group - Border Area Hard Mode](../assets/npcs/200.png) |
| **Quest id** | `757` |
| **Kind** | Sub (kind 1) |
| **Level** | 24+ |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 105 |
| **Requires bit** | 104 |

### Chain

- **After:** [[wiki/quests/756-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** [[wiki/quests/1023-swamps-of-the-snake-warrior-boss-hunting|Swamps of the Snake Warrior : Boss Hunting]]

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 24+ |

### Objectives

1. Go to [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123) — tracker: “Go to the Swamps of the Snake Warrior” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
2. Kill any unit of kill group 10016 ([[wiki/monsters/675-slayer-komodo|Slayer Komodo]], [[wiki/monsters/710-chepa-warrior-officer|Chepa Warrior Officer]], [[wiki/monsters/711-chepa-archer-officer|Chepa Archer Officer]]) × 1 — tracker: “Kill Slayer Komodo (0/1)” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
3. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

- **Basic reward:** 1,800,000 exp (shown in game as 1,500,000); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 6

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
