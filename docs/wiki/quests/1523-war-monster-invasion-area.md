---
title: "War - Monster Invasion Area"
type: "quest"
id: 1523
status: "stub"
missing: ["turn_in", "objectives"]
sources: ["client: Quest.cdb id 1523", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)"]
name_key: "Quest_Title_Help_697"
kind: 12
kind_name: "Advice"
giver: {"auto": true}
turn_in: null
bit: 62
prev: []
next: []
stages: [1, 2, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 14, "what": null, "a": 4, "b": 1, "text_key": "Quest_QuickText_Help_697_1"}
  - {"n": 2, "type": 29, "what": null, "a": 4, "b": 1, "text_key": "Quest_QuickText_Help_697_2"}
  - {"n": 3, "type": 15, "what": null, "a": 4, "b": 1, "text_key": "Quest_QuickText_Help_697_3"}
rewards: []
help: {"text_key": "Quest_Title_Help_String_697"}
---
<!-- generated:start -->
<!-- generated-keys: title=ed0197 type=eb5b2b id=d077ba sources=0e8444 name_key=561b0f kind=7b5200 kind_name=ec7dd4 giver=847ad4 turn_in=2be88c bit=511a41 prev=97d170 next=97d170 stages=642aaf objectives=2be88c objectives_client=790232 rewards=97d170 help=6f35fc -->
|  |  |
|---|---|
| **Quest id** | `1523` |
| **Kind** | Advice (kind 12) |
| **Giver** | automatic |
| **Turn in** | **unknown** |
| **Completion bit** | 62 |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 62 with:** [[wiki/quests/696-occupation-of-monster-invasion-area|Occupation of Monster Invasion Area]] (completing one closes the others)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 14 — move to battlefield / monster area?; values a=4, b=1 — tracker: “When entering the area where the skull mark was created on the World map, start before the invasion”
2. Type 29 — attack tower?; values a=4, b=1 — tracker: “Increased stability rate when building destroyed attack tower”
3. Type 15 — monster-area war / occupation?; values a=4, b=1 — tracker: “All destroyed attack towers can occupy territory during construction.”

Stages (`flag1..5` = [1, 2, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

None in the client.

### Tip window

> Monsters invasion land is the area where monsters invade because the stability rate is reduced in the country's land
> Tip : When the stability rate is less than 30, the monsters invade.
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
