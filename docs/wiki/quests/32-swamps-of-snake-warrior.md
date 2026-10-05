---
title: "Swamps of Snake Warrior"
type: "quest"
id: 32
status: "complete"
missing: []
sources: ["client: Quest.cdb id 32", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 794", "client: QuestTalk.cdb id 795", "client: QuestTalk.cdb id 896"]
name_key: "Quest_Title_18"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 28
requires_bit: 15
prev: [16]
next: [761, 769, 772, 773, 778]
stages: [1, 2, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 99, "talk": 896, "maps": [120, 120, 120], "text_key": "Quest_QuickText_Area"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 123, "maps": [123, 123, 123], "text_key": "Quest_QuickText_18_0"}
  - {"n": 3, "type": 1, "what": "kill", "unit_group": 10011, "units": [646, 647], "count": 5, "maps": [123, 123, 123], "text_key": "Quest_QuickText_18_1"}
  - {"n": 4, "type": 1, "what": "kill", "unit_group": 10012, "units": [648, 649], "count": 5, "maps": [123, 123, 123], "text_key": "Quest_QuickText_18_2"}
  - {"n": 5, "type": 0, "what": "report", "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1500000, "shown": 1363636}
  - {"type": 1, "what": "item", "item": 688, "count": 6, "pick": "fixed"}
offer_talk: 794
complete_talk: 795
---
<!-- generated:start -->
<!-- generated-keys: title=510c1f type=eb5b2b id=cb4e52 sources=fd8679 name_key=a425c9 kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=0a57cb requires_bit=f1abd6 prev=504845 next=2382cd stages=642aaf objectives=e5ff1e rewards=471c1b offer_talk=41990b complete_talk=61b5df -->
|  |  |
|---|---|
|  | ![Swamps of Snake Warrior](wiki/assets/npcs/200.png) |
| **Quest id** | `32` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 28 |
| **Requires bit** | 15 |

### Chain

- **After:** [[wiki/quests/16-farrell-s-request|Farrell's Request]]
- **Next:** [[wiki/quests/761-killed-boss-of-border-area-no-1|killed boss of Border area No.1]], [[wiki/quests/769-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/772-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/773-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/778-ghost-soldier|Ghost soldier]]

### Objectives

1. Talk to Dimension Gate (dialogue 896) — tracker: “Go to Dimension Gate”
2. Go to [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123) — tracker: “Move to Swampps of Snake Warrior's border” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
3. Kill any unit of kill group 10011 ([[wiki/monsters/646-lizard-swordsman|Lizard Swordsman]], [[wiki/monsters/647-lizard-swordsman|Lizard Swordsman]]) × 5 — tracker: “Killed Lizard (0/5)” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
4. Kill any unit of kill group 10012 ([[wiki/monsters/648-elite-lizard-swordsman|Elite Lizard Swordsman]], [[wiki/monsters/649-elite-lizard-lancer|Elite Lizard Lancer]]) × 5 — tracker: “Killed elite Lizard (0/5)” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
5. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

Stages (`flag1..5` = [1, 2, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 1,500,000 exp (shown in game as 1,363,636); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 6

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 794)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** I just received a message that someone saw a strange object in the Swamps of the Snake Warrior… Could you go find it and bring it to me?  
> *(accept / continue)*  
> *(accept / continue)*

#### Objective 1 (QuestTalk 896)

Speaker: NPC

> *(end)*

#### Completion (QuestTalk 795)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **You:** I went to the Swamps of the Snake Warrior but I did not find anything strange…  
> **Freya:** I do not think the information is wrong…  
> *(accept / continue)*  
> *(accept / continue)*

### Mentioned in

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
