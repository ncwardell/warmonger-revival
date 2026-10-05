---
title: "Doping Create"
type: "quest"
id: 48
status: "complete"
missing: []
sources: ["client: Quest.cdb id 48", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 906"]
name_key: "Quest_Title_48"
kind: 0
kind_name: "Main"
giver: {"npc": 208}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 124
requires_bit: 52
automatic: true
prev: [29]
next: [49]
prerequisites:
  - {"type": 6, "what": "item", "item": 2595, "count": 30}
  - {"type": 6, "what": "item", "item": 2596, "count": 1}
  - {"type": 6, "what": "item", "item": 2597, "count": 2}
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 214, "maps": [120, 120, 120], "text_key": "Quest_QuickText_48_0"}
  - {"n": 2, "type": 11, "what": "craft_item", "item": 2599, "count": 10, "maps": [120, 120, 120], "text_key": "Quest_QuickText_48_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 850000, "shown": 772727}
  - {"type": 1, "what": "item", "item": 7022, "count": 1, "pick": "fixed"}
offer_talk: 906
---
<!-- generated:start -->
<!-- generated-keys: title=a3f81d type=eb5b2b id=64e095 sources=77816b name_key=68acc7 kind=b6589f kind_name=b3f808 giver=58f603 turn_in=847ad4 offer_maps=15f2a7 bit=f38cfe requires_bit=a93349 automatic=5ffe53 prev=f7cf3c next=3915bb prerequisites=f2e0b4 stages=a80fa1 objectives=b08d76 rewards=60a240 offer_talk=624ec0 -->
|  |  |
|---|---|
|  | ![Doping Create](wiki/assets/npcs/208.png) |
| **Quest id** | `48` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/208-bell-thain\|Bell Thain]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 124 |
| **Requires bit** | 52 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/29-kesley-s-disgrace|Kesley's Disgrace]]
- **Next:** [[wiki/quests/49-war-objects|War - Objects]]

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/2595-peppermint-powder\|Peppermint powder]] × 30 |
| 6 | item | carries [[wiki/items/2596-empty-scroll-a\|Empty Scroll (A)]] |
| 6 | item | carries [[wiki/items/2597-burning-water\|Burning water]] × 2 |

### Objectives

1. Talk to [[wiki/npcs/214-owen|Owen]] — tracker: “Go to Owen”
2. Craft [[wiki/items/2599-tome-of-cooldown-quest|Tome of Cooldown (Quest)]] × 10 — tracker: “Create a Tome of Cooldown [Quest] (0/10)”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 850,000 exp (shown in game as 772,727); [[wiki/items/7022-armor-rune|Armor Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 906)

Speaker: [[wiki/npcs/208-bell-thain|Bell Thain]]

> **Bell Thain:** Before I go to war, I'll introduce you to a production NPC. Find it!  
> *(accept / continue)*

### Seen in

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
