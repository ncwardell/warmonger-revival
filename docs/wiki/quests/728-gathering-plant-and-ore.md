---
title: "Gathering plant and ore"
type: "quest"
id: 728
status: "complete"
missing: []
sources: ["client: Quest.cdb id 728", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 696", "client: QuestTalk.cdb id 697"]
name_key: "Quest_Title_677"
kind: 1
kind_name: "Sub"
level: {"min": 21, "max": 23}
giver: {"npc": 213}
turn_in: {"npc": 213}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 48
requires_bit: 25
owned_field: 121
prev: [30, 1524]
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 21, "max": 23}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 8, "what": "gather", "item": 802, "count": 2, "maps": [121, 121, 121], "text_key": "Quest_QuickText_677_1"}
  - {"n": 2, "type": 8, "what": "gather", "item": 812, "count": 2, "maps": [121, 121, 121], "text_key": "Quest_QuickText_677_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_B_ODIN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 5000, "shown": 4167}
  - {"type": 1, "what": "item", "item": 611, "count": 15, "pick": "fixed"}
offer_talk: 696
complete_talk: 697
---
<!-- generated:start -->
<!-- generated-keys: title=ab9ee6 type=eb5b2b id=8e6b8a sources=a3effa name_key=a1ec13 kind=356a19 kind_name=0bac50 level=b6ceff giver=91ad7d turn_in=91ad7d offer_maps=15f2a7 turn_in_maps=15f2a7 bit=64e095 requires_bit=f6e112 owned_field=8bd795 prev=71a868 next=97d170 prerequisites=528705 stages=30caa7 objectives=8b4179 rewards=83e2e2 offer_talk=4c87e5 complete_talk=ff5ae4 -->
|  |  |
|---|---|
|  | ![Gathering plant and ore](wiki/assets/npcs/213.png) |
| **Quest id** | `728` |
| **Kind** | Sub (kind 1) |
| **Level** | 21–23 |
| **Giver** | [[wiki/npcs/213-odin\|Odin]] |
| **Turn in** | [[wiki/npcs/213-odin\|Odin]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 48 |
| **Requires bit** | 25 |
| **Field c7@10** | [[wiki/dungeons/121-lv-1-skull-temple\|(Lv 1) Skull Temple]] (121) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/30-chepa-village|Chepa Village]], [[wiki/quests/1524-party-party-person|Party - Party Person]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 21–23 |

### Objectives

1. Gather [[wiki/items/802-garnet|Garnet]] × 2 — tracker: “Gather Garnet (0/2)” — on [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121)
2. Gather [[wiki/items/812-red-bloodstone|Red bloodstone]] × 2 — tracker: “Gather Red Bloodstone (0/2)” — on [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Odin”

### Rewards

- **Basic reward:** 5,000 exp (shown in game as 4,167); [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 15

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 696)

Speaker: [[wiki/npcs/213-odin|Odin]]

> **Odin:** A fierce war is on the horizon, so  I lack all sorts of materials. Can you help me out?  
> *(accept / continue)*

#### Completion (QuestTalk 697)

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
