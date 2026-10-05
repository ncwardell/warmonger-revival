---
title: "[Daily] Win in Battle"
type: "quest"
id: 952
status: "partial"
missing: ["objectives", "rewards"]
sources: ["client: Quest.cdb id 952", "client: NoticeQuest.cdb id 4"]
name_key: "Quest_Title_952"
kind: 9
kind_name: "Daily"
level: {"min": 30}
giver: {"board": 4}
turn_in: {"auto": true}
periodic: {"reset": "daily", "mask_bit": 4}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 30}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 2, "d": 1, "text_key": "Quest_QuickText_952_1"}
rewards: null
rewards_client:
  - {"type": 10, "what": null, "a": 200}
  - {"type": 5, "what": null, "a": 300}
help: {"text_key": "Quest_Talk_dailyquest_Speech_3"}
board:
  - {"row": 4, "tab": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=d6cdf2 type=eb5b2b id=da5e05 sources=b61618 name_key=0df427 kind=0ade7c kind_name=b6566f level=93fcd1 giver=686e4b turn_in=847ad4 periodic=3bb2dc automatic=5ffe53 prev=97d170 next=97d170 prerequisites=0dd2f6 stages=30caa7 objectives=2be88c objectives_client=4a4d04 rewards=2be88c rewards_client=33591a help=07c31e board=a60423 -->
|  |  |
|---|---|
| **Quest id** | `952` |
| **Kind** | Daily (kind 9) |
| **Level** | 30+ |
| **Giver** | quest board (NoticeQuest row 4) |
| **Turn in** | automatic |
| **Repeats** | daily (periodic done-mask bit 4; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |
| **Quest board** | row 4, Daily tab |

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

1. Type 15 — monster-area war / occupation?; values a=2, d=1 — tracker: “Win in field battle”

### Rewards

> [!warning] Not all reward types are decoded
> The rows below are the client's (`rewards_client`). Write the server-ready list into `rewards:` once the unclear ones are understood.

- Type 10 — unknown 10; values a=200
- Type 5 — fame?; values a=300

### Tip window

> &lt;Daily Quest&gt;Can only be done once a day,
> resets at 00:00 UTC+1.
>
> Win a Field Battle against an enemy.
<!-- generated:end -->

## Notes

Daily, weekly and monthly "Win in Battle" quests appear in the guides' quest window; queued battles existed alongside land wars ([[gameplay/progression-and-economy]] §2, [[gameplay/pvp-and-matches]], *image*).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/progression-and-economy]]
- [[gameplay/pvp-and-matches]]
- [[gameplay/patch-history]]

## Open questions

Reward types 10 and 5 are not decoded. The guides say max-level daily/weekly/monthly quests pay yellow jewels ([[gameplay/progression-and-economy]] §2), and WM 0726 gave daily quests more jewels and fame ([[gameplay/patch-history]]); type 10 = jewels and type 5 = fame would fit, but that is a guess.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
