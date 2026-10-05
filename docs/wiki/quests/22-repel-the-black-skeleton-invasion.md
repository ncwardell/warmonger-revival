---
title: "Repel the Black Skeleton Invasion"
type: "quest"
id: 22
status: "complete"
missing: []
sources: ["client: Quest.cdb id 22", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 664", "client: QuestTalk.cdb id 665", "client: QuestTalk.cdb id 896"]
name_key: "Quest_Title_648"
kind: 0
kind_name: "Main"
level: {"min": 23, "max": 30}
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 22
requires_bit: 14
prev: [15]
next: [16, 105, 111, 112, 113, 119, 691, 730, 731, 732, 1016, 1017, 1518]
prerequisites:
  - {"type": 4, "what": "level", "min": 23, "max": 30}
stages: [1, 2, 3, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 99, "talk": 896, "maps": [120, 120, 120], "text_key": "Quest_QuickText_Area"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 128, "maps": [128, 128, 128], "text_key": "Quest_QuickText_648_1"}
  - {"n": 3, "type": 1, "what": "kill", "unit": 81, "count": 1, "maps": [128, 128, 128], "text_key": "Quest_QuickText_648_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1100000, "shown": 1000000}
  - {"type": 1, "what": "item", "item": 854, "count": 3, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 688, "count": 6, "pick": "fixed"}
offer_talk: 664
complete_talk: 665
---
<!-- generated:start -->
<!-- generated-keys: title=edb162 type=eb5b2b id=12c6fc sources=925377 name_key=d96804 kind=b6589f kind_name=b3f808 level=b3be7d giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=12c6fc requires_bit=fa35e1 prev=017b8e next=204dd2 prerequisites=f47092 stages=0f733e objectives=6ecf90 rewards=8e225c offer_talk=88547b complete_talk=af7166 -->
|  |  |
|---|---|
|  | ![Repel the Black Skeleton Invasion](../assets/npcs/200.png) |
| **Quest id** | `22` |
| **Kind** | Main (kind 0) |
| **Level** | 23–30 |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 22 |
| **Requires bit** | 14 |

### Chain

- **After:** [[wiki/quests/15-repel-the-skeleton-invasion|Repel the Skeleton Invasion]]
- **Next:** [[wiki/quests/16-farrell-s-request|Farrell's Request]], [[wiki/quests/105-kesley-s-disgrace|Kesley's Disgrace]], [[wiki/quests/111-weapon-manufacturing|Weapon manufacturing]], [[wiki/quests/112-weapon-manufacturing|Weapon manufacturing]], [[wiki/quests/113-weapon-manufacturing|Weapon manufacturing]], [[wiki/quests/119-monster-area-wars|Monster area wars]], [[wiki/quests/691-items-ai-steering-item-use|Items - AI Steering & Item Use]], [[wiki/quests/730-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/731-collecting-material|Collecting material]], [[wiki/quests/732-fisher-s-scales|Fisher's scales]], [[wiki/quests/1016-tsunami-lake-hunting|Tsunami Lake : Hunting]], [[wiki/quests/1017-tsunami-lake-collecting-material|Tsunami Lake : Collecting material]], [[wiki/quests/1518-items-ai-steering-item-use|Items - AI Steering & Item Use]]

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 23–30 |

### Objectives

1. Talk to Dimension Gate (dialogue 896) — tracker: “Go to Dimension Gate”
2. Go to [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128) — tracker: “Go to the Skull Cemetery” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
3. Kill [[wiki/npcs/81-transmission-equipment|Transmission equipment]] × 1 — tracker: “Destroy the Transmission equipment” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
4. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

Stages (`flag1..5` = [1, 2, 3, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 1,100,000 exp (shown in game as 1,000,000); [[wiki/items/854-shining-passion|Shining Passion]] × 3; [[wiki/items/688-dimensional-energy|Dimensional energy]] × 6

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 664)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** I have another mission for you, but it will be difficult. Go to the Skull Cemetery and...  
> **You:** That sounds oddly familiar ...  
> **Freya:** Is that so? As I was saying before you interrupted me ... destroy the Transmission Equipment there!  
> *(accept / continue)*

#### Objective 1 (QuestTalk 896)

Speaker: NPC

> *(end)*

#### Completion (QuestTalk 665)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** You done already? Great!  
> **Freya:** See you soon!<br>This is New Gear. When you set all set You will be stronger than now, I swear.  
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
