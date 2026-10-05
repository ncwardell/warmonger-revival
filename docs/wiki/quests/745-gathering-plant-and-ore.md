---
title: "Gathering plant and ore"
type: "quest"
id: 745
status: "complete"
missing: []
sources: ["client: Quest.cdb id 745", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 767", "client: QuestTalk.cdb id 768"]
name_key: "Quest_Title_762"
kind: 1
kind_name: "Sub"
level: {"min": 27}
giver: {"npc": 210}
turn_in: {"npc": 210}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 120
requires_bit: 30
owned_field: 126
prev: [34]
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 27}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 8, "what": "gather", "item": 810, "count": 4, "maps": [126, 126, 126], "text_key": "Quest_QuickText_762_1"}
  - {"n": 2, "type": 8, "what": "gather", "item": 828, "count": 4, "maps": [126, 126, 126], "text_key": "Quest_QuickText_762_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_650_3"}
rewards:
  - {"type": 2, "what": "exp", "amount": 40000, "shown": 33333}
  - {"type": 1, "what": "item", "item": 601, "count": 50, "pick": "fixed"}
offer_talk: 767
complete_talk: 768
---
<!-- generated:start -->
<!-- generated-keys: title=ab9ee6 type=eb5b2b id=de8627 sources=520bac name_key=296ad8 kind=356a19 kind_name=0bac50 level=8c32e3 giver=7abdb8 turn_in=7abdb8 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=775bc5 requires_bit=22d200 owned_field=114d4e prev=91a33c next=97d170 prerequisites=eb6b9f stages=30caa7 objectives=83ae2d rewards=3921a9 offer_talk=81755a complete_talk=ad2ad5 -->
|  |  |
|---|---|
|  | ![Gathering plant and ore](../assets/npcs/210.png) |
| **Quest id** | `745` |
| **Kind** | Sub (kind 1) |
| **Level** | 27+ |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 120 |
| **Requires bit** | 30 |
| **Field c7@10** | [[wiki/dungeons/126-lv-7-demon-hell\|(Lv 7) Demon Hell]] (126) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/34-tow-canyon|Tow Canyon]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 27+ |

### Objectives

1. Gather [[wiki/items/810-diamond|Diamond]] × 4 — tracker: “Gathering Diamond (0/4)” — on [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] (126)
2. Gather [[wiki/items/828-spartium|Spartium]] × 4 — tracker: “Gathering Spartium (0/4)” — on [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] (126)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Kesley”

### Rewards

- **Basic reward:** 40,000 exp (shown in game as 33,333); [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 50

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 767)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** The war is tough, and it's really hard to save materials. Can you help me out?  
> *(accept / continue)*

#### Completion (QuestTalk 768)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** Do you have the materials I asked for?  
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
