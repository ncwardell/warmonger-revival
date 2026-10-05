---
title: "Gathering plant and ore"
type: "quest"
id: 730
status: "complete"
missing: []
sources: ["client: Quest.cdb id 730", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 700", "client: QuestTalk.cdb id 701"]
name_key: "Quest_Title_679"
kind: 1
kind_name: "Sub"
level: {"min": 23, "max": 25}
giver: {"npc": 213}
turn_in: {"npc": 213}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 49
requires_bit: 22
owned_field: 122
prev: [22]
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 23, "max": 25}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 8, "what": "gather", "item": 814, "count": 2, "maps": [122, 122, 122], "text_key": "Quest_QuickText_679_1"}
  - {"n": 2, "type": 8, "what": "gather", "item": 822, "count": 2, "maps": [122, 122, 122], "text_key": "Quest_QuickText_679_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_B_ODIN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 20000, "shown": 16667}
  - {"type": 1, "what": "item", "item": 601, "count": 15, "pick": "fixed"}
offer_talk: 700
complete_talk: 701
---
<!-- generated:start -->
<!-- generated-keys: title=ab9ee6 type=eb5b2b id=16a9ef sources=ba9fdf name_key=1b3e9c kind=356a19 kind_name=0bac50 level=8b9af7 giver=91ad7d turn_in=91ad7d offer_maps=15f2a7 turn_in_maps=15f2a7 bit=2e01e1 requires_bit=12c6fc owned_field=05a8ea prev=5c6c1d next=97d170 prerequisites=8a4922 stages=30caa7 objectives=c805d0 rewards=502c72 offer_talk=d8e4bb complete_talk=917098 -->
|  |  |
|---|---|
|  | ![Gathering plant and ore](../assets/npcs/213.png) |
| **Quest id** | `730` |
| **Kind** | Sub (kind 1) |
| **Level** | 23–25 |
| **Giver** | [[wiki/npcs/213-odin\|Odin]] |
| **Turn in** | [[wiki/npcs/213-odin\|Odin]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 49 |
| **Requires bit** | 22 |
| **Field c7@10** | [[wiki/dungeons/122-lv-3-tsunami-lake\|(Lv 3) Tsunami Lake]] (122) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 23–25 |

### Objectives

1. Gather [[wiki/items/814-topaz|Topaz]] × 2 — tracker: “Gather Topaz (0/2)” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
2. Gather [[wiki/items/822-rosemary|Rosemary]] × 2 — tracker: “Gather Rosemary (0/2)” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Odin”

### Rewards

- **Basic reward:** 20,000 exp (shown in game as 16,667); [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 15

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 700)

Speaker: [[wiki/npcs/213-odin|Odin]]

> **Odin:** A fierce war is raging on the horizon, so I lack all sorts of materials. Can you help me out?  
> *(accept / continue)*

#### Completion (QuestTalk 701)

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
