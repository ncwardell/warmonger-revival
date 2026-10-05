---
title: "[Weekly] Win in Mock Battle"
type: "quest"
id: 964
status: "stub"
missing: ["giver", "objectives"]
sources: ["client: Quest.cdb id 964"]
name_key: "Quest_Title_963"
kind: 10
kind_name: "Weekly"
level: {"min": 30}
giver: null
turn_in: {"auto": true}
periodic: {"reset": "weekly", "mask_bit": 16}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 30}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 6, "d": 10, "text_key": "Quest_QuickText_963_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 300000}
help: {"text_key": "Quest_Talk_dailyquest_Speech_14"}
---
<!-- generated:start -->
<!-- generated-keys: title=20b008 type=eb5b2b id=f03ac2 sources=0e34da name_key=d3118c kind=b1d578 kind_name=f3fde7 level=93fcd1 giver=2be88c turn_in=847ad4 periodic=bc78aa automatic=5ffe53 prev=97d170 next=97d170 prerequisites=0dd2f6 stages=30caa7 objectives=2be88c objectives_client=3f2a61 rewards=88daf9 help=7cbdfb -->
|  |  |
|---|---|
| **Quest id** | `964` |
| **Kind** | Weekly (kind 10) |
| **Level** | 30+ |
| **Giver** | **unknown** |
| **Turn in** | automatic |
| **Repeats** | weekly (periodic done-mask bit 16; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |

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

1. Type 15 — monster-area war / occupation?; values a=6, d=10 — tracker: “Win in Mock Battle”

### Rewards

- **Basic reward:** 300,000 exp

### Tip window

> &lt;Weekly Quest&gt;Can only be done once a week,
> resets every Monday at 00:00 UTC+1.
>
>  Win a Mock Battle against an enemy.
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
