---
title: "Tow Canyon : Collecting material"
type: "quest"
id: 1033
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1033", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 759", "client: QuestTalk.cdb id 760"]
name_key: "Quest_Title_1033"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 213}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 29
excludes_bit: 30
prev: [33]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 213, "talk": 759, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_ODIN"}
  - {"n": 2, "type": 3, "what": "acquire_item", "item": 838, "count": 3, "maps": [125, 125, 125], "text_key": "Quest_QuickText_1033_1"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_B_ODIN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 80000, "shown": 80000}
  - {"type": 1, "what": "item", "item": 611, "count": 30, "pick": "fixed"}
complete_talk: 760
---
<!-- generated:start -->
<!-- generated-keys: title=99bbc1 type=eb5b2b id=e0f05e sources=feca74 name_key=b2bdd3 kind=77de68 kind_name=01e781 giver=2be88c turn_in=91ad7d turn_in_maps=15f2a7 bit=b6589f requires_bit=7719a1 excludes_bit=22d200 prev=78415f next=97d170 stages=a80fa1 objectives=0ac41c rewards=aa7335 complete_talk=1382ac -->
|  |  |
|---|---|
| **Quest id** | `1033` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/213-odin\|Odin]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 29 |
| **Not after bit** | 30 |

### Chain

- **After:** [[wiki/quests/33-ghost-fortress|Ghost Fortress]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/34-tow-canyon|Tow Canyon]]

### Objectives

1. Talk to [[wiki/npcs/213-odin|Odin]] (dialogue 759) — tracker: “Go to Odin” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Acquire [[wiki/items/838-ointment-of-spirit|Ointment of Spirit]] × 3 — tracker: “Spirit's ointment (0/3) (Elite monster hunting)” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Odin” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 80,000 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30

### Dialogue

#### Objective 1 (QuestTalk 759)

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
