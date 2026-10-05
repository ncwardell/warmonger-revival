---
title: "[Monthly] Kill Player and Bot"
type: "quest"
id: 982
status: "complete"
missing: []
sources: ["client: Quest.cdb id 982", "client: NoticeQuest.cdb id 12", "image: [[gameplay/pvp-and-matches]], [[gameplay/skull-artifact-set]] (monthly Kill Player = 240 kills, tracker 80/240)"]
manual: ["objectives"]
name_key: "Quest_Title_959"
kind: 11
kind_name: "Monthly"
level: {"min": 30}
giver: {"board": 12}
turn_in: {"auto": true}
periodic: {"reset": "monthly", "mask_bit": 4}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 30}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 2, "what": "kill_player", "count": 240, "a": 5, "c": 1, "text_key": "Quest_QuickText_959_1"}
objectives_client:
  - {"n": 1, "type": 2, "what": null, "a": 5, "b": 240, "c": 1, "text_key": "Quest_QuickText_959_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 400000}
  - {"type": 4, "what": "gold", "amount": 200000}
help: {"text_key": "Quest_Talk_dailyquest_Speech_10"}
board:
  - {"row": 12, "tab": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=5cd8b0 type=eb5b2b id=1047b5 sources=cded61 name_key=8097a3 kind=17ba07 kind_name=b2d8d4 level=93fcd1 giver=31c9a1 turn_in=847ad4 periodic=fc9f25 automatic=5ffe53 prev=97d170 next=97d170 prerequisites=0dd2f6 stages=30caa7 objectives=2be88c objectives_client=4057ee rewards=15183d help=1f5b0b board=184d9a -->
|  |  |
|---|---|
| **Quest id** | `982` |
| **Kind** | Monthly (kind 11) |
| **Level** | 30+ |
| **Giver** | quest board (NoticeQuest row 12) |
| **Turn in** | automatic |
| **Repeats** | monthly (periodic done-mask bit 4; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |
| **Quest board** | row 12, Daily tab |

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

1. Type 2 — kill enemy players?; values a=5, b=240, c=1 — tracker: “Destroy the enemy player and Bot from the Gaia field”

### Rewards

- **Basic reward:** 400,000 exp; 200,000 gold

### Tip window

> &lt;Monthly Quest&gt;Can only be done once a Month,
> resets on the 1st of every month at 00:00 UTC+1.  
>
> Kill enemy players and bot. [Gaia Field]
<!-- generated:end -->

## Notes

Monthly Kill Player: 240 kills; one screenshot's tracker reads 80/240 ([[gameplay/pvp-and-matches]], [[gameplay/skull-artifact-set]], *image*). From WM 0124 bot kills count ([[gameplay/events-and-schedules]] §1). *image*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/pvp-and-matches]]
- [[gameplay/skull-artifact-set]]
- [[gameplay/events-and-schedules]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
