---
title: "Occupation of Enemy territory"
type: "quest"
id: 695
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 695", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "video: [[gameplay/video-tutorial-walkthrough]] steps 3-5 (lesson exp shown = table value)"]
name_key: "Quest_Title_695"
kind: 2
kind_name: "Guide"
giver: {"auto": true}
turn_in: {"auto": true}
bit: 61
automatic: true
prev: []
next: []
stages: [1, 2, 3, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 30, "what": null, "a": 2, "b": 1, "text_key": "Quest_QuickText_695_1"}
  - {"n": 2, "type": 1, "what": "kill", "unit": 77, "count": 1, "text_key": "Quest_QuickText_695_2"}
  - {"n": 3, "type": 29, "what": null, "a": 2, "b": 1, "text_key": "Quest_QuickText_695_3"}
  - {"n": 4, "type": 1, "what": "kill", "unit": 5, "count": 1, "text_key": "Quest_QuickText_695_4"}
rewards:
  - {"type": 2, "what": "exp", "amount": 150000, "shown": 150000}
---
<!-- generated:start -->
<!-- generated-keys: title=962455 type=eb5b2b id=00a691 sources=0b2bab name_key=9d271e kind=da4b92 kind_name=875cc6 giver=847ad4 turn_in=847ad4 bit=6c1e67 automatic=5ffe53 prev=97d170 next=97d170 stages=0f733e objectives=2be88c objectives_client=802952 rewards=e154c2 -->
|  |  |
|---|---|
| **Quest id** | `695` |
| **Kind** | Guide (kind 2) |
| **Giver** | automatic |
| **Turn in** | automatic |
| **Completion bit** | 61 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 61 with:** [[wiki/quests/1521-war-enemy-occupation-territory|War - enemy occupation territory]] (completing one closes the others)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 30 — build nexus?; values a=2, b=1 — tracker: “Constructing Nexus for the first time”
2. Kill Attack Tower × 1 — tracker: “Destroy a tower (0/1)”
3. Type 29 — attack tower?; values a=2, b=1 — tracker: “Constructing tower”
4. Kill Warrior (Male) × 1 — tracker: “Destroy enemy nexus”

Stages (`flag1..5` = [1, 2, 3, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 150,000 exp
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
