---
title: "Rank[D] Crafting"
type: "quest"
id: 801
status: "partial"
missing: ["giver", "objectives"]
sources: ["client: Quest.cdb id 801", "client: QuestTalk.cdb id 720"]
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
  - {"n": 1, "type": 34, "what": null, "b": 7, "text_key": "Quest_QuickText_801_1"}
  - {"n": 5, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 1, "what": "item", "item": 601, "count": 50, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 611, "count": 30, "pick": "choose"}
complete_talk: 720
---
<!-- generated:start -->
<!-- generated-keys: title=f988e7 type=eb5b2b id=549843 sources=63be7d name_key=ea749e kind=c1dfd9 kind_name=5432ef giver=2be88c turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 prerequisites=6ffc47 stages=30caa7 objectives=2be88c objectives_client=87797b rewards=5521e2 complete_talk=aeaa8a -->
|  |  |
|---|---|
| **Quest id** | `801` |
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

1. Type 34 — dimension gate?; values b=7 — tracker: “Create Dimension Gate”
5. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

- **Choose one:** [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 50 *or* [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30

### Dialogue

#### Completion (QuestTalk 720)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Wonderful, you made it, you can start the next one whenever you like.  
> *(accept / continue)*

### Seen in

- [[gameplay/server-rules|Server rules checklist]]
<!-- generated:end -->

## Notes

Started by using a precept scroll (item kind 44), not by talking to an NPC: Rank[D] scrolls 1201–1204 start quests 800–803 and Rank[C] scrolls 1251–1255 start 811–815 (`opt1_value`). Shop 289, Freya's, sells 1201–1204 and 1251–1253 ([[gameplay/precept-shop]] §1). In October 2016 a D scroll cost 4,650 gold and a C scroll 9,300 ([[gameplay/precept-shop]] §1, *image*). Only one precept quest can be active; it shows in red in the quest log as "Rank [D/C/B] Crafting" in its own "Precept" group, and dropping it and buying another scroll re-rolls it ([[gameplay/precept-shop]] §2, *guide*). Players said precept quests give no exp ([[gameplay/warmonger-forum]] §3).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/precept-shop]]
- [[gameplay/warmonger-forum]]
- [[gameplay/crush-mechanics]]

## Open questions

In 2016 the server rolled a random quest and paid random medals (D mostly bronze, C silver) plus 20–150 D spell stones ([[gameplay/crush-mechanics]] §1, [[gameplay/precept-shop]] §2); this client row pays a fixed set of Passion fragments and no medals. A minimum level of 30 (pre type 4, a = 30) is a guess. Players in early 2017 said precepts had been removed ([[gameplay/crush-mechanics]]). The client has no giver shape for "started by an item", so `giver` stays empty.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
