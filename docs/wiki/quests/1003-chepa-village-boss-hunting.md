---
title: "Chepa Village : Boss Hunting"
type: "quest"
id: 1003
status: "partial"
missing: ["giver"]
sources: ["client: Quest.cdb id 1003", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 858", "client: QuestTalk.cdb id 859"]
name_key: "Quest_Title_1003"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 200}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 56
prev: [769, 772, 773]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 200, "talk": 858, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_FREYA"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 127, "maps": [127, 127, 127], "text_key": "Quest_QuickText_1003_1"}
  - {"n": 3, "type": 1, "what": "kill", "unit_group": 10000, "units": [870], "count": 1, "maps": [127, 127, 127], "text_key": "Quest_QuickText_1003_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 50000, "shown": 50000}
  - {"type": 1, "what": "item", "item": 601, "count": 30, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 30, "pick": "fixed"}
complete_talk: 859
---
<!-- generated:start -->
<!-- generated-keys: title=a48c82 type=eb5b2b id=9f6bf8 sources=f6851d name_key=13b816 kind=77de68 kind_name=01e781 giver=2be88c turn_in=1caac0 turn_in_maps=15f2a7 bit=b6589f requires_bit=54ceb9 prev=46b5ec next=97d170 stages=a80fa1 objectives=d7e169 rewards=a6c452 complete_talk=812cd8 -->
|  |  |
|---|---|
| **Quest id** | `1003` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 56 |

### Chain

- **After:** [[wiki/quests/769-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/772-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/773-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Talk to [[wiki/npcs/200-freya|Freya]] (dialogue 858) — tracker: “Go to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Go to [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127) — tracker: “Go to the Chepa Village” — on [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127)
3. Kill any unit of kill group 10000 ([[wiki/monsters/870-chepa-sorcerer|Chepa Sorcerer]]) × 1 — tracker: “Chepa Sorcerer (0/1)” — on [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127)
4. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 50,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 30; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30

### Dialogue

#### Objective 1 (QuestTalk 858)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Chepa Village is now saturated. I don't know what happened all of a sudden, but I need you to clean up Chepa Village to stabilize it.  
> *(accept / continue)*

#### Completion (QuestTalk 859)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **You:** The conditions in the Chepa Village are not good. There's even a Chepa Sorcerer now.  
> **Freya:** Chepa sorcerer...Umm.. A big change is likely to happen.  
> *(accept / continue)*
<!-- generated:end -->

## Notes

Repeatable ("Free") quest. The WM 0110 patch moved repeatable quests to a "Free Quests" tab on the quest board, and WM 0124 removed that tab again ([[gameplay/patch-history]]). *patch notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/patch-history]]

## Open questions

The client names no giver for this row. Whether it was offered from the quest board or by the NPC of its first "talk" step is not known ([[gameplay/patch-history]] 0110/0124).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
