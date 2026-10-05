---
title: "Basic function - Basic attack"
type: "quest"
id: 1502
status: "partial"
missing: ["turn_in"]
sources: ["client: Quest.cdb id 1502", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)"]
name_key: "Quest_Title_Help_666"
kind: 12
kind_name: "Advice"
giver: {"auto": true}
turn_in: null
bit: 70
prev: []
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 10001, "what": "client_attack", "text_key": "Quest_QuickText_Help_666_1"}
rewards: []
help: {"image": "ui/HelpImage/Help_09.png", "text_key": "Quest_Title_Help_String_666"}
---
<!-- generated:start -->
<!-- generated-keys: title=82b92f type=eb5b2b id=104469 sources=bf709c name_key=4465ee kind=7b5200 kind_name=ec7dd4 giver=847ad4 turn_in=2be88c bit=b7103c prev=97d170 next=97d170 stages=30caa7 objectives=1ae9c1 rewards=97d170 help=5ef0de -->
|  |  |
|---|---|
|  | ![Basic function - Basic attack](wiki/assets/quests/1502.png) |
| **Quest id** | `1502` |
| **Kind** | Advice (kind 12) |
| **Giver** | automatic |
| **Turn in** | **unknown** |
| **Completion bit** | 70 |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 70 with:** [[wiki/quests/700-basic-combat-lesson-1|Basic Combat Lesson 1]] (completing one closes the others)

### Objectives

1. client event: attack / skill used — tracker: “Basic attack”

### Rewards

None in the client.

### Tip window

> When you right-click on an enemy NPC, it approaches the NPC and makes a basic attack

Image `ui/HelpImage/Help_09.png`.
<!-- generated:end -->

## Notes

The HUD's Help button opens an "Advice" list of the lessons finished so far: Basic function – Move character, Basic attack, Skill Use, QuickSlot Use and Item – Gear Wear at [6:35](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=395s); these are the `Quest_Title_Help_<n>` strings of quests 1, 700, 701, 722 and 704 ([[gameplay/video-character-creation-and-tutorial]] §2). *video + client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-character-creation-and-tutorial]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
