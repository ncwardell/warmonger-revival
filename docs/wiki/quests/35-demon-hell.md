---
title: "Demon Hell"
type: "quest"
id: 35
status: "complete"
missing: []
sources: ["client: Quest.cdb id 35", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 800", "client: QuestTalk.cdb id 801", "client: QuestTalk.cdb id 896"]
name_key: "Quest_Title_21"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 31
requires_bit: 30
prev: [34]
next: [36, 746, 747, 748, 780, 1041, 1042]
prerequisites:
  - {"type": 6, "what": "item", "item": 2583, "count": 1}
stages: [1, 2, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 99, "talk": 896, "maps": [120, 120, 120], "text_key": "Quest_QuickText_Area"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 126, "maps": [126, 126, 126], "text_key": "Quest_QuickText_21_0"}
  - {"n": 3, "type": 1, "what": "collect", "unit_group": 10031, "units": [662], "count": 1, "item": 2582, "rate": 10, "maps": [126, 126, 126], "text_key": "Quest_QuickText_21_1"}
  - {"n": 4, "type": 0, "what": "report", "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1900000, "shown": 1727273}
  - {"type": 1, "what": "item", "item": 688, "count": 9, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 7082, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 7092, "count": 1, "pick": "choose"}
offer_talk: 800
complete_talk: 801
---
<!-- generated:start -->
<!-- generated-keys: title=be0e6f type=eb5b2b id=972a67 sources=7aa9cd name_key=dcaebe kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=632667 requires_bit=22d200 prev=91a33c next=3ec111 prerequisites=a7d2c7 stages=642aaf objectives=255dc8 rewards=fb1c8a offer_talk=290a52 complete_talk=549843 -->
|  |  |
|---|---|
|  | ![Demon Hell](wiki/assets/npcs/200.png) |
| **Quest id** | `35` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 31 |
| **Requires bit** | 30 |

### Chain

- **After:** [[wiki/quests/34-tow-canyon|Tow Canyon]]
- **Next:** [[wiki/quests/36-thorn-s-hell|Thorn's Hell]], [[wiki/quests/746-devil-s-material|Devil's material]], [[wiki/quests/747-acquire-materials|Acquire materials]], [[wiki/quests/748-ore-and-plant-collection|Ore and plant collection]], [[wiki/quests/780-bring-the-demon-crystals|Bring the Demon Crystals]], [[wiki/quests/1041-thorn-s-hell-hunting|Thorn's Hell : Hunting]], [[wiki/quests/1042-thorn-s-hell-collecting-material|Thorn's Hell : Collecting material]]

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/2583-half-innocence\|Half-innocence]] |

### Objectives

1. Talk to Dimension Gate (dialogue 896) — tracker: “Go to Dimension Gate”
2. Go to [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] (126) — tracker: “Move to the Demon Hell Border” — on [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] (126)
3. Collect [[wiki/items/2582-innocence-piece|Innocence Piece]] from any unit of kill group 10031 ([[wiki/monsters/662-demon-hunter|Demon Hunter]]) (drop 10%) — tracker: “Kill Demons to collect Sculptures (0/1)” — on [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] (126)
4. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

Stages (`flag1..5` = [1, 2, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 1,900,000 exp (shown in game as 1,727,273); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 9
- **Choose one:** [[wiki/items/7082-armor-penetration-rune|Armor Penetration Rune]] *or* [[wiki/items/7092-magic-resist-penetration-rune|Magic resist Penetration Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 800)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** I hope you will be able to use the power of Innocence freely  
> **Freya:** Urgent news! The piece is in the Demon Hell~ Please come quickly! I think we should find it before anyone else does.  
> *(accept / continue)*  
> *(accept / continue)*

#### Objective 1 (QuestTalk 896)

Speaker: NPC

> *(end)*

#### Completion (QuestTalk 801)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** You got it ~ Now you have 3 pieces ~  
> **Freya:** This piece seems to be divided by four ~ I will call you when you find the last piece.  
> *(accept / continue)*  
> *(accept / continue)*

### Mentioned in

- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/patch-history|Patch notes and other sources]]
- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]]
- [[gameplay/server-rules|Server rules checklist]]
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
