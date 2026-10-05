---
title: "War - How to use TP Skill"
type: "quest"
id: 1522
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 1522", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)"]
name_key: "Quest_Title_Help_702"
kind: 12
kind_name: "Advice"
giver: {"auto": true}
turn_in: {"auto": true}
bit: 64
automatic: true
prev: []
next: []
stages: [1, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 10004, "what": "client_open_panel", "panel": 3, "text_key": "Quest_QuickText_Help_702_1"}
  - {"n": 2, "type": 32, "what": null, "c": 1, "text_key": "Quest_QuickText_Help_702_2"}
rewards: []
help: {"text_key": "Quest_Title_Help_String_702"}
---
<!-- generated:start -->
<!-- generated-keys: title=0bac1a type=eb5b2b id=c718aa sources=3b0823 name_key=5b9455 kind=7b5200 kind_name=ec7dd4 giver=847ad4 turn_in=847ad4 bit=c66c65 automatic=5ffe53 prev=97d170 next=97d170 stages=a80fa1 objectives=2be88c objectives_client=f3f209 rewards=97d170 help=9125bd -->
|  |  |
|---|---|
| **Quest id** | `1522` |
| **Kind** | Advice (kind 12) |
| **Giver** | automatic |
| **Turn in** | automatic |
| **Completion bit** | 64 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 64 with:** [[wiki/quests/702-how-to-use-tp-skill|How to use TP Skill]] (completing one closes the others)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. client event: panel opened (a: 1 world map, 2 reinforce, 3 TP panel, 4 quest board) (a = 3) — tracker: “Open the TP Skill Window by imprinted the generated nexus or attack tower”
2. Type 32 — set TP skill?; values c=1 — tracker: “Set TP skills  (Click to use completed TP skill)”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

None in the client.

### Tip window

> The strategic skills available in war zones are called TP skills.
> You can use TP skills by destroying monsters and objects to gain TP points.
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
