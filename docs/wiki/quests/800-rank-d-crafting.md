---
title: "Rank[D] Crafting"
type: "quest"
id: 800
status: "stub"
missing: ["giver", "objectives", "rewards"]
sources: ["client: Quest.cdb id 800", "client: QuestTalk.cdb id 720"]
name_key: "Quest_Title_1299"
kind: 6
kind_name: "War"
giver: null
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 0
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "a": 30}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 2, "what": null, "a": 5, "b": 10, "text_key": "Quest_QuickText_800_1"}
  - {"n": 5, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards: null
rewards_client:
  - {"type": 1, "what": "item", "item": 887, "count": 25, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 891, "count": 25, "pick": "choose"}
  - {"type": 5, "what": null, "a": 100}
complete_talk: 720
---
<!-- generated:start -->
<!-- generated-keys: title=f988e7 type=eb5b2b id=290a52 sources=24fffe name_key=ea749e kind=c1dfd9 kind_name=5432ef giver=2be88c turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 prerequisites=6ffc47 stages=30caa7 objectives=2be88c objectives_client=3e7485 rewards=2be88c rewards_client=d56183 complete_talk=aeaa8a -->
|  |  |
|---|---|
| **Quest id** | `800` |
| **Kind** | War (kind 6) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level ?+ (a = 30, meaning unknown) |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 2 — kill enemy players?; values a=5, b=10 — tracker: “Destroy the enemy player from the Gaia field”
5. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

> [!warning] Not all reward types are decoded
> The rows below are the client's (`rewards_client`). Write the server-ready list into `rewards:` once the unclear ones are understood.

- **Choose one:** [[wiki/items/887-potion-of-health-a|Potion of Health (A)]] × 25 *or* [[wiki/items/891-potion-of-mana-a|Potion of Mana (A)]] × 25
- Type 5 — fame?; values a=100

### Dialogue

#### Completion (QuestTalk 720)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Wonderful, you made it, you can start the next one whenever you like.  
> *(accept / continue)*

### Seen in

- [[gameplay/server-rules|Server rules checklist]]
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
