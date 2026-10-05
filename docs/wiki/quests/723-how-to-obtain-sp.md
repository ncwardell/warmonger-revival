---
title: "How to obtain SP"
type: "quest"
id: 723
status: "complete"
missing: []
sources: ["client: Quest.cdb id 723", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "video: [[gameplay/video-tutorial-walkthrough]] steps 3-5 (lesson exp shown = table value)"]
name_key: "Quest_Title_723"
kind: 2
kind_name: "Guide"
giver: {"auto": true}
turn_in: {"auto": true}
bit: 54
automatic: true
prev: []
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 13, "what": "use_item", "item": 948, "count": 1, "text_key": "Quest_QuickText_723_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 5000, "shown": 5000}
help: {"image": "ui/HelpImage/Help_23.png", "text_key": "Quest_HelpText_741"}
---
<!-- generated:start -->
<!-- generated-keys: title=69a5b7 type=eb5b2b id=f5354c sources=0a353e name_key=421dfb kind=da4b92 kind_name=875cc6 giver=847ad4 turn_in=847ad4 bit=80e28a automatic=5ffe53 prev=97d170 next=97d170 stages=30caa7 objectives=f58890 rewards=c8c2ac help=b393d0 -->
|  |  |
|---|---|
|  | ![How to obtain SP](wiki/assets/quests/723.png) |
| **Quest id** | `723` |
| **Kind** | Guide (kind 2) |
| **Giver** | automatic |
| **Turn in** | automatic |
| **Completion bit** | 54 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Use [[wiki/items/948-auto-decomposition-hammer|Auto decomposition hammer]] — tracker: “Automatism decomposition item use (0/1)”

### Rewards

- **Basic reward:** 5,000 exp

### Tip window

> Use auto decomposition hammer item and auto decomposition point will be increase 
>  Achieve item will be decompose automatically for item's condition

Image `ui/HelpImage/Help_23.png`.

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: at [25:55](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1555s)
<!-- generated:end -->

## Notes

Shown on screen as "How to obtain SP" in June 2018 ([25:55](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1555s), [[gameplay/video-character-creation-and-tutorial]] §3 After the tutorial). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-character-creation-and-tutorial]]

## Open questions

[[gameplay/video-character-creation-and-tutorial]] says the client string for this lesson reads "Automatism decomposition point recharging" although the objective text matches; this wiki's title comes from the client and reads "How to obtain SP", so the two string tables may differ.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
