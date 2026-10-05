---
title: "Tsunami Lake : Hunting"
type: "quest"
id: 1016
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1016", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 671", "client: QuestTalk.cdb id 672"]
name_key: "Quest_Title_1016"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 210}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 22
excludes_bit: 15
prev: [22]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 210, "talk": 671, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_Kes"}
  - {"n": 2, "type": 1, "what": "collect", "unit": 644, "count": 20, "item": 2677, "rate": 100, "maps": [122, 122, 122], "text_key": "Quest_QuickText_1016_1"}
  - {"n": 3, "type": 1, "what": "collect", "unit": 645, "count": 10, "item": 2676, "rate": 100, "maps": [122, 122, 122], "text_key": "Quest_QuickText_1016_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_Kes"}
rewards:
  - {"type": 2, "what": "exp", "amount": 45000, "shown": 45000}
  - {"type": 1, "what": "item", "item": 601, "count": 25, "pick": "fixed"}
complete_talk: 672
---
<!-- generated:start -->
<!-- generated-keys: title=5f04e2 type=eb5b2b id=49ae64 sources=245abd name_key=76459e kind=77de68 kind_name=01e781 giver=2be88c turn_in=7abdb8 turn_in_maps=15f2a7 bit=b6589f requires_bit=12c6fc excludes_bit=f1abd6 prev=5c6c1d next=97d170 stages=a80fa1 objectives=53b157 rewards=8fe2d7 complete_talk=540d3e -->
|  |  |
|---|---|
| **Quest id** | `1016` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 22 |
| **Not after bit** | 15 |

### Chain

- **After:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/16-farrell-s-request|Farrell's Request]]

### Objectives

1. Talk to [[wiki/npcs/210-kesley|Kesley]] (dialogue 671) — tracker: “Go to Kesley” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Collect [[wiki/items/2677-fisher-s-scales|Fisher's Scales]] × 20 from [[wiki/monsters/644-fisher|Fisher]] (drop 100%) — tracker: “Fisher's Scales (0/20)” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
3. Collect [[wiki/items/2676-elite-fisher-s-scales|Elite Fisher's Scales]] × 10 from [[wiki/monsters/645-elite-fisher|Elite Fisher]] (drop 100%) — tracker: “Elite Fisher's Scales (0/10)” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
4. Report (tracker line; done by turning the quest in) — tracker: “Return to Kesley” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 45,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 25

### Dialogue

#### Objective 1 (QuestTalk 671)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** Can you kill the mutant Fisher living in the water?  
> **Kesley:** Please kill the fisher and bring the token ~  
> *(accept / continue)*

#### Completion (QuestTalk 672)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **You:** Oh ~ This is Fisher's scales ~ Thank you  
> *(accept / continue)*  
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
