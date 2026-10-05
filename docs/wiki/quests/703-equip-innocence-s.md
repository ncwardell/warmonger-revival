---
title: "Equip Innocence's"
type: "quest"
id: 703
status: "complete"
missing: []
sources: ["client: Quest.cdb id 703", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "video: [[gameplay/video-tutorial-walkthrough]] steps 3-5 (lesson exp shown = table value)"]
name_key: "Quest_Title_703"
kind: 2
kind_name: "Guide"
giver: {"auto": true}
turn_in: {"auto": true}
bit: 65
automatic: true
prev: []
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 10003, "what": "client_equip", "slot": 3, "text_key": "Quest_QuickText_703_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 200000, "shown": 200000}
---
<!-- generated:start -->
<!-- generated-keys: title=5bb2ef type=eb5b2b id=8fc1bb sources=77ee46 name_key=6c74a2 kind=da4b92 kind_name=875cc6 giver=847ad4 turn_in=847ad4 bit=2a4593 automatic=5ffe53 prev=97d170 next=97d170 stages=a80fa1 objectives=54db0f rewards=a438e5 -->
|  |  |
|---|---|
| **Quest id** | `703` |
| **Kind** | Guide (kind 2) |
| **Giver** | automatic |
| **Turn in** | automatic |
| **Completion bit** | 65 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 65 with:** [[wiki/quests/1519-item-how-to-use-innocence-s|Item - How to use Innocence's]] (completing one closes the others)

### Objectives

1. client event: equip (a = slot kind) (a = 3) — tracker: “Equip Innocence from Inventory [I]”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 200,000 exp
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
