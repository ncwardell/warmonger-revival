---
title: "Collecting material"
type: "quest"
id: 729
status: "complete"
missing: []
sources: ["client: Quest.cdb id 729", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 698", "client: QuestTalk.cdb id 699"]
name_key: "Quest_Title_678"
kind: 3
kind_name: "Free"
giver: {"npc": 214}
turn_in: {"npc": 214}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 25
excludes_bit: 14
owned_field: 121
prev: [30, 1524]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 3, "what": "acquire_item", "item": 841, "count": 3, "maps": [121, 121, 121], "text_key": "Quest_QuickText_678_1"}
  - {"n": 2, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 52500, "shown": 52500}
  - {"type": 1, "what": "item", "item": 611, "count": 20, "pick": "fixed"}
offer_talk: 698
complete_talk: 699
---
<!-- generated:start -->
<!-- generated-keys: title=e2c8e1 type=eb5b2b id=baa924 sources=89be48 name_key=cd036a kind=77de68 kind_name=01e781 giver=fb5a8b turn_in=fb5a8b offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f requires_bit=f6e112 excludes_bit=fa35e1 owned_field=8bd795 prev=71a868 next=97d170 stages=30caa7 objectives=387843 rewards=ff1aed offer_talk=07eb1c complete_talk=8666e1 -->
|  |  |
|---|---|
|  | ![Collecting material](../assets/npcs/214.png) |
| **Quest id** | `729` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/214-owen\|Owen]] |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 25 |
| **Not after bit** | 14 |
| **Field c7@10** | [[wiki/dungeons/121-lv-1-skull-temple\|(Lv 1) Skull Temple]] (121) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/30-chepa-village|Chepa Village]], [[wiki/quests/1524-party-party-person|Party - Party Person]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/15-repel-the-skeleton-invasion|Repel the Skeleton Invasion]]

### Objectives

1. Acquire [[wiki/items/841-clown-mushroom|Clown mushroom]] × 3 — tracker: “Acquire the Clown mushroom (0/3)” — on [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121)
2. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen”

### Rewards

- **Basic reward:** 52,500 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 20

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
