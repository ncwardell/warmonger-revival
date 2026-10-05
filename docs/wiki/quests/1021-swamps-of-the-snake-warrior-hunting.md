---
title: "Swamps of the Snake Warrior : Hunting"
type: "quest"
id: 1021
status: "partial"
missing: ["giver"]
sources: ["client: Quest.cdb id 1021", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 704", "client: QuestTalk.cdb id 852"]
name_key: "Quest_Title_1021"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 205}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 15
excludes_bit: 28
prev: [16]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 205, "talk": 704, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_Lewe"}
  - {"n": 2, "type": 1, "what": "collect", "unit_group": 10011, "units": [646, 647], "count": 10, "item": 2678, "rate": 100, "maps": [123, 123, 123], "text_key": "Quest_QuickText_1021_1"}
  - {"n": 3, "type": 1, "what": "collect", "unit_group": 10012, "units": [648, 649], "count": 5, "item": 2679, "rate": 100, "maps": [123, 123, 123], "text_key": "Quest_QuickText_1021_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_Lewe"}
rewards:
  - {"type": 2, "what": "exp", "amount": 40000, "shown": 40000}
  - {"type": 1, "what": "item", "item": 601, "count": 25, "pick": "fixed"}
complete_talk: 852
---
<!-- generated:start -->
<!-- generated-keys: title=4021c5 type=eb5b2b id=00e263 sources=91a271 name_key=43b48a kind=77de68 kind_name=01e781 giver=2be88c turn_in=37f9c0 turn_in_maps=15f2a7 bit=b6589f requires_bit=f1abd6 excludes_bit=0a57cb prev=504845 next=97d170 stages=a80fa1 objectives=aee6ba rewards=85d26a complete_talk=2dcc38 -->
|  |  |
|---|---|
| **Quest id** | `1021` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/205-lewellyn\|Lewellyn]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 15 |
| **Not after bit** | 28 |

### Chain

- **After:** [[wiki/quests/16-farrell-s-request|Farrell's Request]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/32-swamps-of-snake-warrior|Swamps of Snake Warrior]]

### Objectives

1. Talk to [[wiki/npcs/205-lewellyn|Lewellyn]] (dialogue 704) — tracker: “Go to Lewellyn” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Collect [[wiki/items/2678-lizard-spear|Lizard spear]] × 10 from any unit of kill group 10011 ([[wiki/monsters/646-lizard-swordsman|Lizard Swordsman]], [[wiki/monsters/647-lizard-swordsman|Lizard Swordsman]]) (drop 100%) — tracker: “Lizard spear acquistion (0/10)” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
3. Collect [[wiki/items/2679-lizard-knife|Lizard knife]] × 5 from any unit of kill group 10012 ([[wiki/monsters/648-elite-lizard-swordsman|Elite Lizard Swordsman]], [[wiki/monsters/649-elite-lizard-lancer|Elite Lizard Lancer]]) (drop 100%) — tracker: “Lizard sword acquisition (0/5)” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
4. Report (tracker line; done by turning the quest in) — tracker: “Return to Lewellyn” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 40,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 25

### Dialogue

#### Objective 1 (QuestTalk 704)

Speaker: [[wiki/npcs/205-lewellyn|Lewellyn]]

> **Lewellyn:** The weapon in the arsenal is almost gone.<br>So the Lizard have they have a lot of weapons.  
> **Lewellyn:** I want you to bring the Lizardmen 's weapons and fill them with weapons.  
> *(accept / continue)*

#### Completion (QuestTalk 852)

Speaker: [[wiki/npcs/205-lewellyn|Lewellyn]]

> **Lewellyn:** I am proud to see the arsenal being filled again.  
> *(accept / continue)*
<!-- generated:end -->

## Notes

Repeatable ("Free") quest. The WM 0110 patch moved repeatable quests to a "Free Quests" tab on the quest board, and WM 0124 removed that tab again ([[gameplay/patch-history]]). *patch notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/patch-history]]

## Open questions

The client names no giver for this row. Whether it was offered from the quest board or by the NPC of its first "talk" step is not known ([[gameplay/patch-history]] 0110/0124).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
