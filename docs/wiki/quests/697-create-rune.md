---
title: "Create Rune"
type: "quest"
id: 697
status: "complete"
missing: []
sources: ["client: Quest.cdb id 697", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 901"]
name_key: "Quest_Title_121"
kind: 1
kind_name: "Sub"
giver: {"auto": true}
turn_in: {"auto": true}
bit: 57
requires_bit: 36
automatic: true
prev: [770]
next: [699]
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 323, "talk": 901, "maps": [120, 120, 120], "text_key": "Quest_QuickText_121_1_"}
rewards:
  - {"type": 2, "what": "exp", "amount": 120000, "shown": 100000}
---
<!-- generated:start -->
<!-- generated-keys: title=4cbc92 type=eb5b2b id=ff5ae4 sources=b2b2f8 name_key=2ce04c kind=356a19 kind_name=0bac50 giver=847ad4 turn_in=847ad4 bit=9109c8 requires_bit=fc074d automatic=5ffe53 prev=d8e285 next=6a1a83 stages=30caa7 objectives=7fde64 rewards=3f5128 -->
|  |  |
|---|---|
| **Quest id** | `697` |
| **Kind** | Sub (kind 1) |
| **Giver** | automatic |
| **Turn in** | automatic |
| **Completion bit** | 57 |
| **Requires bit** | 36 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/770-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** [[wiki/quests/699-rune-reinforcement|Rune Reinforcement]]
- **Shares completion bit 57 with:** [[wiki/quests/1515-item-create-rune|Item - Create Rune]] (completing one closes the others)

### Objectives

1. Talk to [[wiki/npcs/323-alan|Alan]] (dialogue 901) — tracker: “Go to Alan” — on [[wiki/fields/120-fortress|Fortress]] (120)

### Rewards

- **Basic reward:** 120,000 exp (shown in game as 100,000)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Objective 1 (QuestTalk 901)

Speaker: [[wiki/npcs/323-alan|Alan]]

> **Alan:** Go to Alan and make a rune~  
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
