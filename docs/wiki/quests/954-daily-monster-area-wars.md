---
title: "[Daily] Monster area wars"
type: "quest"
id: 954
status: "partial"
missing: ["objectives"]
sources: ["client: Quest.cdb id 954", "client: NoticeQuest.cdb id 3"]
name_key: "Quest_Title_965"
kind: 9
kind_name: "Daily"
level: {"min": 28}
giver: {"board": 3}
turn_in: {"auto": true}
periodic: {"reset": "daily", "mask_bit": 16}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 28}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 3, "d": 1, "text_key": "Quest_QuickText_965_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 100000}
  - {"type": 1, "what": "item", "item": 1001, "count": 1, "pick": "fixed"}
help: {"text_key": "Quest_Talk_dailyquest_Speech_16"}
board:
  - {"row": 3, "tab": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=86cc6c type=eb5b2b id=b3be0e sources=388804 name_key=daed3c kind=0ade7c kind_name=b6566f level=84a59c giver=a79521 turn_in=847ad4 periodic=c4583e automatic=5ffe53 prev=97d170 next=97d170 prerequisites=c3110a stages=30caa7 objectives=2be88c objectives_client=51d62c rewards=3ae655 help=336576 board=f5c302 -->
|  |  |
|---|---|
| **Quest id** | `954` |
| **Kind** | Daily (kind 9) |
| **Level** | 28+ |
| **Giver** | quest board (NoticeQuest row 3) |
| **Turn in** | automatic |
| **Repeats** | daily (periodic done-mask bit 16; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |
| **Quest board** | row 3, Daily tab |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 28+ |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 15 — monster-area war / occupation?; values a=3, d=1 — tracker: “Monster area wars”

### Rewards

- **Basic reward:** 100,000 exp; [[wiki/items/1001-medal-silver|Medal : Silver]]

### Tip window

> &lt;Daily Quest&gt;Can only be done once a day,
>  resets at 00:00 UTC+1. 
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
