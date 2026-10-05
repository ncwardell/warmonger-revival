---
title: "Collecting material"
type: "quest"
id: 735
status: "complete"
missing: []
sources: ["client: Quest.cdb id 735", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 708", "client: QuestTalk.cdb id 709"]
name_key: "Quest_Title_683"
kind: 3
kind_name: "Free"
giver: {"npc": 214}
turn_in: {"npc": 214}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 15
excludes_bit: 28
owned_field: 123
prev: [16]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 3, "what": "acquire_item", "item": 844, "count": 3, "maps": [123, 123, 123], "text_key": "Quest_QuickText_683_1"}
  - {"n": 2, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 97500, "shown": 97500}
  - {"type": 1, "what": "item", "item": 611, "count": 25, "pick": "fixed"}
offer_talk: 708
complete_talk: 709
---
<!-- generated:start -->
<!-- generated-keys: title=e2c8e1 type=eb5b2b id=a6b21a sources=36898a name_key=6fae1c kind=77de68 kind_name=01e781 giver=fb5a8b turn_in=fb5a8b offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f requires_bit=f1abd6 excludes_bit=0a57cb owned_field=40bd00 prev=504845 next=97d170 stages=30caa7 objectives=f11996 rewards=6804bb offer_talk=b6c3f8 complete_talk=29da9b -->
|  |  |
|---|---|
|  | ![Collecting material](../assets/npcs/214.png) |
| **Quest id** | `735` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/214-owen\|Owen]] |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 15 |
| **Not after bit** | 28 |
| **Field c7@10** | [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior\|(Lv 4) Swamps of Snake Warrior]] (123) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/16-farrell-s-request|Farrell's Request]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/32-swamps-of-snake-warrior|Swamps of Snake Warrior]]

### Objectives

1. Acquire [[wiki/items/844-dried-flower|Dried flower]] × 3 — tracker: “Acquire Dried flower (0/3)” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
2. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen”

### Rewards

- **Basic reward:** 97,500 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 25

### Dialogue

#### Offer (QuestTalk 708)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** The war is tough, and it's really hard to save materials. Can you help me out?  
> *(accept / continue)*

#### Completion (QuestTalk 709)

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
