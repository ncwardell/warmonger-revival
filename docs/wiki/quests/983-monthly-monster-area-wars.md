---
title: "[Monthly] Monster area wars"
type: "quest"
id: 983
status: "partial"
missing: ["objectives"]
sources: ["client: Quest.cdb id 983", "client: NoticeQuest.cdb id 13"]
name_key: "Quest_Title_960"
kind: 11
kind_name: "Monthly"
level: {"min": 30}
giver: {"board": 13}
turn_in: {"auto": true}
periodic: {"reset": "monthly", "mask_bit": 8}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 30}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 3, "d": 20, "text_key": "Quest_QuickText_960_1"}
rewards:
  - {"type": 1, "what": "item", "item": 999, "count": 1, "pick": "fixed"}
help: {"text_key": "Quest_Talk_dailyquest_Speech_11"}
board:
  - {"row": 13, "tab": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=a67cb9 type=eb5b2b id=0514ab sources=e68460 name_key=dce4ec kind=17ba07 kind_name=b2d8d4 level=93fcd1 giver=cf5000 turn_in=847ad4 periodic=7b3258 automatic=5ffe53 prev=97d170 next=97d170 prerequisites=0dd2f6 stages=30caa7 objectives=2be88c objectives_client=9c1c85 rewards=a0782e help=7ebff6 board=b302e2 -->
|  |  |
|---|---|
| **Quest id** | `983` |
| **Kind** | Monthly (kind 11) |
| **Level** | 30+ |
| **Giver** | quest board (NoticeQuest row 13) |
| **Turn in** | automatic |
| **Repeats** | monthly (periodic done-mask bit 8; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |
| **Quest board** | row 13, Daily tab |

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

1. Type 15 — monster-area war / occupation?; values a=3, d=20 — tracker: “Monster area wars”

### Rewards

- **Basic reward:** [[wiki/items/999-medal-mithril|Medal : Mithril]]

### Tip window

> &lt;Monthly Quest&gt;Can only be done once a Month,
> resets on the 1st of every month at 00:00 UTC+1.  
>
> Win in Monster area wars.

### Mentioned in

- [[gameplay/patch-history|Patch notes and other sources]]
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
