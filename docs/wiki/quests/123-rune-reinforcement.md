---
title: "Rune Reinforcement"
type: "quest"
id: 123
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 123", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 840", "client: QuestTalk.cdb id 841"]
name_key: "Quest_Title_123"
kind: 1
kind_name: "Sub"
giver: {"npc": 324}
turn_in: {"npc": 324}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 121
requires_bit: 73
prev: [121]
next: []
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 28, "what": null, "b": 1, "maps": [120, 120, 120], "text_key": "Quest_QuickText_123_1"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_123_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 120000, "shown": 100000}
  - {"type": 1, "what": "item", "item": 7042, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 7052, "count": 1, "pick": "choose"}
offer_talk: 840
complete_talk: 841
---
<!-- generated:start -->
<!-- generated-keys: title=c0e37c type=eb5b2b id=40bd00 sources=2cf1e2 name_key=129481 kind=356a19 kind_name=0bac50 giver=de218c turn_in=de218c offer_maps=15f2a7 turn_in_maps=15f2a7 bit=8bd795 requires_bit=35e995 prev=a5a5cb next=97d170 stages=30caa7 objectives=2be88c objectives_client=2e9054 rewards=8a62c5 offer_talk=c1d2fb complete_talk=dcb63a -->
|  |  |
|---|---|
|  | ![Rune Reinforcement](wiki/assets/npcs/324.png) |
| **Quest id** | `123` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/324-casta\|Casta]] |
| **Turn in** | [[wiki/npcs/324-casta\|Casta]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 121 |
| **Requires bit** | 73 |

### Chain

- **After:** [[wiki/quests/121-create-rune|Create Rune]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 28 — rune reinforcement?; values b=1 — tracker: “Rune Reinforcement from Casta”
2. Report (tracker line; done by turning the quest in) — tracker: “Go to Casta”

### Rewards

- **Basic reward:** 120,000 exp (shown in game as 100,000)
- **Choose one:** [[wiki/items/7042-health-rune|Health Rune]] *or* [[wiki/items/7052-mana-rune|Mana Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 840)

Speaker: [[wiki/npcs/324-casta|Casta]]

> **Casta:** Have you come to reinforce something?  
> *(end)*

#### Completion (QuestTalk 841)

Speaker: [[wiki/npcs/324-casta|Casta]]

> **Casta:** Was it successful? The higher you climb, the deeper you fall!  
> *(accept / continue)*

### Mentioned in

- [[gameplay/items-and-crafting|Items, upgrades and crafting]]
- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]]
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
