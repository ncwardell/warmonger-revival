---
title: "Occupation of Monster Invasion Area"
type: "quest"
id: 696
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 696", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "video: [[gameplay/video-tutorial-walkthrough]] steps 3-5 (lesson exp shown = table value)"]
name_key: "Quest_Title_697"
kind: 2
kind_name: "Guide"
giver: {"auto": true}
turn_in: {"auto": true}
bit: 62
requires_bit: 127
automatic: true
prev: [51]
next: []
stages: [1, 2, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 14, "what": null, "a": 4, "b": 1, "text_key": "Quest_QuickText_697_1"}
  - {"n": 2, "type": 15, "what": null, "a": 4, "b": 1, "text_key": "Quest_QuickText_697_3"}
rewards:
  - {"type": 2, "what": "exp", "amount": 150000, "shown": 150000}
---
<!-- generated:start -->
<!-- generated-keys: title=859cdd type=eb5b2b id=4c87e5 sources=7abe1f name_key=405893 kind=da4b92 kind_name=875cc6 giver=847ad4 turn_in=847ad4 bit=511a41 requires_bit=008451 automatic=5ffe53 prev=c6af6d next=97d170 stages=642aaf objectives=2be88c objectives_client=490c62 rewards=e154c2 -->
|  |  |
|---|---|
| **Quest id** | `696` |
| **Kind** | Guide (kind 2) |
| **Giver** | automatic |
| **Turn in** | automatic |
| **Completion bit** | 62 |
| **Requires bit** | 127 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/51-war-winning-means|War - Winning means]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 62 with:** [[wiki/quests/1523-war-monster-invasion-area|War - Monster Invasion Area]] (completing one closes the others)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 14 — move to battlefield / monster area?; values a=4, b=1 — tracker: “Go to Monster Invasion Area”
2. Type 15 — monster-area war / occupation?; values a=4, b=1 — tracker: “Build all Dimension Gate and win”

Stages (`flag1..5` = [1, 2, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 150,000 exp

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/progression-and-economy|Progression and economy]]
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
