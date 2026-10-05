---
title: "Item - How to use Innocence's"
type: "quest"
id: 1519
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 1519", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)"]
name_key: "Quest_Title_Help_703"
kind: 12
kind_name: "Advice"
giver: {"auto": true}
turn_in: {"auto": true}
bit: 65
automatic: true
prev: []
next: []
stages: [1, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 10003, "what": "client_equip", "slot": 3, "text_key": "Quest_QuickText_Help_703_1"}
  - {"n": 2, "type": 10013, "what": null, "text_key": "Quest_QuickText_Help_703_2"}
rewards: []
help: {"text_key": "Quest_Title_Help_String_703"}
---
<!-- generated:start -->
<!-- generated-keys: title=21bd07 type=eb5b2b id=b43f38 sources=20e311 name_key=7971af kind=7b5200 kind_name=ec7dd4 giver=847ad4 turn_in=847ad4 bit=2a4593 automatic=5ffe53 prev=97d170 next=97d170 stages=a80fa1 objectives=2be88c objectives_client=0af177 rewards=97d170 help=2380a1 -->
|  |  |
|---|---|
| **Quest id** | `1519` |
| **Kind** | Advice (kind 12) |
| **Giver** | automatic |
| **Turn in** | automatic |
| **Completion bit** | 65 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 65 with:** [[wiki/quests/703-equip-innocence-s|Equip Innocence's]] (completing one closes the others)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. client event: equip (a = slot kind) (a = 3) — tracker: “Equip Innocence from Inventory [I]”
2. Type 10013 — client event: transform? (no client sender found); values none — tracker: “Press [X] to transform (if you have more than 115,000 exp)”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

None in the client.

### Tip window

> When you achieve 30Lv, you can mount the Innocence, and experience can be consumed to transform.
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
