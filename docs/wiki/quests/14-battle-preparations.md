---
title: "Battle preparations"
type: "quest"
id: 14
status: "complete"
missing: []
sources: ["client: Quest.cdb id 14", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 668", "client: QuestTalk.cdb id 680", "client: QuestTalk.cdb id 739"]
name_key: "Quest_Title_640"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 13
requires_bit: 12
prev: [13]
next: [17, 104, 110]
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 214, "talk": 680, "maps": [120, 120, 120], "text_key": "Quest_QuickText_C_OWEN"}
  - {"n": 2, "type": 11, "what": "craft_item", "item": 885, "count": 100, "maps": [120, 120, 120], "text_key": "Quest_QuickText_640_3"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 55000, "shown": 50000}
  - {"type": 1, "what": "item", "item": 404, "count": 1, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 601, "count": 15, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 15, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 948, "count": 1, "pick": "fixed"}
offer_talk: 739
complete_talk: 668
---
<!-- generated:start -->
<!-- generated-keys: title=229ae6 type=eb5b2b id=fa35e1 sources=b72860 name_key=9aafdf kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=bd307a requires_bit=7b5200 prev=758a13 next=887a73 stages=30caa7 objectives=9db696 rewards=df8824 offer_talk=1c710b complete_talk=34c664 -->
|  |  |
|---|---|
|  | ![Battle preparations](wiki/assets/npcs/200.png) |
| **Quest id** | `14` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 13 |
| **Requires bit** | 12 |

### Chain

- **After:** [[wiki/quests/13-battle-preparations|Battle preparations]]
- **Next:** [[wiki/quests/17-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/104-delivering-punishment|Delivering Punishment]], [[wiki/quests/110-gear-manufacturing|Gear manufacturing]]

### Objectives

1. Talk to [[wiki/npcs/214-owen|Owen]] (dialogue 680) — tracker: “Go to Owen”
2. Craft [[wiki/items/885-potion-of-health-c|Potion of Health (C)]] × 100 — tracker: “Create a Health Potion [C]”
3. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

- **Basic reward:** 55,000 exp (shown in game as 50,000); [[wiki/items/404-shoes-of-life|Shoes of Life]]; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 15; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 15; [[wiki/items/948-auto-decomposition-hammer|Auto decomposition hammer]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 739)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Go to Owen and get some consumables.<br>Prepare for battle.  
> *(accept / continue)*  
> *(accept / continue)*  
> *(accept / continue)*

#### Objective 1 (QuestTalk 680)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** What brought you here?  
> **You:** I want to create new Gears.  
> **Owen:** Choose what you'd like and press the "Create"-button.  
> *(end)*

#### Completion (QuestTalk 668)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Did you finish your preparations? Maybe this will help.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: at [22:05](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1325s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 15 at [38:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=2312s)

### Mentioned in

- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]
<!-- generated:end -->

## Notes

Talk to Owen (214), craft 100 Potion of Health [C], then return to Freya ([40:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=2430s)–[41:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2480s); [[gameplay/video-character-creation-and-tutorial]] §3 After the tutorial). Panel: 50,000 exp + Shoes of Life (404) + 15/15 Passion Fragments + Auto decomposition hammer (948). Lesson 721 (decompose blue jewels) runs alongside ([[gameplay/video-early-quests]] step 15). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-character-creation-and-tutorial]]
- [[gameplay/video-early-quests]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
