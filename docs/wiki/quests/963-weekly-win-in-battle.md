---
title: "[Weekly] Win in battle"
type: "quest"
id: 963
status: "stub"
missing: ["objectives", "rewards"]
sources: ["client: Quest.cdb id 963", "client: NoticeQuest.cdb id 9"]
name_key: "Quest_Title_956"
kind: 10
kind_name: "Weekly"
level: {"min": 30}
giver: {"board": 9}
turn_in: {"auto": true}
periodic: {"reset": "weekly", "mask_bit": 8}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 30}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 2, "d": 10, "text_key": "Quest_QuickText_956_1"}
rewards: null
rewards_client:
  - {"type": 10, "what": null, "a": 500}
  - {"type": 5, "what": null, "a": 1000}
help: {"text_key": "Quest_Talk_dailyquest_Speech_7"}
board:
  - {"row": 9, "tab": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=886c6c type=eb5b2b id=4b1a62 sources=e96e9d name_key=8ce646 kind=b1d578 kind_name=f3fde7 level=93fcd1 giver=df9e1e turn_in=847ad4 periodic=74c4ae automatic=5ffe53 prev=97d170 next=97d170 prerequisites=0dd2f6 stages=30caa7 objectives=2be88c objectives_client=efb832 rewards=2be88c rewards_client=497d06 help=321373 board=2c0ba0 -->
|  |  |
|---|---|
| **Quest id** | `963` |
| **Kind** | Weekly (kind 10) |
| **Level** | 30+ |
| **Giver** | quest board (NoticeQuest row 9) |
| **Turn in** | automatic |
| **Repeats** | weekly (periodic done-mask bit 8; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |
| **Quest board** | row 9, Daily tab |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 30+ |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 15 — monster-area war / occupation?; values a=2, d=10 — tracker: “Win in field battle”

### Rewards

> [!warning] Not all reward types are decoded
> The rows below are the client's (`rewards_client`). Write the server-ready list into `rewards:` once the unclear ones are understood.

- Type 10 — unknown 10; values a=500
- Type 5 — fame?; values a=1000

### Tip window

> &lt;Weekly Quest&gt;Can only be done once a week,
>  resets every Monday at 00:00 UTC+1. 
>
> Win a Field Battle against an enemy.
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
