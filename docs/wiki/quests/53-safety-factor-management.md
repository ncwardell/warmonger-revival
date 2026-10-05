---
title: "Safety factor Management"
type: "quest"
id: 53
status: "stub"
missing: ["objectives", "next"]
sources: ["client: Quest.cdb id 53", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 911", "client: QuestTalk.cdb id 913"]
name_key: "Quest_Title_53"
kind: 0
kind_name: "Main"
giver: {"npc": 208}
turn_in: {"npc": 208}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 128
requires_bit: 127
prev: [51]
next: []
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 4, "b": 1, "text_key": "Quest_QuickText_53_0"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_53_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 2000000, "shown": 1818182}
  - {"type": 1, "what": "item", "item": 7042, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 7052, "count": 1, "pick": "choose"}
offer_talk: 913
complete_talk: 911
---
<!-- generated:start -->
<!-- generated-keys: title=50ec04 type=eb5b2b id=c5b76d sources=a55283 name_key=5bd822 kind=b6589f kind_name=b3f808 giver=58f603 turn_in=58f603 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b4182b requires_bit=008451 prev=c6af6d next=97d170 stages=30caa7 objectives=2be88c objectives_client=1245b2 rewards=f0a4f0 offer_talk=fa5b7e complete_talk=f37511 -->
|  |  |
|---|---|
|  | ![Safety factor Management](wiki/assets/npcs/208.png) |
| **Quest id** | `53` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/208-bell-thain\|Bell Thain]] |
| **Turn in** | [[wiki/npcs/208-bell-thain\|Bell Thain]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 128 |
| **Requires bit** | 127 |

### Chain

- **After:** [[wiki/quests/51-war-winning-means|War - Winning means]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 15 — monster-area war / occupation?; values a=4, b=1 — tracker: “Occupation of Monster Invasion Area”
2. Report (tracker line; done by turning the quest in) — tracker: “Meeting Balten”

### Rewards

- **Basic reward:** 2,000,000 exp (shown in game as 1,818,182)
- **Choose one:** [[wiki/items/7042-health-rune|Health Rune]] *or* [[wiki/items/7052-mana-rune|Mana Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 913)

Speaker: [[wiki/npcs/208-bell-thain|Bell Thain]]

> **Bell Thain:** Did not you go to the Monster Invasion Area? <br>Go quickly.  
> *(accept / continue)*

#### Completion (QuestTalk 911)

Speaker: [[wiki/npcs/208-bell-thain|Bell Thain]]

> **Bell Thain:** Did you learn how to increase the Safety factor? So good.  
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
