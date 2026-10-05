---
title: "Gathering plant and ore"
type: "quest"
id: 742
status: "complete"
missing: []
sources: ["client: Quest.cdb id 742", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 761", "client: QuestTalk.cdb id 762"]
name_key: "Quest_Title_759"
kind: 1
kind_name: "Sub"
level: {"min": 26}
giver: {"npc": 214}
turn_in: {"npc": 214}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 119
requires_bit: 29
owned_field: 125
prev: [33]
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 26}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 8, "what": "gather", "item": 806, "count": 4, "maps": [125, 125, 125], "text_key": "Quest_QuickText_759_1"}
  - {"n": 2, "type": 8, "what": "gather", "item": 822, "count": 4, "maps": [125, 125, 125], "text_key": "Quest_QuickText_759_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 35000, "shown": 29167}
  - {"type": 1, "what": "item", "item": 601, "count": 30, "pick": "fixed"}
offer_talk: 761
complete_talk: 762
---
<!-- generated:start -->
<!-- generated-keys: title=ab9ee6 type=eb5b2b id=02c8be sources=d0aeff name_key=33d210 kind=356a19 kind_name=0bac50 level=ee62c8 giver=fb5a8b turn_in=fb5a8b offer_maps=15f2a7 turn_in_maps=15f2a7 bit=a2e33d requires_bit=7719a1 owned_field=0ca927 prev=78415f next=97d170 prerequisites=2913e2 stages=30caa7 objectives=f2948f rewards=337ff2 offer_talk=8d1218 complete_talk=c99a2a -->
|  |  |
|---|---|
|  | ![Gathering plant and ore](../assets/npcs/214.png) |
| **Quest id** | `742` |
| **Kind** | Sub (kind 1) |
| **Level** | 26+ |
| **Giver** | [[wiki/npcs/214-owen\|Owen]] |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 119 |
| **Requires bit** | 29 |
| **Field c7@10** | [[wiki/dungeons/125-lv-5-tow-canyon\|(Lv 5) Tow Canyon]] (125) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/33-ghost-fortress|Ghost Fortress]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 26+ |

### Objectives

1. Gather [[wiki/items/806-emerald|Emerald]] × 4 — tracker: “Gathering Emerald (0/4)” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)
2. Gather [[wiki/items/822-rosemary|Rosemary]] × 4 — tracker: “Gathering rosemary (0/4)” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen”

### Rewards

- **Basic reward:** 35,000 exp (shown in game as 29,167); [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 30

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 761)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** The war is tough, and it's really hard to save materials. Can you help me out?  
> *(accept / continue)*

#### Completion (QuestTalk 762)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** Do you have the materials I asked for?  
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
