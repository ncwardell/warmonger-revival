---
title: "Acquire materials"
type: "quest"
id: 744
status: "complete"
missing: []
sources: ["client: Quest.cdb id 744", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 765", "client: QuestTalk.cdb id 766"]
name_key: "Quest_Title_761_"
kind: 3
kind_name: "Free"
giver: {"npc": 214}
turn_in: {"npc": 214}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 30
excludes_bit: 31
owned_field: 125
prev: [34]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 3, "what": "acquire_item", "item": 842, "count": 3, "maps": [126, 126, 126], "text_key": "Quest_QuickText_761_1"}
  - {"n": 2, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 127500, "shown": 127500}
  - {"type": 1, "what": "item", "item": 611, "count": 35, "pick": "fixed"}
offer_talk: 765
complete_talk: 766
---
<!-- generated:start -->
<!-- generated-keys: title=66283e type=eb5b2b id=193b34 sources=53722f name_key=86bf7d kind=77de68 kind_name=01e781 giver=fb5a8b turn_in=fb5a8b offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f requires_bit=22d200 excludes_bit=632667 owned_field=0ca927 prev=91a33c next=97d170 stages=30caa7 objectives=2731e7 rewards=7d44df offer_talk=e1f463 complete_talk=581a8e -->
|  |  |
|---|---|
|  | ![Acquire materials](../assets/npcs/214.png) |
| **Quest id** | `744` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/214-owen\|Owen]] |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 30 |
| **Not after bit** | 31 |
| **Field c7@10** | [[wiki/dungeons/125-lv-5-tow-canyon\|(Lv 5) Tow Canyon]] (125) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/34-tow-canyon|Tow Canyon]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/35-demon-hell|Demon Hell]]

### Objectives

1. Acquire [[wiki/items/842-burned-sulphur|Burned sulphur]] × 3 — tracker: “Gathering Burned sulphur (0/3)” — on [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] (126)
2. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen”

### Rewards

- **Basic reward:** 127,500 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 35

### Dialogue

#### Offer (QuestTalk 765)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** A fierce war is on the horizon, so  I lack all sorts of materials. Can you help me out?  
> *(accept / continue)*

#### Completion (QuestTalk 766)

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
