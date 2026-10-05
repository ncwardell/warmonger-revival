---
title: "Collecting material"
type: "quest"
id: 738
status: "complete"
missing: []
sources: ["client: Quest.cdb id 738", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 753", "client: QuestTalk.cdb id 754"]
name_key: "Quest_Title_755"
kind: 3
kind_name: "Free"
giver: {"npc": 214}
turn_in: {"npc": 214}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 123
excludes_bit: 29
owned_field: 124
prev: [47]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 3, "what": "acquire_item", "item": 850, "count": 3, "maps": [124, 124, 124], "text_key": "Quest_QuickText_755_1"}
  - {"n": 2, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 112500, "shown": 112500}
  - {"type": 1, "what": "item", "item": 611, "count": 30, "pick": "fixed"}
offer_talk: 753
complete_talk: 754
---
<!-- generated:start -->
<!-- generated-keys: title=e2c8e1 type=eb5b2b id=641e2c sources=c62c9e name_key=1dd35a kind=77de68 kind_name=01e781 giver=fb5a8b turn_in=fb5a8b offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f requires_bit=40bd00 excludes_bit=7719a1 owned_field=f38cfe prev=80af3c next=97d170 stages=30caa7 objectives=d0e46f rewards=2a9bca offer_talk=c32a67 complete_talk=b246c7 -->
|  |  |
|---|---|
|  | ![Collecting material](wiki/assets/npcs/214.png) |
| **Quest id** | `738` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/214-owen\|Owen]] |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 123 |
| **Not after bit** | 29 |
| **Field c7@10** | [[wiki/dungeons/124-lv-6-ghost-fortress\|(Lv 6) Ghost Fortress]] (124) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/47-create-potion|Create Potion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/33-ghost-fortress|Ghost Fortress]]

### Objectives

1. Acquire [[wiki/items/850-refined-oil|Refined oil]] × 3 — tracker: “Acquire Refined Oil (0/3)” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
2. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen”

### Rewards

- **Basic reward:** 112,500 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30

### Dialogue

#### Offer (QuestTalk 753)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** A fierce war is raging on the horizon, so I lack all sorts of materials. Can you help me out?  
> *(accept / continue)*

#### Completion (QuestTalk 754)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** Do you have the materials I asked for?  
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
