---
title: "Tow Canyon"
type: "quest"
id: 34
status: "complete"
missing: []
sources: ["client: Quest.cdb id 34", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 798", "client: QuestTalk.cdb id 799", "client: QuestTalk.cdb id 896"]
name_key: "Quest_Title_20"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 30
requires_bit: 29
prev: [33]
next: [35, 743, 744, 745, 1036, 1038]
stages: [1, 2, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 99, "talk": 896, "maps": [120, 120, 120], "text_key": "Quest_QuickText_Area"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 125, "maps": [125, 125, 125], "text_key": "Quest_QuickText_20_0"}
  - {"n": 3, "type": 1, "what": "collect", "unit_group": 10023, "units": [658, 659], "count": 1, "item": 2582, "rate": 10, "maps": [125, 125, 125], "text_key": "Quest_QuickText_20_1"}
  - {"n": 4, "type": 0, "what": "report", "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1800000, "shown": 1636364}
  - {"type": 1, "what": "item", "item": 688, "count": 8, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 7162, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 7172, "count": 1, "pick": "choose"}
offer_talk: 798
complete_talk: 799
---
<!-- generated:start -->
<!-- generated-keys: title=30a3eb type=eb5b2b id=f1f836 sources=aac74f name_key=edaf43 kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=22d200 requires_bit=7719a1 prev=78415f next=b444ad stages=642aaf objectives=7556ae rewards=20e00d offer_talk=0c0266 complete_talk=01c0c9 -->
|  |  |
|---|---|
|  | ![Tow Canyon](wiki/assets/npcs/200.png) |
| **Quest id** | `34` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 30 |
| **Requires bit** | 29 |

### Chain

- **After:** [[wiki/quests/33-ghost-fortress|Ghost Fortress]]
- **Next:** [[wiki/quests/35-demon-hell|Demon Hell]], [[wiki/quests/743-demon-hell|Demon Hell]], [[wiki/quests/744-acquire-materials|Acquire materials]], [[wiki/quests/745-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/1036-demon-hell-hunting|Demon Hell : Hunting]], [[wiki/quests/1038-demon-hell-collecting-material|Demon Hell : Collecting material]]

### Objectives

1. Talk to Dimension Gate (dialogue 896) — tracker: “Go to Dimension Gate”
2. Go to [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125) — tracker: “Move to the Tow Canyon Border” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)
3. Collect [[wiki/items/2582-innocence-piece|Innocence Piece]] from any unit of kill group 10023 ([[wiki/monsters/658-tow-warrior|Tow Warrior]], [[wiki/monsters/659-tow-sorcerer|Tow Sorcerer]]) (drop 10%) — tracker: “Kill Tows to collect Sculptures (0/1)” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)
4. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

Stages (`flag1..5` = [1, 2, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 1,800,000 exp (shown in game as 1,636,364); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 8
- **Choose one:** [[wiki/items/7162-movement-rune|Movement(%) Rune]] *or* [[wiki/items/7172-attack-speed-rune|Attack Speed(%) Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 798)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** I'll tell you about the analysis. This piece is a Piece of Innocence. <br> Do you know what that is?  
> **You:** Yes... I heard about it from the Castle Priest.  
> **Freya:** Oh, so you know how dangerous this is? I believe there is a piece in the Tow Canyon now.  
> *(accept / continue)*

#### Objective 1 (QuestTalk 896)

Speaker: NPC

> *(end)*

#### Completion (QuestTalk 799)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** You brought it ~ I will give you the pieces that come next when you come.  
> **Freya:** you said that you can use Innocence~~  
> *(accept / continue)*  
> *(accept / continue)*

### Mentioned in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]]
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/npc-locations|NPC and point-of-interest locations]]
- [[gameplay/patch-history|Patch notes and other sources]]
- [[gameplay/server-rules|Server rules checklist]]
<!-- generated:end -->

## Notes

<!-- hand-written: add what you know, with a source -->

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/crush-mechanics]]
- [[gameplay/patch-history]]

## Open questions

Crush Online had Ghost Fortress as the level-5 and Tow Canyon as the level-6 dungeon, and players reported quest markers mixed up between the two; the Warmonger client names field 124 "[Lv 6] Ghost Fortress" and 125 "[Lv 5] Tow Canyon", and WM 0615 unlocks Tow Canyon at 24 and Ghost Fortress at 25 ([[gameplay/crush-mechanics]], [[gameplay/patch-history]]). The client order is used.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
