---
title: "Innocence Crystal"
type: "quest"
id: 692
status: "complete"
missing: []
sources: ["client: Quest.cdb id 692", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 878", "client: QuestTalk.cdb id 879", "client: QuestTalk.cdb id 882"]
name_key: "Quest_Title_501"
kind: 1
kind_name: "Sub"
giver: {"npc": 200}
turn_in: {"npc": 325}
offer_maps: [120, 120, 120]
bit: 81
requires_bit: 67
prev: [762]
next: [693]
prerequisites:
  - {"type": 6, "what": "item", "item": 911, "count": 1}
stages: [3, 4, 5, 5, 5]
objectives:
  - {"n": 1, "type": 13, "what": "use_item", "item": 911, "count": 1, "text_key": "Quest_QuickText_501_1"}
  - {"n": 2, "type": 4, "what": "talk", "npc": 327, "talk": 882, "text_key": "Quest_QuickText_31_3"}
  - {"n": 3, "type": 0, "what": "report", "text_key": "Quest_QuickText_24_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 150000, "shown": 125000}
  - {"type": 1, "what": "item", "item": 611, "count": 50, "pick": "fixed"}
offer_talk: 878
complete_talk: 879
---
<!-- generated:start -->
<!-- generated-keys: title=8a45bb type=eb5b2b id=6d3eeb sources=770dca name_key=6ba2e9 kind=356a19 kind_name=0bac50 giver=1caac0 turn_in=ad0cc6 offer_maps=15f2a7 bit=1d513c requires_bit=4d89d2 prev=f425d7 next=8d6f6c prerequisites=154ad3 stages=260252 objectives=6f2f72 rewards=066b5c offer_talk=02db8e complete_talk=339e2e -->
|  |  |
|---|---|
|  | ![Innocence Crystal](../assets/npcs/200.png) |
| **Quest id** | `692` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/325-joel\|Joel]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 81 |
| **Requires bit** | 67 |

### Chain

- **After:** [[wiki/quests/762-killed-boss-of-border-area-no-2|killed boss of Border area No.2]]
- **Next:** [[wiki/quests/693-create-innocence-crystal|Create Innocence Crystal]]

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/911-scroll-castle\|Scroll : Castle]] |

### Objectives

1. Use [[wiki/items/911-scroll-castle|Scroll : Castle]] — tracker: “Move to castle”
2. Talk to [[wiki/npcs/327-aenes|Aenes]] (dialogue 882) — tracker: “Moving to the Temple through Oracle of the Protection”
3. Report (tracker line; done by turning the quest in) — tracker: “Go to Joel: (Moving the Temple through the Oracle of the Protection)”

Stages (`flag1..5` = [3, 4, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 150,000 exp (shown in game as 125,000); [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 50

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 878)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** There is a gift for you who always tried so hard~ Do you have a Piece of Innocence? <br> Go to the Temple with it.  
> *(accept / continue)*

#### Objective 2 (QuestTalk 882)

Speaker: [[wiki/npcs/327-aenes|Aenes]]

> **Aenes:** This time you came to find Joel. You are on your way to the Temple.  
> *(end)*

#### Completion (QuestTalk 879)

Speaker: [[wiki/npcs/325-joel|Joel]]

> **Joel:** Oh, you have your Piece of Innocence. The piece can only see the light through me ~ Would you like to make one?  
> *(accept / continue)*

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]]
- [[gameplay/patch-history|Patch notes and other sources]]
- [[gameplay/server-rules|Server rules checklist]]
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
