---
title: "Ghost Fortress : Collecting material"
type: "quest"
id: 1028
status: "partial"
missing: ["giver"]
sources: ["client: Quest.cdb id 1028", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 753", "client: QuestTalk.cdb id 754"]
name_key: "Quest_Title_1028"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 214}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 123
excludes_bit: 29
prev: [47]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 214, "talk": 753, "maps": [120, 120, 120], "text_key": "Quest_QuickText_C_OWEN"}
  - {"n": 2, "type": 3, "what": "acquire_item", "item": 850, "count": 3, "maps": [124, 124, 124], "text_key": "Quest_QuickText_1028_1"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 75000, "shown": 75000}
  - {"type": 1, "what": "item", "item": 611, "count": 30, "pick": "fixed"}
complete_talk: 754
---
<!-- generated:start -->
<!-- generated-keys: title=d81e57 type=eb5b2b id=d9935e sources=7f65d4 name_key=9fe213 kind=77de68 kind_name=01e781 giver=2be88c turn_in=fb5a8b turn_in_maps=15f2a7 bit=b6589f requires_bit=40bd00 excludes_bit=7719a1 prev=80af3c next=97d170 stages=a80fa1 objectives=45ebfa rewards=1e74f1 complete_talk=b246c7 -->
|  |  |
|---|---|
| **Quest id** | `1028` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 123 |
| **Not after bit** | 29 |

### Chain

- **After:** [[wiki/quests/47-create-potion|Create Potion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/33-ghost-fortress|Ghost Fortress]]

### Objectives

1. Talk to [[wiki/npcs/214-owen|Owen]] (dialogue 753) — tracker: “Go to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Acquire [[wiki/items/850-refined-oil|Refined oil]] × 3 — tracker: “Acquire Refined Oil (0/3) (Elite monster hunting)” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 75,000 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30

### Dialogue

#### Objective 1 (QuestTalk 753)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** A fierce war is raging on the horizon, so I lack all sorts of materials. Can you help me out?  
> *(accept / continue)*

#### Completion (QuestTalk 754)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** Do you have the materials I asked for?  
> *(accept / continue)*
<!-- generated:end -->

## Notes

Repeatable ("Free") quest. The WM 0110 patch moved repeatable quests to a "Free Quests" tab on the quest board, and WM 0124 removed that tab again ([[gameplay/patch-history]]). *patch notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/patch-history]]

## Open questions

The client names no giver for this row. Whether it was offered from the quest board or by the NPC of its first "talk" step is not known ([[gameplay/patch-history]] 0110/0124).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
