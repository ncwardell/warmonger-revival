---
title: "Gear manufacturing"
type: "quest"
id: 110
status: "complete"
missing: []
sources: ["client: Quest.cdb id 110", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 807", "client: QuestTalk.cdb id 808", "video: [[gameplay/video-early-quests]] step 19 (objective 1 = craft one piece of gear at Odin; type 26 a=2 read as the gear category, *inferred*)"]
manual: ["objectives"]
name_key: "Quest_Title_110"
kind: 1
kind_name: "Sub"
giver: {"npc": 213}
turn_in: {"npc": 213}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 33
requires_bit: 13
prev: [14]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 26, "what": "craft_gear", "a": 2, "b": 1, "maps": [120, 120, 120], "text_key": "Quest_QuickText_110_1"}
  - {"n": 2, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_ODIN"}
objectives_client:
  - {"n": 1, "type": 26, "what": null, "a": 2, "b": 1, "maps": [120, 120, 120], "text_key": "Quest_QuickText_110_1"}
  - {"n": 2, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_ODIN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 12000, "shown": 10000}
  - {"type": 4, "what": "gold", "amount": 30000}
  - {"type": 1, "what": "item", "item": 7002, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 7012, "count": 1, "pick": "choose"}
offer_talk: 807
complete_talk: 808
---
<!-- generated:start -->
<!-- generated-keys: title=a84d52 type=eb5b2b id=5e796e sources=0eb369 name_key=5a3101 kind=356a19 kind_name=0bac50 giver=91ad7d turn_in=91ad7d offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6692e requires_bit=bd307a prev=76cdc5 next=97d170 stages=30caa7 objectives_client=bee846 rewards=237d96 offer_talk=425ac6 complete_talk=38afd2 -->
|  |  |
|---|---|
|  | ![Gear manufacturing](wiki/assets/npcs/213.png) |
| **Quest id** | `110` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/213-odin\|Odin]] |
| **Turn in** | [[wiki/npcs/213-odin\|Odin]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 33 |
| **Requires bit** | 13 |

### Chain

- **After:** [[wiki/quests/14-battle-preparations|Battle preparations]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Type 26 — craft gear (category a)?; values a=2, b=1 — tracker: “Manufacture Gear you need”
2. Report (tracker line; done by turning the quest in) — tracker: “Go to Odin”

### Rewards

- **Basic reward:** 12,000 exp (shown in game as 10,000); 30,000 gold
- **Choose one:** [[wiki/items/7002-attack-rune|Attack Rune]] *or* [[wiki/items/7012-ability-power-rune|Ability Power Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 807)

Speaker: [[wiki/npcs/213-odin|Odin]]

> **Odin:** Here for create Gear?  There is item that can go up to the maximum level depending on the type of Gear. <br> The material you need to make is to disassemble the stone.  
> *(end)*

#### Completion (QuestTalk 808)

Speaker: [[wiki/npcs/213-odin|Odin]]

> **Odin:** Did you make the Gear you wanted to? Reinforcement Gear. It will make you stronger than anybody else.  
> *(accept / continue)*  
> *(accept / continue)*

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 19 at [42:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=2555s)

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
<!-- generated:end -->

## Notes

Odin (213, Fortress) asks for one crafted piece of gear ([42:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=2555s)); done at [46:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=2785s). Odin's Create menu charged 0 gold for Life gear and 15,000 for Honor/Rise gear ([[gameplay/video-early-quests]] §3). Panel: 10,000 exp + 30,000 gold ([[gameplay/video-early-quests]] step 19). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-early-quests]]

## Open questions

The table lists a choice of Attack or Ability Power rune (7002/7012), but the reward panel showed no rune choice ([[gameplay/video-early-quests]] step 19). Objective type 26 is "craft gear" here and "craft consumables" in the Doping quests (961, 981); parameter a = 2 is read as the category, which is an inference.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
