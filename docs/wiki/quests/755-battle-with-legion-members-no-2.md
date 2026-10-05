---
title: "Battle with Legion members No. 2"
type: "quest"
id: 755
status: "partial"
missing: ["objectives"]
sources: ["client: Quest.cdb id 755", "client: QuestTalk.cdb id 747", "client: QuestTalk.cdb id 748"]
name_key: "Quest_Title_746"
kind: 1
kind_name: "Sub"
giver: {"npc": 210}
turn_in: {"npc": 210}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 103
requires_bit: 102
prev: [754, 1527]
next: []
prerequisites:
  - {"type": 7, "what": "legion?"}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 23, "what": null, "a": 2, "b": 1, "text_key": "Quest_QuickText_746_1"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_650_3"}
rewards:
  - {"type": 1, "what": "item", "item": 1000, "count": 4, "pick": "fixed"}
offer_talk: 747
complete_talk: 748
---
<!-- generated:start -->
<!-- generated-keys: title=371ed0 type=eb5b2b id=52342f sources=92b25f name_key=2fb26b kind=356a19 kind_name=0bac50 giver=7abdb8 turn_in=7abdb8 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=934385 requires_bit=c8306a prev=10598e next=97d170 prerequisites=a1b25b stages=30caa7 objectives=2be88c objectives_client=10ab8c rewards=756548 offer_talk=5c1dc0 complete_talk=6d40f9 -->
|  |  |
|---|---|
|  | ![Battle with Legion members No. 2](wiki/assets/npcs/210.png) |
| **Quest id** | `755` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 103 |
| **Requires bit** | 102 |

### Chain

- **After:** [[wiki/quests/754-battle-with-legion-members-no-1|Battle with Legion members No. 1]], [[wiki/quests/1527-legion-civil-wars|legion - Civil wars]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 7 | legion? | no values |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 23 — legion battle?; values a=2, b=1 — tracker: “Battle with 10 Legion members.”
2. Report (tracker line; done by turning the quest in) — tracker: “Return to Kesley”

### Rewards

- **Basic reward:** [[wiki/items/1000-medal-bronze|Medal : Bronze]] × 4

### Dialogue

#### Offer (QuestTalk 747)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** The more legion members participating, the greater are the rewards.  
> *(accept / continue)*

#### Completion (QuestTalk 748)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** Did you get a reward?<br>Join the fight together with your legion again.  
> *(accept / continue)*

### Seen in

- [[gameplay/precept-shop|Precept shop and precept quests]]

### Mentioned in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]]
- [[gameplay/skull-artifact-set|Skull artifact set tooltips (Crush Online, Feb 2017)]]
<!-- generated:end -->

## Notes

A Crush Online screenshot shows the tracker entry "Battle with Legion members No. 2": battle together with 10 legion members, then return to Kelsey ([[gameplay/precept-shop]] §6, [[gameplay/skull-artifact-set]]). *image*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/precept-shop]]
- [[gameplay/skull-artifact-set]]

## Open questions

The "10" is not in the client row (objective type 23, a = 2, b = 1); it may come from the tracker text or from the 2016 server ([[gameplay/precept-shop]] §6). The screenshot spells the NPC "Kelsey", other pages "Kesley".

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
