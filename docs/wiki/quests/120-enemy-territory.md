---
title: "Enemy territory"
type: "quest"
id: 120
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 120", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 788"]
name_key: "Quest_Title_846"
kind: 1
kind_name: "Sub"
giver: {"npc": 237}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 118
requires_bit: 52
automatic: true
prev: [29]
next: []
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 2, "b": 3, "text_key": "Quest_QuickText_846_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 2000000, "shown": 1666667}
offer_talk: 788
---
<!-- generated:start -->
<!-- generated-keys: title=75a6d8 type=eb5b2b id=775bc5 sources=b01983 name_key=70502c kind=356a19 kind_name=0bac50 giver=65eab4 turn_in=847ad4 offer_maps=15f2a7 bit=12f0de requires_bit=a93349 automatic=5ffe53 prev=f7cf3c next=97d170 stages=30caa7 objectives=2be88c objectives_client=1d7830 rewards=202a6f offer_talk=0fe36d -->
|  |  |
|---|---|
|  | ![Enemy territory](../assets/npcs/237.png) |
| **Quest id** | `120` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/237-farrell\|Farrell]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 118 |
| **Requires bit** | 52 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/29-kesley-s-disgrace|Kesley's Disgrace]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 15 — monster-area war / occupation?; values a=2, b=3 — tracker: “Conquer Enemy's territory”

### Rewards

- **Basic reward:** 2,000,000 exp (shown in game as 1,666,667)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 788)

Speaker: [[wiki/npcs/237-farrell|Farrell]]

> **Farrell:** Could I ask for a favour? We have to conquer enemy territory. That's the easiest way to create a strong union. <br>We will get huge resources as a reward for sure.  
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
