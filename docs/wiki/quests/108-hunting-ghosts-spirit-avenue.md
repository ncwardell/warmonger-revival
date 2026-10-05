---
title: "Hunting Ghosts (Spirit Avenue)"
type: "quest"
id: 108
status: "complete"
missing: []
sources: ["client: Quest.cdb id 108", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 736"]
name_key: "Quest_Title_675"
kind: 1
kind_name: "Sub"
giver: {"npc": 214}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 47
requires_bit: 16
automatic: true
prev: [17]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "unit_group": 10007, "units": [715, 716], "count": 10, "maps": [113, 113, 113], "text_key": "Quest_QuickText_675_1"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10008, "units": [717, 718], "count": 10, "maps": [113, 113, 113], "text_key": "Quest_QuickText_675_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 600000, "shown": 500000}
  - {"type": 1, "what": "item", "item": 601, "count": 50, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 50, "pick": "fixed"}
offer_talk: 736
---
<!-- generated:start -->
<!-- generated-keys: title=cfe39d type=eb5b2b id=17503a sources=2326c2 name_key=bbd4b9 kind=356a19 kind_name=0bac50 giver=fb5a8b turn_in=847ad4 offer_maps=15f2a7 bit=827bfc requires_bit=1574bd automatic=5ffe53 prev=79d296 next=97d170 stages=30caa7 objectives=7922c4 rewards=55abfa offer_talk=4b14fe -->
|  |  |
|---|---|
|  | ![Hunting Ghosts (Spirit Avenue)](wiki/assets/npcs/214.png) |
| **Quest id** | `108` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/214-owen\|Owen]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 47 |
| **Requires bit** | 16 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/17-support-the-abyss-expedition|Support the Abyss expedition]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Kill any unit of kill group 10007 ([[wiki/monsters/715-fragile-black-ghost|Fragile Black Ghost]], [[wiki/monsters/716-fragile-red-ghost|Fragile Red Ghost]]) × 10 — tracker: “Fragile Kill Ghost (0/10)” — on [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] (113)
2. Kill any unit of kill group 10008 ([[wiki/monsters/717-fragile-elite-black-ghost|Fragile Elite Black Ghost]], [[wiki/monsters/718-fragile-elite-red-ghost|Fragile Elite Red Ghost]]) × 10 — tracker: “Fragile Kill Elite Ghost (0/10)” — on [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] (113)

### Rewards

- **Basic reward:** 600,000 exp (shown in game as 500,000); [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 50; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 50

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 736)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** More and more march into the Abyss, it will be an fierce battle.  
> **Owen:** But our most important goal is to find the sage.  
> **Owen:** So, please eliminate the Ghost that interferes with finding the Sage. The Ghost is in the Spirit Avenue.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 25 at [66:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=3962s)
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
