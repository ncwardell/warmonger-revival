---
title: "Join the Legion"
type: "quest"
id: 753
status: "partial"
missing: ["objectives"]
sources: ["client: Quest.cdb id 753", "client: QuestTalk.cdb id 743", "client: QuestTalk.cdb id 744"]
name_key: "Quest_Title_744"
kind: 1
kind_name: "Sub"
giver: {"npc": 210}
turn_in: {"npc": 210}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 101
requires_bit: 100
prev: [752, 1525]
next: [767, 774, 775, 776]
prerequisites:
  - {"type": 7, "what": "legion?", "a": 4, "b": 2}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 22, "what": null, "a": 10, "text_key": "Quest_QuickText_744_1"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_650_3"}
rewards:
  - {"type": 1, "what": "item", "item": 1000, "count": 2, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 1408, "count": 1, "pick": "fixed"}
offer_talk: 743
complete_talk: 744
---
<!-- generated:start -->
<!-- generated-keys: title=31487e type=eb5b2b id=c32a67 sources=bc2ea4 name_key=0f78e4 kind=356a19 kind_name=0bac50 giver=7abdb8 turn_in=7abdb8 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=dbc0f0 requires_bit=310b86 prev=0352d5 next=3c259b prerequisites=7dc7fa stages=30caa7 objectives=2be88c objectives_client=48c824 rewards=f63309 offer_talk=f032e5 complete_talk=193b34 -->
|  |  |
|---|---|
|  | ![Join the Legion](wiki/assets/npcs/210.png) |
| **Quest id** | `753` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 101 |
| **Requires bit** | 100 |

### Chain

- **After:** [[wiki/quests/752-join-create-legion|Join & Create Legion]], [[wiki/quests/1525-legion-create|legion - Create]]
- **Next:** [[wiki/quests/767-buy-ether|Buy Ether]], [[wiki/quests/774-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]], [[wiki/quests/775-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]], [[wiki/quests/776-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]]
- **Shares completion bit 101 with:** [[wiki/quests/1526-legion-invite-or-join|legion - Invite or join]] (completing one closes the others)

### Requirements

| type | meaning | value |
|---|---|---|
| 7 | legion? | a=4, b=2 |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 22 — invite legion members?; values a=10 — tracker: “Invite a new member .”
2. Report (tracker line; done by turning the quest in) — tracker: “Return to Kesley”

### Rewards

- **Basic reward:** [[wiki/items/1000-medal-bronze|Medal : Bronze]] × 2; [[wiki/items/1408-highly-concentrated-bomb|Highly Concentrated Bomb]]

### Dialogue

#### Offer (QuestTalk 743)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** All members can gain fame for their legion. <br>Spread the word friend!  
> *(accept / continue)*

#### Completion (QuestTalk 744)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** Joining a legion will make it easier for you to defeat tough opponents.<br>You can just ask the other members for help.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 20 at [47:10](https://www.youtube.com/watch?v=s04CSN16w1s&t=2832s)
<!-- generated:end -->

## Notes

Appeared in the tracker at [75:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=4540s) after "Join & Create Legion" (752), which the player had not finished ([[gameplay/video-early-quests]] step 20). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-early-quests]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
