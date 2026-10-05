---
title: "Swamps of the Snake Warrior : Collecting material"
type: "quest"
id: 1022
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1022", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 708", "client: QuestTalk.cdb id 709"]
name_key: "Quest_Title_1022"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 214}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 15
excludes_bit: 28
prev: [16]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 214, "talk": 708, "maps": [120, 120, 120], "text_key": "Quest_QuickText_C_OWEN"}
  - {"n": 2, "type": 3, "what": "acquire_item", "item": 844, "count": 3, "maps": [123, 123, 123], "text_key": "Quest_QuickText_1022_1"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 65000, "shown": 65000}
  - {"type": 1, "what": "item", "item": 611, "count": 25, "pick": "fixed"}
complete_talk: 709
---
<!-- generated:start -->
<!-- generated-keys: title=d77d59 type=eb5b2b id=2e2f7b sources=621b19 name_key=bd34f7 kind=77de68 kind_name=01e781 giver=2be88c turn_in=fb5a8b turn_in_maps=15f2a7 bit=b6589f requires_bit=f1abd6 excludes_bit=0a57cb prev=504845 next=97d170 stages=a80fa1 objectives=1d8b26 rewards=7c0ac1 complete_talk=29da9b -->
|  |  |
|---|---|
| **Quest id** | `1022` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 15 |
| **Not after bit** | 28 |

### Chain

- **After:** [[wiki/quests/16-farrell-s-request|Farrell's Request]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/32-swamps-of-snake-warrior|Swamps of Snake Warrior]]

### Objectives

1. Talk to [[wiki/npcs/214-owen|Owen]] (dialogue 708) — tracker: “Go to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Acquire [[wiki/items/844-dried-flower|Dried flower]] × 3 — tracker: “Acquire Dried flower (0/3) (Elite monster hunting)” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 65,000 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 25

### Dialogue

#### Objective 1 (QuestTalk 708)

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
