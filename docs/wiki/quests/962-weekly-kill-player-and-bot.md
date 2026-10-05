---
title: "[Weekly] Kill Player and Bot"
type: "quest"
id: 962
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 962", "client: NoticeQuest.cdb id 7"]
name_key: "Quest_Title_955"
kind: 10
kind_name: "Weekly"
level: {"min": 29}
giver: {"board": 7}
turn_in: {"auto": true}
periodic: {"reset": "weekly", "mask_bit": 4}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 29}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 2, "what": null, "a": 5, "b": 70, "c": 1, "text_key": "Quest_QuickText_955_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 150000}
  - {"type": 4, "what": "gold", "amount": 100000}
help: {"text_key": "Quest_Talk_dailyquest_Speech_6"}
board:
  - {"row": 7, "tab": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=07d17e type=eb5b2b id=89c48c sources=944495 name_key=bab9cb kind=b1d578 kind_name=f3fde7 level=6d8d3c giver=4cde45 turn_in=847ad4 periodic=440243 automatic=5ffe53 prev=97d170 next=97d170 prerequisites=1efb5e stages=30caa7 objectives=2be88c objectives_client=6bed45 rewards=0771c9 help=0e023b board=359b5e -->
|  |  |
|---|---|
| **Quest id** | `962` |
| **Kind** | Weekly (kind 10) |
| **Level** | 29+ |
| **Giver** | quest board (NoticeQuest row 7) |
| **Turn in** | automatic |
| **Repeats** | weekly (periodic done-mask bit 4; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |
| **Quest board** | row 7, Daily tab |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 29+ |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 2 — kill enemy players?; values a=5, b=70, c=1 — tracker: “Destroy the enemy player and Bot from the Gaia field”

### Rewards

- **Basic reward:** 150,000 exp; 100,000 gold

### Tip window

> &lt;Weekly Quest&gt;Can only be done once a week,
>  resets every Monday at 00:00 UTC+1. 
>
> Kill enemy players and Bot. [Gaia Field]
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
