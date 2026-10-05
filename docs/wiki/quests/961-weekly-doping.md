---
title: "[Weekly] Doping"
type: "quest"
id: 961
status: "partial"
missing: ["rewards"]
sources: ["client: Quest.cdb id 961", "client: NoticeQuest.cdb id 6", "image: [[gameplay/progression-and-economy]] §2 (Doping = craft consumables; the monthly row's 200 matches b, so b = count); count 20 = client b"]
manual: ["objectives"]
name_key: "Quest_Title_954"
kind: 10
kind_name: "Weekly"
level: {"min": 28}
giver: {"board": 6}
turn_in: {"auto": true}
periodic: {"reset": "weekly", "mask_bit": 2}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 28}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 26, "what": "craft_consumable", "count": 20, "a": 1, "text_key": "Quest_QuickText_954_1"}
objectives_client:
  - {"n": 1, "type": 26, "what": null, "a": 1, "b": 20, "text_key": "Quest_QuickText_954_1"}
rewards: null
rewards_client:
  - {"type": 10, "what": null, "a": 100}
help: {"text_key": "Quest_Talk_dailyquest_Speech_5"}
board:
  - {"row": 6, "tab": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=07b29d type=eb5b2b id=1f37ad sources=18252b name_key=53ddba kind=b1d578 kind_name=f3fde7 level=84a59c giver=aeb1e0 turn_in=847ad4 periodic=f596a6 automatic=5ffe53 prev=97d170 next=97d170 prerequisites=c3110a stages=30caa7 objectives_client=cf51d4 rewards=2be88c rewards_client=aa3b46 help=106933 board=25fbff -->
|  |  |
|---|---|
| **Quest id** | `961` |
| **Kind** | Weekly (kind 10) |
| **Level** | 28+ |
| **Giver** | quest board (NoticeQuest row 6) |
| **Turn in** | automatic |
| **Repeats** | weekly (periodic done-mask bit 2; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |
| **Quest board** | row 6, Daily tab |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 28+ |

### Objectives

1. Type 26 — craft gear (category a)?; values a=1 — tracker: “Make [A~S] Grade Scroll, Tome, Flask, Elixir (0/20)”

### Rewards

> [!warning] Not all reward types are decoded
> The rows below are the client's (`rewards_client`). Write the server-ready list into `rewards:` once the unclear ones are understood.

- Type 10 — unknown 10; values a=100

### Tip window

> &lt;Weekly Quest&gt;Can only be done once a week,
>  resets every Monday at 00:00 UTC+1. 
>
> Craft [A~S]Doping (Scroll / Tome / Flask / Elixir)
<!-- generated:end -->

## Notes

Weekly Doping: craft consumables ([[gameplay/progression-and-economy]] §2, *image*). *image*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/progression-and-economy]]
- [[gameplay/patch-history]]

## Open questions

Reward types 10 and 5 are not decoded. The guides say max-level daily/weekly/monthly quests pay yellow jewels ([[gameplay/progression-and-economy]] §2), and WM 0726 gave daily quests more jewels and fame ([[gameplay/patch-history]]); type 10 = jewels and type 5 = fame would fit, but that is a guess.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
