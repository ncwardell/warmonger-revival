---
title: "Gathering plant and ore"
type: "quest"
id: 734
status: "complete"
missing: []
sources: ["client: Quest.cdb id 734", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 706", "client: QuestTalk.cdb id 707"]
name_key: "Quest_Title_682"
kind: 1
kind_name: "Sub"
level: {"min": 24, "max": 26}
giver: {"npc": 213}
turn_in: {"npc": 213}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 50
requires_bit: 15
owned_field: 123
prev: [16]
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 24, "max": 26}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 8, "what": "gather", "item": 816, "count": 4, "maps": [123, 123, 123], "text_key": "Quest_QuickText_682_1"}
  - {"n": 2, "type": 8, "what": "gather", "item": 826, "count": 4, "maps": [123, 123, 123], "text_key": "Quest_QuickText_682_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_B_ODIN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 25000, "shown": 20833}
  - {"type": 1, "what": "item", "item": 601, "count": 15, "pick": "fixed"}
offer_talk: 706
complete_talk: 707
---
<!-- generated:start -->
<!-- generated-keys: title=ab9ee6 type=eb5b2b id=6229d3 sources=927107 name_key=ad202d kind=356a19 kind_name=0bac50 level=b8f85a giver=91ad7d turn_in=91ad7d offer_maps=15f2a7 turn_in_maps=15f2a7 bit=e1822d requires_bit=f1abd6 owned_field=40bd00 prev=504845 next=97d170 prerequisites=bb0be2 stages=30caa7 objectives=0205db rewards=62c9f8 offer_talk=de9a90 complete_talk=2a8ae2 -->
|  |  |
|---|---|
|  | ![Gathering plant and ore](wiki/assets/npcs/213.png) |
| **Quest id** | `734` |
| **Kind** | Sub (kind 1) |
| **Level** | 24–26 |
| **Giver** | [[wiki/npcs/213-odin\|Odin]] |
| **Turn in** | [[wiki/npcs/213-odin\|Odin]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 50 |
| **Requires bit** | 15 |
| **Field c7@10** | [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior\|(Lv 4) Swamps of Snake Warrior]] (123) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/16-farrell-s-request|Farrell's Request]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 24–26 |

### Objectives

1. Gather [[wiki/items/816-onyx|Onyx]] × 4 — tracker: “Gather Onyx (0/4)” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
2. Gather [[wiki/items/826-borage|Borage]] × 4 — tracker: “Gather Borage (0/4)” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Odin”

### Rewards

- **Basic reward:** 25,000 exp (shown in game as 20,833); [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 15

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 706)

Speaker: [[wiki/npcs/213-odin|Odin]]

> **Odin:** A fierce war is on the horizon, so  I lack all sorts of materials. Can you help me out?  
> *(accept / continue)*

#### Completion (QuestTalk 707)

Speaker: [[wiki/npcs/213-odin|Odin]]

> **Odin:** Do you have the materials I asked for?  
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
