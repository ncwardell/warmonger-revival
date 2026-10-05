---
title: "Collecting material"
type: "quest"
id: 725
status: "complete"
missing: []
sources: ["client: Quest.cdb id 725", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 699", "client: QuestTalk.cdb id 738"]
name_key: "Quest_Title_698"
kind: 3
kind_name: "Free"
giver: {"npc": 214}
turn_in: {"npc": 214}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 14
excludes_bit: 22
owned_field: 128
prev: [15]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 3, "what": "acquire_item", "item": 848, "count": 3, "maps": [128, 128, 128], "text_key": "Quest_QuickText_698_1"}
  - {"n": 2, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 67500, "shown": 67500}
  - {"type": 1, "what": "item", "item": 611, "count": 20, "pick": "fixed"}
offer_talk: 738
complete_talk: 699
---
<!-- generated:start -->
<!-- generated-keys: title=e2c8e1 type=eb5b2b id=75d2a5 sources=9b6be9 name_key=c59664 kind=77de68 kind_name=01e781 giver=fb5a8b turn_in=fb5a8b offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f requires_bit=fa35e1 excludes_bit=12c6fc owned_field=b4182b prev=017b8e next=97d170 stages=30caa7 objectives=763f7d rewards=9ed996 offer_talk=641e2c complete_talk=8666e1 -->
|  |  |
|---|---|
|  | ![Collecting material](wiki/assets/npcs/214.png) |
| **Quest id** | `725` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/214-owen\|Owen]] |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 14 |
| **Not after bit** | 22 |
| **Field c7@10** | [[wiki/dungeons/128-lv-2-skull-cemetery\|(Lv 2) Skull Cemetery]] (128) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/15-repel-the-skeleton-invasion|Repel the Skeleton Invasion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]

### Objectives

1. Acquire [[wiki/items/848-medical-herb-water|Medical herb water]] × 3 — tracker: “Acquire the medical herb water (0/3)” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
2. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen”

### Rewards

- **Basic reward:** 67,500 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 20

### Dialogue

#### Offer (QuestTalk 738)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** A fierce war is on the horizon, so  I lack all sorts of materials. Can you help me out?  
> **Owen:** Grab the elite bottles in the Dimension gate and give me the ingredients.  
> *(accept / continue)*  
> *(accept / continue)*

#### Completion (QuestTalk 699)

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
