---
title: "Talk to Krister"
type: "quest"
id: 106
status: "complete"
missing: []
sources: ["client: Quest.cdb id 106", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 677", "client: QuestTalk.cdb id 678"]
name_key: "Quest_Title_653"
kind: 1
kind_name: "Sub"
level: {"min": 25}
giver: {"npc": 219}
turn_in: {"auto": true}
offer_maps: [90, 94, 98]
bit: 45
requires_bit: 85
automatic: true
prev: [783, 784]
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 25}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 219, "talk": 677, "maps": [90, 94, 98], "text_key": "Quest_QuickText_653_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 12000, "shown": 10000}
offer_talk: 678
---
<!-- generated:start -->
<!-- generated-keys: title=8c4dfb type=eb5b2b id=7224f9 sources=e3ce5f name_key=37a6f7 kind=356a19 kind_name=0bac50 level=00652f giver=3fbcaa turn_in=847ad4 offer_maps=18e60d bit=fb6443 requires_bit=135224 automatic=5ffe53 prev=03785d next=97d170 prerequisites=34d94a stages=30caa7 objectives=049370 rewards=2c05c9 offer_talk=b2029b -->
|  |  |
|---|---|
|  | ![Talk to Krister](wiki/assets/npcs/219.png) |
| **Quest id** | `106` |
| **Kind** | Sub (kind 1) |
| **Level** | 25+ |
| **Giver** | [[wiki/npcs/219-krister\|Krister]] |
| **Turn in** | automatic |
| **Offered on** | Arslan: [[wiki/fields/90-castle\|Castle]] (90) · Erion: [[wiki/fields/94-castle\|Castle]] (94) · Armia: [[wiki/fields/98-castle\|Castle]] (98) |
| **Completion bit** | 45 |
| **Requires bit** | 85 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/783-swamps-of-the-snake-warrior|Swamps of the Snake Warrior]], [[wiki/quests/784-swamps-of-the-snake-warrior|Swamps of the Snake Warrior]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 25+ |

### Objectives

1. Talk to [[wiki/npcs/219-krister|Krister]] (dialogue 677) — tracker: “Take a look at the description of the Legion Stocks”

### Rewards

- **Basic reward:** 12,000 exp (shown in game as 10,000)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 678)

Speaker: [[wiki/npcs/219-krister|Krister]]

> **Krister:** How can I help you? Do you have any questions?  
> **You:** Yes, can you tell me about the Legion stocks?  
> **Krister:** Of course I can.  
> *(accept / continue)*

#### Objective 1 (QuestTalk 677)

Speaker: [[wiki/npcs/219-krister|Krister]]

> **Krister:** Legion stocks are bought and sold. These actions are not difficult, they are actually really easy.  
> **Krister:** All you have to remember is buying and selling!  
> *(accept / continue)*

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 23 at [58:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=3530s)
<!-- generated:end -->

## Notes

Krister (219, Stock Administrator, Castle) explains legion stocks; the first-session player talked to him at [58:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=3530s) but did not take this quest ([[gameplay/video-early-quests]] step 23). *video*

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
