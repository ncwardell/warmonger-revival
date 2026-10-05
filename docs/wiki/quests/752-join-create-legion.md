---
title: "Join & Create Legion"
type: "quest"
id: 752
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 752", "client: QuestTalk.cdb id 741", "client: QuestTalk.cdb id 742"]
name_key: "Quest_Title_743"
kind: 1
kind_name: "Sub"
giver: {"npc": 210}
turn_in: {"npc": 210}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 100
prev: []
next: [753, 754]
prerequisites:
  - {"type": 7, "what": "legion?", "a": -1}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 21, "what": null, "text_key": "Quest_QuickText_743_1"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_650_3"}
rewards:
  - {"type": 1, "what": "item", "item": 1000, "count": 1, "pick": "fixed"}
offer_talk: 741
complete_talk: 742
---
<!-- generated:start -->
<!-- generated-keys: title=33f137 type=eb5b2b id=b7ecf1 sources=335b9b name_key=fb86ce kind=356a19 kind_name=0bac50 giver=7abdb8 turn_in=7abdb8 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=310b86 prev=97d170 next=93d31a prerequisites=af2dc3 stages=30caa7 objectives=2be88c objectives_client=54bea2 rewards=7a6730 offer_talk=23b23b complete_talk=02c8be -->
|  |  |
|---|---|
|  | ![Join & Create Legion](../assets/npcs/210.png) |
| **Quest id** | `752` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 100 |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** [[wiki/quests/753-join-the-legion|Join the Legion]], [[wiki/quests/754-battle-with-legion-members-no-1|Battle with Legion members No. 1]]
- **Shares completion bit 100 with:** [[wiki/quests/1525-legion-create|legion - Create]] (completing one closes the others)

### Requirements

| type | meaning | value |
|---|---|---|
| 7 | legion? | a=-1 |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 21 — join or create a legion?; values none — tracker: “Join Legion or Create Legion.”
2. Report (tracker line; done by turning the quest in) — tracker: “Return to Kesley”

### Rewards

- **Basic reward:** [[wiki/items/1000-medal-bronze|Medal : Bronze]]

### Dialogue

#### Offer (QuestTalk 741)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** I didn't see you before, are you new in town?<br>Did you know? If you participate in activities together with your Legion's members you can receive various bonuses.  
> *(accept / continue)*

#### Completion (QuestTalk 742)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** Oh, did you join Legion? Go and develop your legion.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 20 at [47:10](https://www.youtube.com/watch?v=s04CSN16w1s&t=2832s)

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]]
- [[gameplay/progression-and-economy|Progression and economy]]
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
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
