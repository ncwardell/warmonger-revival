---
title: "Skull Cemetery : Collecting material"
type: "quest"
id: 1012
status: "partial"
missing: ["giver"]
sources: ["client: Quest.cdb id 1012", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 699", "client: QuestTalk.cdb id 738"]
name_key: "Quest_Title_1012"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 214}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 14
excludes_bit: 22
prev: [15]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 214, "talk": 738, "maps": [120, 120, 120], "text_key": "Quest_QuickText_C_OWEN"}
  - {"n": 2, "type": 3, "what": "acquire_item", "item": 839, "count": 3, "maps": [128, 128, 128], "text_key": "Quest_QuickText_1012_1"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 45000, "shown": 45000}
  - {"type": 1, "what": "item", "item": 611, "count": 20, "pick": "fixed"}
complete_talk: 699
---
<!-- generated:start -->
<!-- generated-keys: title=5aef4f type=eb5b2b id=899a19 sources=8c6890 name_key=36d7cb kind=77de68 kind_name=01e781 giver=2be88c turn_in=fb5a8b turn_in_maps=15f2a7 bit=b6589f requires_bit=fa35e1 excludes_bit=12c6fc prev=017b8e next=97d170 stages=a80fa1 objectives=76791d rewards=6530c9 complete_talk=8666e1 -->
|  |  |
|---|---|
| **Quest id** | `1012` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 14 |
| **Not after bit** | 22 |

### Chain

- **After:** [[wiki/quests/15-repel-the-skeleton-invasion|Repel the Skeleton Invasion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]

### Objectives

1. Talk to [[wiki/npcs/214-owen|Owen]] (dialogue 738) — tracker: “Go to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Acquire [[wiki/items/839-wild-herb|Wild herb]] × 3 — tracker: “Acquire the Wild herb (0/3) (Elite monster hunting)” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 45,000 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 20

### Dialogue

#### Objective 1 (QuestTalk 738)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** A fierce war is on the horizon, so  I lack all sorts of materials. Can you help me out?  
> **Owen:** Grab the elite bottles in the Dimension gate and give me the ingredients.  
> *(accept / continue)*  
> *(accept / continue)*

#### Completion (QuestTalk 699)

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
