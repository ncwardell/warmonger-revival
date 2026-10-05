---
title: "Sell Ether"
type: "quest"
id: 766
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 766", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 781"]
name_key: "Quest_Title_766"
kind: 1
kind_name: "Sub"
giver: {"npc": 210}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 115
requires_bit: 114
automatic: true
prev: [767]
next: []
prerequisites:
  - {"type": 7, "what": "legion?", "a": 4, "b": 2}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 24, "what": null, "a": 500, "text_key": "Quest_QuickText_766_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 5000, "shown": 4167}
offer_talk: 781
---
<!-- generated:start -->
<!-- generated-keys: title=fadf98 type=eb5b2b id=581a8e sources=60165e name_key=fd62fa kind=356a19 kind_name=0bac50 giver=7abdb8 turn_in=847ad4 offer_maps=15f2a7 bit=efa6e4 requires_bit=ecb793 automatic=5ffe53 prev=50b706 next=97d170 prerequisites=7dc7fa stages=30caa7 objectives=2be88c objectives_client=ae21c7 rewards=3a37a7 offer_talk=c7e47b -->
|  |  |
|---|---|
|  | ![Sell Ether](wiki/assets/npcs/210.png) |
| **Quest id** | `766` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 115 |
| **Requires bit** | 114 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/767-buy-ether|Buy Ether]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 115 with:** [[wiki/quests/1528-legion-buy-or-sell-ether|legion - Buy or sell ether]] (completing one closes the others)

### Requirements

| type | meaning | value |
|---|---|---|
| 7 | legion? | a=4, b=2 |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 24 — sell ether?; values a=500 — tracker: “Sell Ether at Legion Window”

### Rewards

- **Basic reward:** 5,000 exp (shown in game as 4,167)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 781)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** Do you know? You can sell Ether. Try sell it!  
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
