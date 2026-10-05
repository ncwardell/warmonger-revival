---
title: "Create Innocence Crystal"
type: "quest"
id: 693
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 693", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 880", "client: QuestTalk.cdb id 881"]
name_key: "Quest_Title_502"
kind: 1
kind_name: "Sub"
giver: {"npc": 325}
turn_in: {"npc": 325}
bit: 88
requires_bit: 81
prev: [692]
next: []
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 26, "what": null, "a": 7, "b": 1, "text_key": "Quest_QuickText_502_1"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_24_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 150000, "shown": 125000}
offer_talk: 880
complete_talk: 881
---
<!-- generated:start -->
<!-- generated-keys: title=f65a8d type=eb5b2b id=d69b92 sources=dba51b name_key=b911bf kind=356a19 kind_name=0bac50 giver=ad0cc6 turn_in=ad0cc6 bit=b37f6d requires_bit=1d513c prev=f8c5a3 next=97d170 stages=30caa7 objectives=2be88c objectives_client=37d03d rewards=9e8677 offer_talk=0b5e7f complete_talk=c425c6 -->
|  |  |
|---|---|
|  | ![Create Innocence Crystal](wiki/assets/npcs/325.png) |
| **Quest id** | `693` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/325-joel\|Joel]] |
| **Turn in** | [[wiki/npcs/325-joel\|Joel]] |
| **Completion bit** | 88 |
| **Requires bit** | 81 |

### Chain

- **After:** [[wiki/quests/692-innocence-crystal|Innocence Crystal]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 26 — craft gear (category a)?; values a=7, b=1 — tracker: “Create Innocence Crystal from Joel”
2. Report (tracker line; done by turning the quest in) — tracker: “Go to Joel: (Moving the Temple through the Oracle of the Protection)”

### Rewards

- **Basic reward:** 150,000 exp (shown in game as 125,000)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 880)

Speaker: [[wiki/npcs/325-joel|Joel]]

> **Joel:** I want to make a piece together with the pieces I gave you. For reference, innocence crystals disappear quickly.  
> *(end)*

#### Completion (QuestTalk 881)

Speaker: [[wiki/npcs/325-joel|Joel]]

> **Joel:** You must have made it! Then let me use it well!  
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
