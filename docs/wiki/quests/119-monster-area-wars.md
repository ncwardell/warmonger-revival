---
title: "Monster area wars"
type: "quest"
id: 119
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 119", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 787"]
name_key: "Quest_Title_845"
kind: 1
kind_name: "Sub"
giver: {"npc": 205}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 117
requires_bit: 22
automatic: true
prev: [22]
next: []
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 3, "b": 3, "text_key": "Quest_QuickText_845_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 2000000, "shown": 1666667}
offer_talk: 787
---
<!-- generated:start -->
<!-- generated-keys: title=d1901b type=eb5b2b id=a2e33d sources=b812f7 name_key=f942fd kind=356a19 kind_name=0bac50 giver=37f9c0 turn_in=847ad4 offer_maps=15f2a7 bit=d0e2db requires_bit=12c6fc automatic=5ffe53 prev=5c6c1d next=97d170 stages=30caa7 objectives=2be88c objectives_client=8b8775 rewards=202a6f offer_talk=e00988 -->
|  |  |
|---|---|
|  | ![Monster area wars](../assets/npcs/205.png) |
| **Quest id** | `119` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/205-lewellyn\|Lewellyn]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 117 |
| **Requires bit** | 22 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 15 — monster-area war / occupation?; values a=3, b=3 — tracker: “Monster area wars”

### Rewards

- **Basic reward:** 2,000,000 exp (shown in game as 1,666,667)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 787)

Speaker: [[wiki/npcs/205-lewellyn|Lewellyn]]

> **Lewellyn:** Hi, Keeper. Did you know? Your Nation can earn resources when your side conquers and keeps territory. <br> The monster's territories are easier to conquer than the other Nations.  
> *(accept / continue)*

### Mentioned in

- [[gameplay/patch-history|Patch notes and other sources]]
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
