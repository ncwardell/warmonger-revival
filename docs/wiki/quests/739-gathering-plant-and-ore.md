---
title: "Gathering plant and ore"
type: "quest"
id: 739
status: "complete"
missing: []
sources: ["client: Quest.cdb id 739", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 755", "client: QuestTalk.cdb id 756"]
name_key: "Quest_Title_756"
kind: 1
kind_name: "Sub"
level: {"min": 25}
giver: {"npc": 213}
turn_in: {"npc": 213}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 116
requires_bit: 123
owned_field: 124
prev: [47]
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 25}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 8, "what": "gather", "item": 808, "count": 4, "maps": [124, 124, 124], "text_key": "Quest_QuickText_756_1"}
  - {"n": 2, "type": 8, "what": "gather", "item": 820, "count": 4, "maps": [124, 124, 124], "text_key": "Quest_QuickText_756_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_B_ODIN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 30000, "shown": 25000}
  - {"type": 1, "what": "item", "item": 611, "count": 30, "pick": "fixed"}
offer_talk: 755
complete_talk: 756
---
<!-- generated:start -->
<!-- generated-keys: title=ab9ee6 type=eb5b2b id=1c710b sources=2b7d4d name_key=635502 kind=356a19 kind_name=0bac50 level=00652f giver=91ad7d turn_in=91ad7d offer_maps=15f2a7 turn_in_maps=15f2a7 bit=683e72 requires_bit=40bd00 owned_field=f38cfe prev=80af3c next=97d170 prerequisites=34d94a stages=30caa7 objectives=dbf6b6 rewards=7fbb41 offer_talk=52342f complete_talk=8989f7 -->
|  |  |
|---|---|
|  | ![Gathering plant and ore](../assets/npcs/213.png) |
| **Quest id** | `739` |
| **Kind** | Sub (kind 1) |
| **Level** | 25+ |
| **Giver** | [[wiki/npcs/213-odin\|Odin]] |
| **Turn in** | [[wiki/npcs/213-odin\|Odin]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 116 |
| **Requires bit** | 123 |
| **Field c7@10** | [[wiki/dungeons/124-lv-6-ghost-fortress\|(Lv 6) Ghost Fortress]] (124) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/47-create-potion|Create Potion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 25+ |

### Objectives

1. Gather [[wiki/items/808-moonstone|Moonstone]] × 4 — tracker: “Gathering Moonstone (0/4)” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
2. Gather [[wiki/items/820-peppermint|Peppermint]] × 4 — tracker: “Gathering Peppermint (0/4)” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Odin”

### Rewards

- **Basic reward:** 30,000 exp (shown in game as 25,000); [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 755)

Speaker: [[wiki/npcs/213-odin|Odin]]

> **Odin:** The war is tough, and it's really hard to save materials. Can you help me out?  
> *(accept / continue)*

#### Completion (QuestTalk 756)

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
