---
title: "Repel the Skeleton Invasion"
type: "quest"
id: 15
status: "complete"
missing: []
sources: ["client: Quest.cdb id 15", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 653", "client: QuestTalk.cdb id 654", "client: QuestTalk.cdb id 896"]
name_key: "Quest_Title_641"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 14
requires_bit: 25
prev: [30, 1524]
next: [22, 724, 725, 726, 1011, 1012]
stages: [1, 2, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 99, "talk": 896, "maps": [120, 120, 120], "text_key": "Quest_QuickText_Area"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 121, "maps": [121, 121, 121], "text_key": "Quest_QuickText_641_1"}
  - {"n": 3, "type": 1, "what": "kill", "unit": 81, "count": 1, "maps": [121, 121, 121], "text_key": "Quest_QuickText_641_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 600000, "shown": 545455}
  - {"type": 1, "what": "item", "item": 688, "count": 6, "pick": "fixed"}
offer_talk: 653
complete_talk: 654
---
<!-- generated:start -->
<!-- generated-keys: title=532a4c type=eb5b2b id=f1abd6 sources=af8ac1 name_key=9d0103 kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=fa35e1 requires_bit=f6e112 prev=71a868 next=2cc013 stages=642aaf objectives=ecdf9c rewards=af45f4 offer_talk=e1c03d complete_talk=db00e4 -->
|  |  |
|---|---|
|  | ![Repel the Skeleton Invasion](../assets/npcs/200.png) |
| **Quest id** | `15` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 14 |
| **Requires bit** | 25 |

### Chain

- **After:** [[wiki/quests/30-chepa-village|Chepa Village]], [[wiki/quests/1524-party-party-person|Party - Party Person]]
- **Next:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]], [[wiki/quests/724-find-lost-item|Find lost item]], [[wiki/quests/725-collecting-material|Collecting material]], [[wiki/quests/726-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/1011-skull-cemetery-hunting|Skull Cemetery : Hunting]], [[wiki/quests/1012-skull-cemetery-collecting-material|Skull Cemetery : Collecting material]]

### Objectives

1. Talk to Dimension Gate (dialogue 896) — tracker: “Go to Dimension Gate”
2. Go to [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121) — tracker: “Go to the Skull Temple” — on [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121)
3. Kill [[wiki/npcs/81-transmission-equipment|Transmission equipment]] × 1 — tracker: “Destroy the Transmission equipment” — on [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121)
4. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

Stages (`flag1..5` = [1, 2, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 600,000 exp (shown in game as 545,455); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 6

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 653)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Now you look ready for battle.  As I said before the Undead's invasion is close.  
> **Freya:** We need all the help we can get.<br>If monsters invade to Gaia now, the world will fall into chaos.  
> **Freya:** Go to the Skull Temple and destroy the Transmission Equipment.  
> **You:** Trust me. I will be able to complete the mission.  
> *(accept / continue)*

#### Objective 1 (QuestTalk 896)

Speaker: NPC

> *(end)*

#### Completion (QuestTalk 654)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **You:** I'm back and I finished the mission!  
> **Freya:** Thank you for your efforts. Because of your actions we prevented the world falling into chaos.<br>I will offer this new Gear which is adapted now.  
> **You:** And so I became a real Protector ..... Hahahaha, finally I'm getting the recognition I deserve!  
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
