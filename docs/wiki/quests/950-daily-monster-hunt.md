---
title: "[Daily] Monster Hunt"
type: "quest"
id: 950
status: "complete"
missing: []
sources: ["client: Quest.cdb id 950", "client: NoticeQuest.cdb id 1"]
name_key: "Quest_Title_950"
kind: 9
kind_name: "Daily"
level: {"min": 27}
giver: {"board": 1}
turn_in: {"auto": true}
periodic: {"reset": "daily", "mask_bit": 1}
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 27}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "target": "any_monster", "count": 50, "text_key": "Quest_QuickText_950_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 100000}
  - {"type": 1, "what": "item", "item": 1000, "count": 1, "pick": "fixed"}
help: {"text_key": "Quest_Talk_dailyquest_Speech_1"}
board:
  - {"row": 1, "tab": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=cdf67d type=eb5b2b id=b63c6a sources=5ffa9f name_key=3a9cfc kind=0ade7c kind_name=b6566f level=8c32e3 giver=62b6a9 turn_in=847ad4 periodic=8eba0e automatic=5ffe53 prev=97d170 next=97d170 prerequisites=eb6b9f stages=30caa7 objectives=5217e9 rewards=f4c3cf help=b6e8a2 board=5c59e2 -->
|  |  |
|---|---|
| **Quest id** | `950` |
| **Kind** | Daily (kind 9) |
| **Level** | 27+ |
| **Giver** | quest board (NoticeQuest row 1) |
| **Turn in** | automatic |
| **Repeats** | daily (periodic done-mask bit 1; contract: resets daily 00:00 UTC+1 / Monday / the 1st) |
| **Automatic flag** | set (c14@11) |
| **Quest board** | row 1, Daily tab |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 27+ |

### Objectives

1. Kill any monster (target code 1) × 50 — tracker: “Monster Hunting (0/50)”

### Rewards

- **Basic reward:** 100,000 exp; [[wiki/items/1000-medal-bronze|Medal : Bronze]]

### Tip window

> &lt;Daily Quest&gt;Can only be done once a day,
> resets at 00:00 UTC+1. 
>
> Every monster will be counted.
<!-- generated:end -->

## Notes

Daily Monster Hunt: kill 50 monsters for 100,000 exp and 1 bronze medal; daily quests reset every day at 00:00 ([[gameplay/progression-and-economy]] §2, [[gameplay/server-rules]], *image*). The client row agrees (100,000 exp + Medal: Bronze 1000). From WM 0726 the daily-quest panel opens on its own above level 27 ([[gameplay/patch-history]]); this row's minimum level is 27. In Crush Online Season 2 players could take up to 3 daily, 4 weekly and 5 monthly quests ([[gameplay/crush-patch-notes]]). *image + client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/progression-and-economy]]
- [[gameplay/server-rules]]
- [[gameplay/patch-history]]
- [[gameplay/crush-patch-notes]]

## Open questions

A 2018 patch says Abyss kills stopped counting for "the daily kill quest" ([[gameplay/patch-history]], Dungeons and world); whether that means this quest is not stated.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
