---
title: "War - enemy occupation territory"
type: "quest"
id: 1521
status: "stub"
missing: ["turn_in", "objectives"]
sources: ["client: Quest.cdb id 1521", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)"]
name_key: "Quest_Title_Help_695"
kind: 12
kind_name: "Advice"
giver: {"auto": true}
turn_in: null
bit: 61
prev: []
next: []
stages: [1, 2, 3, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 30, "what": null, "a": 2, "b": 1, "text_key": "Quest_QuickText_Help_695_1"}
  - {"n": 2, "type": 1, "what": "kill", "unit": 77, "count": 1, "text_key": "Quest_QuickText_Help_695_2"}
  - {"n": 3, "type": 29, "what": null, "a": 2, "b": 1, "text_key": "Quest_QuickText_Help_695_3"}
  - {"n": 4, "type": 1, "what": "kill", "unit": 5, "count": 1}
rewards: []
help: {"text_key": "Quest_Title_Help_String_695"}
---
<!-- generated:start -->
<!-- generated-keys: title=f55c85 type=eb5b2b id=3ea77f sources=ddccc5 name_key=4ef913 kind=7b5200 kind_name=ec7dd4 giver=847ad4 turn_in=2be88c bit=6c1e67 prev=97d170 next=97d170 stages=0f733e objectives=2be88c objectives_client=5fc3a5 rewards=97d170 help=5236aa -->
|  |  |
|---|---|
| **Quest id** | `1521` |
| **Kind** | Advice (kind 12) |
| **Giver** | automatic |
| **Turn in** | **unknown** |
| **Completion bit** | 61 |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 61 with:** [[wiki/quests/695-occupation-of-enemy-territory|Occupation of Enemy territory]] (completing one closes the others)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 30 — build nexus?; values a=2, b=1 — tracker: “Construct Nexus when entering the war zone”
2. Kill Attack Tower × 1 — tracker: “Destroy attack tower and build friendly attack tower (TP point required for construction)   (Nexus is invulnerable if you have two or more attack towers)”
3. Type 29 — attack tower?; values a=2, b=1 — tracker: “Destroy enemy nexus when occupying territory”
4. Kill [[wiki/classes/5-guardian|Guardian]] × 1

Stages (`flag1..5` = [1, 2, 3, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

None in the client.

### Tip window

> The enemy occupied territories are the territories occupied by the state and are held by three countries.
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
