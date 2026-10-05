---
title: "Chepa Village"
type: "quest"
id: 30
status: "complete"
missing: []
sources: ["client: Quest.cdb id 30", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 790", "client: QuestTalk.cdb id 791", "client: QuestTalk.cdb id 896"]
name_key: "Quest_Title_654"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 25
requires_bit: 26
prev: [26]
next: [15, 727, 728, 729, 1006, 1007]
stages: [1, 2, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 99, "talk": 896, "maps": [120, 120, 120], "text_key": "Quest_QuickText_Area"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 127, "maps": [127, 127, 127], "text_key": "Quest_QuickText_654_1"}
  - {"n": 3, "type": 1, "what": "kill", "unit_group": 10025, "units": [668, 669], "count": 10, "maps": [127, 127, 127], "text_key": "Quest_QuickText_654_2"}
  - {"n": 4, "type": 1, "what": "kill", "unit_group": 10026, "units": [670, 671], "count": 5, "maps": [127, 127, 127], "text_key": "Quest_QuickText_654_3"}
  - {"n": 5, "type": 0, "what": "report", "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 550000, "shown": 500000}
  - {"type": 1, "what": "item", "item": 688, "count": 6, "pick": "fixed"}
offer_talk: 790
complete_talk: 791
---
<!-- generated:start -->
<!-- generated-keys: title=8bdd22 type=eb5b2b id=22d200 sources=fed299 name_key=f78ae2 kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=f6e112 requires_bit=887309 prev=f36b47 next=d5de15 stages=642aaf objectives=b9e4f5 rewards=a4589f offer_talk=4912f5 complete_talk=732506 -->
|  |  |
|---|---|
|  | ![Chepa Village](wiki/assets/npcs/200.png) |
| **Quest id** | `30` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 25 |
| **Requires bit** | 26 |

### Chain

- **After:** [[wiki/quests/26-border-area-normal-mode|Border Area Normal Mode]]
- **Next:** [[wiki/quests/15-repel-the-skeleton-invasion|Repel the Skeleton Invasion]], [[wiki/quests/727-the-necessary-materials|The necessary materials]], [[wiki/quests/728-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/729-collecting-material|Collecting material]], [[wiki/quests/1006-skull-temple-hunting|Skull Temple : Hunting]], [[wiki/quests/1007-skull-temple-collecting-material|Skull Temple : Collecting material]]
- **Shares completion bit 25 with:** [[wiki/quests/1524-party-party-person|Party - Party Person]] (completing one closes the others)

### Objectives

1. Talk to Dimension Gate (dialogue 896) — tracker: “Go to Dimension Gate”
2. Go to [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127) — tracker: “Move to Chepa Village” — on [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127)
3. Kill any unit of kill group 10025 ([[wiki/monsters/668-chepa-warrior|Chepa Warrior]], [[wiki/monsters/669-chepa-archer|Chepa Archer]]) × 10 — tracker: “Kill Chepa (0/10)” — on [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127)
4. Kill any unit of kill group 10026 ([[wiki/monsters/670-elite-chepa-warrior|Elite Chepa Warrior]], [[wiki/monsters/671-elite-chepa-archer|Elite Chepa Archer]]) × 5 — tracker: “Kill Elite Chepa (0/5)” — on [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127)
5. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

Stages (`flag1..5` = [1, 2, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 550,000 exp (shown in game as 500,000); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 6

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 790)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** I just received an urgent message. The number of Chepas in the Chepa Village is increasing extremely quickly at the moment.  
> **Freya:** Go to the Chepa Village and kill all of them immediately!!  
> *(accept / continue)*  
> *(accept / continue)*

#### Objective 1 (QuestTalk 896)

Speaker: NPC

> *(end)*

#### Completion (QuestTalk 791)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **You:** I killed those Chepas like you asked me to.  
> **Freya:** Thanks a lot.  I think we don't have to worry about the Chepa Village for while.  
> *(accept / continue)*  
> *(accept / continue)*

### Mentioned in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]]
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
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
