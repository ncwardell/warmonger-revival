---
title: "[Weekly] Monster Hunt"
type: "quest"
id: 960
status: "complete"
missing: []
sources: ["client: Quest.cdb id 960", "client: NoticeQuest.cdb id 5"]
name_key: "Quest_Title_953"
kind: 10
kind_name: "Weekly"
level: {"min": 28}
giver: {"board": 5}
turn_in: {"auto": true}
periodic: {"reset": "weekly", "mask_bit": 1}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 28}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "target": "any_monster", "count": 250, "text_key": "Quest_QuickText_953_1"}
rewards:
  - {"type": 1, "what": "item", "item": 688, "count": 10, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 1001, "count": 1, "pick": "fixed"}
help: {"text_key": "Quest_Talk_dailyquest_Speech_4"}
board:
  - {"row": 5, "tab": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=08708a type=eb5b2b id=5af8ec sources=4c1d21 name_key=761b40 kind=b1d578 kind_name=f3fde7 level=84a59c giver=a65ed4 turn_in=847ad4 periodic=90c64e automatic=5ffe53 prev=97d170 next=97d170 prerequisites=c3110a stages=30caa7 objectives=f4ab24 rewards=4e2baa help=82d241 board=5d499a -->
|  |  |
|---|---|
| **Quest id** | `960` |
| **Kind** | Weekly (kind 10) |
| **Level** | 28+ |
| **Giver** | quest board (NoticeQuest row 5) |
| **Turn in** | automatic |
| **Repeats** | weekly (periodic done-mask bit 1; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |
| **Quest board** | row 5, Daily tab |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 28+ |

### Objectives

1. Kill any monster (target code 1) × 250 — tracker: “Monster Hunting (0/250)”

### Rewards

- **Basic reward:** [[wiki/items/688-dimensional-energy|Dimensional energy]] × 10; [[wiki/items/1001-medal-silver|Medal : Silver]]

### Tip window

> &lt;Weekly Quest&gt;Can only be done once a day,
> resets at 00:00 UTC+1. 
>
>  Every monster will be counted.
<!-- generated:end -->

## Notes

Weekly Monster Hunt: kill 250 monsters for 10 Dimensional Energy and 1 silver medal; weekly quests reset on Monday at 00:00 ([[gameplay/progression-and-economy]] §2, [[gameplay/server-rules]], *image*). The client row agrees: 10 × item 688 and 1 × item 1001. *image + client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/progression-and-economy]]
- [[gameplay/server-rules]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
