---
title: "War - Monster Area"
type: "quest"
id: 1520
status: "stub"
missing: ["turn_in", "objectives"]
sources: ["client: Quest.cdb id 1520", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)"]
name_key: "Quest_Title_Help_694"
kind: 12
kind_name: "Advice"
giver: {"auto": true}
turn_in: null
bit: 60
prev: []
next: []
stages: [1, 2, 3, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 30, "what": null, "a": 3, "b": 1, "text_key": "Quest_QuickText_Help_694_0"}
  - {"n": 2, "type": 1, "what": "kill", "target": "any_middle_boss", "count": 1, "text_key": "Quest_QuickText_Help_694_1"}
  - {"n": 3, "type": 31, "what": null, "a": 3, "b": 1, "text_key": "Quest_QuickText_Help_694_2"}
  - {"n": 4, "type": 1, "what": "kill", "target": "any_boss", "count": 1, "text_key": "Quest_QuickText_Help_694_3"}
rewards: []
help: {"text_key": "Quest_Title_Help_String_694"}
---
<!-- generated:start -->
<!-- generated-keys: title=f66c50 type=eb5b2b id=5748e8 sources=8745f5 name_key=c78d3a kind=7b5200 kind_name=ec7dd4 giver=847ad4 turn_in=2be88c bit=e6c3dd prev=97d170 next=97d170 stages=0f733e objectives=2be88c objectives_client=4d484b rewards=97d170 help=40833a -->
|  |  |
|---|---|
| **Quest id** | `1520` |
| **Kind** | Advice (kind 12) |
| **Giver** | automatic |
| **Turn in** | **unknown** |
| **Completion bit** | 60 |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 60 with:** [[wiki/quests/694-occupation-of-monster-area|Occupation of Monster area]] (completing one closes the others)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 30 — build nexus?; values a=3, b=1 — tracker: “Nexus construction when entering the war zone”
2. Kill any middle boss (target code 2) × 1 — tracker: “Intermediate boss treatment in Imprint area”
3. Type 31 — imprint?; values a=3, b=1 — tracker: “All imprinted”
4. Kill any boss (target code 3) × 1 — tracker: “After the Middle boss is created, kill the Middle boss and kill the boss (0/1)”

Stages (`flag1..5` = [1, 2, 3, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

None in the client.

### Tip window

> The monster occupation is in the gray map of the world map and is occupied by monsters.
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
