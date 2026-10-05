---
title: "Ore and plant collection"
type: "quest"
id: 748
status: "complete"
missing: []
sources: ["client: Quest.cdb id 748", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 831", "client: QuestTalk.cdb id 832"]
name_key: "Quest_Title_770"
kind: 1
kind_name: "Sub"
level: {"min": 28}
giver: {"npc": 210}
turn_in: {"npc": 210}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 110
requires_bit: 31
owned_field: 129
prev: [35]
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 28}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 8, "what": "gather", "item": 806, "count": 4, "maps": [129, 129, 129], "text_key": "Quest_QuickText_770_1"}
  - {"n": 2, "type": 8, "what": "gather", "item": 822, "count": 4, "maps": [129, 129, 129], "text_key": "Quest_QuickText_770_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_650_3"}
rewards:
  - {"type": 2, "what": "exp", "amount": 45000, "shown": 37500}
  - {"type": 1, "what": "item", "item": 611, "count": 50, "pick": "fixed"}
offer_talk: 831
complete_talk: 832
---
<!-- generated:start -->
<!-- generated-keys: title=01010c type=eb5b2b id=6d40f9 sources=a6fa2c name_key=1babef kind=356a19 kind_name=0bac50 level=84a59c giver=7abdb8 turn_in=7abdb8 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=5e796e requires_bit=632667 owned_field=8b7471 prev=5c3c3a next=97d170 prerequisites=c3110a stages=30caa7 objectives=d7ff93 rewards=9bea34 offer_talk=3741d5 complete_talk=e6c790 -->
|  |  |
|---|---|
|  | ![Ore and plant collection](../assets/npcs/210.png) |
| **Quest id** | `748` |
| **Kind** | Sub (kind 1) |
| **Level** | 28+ |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 110 |
| **Requires bit** | 31 |
| **Field c7@10** | [[wiki/dungeons/129-lv-8-thorn-s-hell\|(Lv 8) Thorn's Hell]] (129) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/35-demon-hell|Demon Hell]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 28+ |

### Objectives

1. Gather [[wiki/items/806-emerald|Emerald]] × 4 — tracker: “Collect Emeralds (0/4)” — on [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] (129)
2. Gather [[wiki/items/822-rosemary|Rosemary]] × 4 — tracker: “Collect Rosemaries (0/4)” — on [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] (129)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Kesley”

### Rewards

- **Basic reward:** 45,000 exp (shown in game as 37,500); [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 50

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 831)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** It's very hard to get material for Gears during a war. Would you please get me some?  
> *(accept / continue)*

#### Completion (QuestTalk 832)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** Thank you very much for your wonderful material. See you next time!  
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
