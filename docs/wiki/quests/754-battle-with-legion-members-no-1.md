---
title: "Battle with Legion members No. 1"
type: "quest"
id: 754
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 754", "client: QuestTalk.cdb id 745", "client: QuestTalk.cdb id 746"]
name_key: "Quest_Title_745"
kind: 1
kind_name: "Sub"
giver: {"npc": 210}
turn_in: {"npc": 210}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 102
requires_bit: 100
prev: [752, 1525]
next: [755]
prerequisites:
  - {"type": 7, "what": "legion?"}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 23, "what": null, "a": 1, "b": 1, "text_key": "Quest_QuickText_745_1"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_650_3"}
rewards:
  - {"type": 1, "what": "item", "item": 1000, "count": 3, "pick": "fixed"}
offer_talk: 745
complete_talk: 746
---
<!-- generated:start -->
<!-- generated-keys: title=1af20c type=eb5b2b id=b246c7 sources=78286c name_key=f25ead kind=356a19 kind_name=0bac50 giver=7abdb8 turn_in=7abdb8 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=c8306a requires_bit=310b86 prev=0352d5 next=0bb466 prerequisites=a1b25b stages=30caa7 objectives=2be88c objectives_client=ddf10a rewards=6f125d offer_talk=de8627 complete_talk=9b3aa2 -->
|  |  |
|---|---|
|  | ![Battle with Legion members No. 1](../assets/npcs/210.png) |
| **Quest id** | `754` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 102 |
| **Requires bit** | 100 |

### Chain

- **After:** [[wiki/quests/752-join-create-legion|Join & Create Legion]], [[wiki/quests/1525-legion-create|legion - Create]]
- **Next:** [[wiki/quests/755-battle-with-legion-members-no-2|Battle with Legion members No. 2]]
- **Shares completion bit 102 with:** [[wiki/quests/1527-legion-civil-wars|legion - Civil wars]] (completing one closes the others)

### Requirements

| type | meaning | value |
|---|---|---|
| 7 | legion? | no values |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 23 — legion battle?; values a=1, b=1 — tracker: “Battle with 5 Legion members.”
2. Report (tracker line; done by turning the quest in) — tracker: “Return to Kesley”

### Rewards

- **Basic reward:** [[wiki/items/1000-medal-bronze|Medal : Bronze]] × 3

### Dialogue

#### Offer (QuestTalk 745)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** When you fight along side your legion members, you will receive more rewards.<br>Let's do that.  
> *(accept / continue)*

#### Completion (QuestTalk 746)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** Did you get a reward?<br>Join the fight together with your legion again.  
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
