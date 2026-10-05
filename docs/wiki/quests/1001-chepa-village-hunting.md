---
title: "Chepa Village : Hunting"
type: "quest"
id: 1001
status: "partial"
missing: ["giver"]
sources: ["client: Quest.cdb id 1001", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 702", "client: QuestTalk.cdb id 703"]
name_key: "Quest_Title_1001"
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
  - {"n": 1, "type": 4, "what": "talk", "npc": 214, "talk": 702, "maps": [120, 120, 120], "text_key": "Quest_QuickText_C_OWEN"}
  - {"n": 2, "type": 1, "what": "collect", "unit": 668, "count": 5, "item": 2654, "rate": 70, "maps": [127, 127, 127], "text_key": "Quest_QuickText_1001_1"}
  - {"n": 3, "type": 1, "what": "collect", "unit": 669, "count": 5, "item": 2653, "rate": 70, "maps": [127, 127, 127], "text_key": "Quest_QuickText_1001_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 20000, "shown": 20000}
  - {"type": 1, "what": "item", "item": 601, "count": 15, "pick": "fixed"}
complete_talk: 703
---
<!-- generated:start -->
<!-- generated-keys: title=302464 type=eb5b2b id=dd0190 sources=ee8b5f name_key=0f7e63 kind=77de68 kind_name=01e781 giver=2be88c turn_in=fb5a8b turn_in_maps=15f2a7 bit=b6589f requires_bit=887309 excludes_bit=f6e112 prev=f36b47 next=97d170 stages=a80fa1 objectives=3745c1 rewards=4d015e complete_talk=8fc1bb -->
|  |  |
|---|---|
| **Quest id** | `1001` |
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

1. Talk to [[wiki/npcs/214-owen|Owen]] (dialogue 702) — tracker: “Go to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Collect [[wiki/items/2654-whiter-chepa-fur|Whiter Chepa Fur]] × 5 from [[wiki/monsters/668-chepa-warrior|Chepa Warrior]] (drop 70%) — tracker: “White Chepa Fur (0/5)” — on [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127)
3. Collect [[wiki/items/2653-black-chepa-fur|Black Chepa Fur]] × 5 from [[wiki/monsters/669-chepa-archer|Chepa Archer]] (drop 70%) — tracker: “Black Chepa Fur (0/5)” — on [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127)
4. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 20,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 15

### Dialogue

#### Objective 1 (QuestTalk 702)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** Do not you think it's getting cold? If you have hair, you will be able to make clothes warmly  
> **Owen:** So, can you get me the some Chepa Fur?  
> *(accept / continue)*

#### Completion (QuestTalk 703)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **You:** I brought black and white Fur, here~  
> **Owen:** It's black and white~ I think I can make warm clothes this way~  
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
