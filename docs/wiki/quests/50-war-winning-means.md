---
title: "War - Winning means"
type: "quest"
id: 50
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 50", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 907"]
name_key: "Quest_Title_50"
kind: 0
kind_name: "Main"
giver: {"npc": 208}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 126
requires_bit: 125
automatic: true
prev: [49]
next: [51]
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 32, "what": null, "a": 2, "c": 2, "text_key": "Quest_QuickText_50_0"}
  - {"n": 2, "type": 1, "what": "kill", "unit": 571, "count": 2, "text_key": "Quest_QuickText_50_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1200000, "shown": 1090909}
  - {"type": 1, "what": "item", "item": 7072, "count": 1, "pick": "fixed"}
offer_talk: 907
---
<!-- generated:start -->
<!-- generated-keys: title=79c38d type=eb5b2b id=e1822d sources=684e89 name_key=202ca4 kind=b6589f kind_name=b3f808 giver=58f603 turn_in=847ad4 offer_maps=15f2a7 bit=114d4e requires_bit=0ca927 automatic=5ffe53 prev=3915bb next=c6af6d stages=30caa7 objectives=2be88c objectives_client=317f2a rewards=3294e1 offer_talk=bd7c80 -->
|  |  |
|---|---|
|  | ![War - Winning means](../assets/npcs/208.png) |
| **Quest id** | `50` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/208-bell-thain\|Bell Thain]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 126 |
| **Requires bit** | 125 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/49-war-objects|War - Objects]]
- **Next:** [[wiki/quests/51-war-winning-means|War - Winning means]]

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 32 — set TP skill?; values a=2, c=2 — tracker: “TP skill Set   (Click to use completed TP skill)”
2. Kill [[wiki/monsters/571-bear|Bear]] × 2 — tracker: “Kill Jungle Monster (0/2)”

### Rewards

- **Basic reward:** 1,200,000 exp (shown in game as 1,090,909); [[wiki/items/7072-mana-regeneration-rune|Mana Regeneration Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 907)

Speaker: [[wiki/npcs/208-bell-thain|Bell Thain]]

> **Bell Thain:** Have not you gone to war yet? Let's go quickly!  
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
