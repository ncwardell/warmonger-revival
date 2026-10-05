---
title: "Create Potion"
type: "quest"
id: 47
status: "complete"
missing: []
sources: ["client: Quest.cdb id 47", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 904", "client: QuestTalk.cdb id 905"]
name_key: "Quest_Title_47"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 123
requires_bit: 122
automatic: true
prev: [46]
next: [33, 737, 738, 739, 1026, 1028]
prerequisites:
  - {"type": 6, "what": "item", "item": 2593, "count": 100}
  - {"type": 6, "what": "item", "item": 2594, "count": 2}
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 214, "maps": [120, 120, 120], "text_key": "Quest_QuickText_47_0"}
  - {"n": 2, "type": 11, "what": "craft_item", "item": 2598, "count": 100, "maps": [120, 120, 120], "text_key": "Quest_QuickText_47_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 600000, "shown": 545455}
  - {"type": 1, "what": "item", "item": 7002, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 7012, "count": 1, "pick": "choose"}
offer_talk: 904
complete_talk: 905
---
<!-- generated:start -->
<!-- generated-keys: title=a601a3 type=eb5b2b id=827bfc sources=285a47 name_key=5aece9 kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=40bd00 requires_bit=05a8ea automatic=5ffe53 prev=10537b next=f38cb9 prerequisites=5baae9 stages=a80fa1 objectives=e907ed rewards=e5dfcb offer_talk=6f2c73 complete_talk=71ef3e -->
|  |  |
|---|---|
|  | ![Create Potion](wiki/assets/npcs/200.png) |
| **Quest id** | `47` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 123 |
| **Requires bit** | 122 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/46-to-oracle-of-knowledge|To Oracle of knowledge]]
- **Next:** [[wiki/quests/33-ghost-fortress|Ghost Fortress]], [[wiki/quests/737-ghost-fortress|Ghost Fortress]], [[wiki/quests/738-collecting-material|Collecting material]], [[wiki/quests/739-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/1026-ghost-fortress-hunting|Ghost Fortress : Hunting]], [[wiki/quests/1028-ghost-fortress-collecting-material|Ghost Fortress : Collecting material]]

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/2593-empty-flask-a\|Empty Flask (A)]] × 100 |
| 6 | item | carries [[wiki/items/2594-crystal-red\|Crystal : Red]] × 2 |

### Objectives

1. Talk to [[wiki/npcs/214-owen|Owen]] — tracker: “Talk to Cassia”
2. Craft [[wiki/items/2598-potion-of-health-quest|Potion of Health (Quest)]] × 100 — tracker: “Create a Potion of Health [Quest]”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 600,000 exp (shown in game as 545,455)
- **Choose one:** [[wiki/items/7002-attack-rune|Attack Rune]] *or* [[wiki/items/7012-ability-power-rune|Ability Power Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 904)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Are you ready to go before you go to a dangerous area? <br>If you go to Cassia, you can make a better potion. Go and come.  
> *(accept / continue)*

#### Completion (QuestTalk 905)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **You:** I have finished all the preparations. Give me a mission to do!  
> *(accept / continue)*

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]]
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
