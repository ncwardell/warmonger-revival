---
title: "Enemy territory"
type: "quest"
id: 842
status: "stub"
missing: ["giver", "objectives"]
sources: ["client: Quest.cdb id 842", "client: QuestTalk.cdb id 774"]
name_key: "Quest_Title_842"
kind: 8
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
  - {"n": 1, "type": 15, "what": null, "a": 2, "c": 1, "text_key": "Quest_QuickText_842_1"}
rewards:
  - {"type": 1, "what": "item", "item": 1000, "count": 5, "pick": "fixed"}
offer_talk: 774
---
<!-- generated:start -->
<!-- generated-keys: title=75a6d8 type=eb5b2b id=62362f sources=29bb7e name_key=5994d4 kind=fe5dbb kind_name=b6566f level=cf7982 giver=2be88c turn_in=847ad4 bit=b6589f automatic=5ffe53 prev=97d170 next=97d170 prerequisites=7f7bb1 stages=30caa7 objectives=2be88c objectives_client=a6e21f rewards=8b0755 offer_talk=66c4d1 -->
|  |  |
|---|---|
| **Quest id** | `842` |
| **Kind** | Daily (kind 8) |
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

1. Type 15 — monster-area war / occupation?; values a=2, c=1 — tracker: “Conquer Enemy's territory”

### Rewards

- **Basic reward:** [[wiki/items/1000-medal-bronze|Medal : Bronze]] × 5

### Dialogue

#### Offer (QuestTalk 774)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** The glorious honor is conquering enemy's territory.<br>Can you do this? You have to prepare to conquer this continent.  
> *(accept / continue)*
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
