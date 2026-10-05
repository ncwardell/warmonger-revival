---
title: "Collecting material"
type: "quest"
id: 731
status: "complete"
missing: []
sources: ["client: Quest.cdb id 731", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 698", "client: QuestTalk.cdb id 699"]
name_key: "Quest_Title_680"
kind: 3
kind_name: "Free"
giver: {"npc": 214}
turn_in: {"npc": 214}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 22
excludes_bit: 15
owned_field: 122
prev: [22]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 3, "what": "acquire_item", "item": 840, "count": 3, "maps": [122, 122, 122], "text_key": "Quest_QuickText_680_1"}
  - {"n": 2, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 90000, "shown": 90000}
  - {"type": 1, "what": "item", "item": 611, "count": 25, "pick": "fixed"}
offer_talk: 698
complete_talk: 699
---
<!-- generated:start -->
<!-- generated-keys: title=e2c8e1 type=eb5b2b id=77895c sources=ddf556 name_key=bc6c17 kind=77de68 kind_name=01e781 giver=fb5a8b turn_in=fb5a8b offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f requires_bit=12c6fc excludes_bit=f1abd6 owned_field=05a8ea prev=5c6c1d next=97d170 stages=30caa7 objectives=fc0639 rewards=1b1759 offer_talk=07eb1c complete_talk=8666e1 -->
|  |  |
|---|---|
|  | ![Collecting material](wiki/assets/npcs/214.png) |
| **Quest id** | `731` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/214-owen\|Owen]] |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 22 |
| **Not after bit** | 15 |
| **Field c7@10** | [[wiki/dungeons/122-lv-3-tsunami-lake\|(Lv 3) Tsunami Lake]] (122) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/16-farrell-s-request|Farrell's Request]]

### Objectives

1. Acquire [[wiki/items/840-soft-leather|Soft leather]] × 3 — tracker: “Acquire Soft leather (0/3)” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
2. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen”

### Rewards

- **Basic reward:** 90,000 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 25

### Dialogue

#### Offer (QuestTalk 698)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** The war is tough, and it's really hard to save materials. Can you help me out?  
> **Owen:** Grab the elite bottles in the Dimension gate and give me the ingredients.  
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
