---
title: "Demon Hell : Collecting material"
type: "quest"
id: 1038
status: "partial"
missing: ["giver"]
sources: ["client: Quest.cdb id 1038", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 765", "client: QuestTalk.cdb id 766"]
name_key: "Quest_Title_1038"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 214}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 30
excludes_bit: 31
prev: [34]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 214, "talk": 765, "maps": [120, 120, 120], "text_key": "Quest_QuickText_C_OWEN"}
  - {"n": 2, "type": 3, "what": "acquire_item", "item": 842, "count": 3, "maps": [126, 126, 126], "text_key": "Quest_QuickText_1038_1"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 85000, "shown": 85000}
  - {"type": 1, "what": "item", "item": 611, "count": 35, "pick": "fixed"}
complete_talk: 766
---
<!-- generated:start -->
<!-- generated-keys: title=576725 type=eb5b2b id=16da81 sources=349ebd name_key=dde26d kind=77de68 kind_name=01e781 giver=2be88c turn_in=fb5a8b turn_in_maps=15f2a7 bit=b6589f requires_bit=22d200 excludes_bit=632667 prev=91a33c next=97d170 stages=a80fa1 objectives=b0a758 rewards=d49878 complete_talk=581a8e -->
|  |  |
|---|---|
| **Quest id** | `1038` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 30 |
| **Not after bit** | 31 |

### Chain

- **After:** [[wiki/quests/34-tow-canyon|Tow Canyon]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/35-demon-hell|Demon Hell]]

### Objectives

1. Talk to [[wiki/npcs/214-owen|Owen]] (dialogue 765) — tracker: “Go to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Acquire [[wiki/items/842-burned-sulphur|Burned sulphur]] × 3 — tracker: “Gathering Burned sulphur (0/3) (Elite monster hunting)” — on [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] (126)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 85,000 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 35

### Dialogue

#### Objective 1 (QuestTalk 765)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** A fierce war is on the horizon, so  I lack all sorts of materials. Can you help me out?  
> *(accept / continue)*

#### Completion (QuestTalk 766)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** Do you have the materials I asked for?  
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
