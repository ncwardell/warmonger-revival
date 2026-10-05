---
title: "Legion - How to use add-on"
type: "quest"
id: 705
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 705", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 894", "client: QuestTalk.cdb id 895"]
name_key: "Quest_Title_705"
kind: 1
kind_name: "Sub"
giver: {"npc": 242}
turn_in: {"npc": 242}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 68
requires_bit: 80
prev: [774, 775, 776, 1530]
next: []
prerequisites:
  - {"type": 7, "what": "legion?", "a": 4, "b": 2}
stages: [1, 2, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 11, "what": "craft_item", "item": 1409, "count": 1, "maps": [120, 120, 120], "text_key": "Quest_QuickText_705_1"}
  - {"n": 2, "type": 10007, "what": "client_legion_core", "item": 1409, "text_key": "Quest_QuickText_705_2"}
  - {"n": 3, "type": 33, "what": null, "a": 1409, "text_key": "Quest_QuickText_705_3"}
  - {"n": 4, "type": 0, "what": "report", "text_key": "Quest_QuickText_774_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 50000, "shown": 41667}
offer_talk: 894
complete_talk: 895
---
<!-- generated:start -->
<!-- generated-keys: title=3b8f4c type=eb5b2b id=794bb3 sources=f82f13 name_key=2ee889 kind=356a19 kind_name=0bac50 giver=c6e5ee turn_in=c6e5ee offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b4c96d requires_bit=b888b2 prev=982951 next=97d170 prerequisites=7dc7fa stages=642aaf objectives=2be88c objectives_client=f5d4e5 rewards=492ee4 offer_talk=1ecaeb complete_talk=f1c6fe -->
|  |  |
|---|---|
|  | ![Legion - How to use add-on](wiki/assets/npcs/242.png) |
| **Quest id** | `705` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/242-raon\|Raon]] |
| **Turn in** | [[wiki/npcs/242-raon\|Raon]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 68 |
| **Requires bit** | 80 |

### Chain

- **After:** [[wiki/quests/774-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]], [[wiki/quests/775-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]], [[wiki/quests/776-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]], [[wiki/quests/1530-legion-create-core|legion - Create Core]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 7 | legion? | a=4, b=2 |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Craft [[wiki/items/1409-reinforce-nexus|Reinforce Nexus]] — tracker: “Reinforce Nexus Add-on Create (0/1)”
2. client event: legion core / item use: [[wiki/items/1409-reinforce-nexus|Reinforce Nexus]] — tracker: “Core installed through legion core window”
3. Type 33 — nexus add-on?; values a=1409 — tracker: “Reinforce Nexus Add-on Use”
4. Report (tracker line; done by turning the quest in) — tracker: “Go to Raon”

Stages (`flag1..5` = [1, 2, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 50,000 exp (shown in game as 41,667)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 894)

Speaker: [[wiki/npcs/242-raon|Raon]]

> **Raon:** Do you know it's an add-on? If you use it, you will be able to use the Gaia field more efficiently!  
> *(accept / continue)*

#### Completion (QuestTalk 895)

Speaker: [[wiki/npcs/242-raon|Raon]]

> **Raon:** Do you know how to use it? Then use a lot of add-ons to take over Gaia!  
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
