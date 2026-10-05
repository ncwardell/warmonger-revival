---
title: "Tsunami Lake : Collecting material"
type: "quest"
id: 1017
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1017", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 698", "client: QuestTalk.cdb id 699"]
name_key: "Quest_Title_1017"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 214}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 22
excludes_bit: 15
prev: [22]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 214, "talk": 698, "maps": [120, 120, 120], "text_key": "Quest_QuickText_C_OWEN"}
  - {"n": 2, "type": 3, "what": "acquire_item", "item": 848, "count": 3, "maps": [122, 122, 122], "text_key": "Quest_QuickText_1017_1"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 60000, "shown": 60000}
  - {"type": 1, "what": "item", "item": 611, "count": 25, "pick": "fixed"}
complete_talk: 699
---
<!-- generated:start -->
<!-- generated-keys: title=78c3aa type=eb5b2b id=4dd260 sources=11404f name_key=fe4d74 kind=77de68 kind_name=01e781 giver=2be88c turn_in=fb5a8b turn_in_maps=15f2a7 bit=b6589f requires_bit=12c6fc excludes_bit=f1abd6 prev=5c6c1d next=97d170 stages=a80fa1 objectives=e68f38 rewards=8dc535 complete_talk=8666e1 -->
|  |  |
|---|---|
| **Quest id** | `1017` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 22 |
| **Not after bit** | 15 |

### Chain

- **After:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/16-farrell-s-request|Farrell's Request]]

### Objectives

1. Talk to [[wiki/npcs/214-owen|Owen]] (dialogue 698) — tracker: “Go to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Acquire [[wiki/items/848-medical-herb-water|Medical herb water]] × 3 — tracker: “Acquire the medical herb water (0/3) (Elite monster hunting)” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 60,000 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 25

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
