---
title: "Battle with legion members."
type: "quest"
id: 840
status: "stub"
missing: ["giver", "objectives"]
sources: ["client: Quest.cdb id 840", "client: QuestTalk.cdb id 772"]
name_key: "Quest_Title_840"
kind: 7
kind_name: "Daily"
level: {"min": 28, "max": 30}
giver: null
turn_in: {"auto": true}
bit: 0
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 7, "what": "legion?"}
  - {"type": 4, "what": "level", "min": 28, "max": 30}
  - {"type": 5, "what": null}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 23, "what": null, "a": 1, "b": 1, "text_key": "Quest_QuickText_840_1"}
rewards: []
offer_talk: 772
---
<!-- generated:start -->
<!-- generated-keys: title=cc162d type=eb5b2b id=c1d2fb sources=5d64c8 name_key=72d9c6 kind=902ba3 kind_name=b6566f level=cf7982 giver=2be88c turn_in=847ad4 bit=b6589f automatic=5ffe53 prev=97d170 next=97d170 prerequisites=470806 stages=30caa7 objectives=2be88c objectives_client=8afc97 rewards=97d170 offer_talk=d04d50 -->
|  |  |
|---|---|
| **Quest id** | `840` |
| **Kind** | Daily (kind 7) |
| **Level** | 28–30 |
| **Giver** | **unknown** |
| **Turn in** | automatic |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 7 | legion? | no values |
| 4 | level | level 28–30 |
| 5 | unknown | no values |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 23 — legion battle?; values a=1, b=1 — tracker: “Fight with 5 legion members.”

### Rewards

None in the client.

### Dialogue

#### Offer (QuestTalk 772)

Speaker: [[wiki/npcs/300-kaysa|Kaysa]]

> **Kaysa:** Let's battle with your Legion members. The massive battle will give you a great win.  
> *(accept / continue)*

### Mentioned in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]]
- [[gameplay/precept-shop|Precept shop and precept quests]]
- [[gameplay/skull-artifact-set|Skull artifact set tooltips (Crush Online, Feb 2017)]]
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
