---
title: "Collecting material"
type: "quest"
id: 741
status: "complete"
missing: []
sources: ["client: Quest.cdb id 741", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 759", "client: QuestTalk.cdb id 760"]
name_key: "Quest_Title_758"
kind: 3
kind_name: "Free"
giver: {"npc": 213}
turn_in: {"npc": 213}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 29
excludes_bit: 30
owned_field: 125
prev: [33]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 3, "what": "acquire_item", "item": 838, "count": 3, "maps": [125, 125, 125], "text_key": "Quest_QuickText_758_1"}
  - {"n": 2, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_B_ODIN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 120000, "shown": 120000}
  - {"type": 1, "what": "item", "item": 611, "count": 30, "pick": "fixed"}
offer_talk: 759
complete_talk: 760
---
<!-- generated:start -->
<!-- generated-keys: title=e2c8e1 type=eb5b2b id=23b23b sources=669595 name_key=217c3a kind=77de68 kind_name=01e781 giver=91ad7d turn_in=91ad7d offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f requires_bit=7719a1 excludes_bit=22d200 owned_field=0ca927 prev=78415f next=97d170 stages=30caa7 objectives=122625 rewards=2ded0b offer_talk=dcdee6 complete_talk=1382ac -->
|  |  |
|---|---|
|  | ![Collecting material](wiki/assets/npcs/213.png) |
| **Quest id** | `741` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/213-odin\|Odin]] |
| **Turn in** | [[wiki/npcs/213-odin\|Odin]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 29 |
| **Not after bit** | 30 |
| **Field c7@10** | [[wiki/dungeons/125-lv-5-tow-canyon\|(Lv 5) Tow Canyon]] (125) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/33-ghost-fortress|Ghost Fortress]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/34-tow-canyon|Tow Canyon]]

### Objectives

1. Acquire [[wiki/items/838-ointment-of-spirit|Ointment of Spirit]] × 3 — tracker: “Spirit's ointment (0/3)” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)
2. Report (tracker line; done by turning the quest in) — tracker: “Return to Odin”

### Rewards

- **Basic reward:** 120,000 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30

### Dialogue

#### Offer (QuestTalk 759)

Speaker: [[wiki/npcs/213-odin|Odin]]

> **Odin:** A fierce war is raging on the horizon, so I lack all sorts of materials. Can you help me out?  
> *(accept / continue)*

#### Completion (QuestTalk 760)

Speaker: [[wiki/npcs/213-odin|Odin]]

> **Odin:** Do you have the materials I asked for?  
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
