---
title: "Weapon tier reinforce"
type: "quest"
id: 114
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 114", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 811", "client: QuestTalk.cdb id 812"]
name_key: "Quest_Title_112"
kind: 1
kind_name: "Sub"
giver: {"npc": 237}
turn_in: {"npc": 237}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 35
requires_bit: 56
prev: [769, 772, 773]
next: []
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 6, "what": null, "a": 1, "b": 1, "c": 1, "maps": [120, 120, 120], "text_key": "Quest_QuickText_112_1"}
  - {"n": 2, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_112_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 60000, "shown": 50000}
offer_talk: 811
complete_talk: 812
---
<!-- generated:start -->
<!-- generated-keys: title=d9e2d3 type=eb5b2b id=ecb793 sources=1a280d name_key=55724a kind=356a19 kind_name=0bac50 giver=65eab4 turn_in=65eab4 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=972a67 requires_bit=54ceb9 prev=46b5ec next=97d170 stages=30caa7 objectives=2be88c objectives_client=d17bd2 rewards=2b23be offer_talk=6f8246 complete_talk=872a31 -->
|  |  |
|---|---|
|  | ![Weapon tier reinforce](../assets/npcs/237.png) |
| **Quest id** | `114` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/237-farrell\|Farrell]] |
| **Turn in** | [[wiki/npcs/237-farrell\|Farrell]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 35 |
| **Requires bit** | 56 |

### Chain

- **After:** [[wiki/quests/769-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/772-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/773-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 35 with:** [[wiki/quests/1514-item-tier-reinforce|Item - Tier reinforce]] (completing one closes the others)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 6 — reinforce?; values a=1, b=1, c=1 — tracker: “For success reinforce tier (first tier)   (same weapon, tier,15Lv 2 of them)”
2. Report (tracker line; done by turning the quest in) — tracker: “Start chat with Farrell”

### Rewards

- **Basic reward:** 60,000 exp (shown in game as 50,000)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 811)

Speaker: [[wiki/npcs/237-farrell|Farrell]]

> **Farrell:** weapons can maximize endlessly~ for that you need level reinforcement. Do you want to try it now?  
> *(accept / continue)*  
> *(accept / continue)*

#### Completion (QuestTalk 812)

Speaker: [[wiki/npcs/237-farrell|Farrell]]

> **Farrell:** Level reinforcement will become  harder and harder. Please try harder.  
> *(accept / continue)*  
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
