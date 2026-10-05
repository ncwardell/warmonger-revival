---
title: "War - Objects"
type: "quest"
id: 49
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 49", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 908"]
name_key: "Quest_Title_49"
kind: 0
kind_name: "Main"
giver: {"npc": 208}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 125
requires_bit: 124
automatic: true
prev: [48]
next: [50]
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 30, "what": null, "a": 2, "b": 1, "text_key": "Quest_QuickText_49_0"}
  - {"n": 2, "type": 29, "what": null, "a": 2, "b": 1, "text_key": "Quest_QuickText_49_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1100000, "shown": 1000000}
  - {"type": 1, "what": "item", "item": 7062, "count": 1, "pick": "fixed"}
offer_talk: 908
---
<!-- generated:start -->
<!-- generated-keys: title=6d96a9 type=eb5b2b id=2e01e1 sources=f25251 name_key=5594f6 kind=b6589f kind_name=b3f808 giver=58f603 turn_in=847ad4 offer_maps=15f2a7 bit=0ca927 requires_bit=f38cfe automatic=5ffe53 prev=b8da6a next=d59264 stages=30caa7 objectives=2be88c objectives_client=a7e18d rewards=b7dcb1 offer_talk=2262b2 -->
|  |  |
|---|---|
|  | ![War - Objects](wiki/assets/npcs/208.png) |
| **Quest id** | `49` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/208-bell-thain\|Bell Thain]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 125 |
| **Requires bit** | 124 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/48-doping-create|Doping Create]]
- **Next:** [[wiki/quests/50-war-winning-means|War - Winning means]]

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 30 — build nexus?; values a=2, b=1 — tracker: “Nexus construction after entry to enemy occupation territory”
2. Type 29 — attack tower?; values a=2, b=1 — tracker: “Constructing Attack Tower”

### Rewards

- **Basic reward:** 1,100,000 exp (shown in game as 1,000,000); [[wiki/items/7062-health-regeneration-rune|Health Regeneration Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 908)

Speaker: [[wiki/npcs/208-bell-thain|Bell Thain]]

> **Bell Thain:** There are many ways to win the war! Go to war zone and learn.  
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
