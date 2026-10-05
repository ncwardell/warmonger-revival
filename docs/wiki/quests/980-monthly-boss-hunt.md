---
title: "[Monthly] Boss Hunt"
type: "quest"
id: 980
status: "complete"
missing: []
sources: ["client: Quest.cdb id 980", "client: NoticeQuest.cdb id 10"]
name_key: "Quest_Title_957"
kind: 11
kind_name: "Monthly"
level: {"min": 29}
giver: {"board": 10}
turn_in: {"auto": true}
periodic: {"reset": "monthly", "mask_bit": 1}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 29}
stages: [1, 2, 3, 4, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "target": "any_boss", "count": 50, "text_key": "Quest_QuickText_957_1"}
rewards:
  - {"type": 1, "what": "item", "item": 688, "count": 20, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 1002, "count": 1, "pick": "fixed"}
help: {"text_key": "Quest_Talk_dailyquest_Speech_8"}
board:
  - {"row": 10, "tab": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=58a974 type=eb5b2b id=cb6c53 sources=b5af5b name_key=449fc1 kind=17ba07 kind_name=b2d8d4 level=6d8d3c giver=897800 turn_in=847ad4 periodic=7598aa automatic=5ffe53 prev=97d170 next=97d170 prerequisites=1efb5e stages=e37647 objectives=259f7d rewards=94e11d help=022b0f board=b772bd -->
|  |  |
|---|---|
| **Quest id** | `980` |
| **Kind** | Monthly (kind 11) |
| **Level** | 29+ |
| **Giver** | quest board (NoticeQuest row 10) |
| **Turn in** | automatic |
| **Repeats** | monthly (periodic done-mask bit 1; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |
| **Quest board** | row 10, Daily tab |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 29+ |

### Objectives

1. Kill any boss (target code 3) × 50 — tracker: “Boss Hunting (0/50)”

Stages (`flag1..5` = [1, 2, 3, 4, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** [[wiki/items/688-dimensional-energy|Dimensional energy]] × 20; [[wiki/items/1002-medal-gold|Medal : Gold]]

### Tip window

> &lt;Monthly Quest&gt;Only can do one time a Month,
> Reset Every 1st 00:00. 
>
> Every boss will be counted.

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]]
- [[gameplay/progression-and-economy|Progression and economy]]
- [[gameplay/server-rules|Server rules checklist]]
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
