---
title: "Buy Ether"
type: "quest"
id: 767
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 767", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 782"]
name_key: "Quest_Title_767"
kind: 1
kind_name: "Sub"
giver: {"npc": 210}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 114
requires_bit: 101
automatic: true
prev: [753, 1526]
next: [766]
prerequisites:
  - {"type": 7, "what": "legion?", "a": 4, "b": 2}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 25, "what": null, "a": 500, "text_key": "Quest_QuickText_767_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 5000, "shown": 4167}
offer_talk: 782
---
<!-- generated:start -->
<!-- generated-keys: title=530686 type=eb5b2b id=81755a sources=1e1f33 name_key=bfc7e3 kind=356a19 kind_name=0bac50 giver=7abdb8 turn_in=847ad4 offer_maps=15f2a7 bit=ecb793 requires_bit=dbc0f0 automatic=5ffe53 prev=efaebd next=8ccebb prerequisites=7dc7fa stages=30caa7 objectives=2be88c objectives_client=edc1a9 rewards=3a37a7 offer_talk=281785 -->
|  |  |
|---|---|
|  | ![Buy Ether](../assets/npcs/210.png) |
| **Quest id** | `767` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 114 |
| **Requires bit** | 101 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/753-join-the-legion|Join the Legion]], [[wiki/quests/1526-legion-invite-or-join|legion - Invite or join]]
- **Next:** [[wiki/quests/766-sell-ether|Sell Ether]]

### Requirements

| type | meaning | value |
|---|---|---|
| 7 | legion? | a=4, b=2 |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 25 — buy ether?; values a=500 — tracker: “Buy Ether at Legion Window”

### Rewards

- **Basic reward:** 5,000 exp (shown in game as 4,167)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 782)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** Do you know? you can buy Ether. Try buy it!  
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
