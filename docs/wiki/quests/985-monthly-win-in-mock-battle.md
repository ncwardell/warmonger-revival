---
title: "[Monthly] Win in Mock Battle"
type: "quest"
id: 985
status: "stub"
missing: ["giver", "objectives"]
sources: ["client: Quest.cdb id 985"]
name_key: "Quest_Title_964"
kind: 11
kind_name: "Monthly"
level: {"min": 30}
giver: null
turn_in: {"auto": true}
periodic: {"reset": "monthly", "mask_bit": 32}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 30}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 6, "d": 50, "text_key": "Quest_QuickText_964_1"}
rewards:
  - {"type": 1, "what": "item", "item": 1002, "count": 5, "pick": "fixed"}
help: {"text_key": "Quest_Talk_dailyquest_Speech_15"}
---
<!-- generated:start -->
<!-- generated-keys: title=e96636 type=eb5b2b id=9486dd sources=c4e992 name_key=07dde7 kind=17ba07 kind_name=b2d8d4 level=93fcd1 giver=2be88c turn_in=847ad4 periodic=0fd416 automatic=5ffe53 prev=97d170 next=97d170 prerequisites=0dd2f6 stages=30caa7 objectives=2be88c objectives_client=c55170 rewards=7e3cbd help=b9893d -->
|  |  |
|---|---|
| **Quest id** | `985` |
| **Kind** | Monthly (kind 11) |
| **Level** | 30+ |
| **Giver** | **unknown** |
| **Turn in** | automatic |
| **Repeats** | monthly (periodic done-mask bit 32; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
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

1. Type 15 — monster-area war / occupation?; values a=6, d=50 — tracker: “Win in Mock Battle”

### Rewards

- **Basic reward:** [[wiki/items/1002-medal-gold|Medal : Gold]] × 5

### Tip window

> &lt;Monthly Quest&gt;Can only be done once a Month,
> resets on the 1st of every month at 00:00 UTC+1. 
>
> Win a Mock Battle against an enemy.
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
