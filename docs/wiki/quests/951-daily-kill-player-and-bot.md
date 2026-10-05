---
title: "[Daily] Kill Player and Bot"
type: "quest"
id: 951
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 951", "client: NoticeQuest.cdb id 2"]
name_key: "Quest_Title_951"
kind: 9
kind_name: "Daily"
level: {"min": 28}
giver: {"board": 2}
turn_in: {"auto": true}
periodic: {"reset": "daily", "mask_bit": 2}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 28}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 2, "what": null, "a": 5, "b": 10, "c": 1, "text_key": "Quest_QuickText_951_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 100000}
  - {"type": 4, "what": "gold", "amount": 50000}
help: {"text_key": "Quest_Talk_dailyquest_Speech_2"}
board:
  - {"row": 2, "tab": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=5e0890 type=eb5b2b id=69fa65 sources=df6b7b name_key=730f24 kind=0ade7c kind_name=b6566f level=84a59c giver=e2bffb turn_in=847ad4 periodic=e8ab7f automatic=5ffe53 prev=97d170 next=97d170 prerequisites=c3110a stages=30caa7 objectives=2be88c objectives_client=d4c61b rewards=d06c9a help=c5042f board=266e71 -->
|  |  |
|---|---|
| **Quest id** | `951` |
| **Kind** | Daily (kind 9) |
| **Level** | 28+ |
| **Giver** | quest board (NoticeQuest row 2) |
| **Turn in** | automatic |
| **Repeats** | daily (periodic done-mask bit 2; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |
| **Quest board** | row 2, Daily tab |

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

1. Type 2 — kill enemy players?; values a=5, b=10, c=1 — tracker: “Destroy the enemy player and Bot from the Gaia field”

### Rewards

- **Basic reward:** 100,000 exp; 50,000 gold

### Tip window

> &lt;Daily Quest&gt;Only can do one time a day,
>  resets at 00:00 UTC+1. 
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
