---
title: "Weapon manufacturing"
type: "quest"
id: 113
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 113", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 809", "client: QuestTalk.cdb id 810"]
name_key: "Quest_Title_111"
kind: 1
kind_name: "Sub"
classes: ["Guardian"]
giver: {"npc": 237}
turn_in: {"npc": 237}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 34
requires_bit: 22
prev: [22]
next: []
prerequisites:
  - {"type": 1, "what": "class", "classes": ["Guardian"], "mask": 16}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 26, "what": null, "a": 5, "b": 1, "maps": [120, 120, 120], "text_key": "Quest_QuickText_111_3"}
  - {"n": 2, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_G_FAREL"}
rewards:
  - {"type": 2, "what": "exp", "amount": 60000, "shown": 50000}
  - {"type": 1, "what": "item", "item": 7082, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 7092, "count": 1, "pick": "choose"}
offer_talk: 809
complete_talk: 810
---
<!-- generated:start -->
<!-- generated-keys: title=2dce85 type=eb5b2b id=e99321 sources=1b0a04 name_key=ec508b kind=356a19 kind_name=0bac50 classes=2160c0 giver=65eab4 turn_in=65eab4 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=f1f836 requires_bit=12c6fc prev=5c6c1d next=97d170 prerequisites=9bef0c stages=30caa7 objectives=2be88c objectives_client=0a57bd rewards=7fc5e4 offer_talk=cd8b7a complete_talk=a1496d -->
|  |  |
|---|---|
|  | ![Weapon manufacturing](../assets/npcs/237.png) |
| **Quest id** | `113` |
| **Kind** | Sub (kind 1) |
| **Classes** | Guardian |
| **Giver** | [[wiki/npcs/237-farrell\|Farrell]] |
| **Turn in** | [[wiki/npcs/237-farrell\|Farrell]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 34 |
| **Requires bit** | 22 |

### Chain

- **After:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 34 with:** [[wiki/quests/111-weapon-manufacturing|Weapon manufacturing]], [[wiki/quests/112-weapon-manufacturing|Weapon manufacturing]] (completing one closes the others)

### Requirements

| type | meaning | value |
|---|---|---|
| 1 | class | Guardian (mask 16) |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 26 — craft gear (category a)?; values a=5, b=1 — tracker: “Craft a new Guardian Weapon”
2. Report (tracker line; done by turning the quest in) — tracker: “Deliver them to Farrell”

### Rewards

- **Basic reward:** 60,000 exp (shown in game as 50,000)
- **Choose one:** [[wiki/items/7082-armor-penetration-rune|Armor Penetration Rune]] *or* [[wiki/items/7092-magic-resist-penetration-rune|Magic resist Penetration Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 809)

Speaker: [[wiki/npcs/237-farrell|Farrell]]

> **Farrell:** I can make you a weapon. Would you like to take a look?  
> *(end)*

#### Completion (QuestTalk 810)

Speaker: [[wiki/npcs/237-farrell|Farrell]]

> **Farrell:** If you bring me some material I will make anything you need - until next time!  
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
