---
title: "Chepa Village : Collecting material"
type: "quest"
id: 1002
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1002", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 698", "client: QuestTalk.cdb id 699"]
name_key: "Quest_Title_1002"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 214}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 26
excludes_bit: 25
prev: [26]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 214, "talk": 698, "maps": [120, 120, 120], "text_key": "Quest_QuickText_C_OWEN"}
  - {"n": 2, "type": 3, "what": "acquire_item", "item": 840, "count": 3, "maps": [128, 128, 128], "text_key": "Quest_QuickText_1002_1"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 25000, "shown": 25000}
  - {"type": 1, "what": "item", "item": 611, "count": 15, "pick": "fixed"}
complete_talk: 699
---
<!-- generated:start -->
<!-- generated-keys: title=d7e015 type=eb5b2b id=a5b1d7 sources=d707c2 name_key=2229ab kind=77de68 kind_name=01e781 giver=2be88c turn_in=fb5a8b turn_in_maps=15f2a7 bit=b6589f requires_bit=887309 excludes_bit=f6e112 prev=f36b47 next=97d170 stages=a80fa1 objectives=74e784 rewards=7442e4 complete_talk=8666e1 -->
|  |  |
|---|---|
| **Quest id** | `1002` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 26 |
| **Not after bit** | 25 |

### Chain

- **After:** [[wiki/quests/26-border-area-normal-mode|Border Area Normal Mode]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/30-chepa-village|Chepa Village]], [[wiki/quests/1524-party-party-person|Party - Party Person]]

### Objectives

1. Talk to [[wiki/npcs/214-owen|Owen]] (dialogue 698) — tracker: “Go to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Acquire [[wiki/items/840-soft-leather|Soft leather]] × 3 — tracker: “Acquire the Soft leather (0/3) (Elite monster hunting)” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 25,000 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 15

### Dialogue

#### Objective 1 (QuestTalk 698)

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
