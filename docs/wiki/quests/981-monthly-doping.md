---
title: "[Monthly] Doping"
type: "quest"
id: 981
status: "partial"
missing: ["rewards"]
sources: ["client: Quest.cdb id 981", "client: NoticeQuest.cdb id 11", "image: [[gameplay/progression-and-economy]] §2 (monthly Doping = make 200 A-S scrolls/tomes/flasks/elixirs)"]
manual: ["objectives"]
name_key: "Quest_Title_958"
kind: 11
kind_name: "Monthly"
level: {"min": 29}
giver: {"board": 11}
turn_in: {"auto": true}
periodic: {"reset": "monthly", "mask_bit": 2}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 29}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 26, "what": "craft_consumable", "count": 200, "a": 1, "text_key": "Quest_QuickText_958_1"}
objectives_client:
  - {"n": 1, "type": 26, "what": null, "a": 1, "b": 200, "text_key": "Quest_QuickText_958_1"}
rewards: null
rewards_client:
  - {"type": 10, "what": null, "a": 300}
help: {"text_key": "Quest_Talk_dailyquest_Speech_9"}
board:
  - {"row": 11, "tab": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=cae099 type=eb5b2b id=32f9e6 sources=a06413 name_key=f06d45 kind=17ba07 kind_name=b2d8d4 level=6d8d3c giver=701ce3 turn_in=847ad4 periodic=13d106 automatic=5ffe53 prev=97d170 next=97d170 prerequisites=1efb5e stages=30caa7 objectives=2be88c objectives_client=12cb1f rewards=2be88c rewards_client=f4f1ba help=169625 board=8cd9a1 -->
|  |  |
|---|---|
| **Quest id** | `981` |
| **Kind** | Monthly (kind 11) |
| **Level** | 29+ |
| **Giver** | quest board (NoticeQuest row 11) |
| **Turn in** | automatic |
| **Repeats** | monthly (periodic done-mask bit 2; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |
| **Quest board** | row 11, Daily tab |

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

1. Type 26 — craft gear (category a)?; values a=1, b=200 — tracker: “Make [A~S] Scroll, Tome, Flask, Elixir”

### Rewards

> [!warning] Not all reward types are decoded
> The rows below are the client's (`rewards_client`). Write the server-ready list into `rewards:` once the unclear ones are understood.

- Type 10 — unknown 10; values a=300

### Tip window

> &lt;Monthly Quest&gt;Can only be done once a Month,
> resets on the 1st of every month at 00:00 UTC+1. 
>
> Craft [A~S]Doping (Scroll / Tome / Flask / Elixir)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]]
<!-- generated:end -->

## Notes

Monthly Doping: make 200 A–S grade scrolls, tomes, flasks or elixirs ([[gameplay/progression-and-economy]] §2, strategy guide *image*). Alchemy recipes are on [[gameplay/consumables]]. *image*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/progression-and-economy]]
- [[gameplay/consumables]]
- [[gameplay/patch-history]]

## Open questions

Reward types 10 and 5 are not decoded. The guides say max-level daily/weekly/monthly quests pay yellow jewels ([[gameplay/progression-and-economy]] §2), and WM 0726 gave daily quests more jewels and fame ([[gameplay/patch-history]]); type 10 = jewels and type 5 = fame would fit, but that is a guess.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
