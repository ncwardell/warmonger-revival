---
title: "Occupation of Monster area"
type: "quest"
id: 694
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 694", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "video: [[gameplay/video-tutorial-walkthrough]] steps 3-5 (lesson exp shown = table value)"]
name_key: "Quest_Title_694"
kind: 2
kind_name: "Guide"
giver: {"auto": true}
turn_in: {"auto": true}
bit: 60
automatic: true
prev: []
next: []
stages: [1, 2, 3, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 30, "what": null, "a": 3, "b": 1, "text_key": "Quest_QuickText_694_0"}
  - {"n": 2, "type": 1, "what": "kill", "target": "any_middle_boss", "count": 1, "text_key": "Quest_QuickText_694_1"}
  - {"n": 3, "type": 31, "what": null, "a": 3, "b": 1, "text_key": "Quest_QuickText_694_2"}
  - {"n": 4, "type": 1, "what": "kill", "target": "any_boss", "count": 1, "text_key": "Quest_QuickText_694_3"}
rewards:
  - {"type": 2, "what": "exp", "amount": 150000, "shown": 150000}
help: {"text_key": "Quest_HelpText_694"}
---
<!-- generated:start -->
<!-- generated-keys: title=1ce6be type=eb5b2b id=d2e19c sources=d7e78f name_key=3b4e77 kind=da4b92 kind_name=875cc6 giver=847ad4 turn_in=847ad4 bit=e6c3dd automatic=5ffe53 prev=97d170 next=97d170 stages=0f733e objectives=2be88c objectives_client=c45d67 rewards=e154c2 help=e3a627 -->
|  |  |
|---|---|
| **Quest id** | `694` |
| **Kind** | Guide (kind 2) |
| **Giver** | automatic |
| **Turn in** | automatic |
| **Completion bit** | 60 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 60 with:** [[wiki/quests/1520-war-monster-area|War - Monster Area]] (completing one closes the others)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 30 — build nexus?; values a=3, b=1 — tracker: “Constructing Nexus for the first time”
2. Kill any middle boss (target code 2) × 1 — tracker: “Killed Middle boss (0/1)”
3. Type 31 — imprint?; values a=3, b=1 — tracker: “Imprinted”
4. Kill any boss (target code 3) × 1 — tracker: “Killed boss (0/1)”

Stages (`flag1..5` = [1, 2, 3, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 150,000 exp

### Tip window

> 1. Constructing Nexus for the first time 
>  2. Killed Middle boss 3. Imprinted the zone where the middle boss is located 
>  4. Killed boss 
> (If you do not kill the middle boss, give the boss a buff.)
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
