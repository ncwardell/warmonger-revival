---
title: "Create Rune"
type: "quest"
id: 121
status: "complete"
missing: []
sources: ["client: Quest.cdb id 121", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 838", "client: QuestTalk.cdb id 839"]
name_key: "Quest_Title_121"
kind: 1
kind_name: "Sub"
giver: {"npc": 323}
turn_in: {"npc": 323}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 73
requires_bit: 77
prev: [122]
next: [123]
prerequisites:
  - {"type": 6, "what": "item", "item": 810, "count": 2}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 11, "what": "craft_item", "item": 7022, "count": 1, "maps": [120, 120, 120], "text_key": "Quest_QuickText_121_3"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_121_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 120000, "shown": 100000}
offer_talk: 838
complete_talk: 839
---
<!-- generated:start -->
<!-- generated-keys: title=4cbc92 type=eb5b2b id=8bd795 sources=b2fcc9 name_key=2ce04c kind=356a19 kind_name=0bac50 giver=80ee25 turn_in=80ee25 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=35e995 requires_bit=d321d6 prev=d4ee27 next=4feada prerequisites=04b86a stages=30caa7 objectives=ba72ac rewards=3f5128 offer_talk=2dc292 complete_talk=706a95 -->
|  |  |
|---|---|
|  | ![Create Rune](wiki/assets/npcs/323.png) |
| **Quest id** | `121` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/323-alan\|Alan]] |
| **Turn in** | [[wiki/npcs/323-alan\|Alan]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 73 |
| **Requires bit** | 77 |

### Chain

- **After:** [[wiki/quests/122-rune-equipment|Rune Equipment.]]
- **Next:** [[wiki/quests/123-rune-reinforcement|Rune Reinforcement]]

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/810-diamond\|Diamond]] × 2 |

### Objectives

1. Craft [[wiki/items/7022-armor-rune|Armor Rune]] — tracker: “Armor Rune Creation by Alan (0/1)”
2. Report (tracker line; done by turning the quest in) — tracker: “Go to Alan”

### Rewards

- **Basic reward:** 120,000 exp (shown in game as 100,000)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 838)

Speaker: [[wiki/npcs/323-alan|Alan]]

> **Alan:** Did you come to make some Runes? Have a look around.  
> *(end)*

#### Completion (QuestTalk 839)

Speaker: [[wiki/npcs/323-alan|Alan]]

> **Alan:** Did you produce what you wanted? You'll need a lot of stuff to craft what you're looking for.  
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
