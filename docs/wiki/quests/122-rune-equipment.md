---
title: "Rune Equipment."
type: "quest"
id: 122
status: "complete"
missing: []
sources: ["client: Quest.cdb id 122", "client: QuestTalk.cdb id 914"]
name_key: "Quest_Title_122"
kind: 1
kind_name: "Sub"
giver: {"npc": 324}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 77
requires_bit: 11
automatic: true
prev: [12]
next: [121]
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 324, "maps": [120, 120, 120], "text_key": "Quest_QuickText_123_2"}
  - {"n": 2, "type": 10012, "what": "client_equip_rune", "text_key": "Quest_QuickText_122_1"}
rewards:
  - {"type": 1, "what": "item", "item": 7032, "count": 1, "pick": "fixed"}
offer_talk: 914
---
<!-- generated:start -->
<!-- generated-keys: title=23d277 type=eb5b2b id=05a8ea sources=993977 name_key=efe1c3 kind=356a19 kind_name=0bac50 giver=de218c turn_in=847ad4 offer_maps=15f2a7 bit=d321d6 requires_bit=17ba07 automatic=5ffe53 prev=707bff next=a5a5cb stages=30caa7 objectives=c0c1c7 rewards=33baa2 offer_talk=b70158 -->
|  |  |
|---|---|
|  | ![Rune Equipment.](wiki/assets/npcs/324.png) |
| **Quest id** | `122` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/324-casta\|Casta]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 77 |
| **Requires bit** | 11 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/12-an-urgent-message|An urgent message]]
- **Next:** [[wiki/quests/121-create-rune|Create Rune]]

### Objectives

1. Talk to [[wiki/npcs/324-casta|Casta]] — tracker: “Go to Casta”
2. client event: rune equipped — tracker: “Equip Rune from Casta”

### Rewards

- **Basic reward:** [[wiki/items/7032-magic-resist-rune|Magic Resist Rune]]

### Dialogue

#### Offer (QuestTalk 914)

Speaker: [[wiki/npcs/324-casta|Casta]]

> **Casta:** Did you come to set the rune from me? <br> you are able to set and delete only through me.  
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
