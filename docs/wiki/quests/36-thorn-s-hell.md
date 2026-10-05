---
title: "Thorn's Hell"
type: "quest"
id: 36
status: "complete"
missing: []
sources: ["client: Quest.cdb id 36", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 802", "client: QuestTalk.cdb id 803", "client: QuestTalk.cdb id 896"]
name_key: "Quest_Title_22"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 32
requires_bit: 31
prev: [35]
next: [44]
prerequisites:
  - {"type": 6, "what": "item", "item": 2584, "count": 1}
stages: [1, 2, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 99, "talk": 896, "maps": [120, 120, 120], "text_key": "Quest_QuickText_Area"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 129, "maps": [129, 129, 129], "text_key": "Quest_QuickText_22_0"}
  - {"n": 3, "type": 1, "what": "collect", "unit_group": 10035, "units": [679, 680], "count": 1, "item": 2582, "rate": 10, "maps": [129, 129, 129], "text_key": "Quest_QuickText_22_1"}
  - {"n": 4, "type": 0, "what": "report", "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 2000000, "shown": 1818182}
  - {"type": 1, "what": "item", "item": 688, "count": 10, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 7082, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 7092, "count": 1, "pick": "choose"}
offer_talk: 802
complete_talk: 803
---
<!-- generated:start -->
<!-- generated-keys: title=2cf110 type=eb5b2b id=fc074d sources=e6f44e name_key=8503e7 kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=cb4e52 requires_bit=632667 prev=5c3c3a next=7aed3f prerequisites=170645 stages=642aaf objectives=69e839 rewards=cacc81 offer_talk=acb033 complete_talk=9d0008 -->
|  |  |
|---|---|
|  | ![Thorn's Hell](../assets/npcs/200.png) |
| **Quest id** | `36` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 32 |
| **Requires bit** | 31 |

### Chain

- **After:** [[wiki/quests/35-demon-hell|Demon Hell]]
- **Next:** [[wiki/quests/44-innocence-report|Innocence report]]

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/2584-innocence-looking-for-shape\|Innocence looking for shape]] |

### Objectives

1. Talk to Dimension Gate (dialogue 896) — tracker: “Go to Dimension Gate”
2. Go to [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] (129) — tracker: “Move to the Thorn's Hell Border” — on [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] (129)
3. Collect [[wiki/items/2582-innocence-piece|Innocence Piece]] from any unit of kill group 10035 ([[wiki/monsters/679-demon-hunter|Demon Hunter]], [[wiki/monsters/680-devil-miner|Devil Miner]]) (drop 10%) — tracker: “Kill Demons to collect Sculptures (0/1)” — on [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] (129)
4. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

Stages (`flag1..5` = [1, 2, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 2,000,000 exp (shown in game as 1,818,182); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 10
- **Choose one:** [[wiki/items/7082-armor-penetration-rune|Armor Penetration Rune]] *or* [[wiki/items/7092-magic-resist-penetration-rune|Magic resist Penetration Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 802)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Three pieces are combined. The last piece is in Thorn's Hell~ It may be hard to find, but it's important that you bring it to me.  
> *(accept / continue)*  
> *(accept / continue)*

#### Objective 1 (QuestTalk 896)

Speaker: NPC

> *(end)*

#### Completion (QuestTalk 803)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Now you're all together. Finally, we can restore the innocence.  
> **Freya:** I know that only priest can restore innocence. Go to priest  
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
