---
title: "[Weekly] Monster area wars"
type: "quest"
id: 965
status: "partial"
missing: ["objectives"]
sources: ["client: Quest.cdb id 965", "client: NoticeQuest.cdb id 8"]
name_key: "Quest_Title_966"
kind: 10
kind_name: "Weekly"
level: {"min": 29}
giver: {"board": 8}
turn_in: {"auto": true}
periodic: {"reset": "weekly", "mask_bit": 32}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 29}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 3, "d": 5, "text_key": "Quest_QuickText_966_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 100000}
  - {"type": 1, "what": "item", "item": 1002, "count": 1, "pick": "fixed"}
help: {"text_key": "Quest_Talk_dailyquest_Speech_17"}
board:
  - {"row": 8, "tab": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=604cce type=eb5b2b id=ab7103 sources=112075 name_key=d1c598 kind=b1d578 kind_name=f3fde7 level=6d8d3c giver=0cba69 turn_in=847ad4 periodic=bfc105 automatic=5ffe53 prev=97d170 next=97d170 prerequisites=1efb5e stages=30caa7 objectives=2be88c objectives_client=db0387 rewards=5f9551 help=36cde1 board=70992c -->
|  |  |
|---|---|
| **Quest id** | `965` |
| **Kind** | Weekly (kind 10) |
| **Level** | 29+ |
| **Giver** | quest board (NoticeQuest row 8) |
| **Turn in** | automatic |
| **Repeats** | weekly (periodic done-mask bit 32; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |
| **Quest board** | row 8, Daily tab |

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

1. Type 15 — monster-area war / occupation?; values a=3, d=5 — tracker: “Monster area wars”

### Rewards

- **Basic reward:** 100,000 exp; [[wiki/items/1002-medal-gold|Medal : Gold]]

### Tip window

> &lt;Weekly Quest&gt;Can only be done once a week,
>  resets every Monday at 00:00 UTC+1.
>
> Win at Monster area wars.
<!-- generated:end -->

## Notes

From WM 1107 the daily, weekly and monthly Monster Area Wars quests also count War of Warmonger ([[gameplay/patch-history]]). *patch notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/patch-history]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
