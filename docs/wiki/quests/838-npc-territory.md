---
title: "NPC territory"
type: "quest"
id: 838
status: "stub"
missing: ["giver", "objectives"]
sources: ["client: Quest.cdb id 838", "client: QuestTalk.cdb id 770"]
name_key: "Quest_Title_838"
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
  - {"type": 4, "what": "level", "min": 28, "max": 30}
  - {"type": 5, "what": null}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 3, "c": 2, "text_key": "Quest_QuickText_838_1"}
rewards:
  - {"type": 1, "what": "item", "item": 1000, "count": 5, "pick": "fixed"}
offer_talk: 770
---
<!-- generated:start -->
<!-- generated-keys: title=494373 type=eb5b2b id=2dc292 sources=312c62 name_key=7aade4 kind=902ba3 kind_name=b6566f level=cf7982 giver=2be88c turn_in=847ad4 bit=b6589f automatic=5ffe53 prev=97d170 next=97d170 prerequisites=7f7bb1 stages=30caa7 objectives=2be88c objectives_client=845607 rewards=8b0755 offer_talk=5b5b33 -->
|  |  |
|---|---|
| **Quest id** | `838` |
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
| 4 | level | level 28–30 |
| 5 | unknown | no values |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 15 — monster-area war / occupation?; values a=3, c=2 — tracker: “Conquer NPC territory”

### Rewards

- **Basic reward:** [[wiki/items/1000-medal-bronze|Medal : Bronze]] × 5

### Dialogue

#### Offer (QuestTalk 770)

Speaker: [[wiki/npcs/303-cathy|Cathy]]

> **Cathy:** There is new quest for you, you will need it.  
> **Cathy:** When you conquer NPC territory, you'll know what the quest is.  
> *(accept / continue)*

### Mentioned in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]]
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]]
- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]]
- [[gameplay/warmonger-forum|Warmonger forum (2018)]]
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
