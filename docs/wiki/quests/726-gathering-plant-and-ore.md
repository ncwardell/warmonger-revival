---
title: "Gathering plant and ore"
type: "quest"
id: 726
status: "complete"
missing: []
sources: ["client: Quest.cdb id 726", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 700", "client: QuestTalk.cdb id 701"]
name_key: "Quest_Title_699"
kind: 1
kind_name: "Sub"
level: {"min": 22, "max": 24}
giver: {"npc": 213}
turn_in: {"npc": 213}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 53
requires_bit: 14
owned_field: 128
prev: [15]
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 22, "max": 24}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 8, "what": "gather", "item": 814, "count": 2, "maps": [128, 128, 128], "text_key": "Quest_QuickText_679_1"}
  - {"n": 2, "type": 8, "what": "gather", "item": 822, "count": 2, "maps": [128, 128, 128], "text_key": "Quest_QuickText_679_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_B_ODIN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 10000, "shown": 8333}
  - {"type": 1, "what": "item", "item": 611, "count": 15, "pick": "fixed"}
offer_talk: 700
complete_talk: 701
---
<!-- generated:start -->
<!-- generated-keys: title=ab9ee6 type=eb5b2b id=db667d sources=a6921b name_key=5daf71 kind=356a19 kind_name=0bac50 level=e5524e giver=91ad7d turn_in=91ad7d offer_maps=15f2a7 turn_in_maps=15f2a7 bit=c5b76d requires_bit=fa35e1 owned_field=b4182b prev=017b8e next=97d170 prerequisites=9fd8dc stages=30caa7 objectives=48b29d rewards=2e769a offer_talk=d8e4bb complete_talk=917098 -->
|  |  |
|---|---|
|  | ![Gathering plant and ore](wiki/assets/npcs/213.png) |
| **Quest id** | `726` |
| **Kind** | Sub (kind 1) |
| **Level** | 22–24 |
| **Giver** | [[wiki/npcs/213-odin\|Odin]] |
| **Turn in** | [[wiki/npcs/213-odin\|Odin]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 53 |
| **Requires bit** | 14 |
| **Field c7@10** | [[wiki/dungeons/128-lv-2-skull-cemetery\|(Lv 2) Skull Cemetery]] (128) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/15-repel-the-skeleton-invasion|Repel the Skeleton Invasion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 22–24 |

### Objectives

1. Gather [[wiki/items/814-topaz|Topaz]] × 2 — tracker: “Gather Topaz (0/2)” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
2. Gather [[wiki/items/822-rosemary|Rosemary]] × 2 — tracker: “Gather Rosemary (0/2)” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Odin”

### Rewards

- **Basic reward:** 10,000 exp (shown in game as 8,333); [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 15

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
