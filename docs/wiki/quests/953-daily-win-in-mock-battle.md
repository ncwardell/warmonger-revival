---
title: "[Daily] Win in Mock Battle"
type: "quest"
id: 953
status: "stub"
missing: ["giver", "objectives"]
sources: ["client: Quest.cdb id 953"]
name_key: "Quest_Title_962"
kind: 9
kind_name: "Daily"
level: {"min": 30}
giver: null
turn_in: {"auto": true}
periodic: {"reset": "daily", "mask_bit": 8}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 30}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 6, "d": 1, "text_key": "Quest_QuickText_962_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 100000}
help: {"text_key": "Quest_Talk_dailyquest_Speech_13"}
---
<!-- generated:start -->
<!-- generated-keys: title=ba1d7f type=eb5b2b id=933580 sources=b2054b name_key=7806bf kind=0ade7c kind_name=b6566f level=93fcd1 giver=2be88c turn_in=847ad4 periodic=e26f4c automatic=5ffe53 prev=97d170 next=97d170 prerequisites=0dd2f6 stages=30caa7 objectives=2be88c objectives_client=74f88a rewards=cc23b9 help=5ca371 -->
|  |  |
|---|---|
| **Quest id** | `953` |
| **Kind** | Daily (kind 9) |
| **Level** | 30+ |
| **Giver** | **unknown** |
| **Turn in** | automatic |
| **Repeats** | daily (periodic done-mask bit 8; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
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

1. Type 15 — monster-area war / occupation?; values a=6, d=1 — tracker: “Win in Mock Battle”

### Rewards

- **Basic reward:** 100,000 exp

### Tip window

> &lt;Daily Quest&gt;Can only be done once a day, 
> resets at 00:00 UTC+1.  
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
