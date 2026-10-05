---
title: "Fisher's scales"
type: "quest"
id: 732
status: "complete"
missing: []
sources: ["client: Quest.cdb id 732", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 671", "client: QuestTalk.cdb id 672"]
name_key: "Quest_Title_650_"
kind: 3
kind_name: "Free"
giver: {"npc": 210}
turn_in: {"npc": 210}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 22
excludes_bit: 15
owned_field: 122
prev: [22]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit": 644, "count": 20, "item": 2577, "rate": 100, "maps": [122, 122, 122], "text_key": "Quest_QuickText_650_1_"}
  - {"n": 2, "type": 1, "what": "collect", "unit": 645, "count": 10, "item": 2576, "rate": 100, "maps": [122, 122, 122], "text_key": "Quest_QuickText_650_2_"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_650_3"}
rewards:
  - {"type": 2, "what": "exp", "amount": 67500, "shown": 67500}
  - {"type": 1, "what": "item", "item": 601, "count": 25, "pick": "fixed"}
offer_talk: 671
complete_talk: 672
---
<!-- generated:start -->
<!-- generated-keys: title=71241a type=eb5b2b id=9deb86 sources=037f51 name_key=c3a427 kind=77de68 kind_name=01e781 giver=7abdb8 turn_in=7abdb8 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f requires_bit=12c6fc excludes_bit=f1abd6 owned_field=05a8ea prev=5c6c1d next=97d170 stages=30caa7 objectives=e9f33a rewards=91396b offer_talk=97e01b complete_talk=540d3e -->
|  |  |
|---|---|
|  | ![Fisher's scales](../assets/npcs/210.png) |
| **Quest id** | `732` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 22 |
| **Not after bit** | 15 |
| **Field c7@10** | [[wiki/dungeons/122-lv-3-tsunami-lake\|(Lv 3) Tsunami Lake]] (122) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/16-farrell-s-request|Farrell's Request]]

### Objectives

1. Collect [[wiki/items/2577-fisher-s-scales|Fisher's Scales]] × 20 from [[wiki/monsters/644-fisher|Fisher]] (drop 100%) — tracker: “Fisher's Scales (0/20)” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
2. Collect [[wiki/items/2576-elite-fisher-s-scales|Elite Fisher's Scales]] × 10 from [[wiki/monsters/645-elite-fisher|Elite Fisher]] (drop 100%) — tracker: “Elite Fisher's Scales (0/10)” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Kesley”

### Rewards

- **Basic reward:** 67,500 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 25

### Dialogue

#### Offer (QuestTalk 671)

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
