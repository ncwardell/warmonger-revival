---
title: "Basic function - Skill Use"
type: "quest"
id: 1503
status: "partial"
missing: ["turn_in"]
sources: ["client: Quest.cdb id 1503", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)"]
name_key: "Quest_Title_Help_667"
kind: 12
kind_name: "Advice"
giver: {"auto": true}
turn_in: null
bit: 71
prev: []
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 10001, "what": "client_attack", "param": 1, "text_key": "Quest_QuickText_Help_667_1"}
rewards: []
help: {"image": "ui/HelpImage/Help_10.png", "text_key": "Quest_Title_Help_String_667"}
---
<!-- generated:start -->
<!-- generated-keys: title=09c9dd type=eb5b2b id=e6cfa8 sources=092cb0 name_key=029331 kind=7b5200 kind_name=ec7dd4 giver=847ad4 turn_in=2be88c bit=d02560 prev=97d170 next=97d170 stages=30caa7 objectives=5e471c rewards=97d170 help=2d062e -->
|  |  |
|---|---|
|  | ![Basic function - Skill Use](wiki/assets/quests/1503.png) |
| **Quest id** | `1503` |
| **Kind** | Advice (kind 12) |
| **Giver** | automatic |
| **Turn in** | **unknown** |
| **Completion bit** | 71 |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 71 with:** [[wiki/quests/701-basic-combat-lesson-2|Basic Combat Lesson 2]] (completing one closes the others)

### Objectives

1. client event: attack / skill used (a = 1) — tracker: “Try one of your skills.”

### Rewards

None in the client.

### Tip window

> You can use the skill by pressing the skill shortcut.

Image `ui/HelpImage/Help_10.png`.
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
