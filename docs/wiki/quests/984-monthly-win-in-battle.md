---
title: "[Monthly] Win in battle"
type: "quest"
id: 984
status: "partial"
missing: ["objectives", "rewards"]
sources: ["client: Quest.cdb id 984", "client: NoticeQuest.cdb id 14"]
name_key: "Quest_Title_961"
kind: 11
kind_name: "Monthly"
level: {"min": 30}
giver: {"board": 14}
turn_in: {"auto": true}
periodic: {"reset": "monthly", "mask_bit": 16}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 30}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 2, "d": 50, "text_key": "Quest_QuickText_961_1"}
rewards: null
rewards_client:
  - {"type": 10, "what": null, "a": 1000}
  - {"type": 5, "what": null, "a": 2000}
help: {"text_key": "Quest_Talk_dailyquest_Speech_12"}
board:
  - {"row": 14, "tab": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=977a2b type=eb5b2b id=388e77 sources=5fee68 name_key=96da0d kind=17ba07 kind_name=b2d8d4 level=93fcd1 giver=e37db7 turn_in=847ad4 periodic=7abe24 automatic=5ffe53 prev=97d170 next=97d170 prerequisites=0dd2f6 stages=30caa7 objectives=2be88c objectives_client=7b4395 rewards=2be88c rewards_client=6955a4 help=ef2769 board=67430a -->
|  |  |
|---|---|
| **Quest id** | `984` |
| **Kind** | Monthly (kind 11) |
| **Level** | 30+ |
| **Giver** | quest board (NoticeQuest row 14) |
| **Turn in** | automatic |
| **Repeats** | monthly (periodic done-mask bit 16; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |
| **Quest board** | row 14, Daily tab |

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

1. Type 15 — monster-area war / occupation?; values a=2, d=50 — tracker: “Win in field battle”

### Rewards

> [!warning] Not all reward types are decoded
> The rows below are the client's (`rewards_client`). Write the server-ready list into `rewards:` once the unclear ones are understood.

- Type 10 — unknown 10; values a=1000
- Type 5 — fame?; values a=2000

### Tip window

> &lt;Monthly Quest&gt;Can only be done once a Month,
> resets on the 1st of every month at 00:00 UTC+1.  
>
>  Win a Field Battle against an enemy.
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
