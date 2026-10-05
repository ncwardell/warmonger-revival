---
title: "Ghost Fortress"
type: "quest"
id: 33
status: "complete"
missing: []
sources: ["client: Quest.cdb id 33", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 796", "client: QuestTalk.cdb id 797", "client: QuestTalk.cdb id 896"]
name_key: "Quest_Title_19"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 29
requires_bit: 123
prev: [47]
next: [34, 740, 741, 742, 779, 1031, 1033]
stages: [1, 2, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 99, "talk": 896, "maps": [120, 120, 120], "text_key": "Quest_QuickText_Area"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 124, "maps": [124, 124, 124], "text_key": "Quest_QuickText_19_0"}
  - {"n": 3, "type": 1, "what": "collect", "unit_group": 10029, "units": [654, 655], "count": 1, "item": 2582, "rate": 10, "maps": [124, 124, 124], "text_key": "Quest_QuickText_19_1"}
  - {"n": 4, "type": 0, "what": "report", "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1700000, "shown": 1545455}
  - {"type": 1, "what": "item", "item": 688, "count": 7, "pick": "fixed"}
offer_talk: 796
complete_talk: 797
---
<!-- generated:start -->
<!-- generated-keys: title=13d702 type=eb5b2b id=b6692e sources=1a919d name_key=2882e2 kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=7719a1 requires_bit=40bd00 prev=80af3c next=7f63fd stages=642aaf objectives=685cd1 rewards=84dd37 offer_talk=732c0a complete_talk=176908 -->
|  |  |
|---|---|
|  | ![Ghost Fortress](wiki/assets/npcs/200.png) |
| **Quest id** | `33` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 29 |
| **Requires bit** | 123 |

### Chain

- **After:** [[wiki/quests/47-create-potion|Create Potion]]
- **Next:** [[wiki/quests/34-tow-canyon|Tow Canyon]], [[wiki/quests/740-tow-canyon|Tow Canyon]], [[wiki/quests/741-collecting-material|Collecting material]], [[wiki/quests/742-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/779-request-of-dispatch-knight|Request of dispatch knight]], [[wiki/quests/1031-tow-canyon-hunting|Tow Canyon : Hunting]], [[wiki/quests/1033-tow-canyon-collecting-material|Tow Canyon : Collecting material]]

### Objectives

1. Talk to Dimension Gate (dialogue 896) — tracker: “Go to Dimension Gate”
2. Go to [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124) — tracker: “Move to the Ghost Fortress Border” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
3. Collect [[wiki/items/2582-innocence-piece|Innocence Piece]] from any unit of kill group 10029 ([[wiki/monsters/654-black-ghost|Black Ghost]], [[wiki/monsters/655-red-ghost|Red Ghost]]) (drop 10%) — tracker: “Kill Ghosts to collect Sculptures (0/1)” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
4. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

Stages (`flag1..5` = [1, 2, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 1,700,000 exp (shown in game as 1,545,455); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 7

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 796)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** This time it's certain information. There is a monster with a strange piece in the border area of the Ghost Fortress. Can you bring it to me?  
> **Freya:** You should never touch things like that! Please take it with you since it may be dangerous.  
> *(accept / continue)*  
> *(accept / continue)*

#### Objective 1 (QuestTalk 896)

Speaker: NPC

> *(end)*

#### Completion (QuestTalk 797)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** You don't mind? I will try to analyze the pieces, so please just take a moment.  
> **Freya:** This piece is, uh... Wait a second... There's a problem with the Oracle of Nature.  
> *(accept / continue)*  
> *(accept / continue)*

### Mentioned in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]]
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/npc-locations|NPC and point-of-interest locations]]
- [[gameplay/patch-history|Patch notes and other sources]]
- [[gameplay/precept-shop|Precept shop and precept quests]]
- [[gameplay/server-rules|Server rules checklist]]
- [[gameplay/video-dungeon-run|Video notes: Nas Village dungeon run (ZonderCoRe)]]
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
