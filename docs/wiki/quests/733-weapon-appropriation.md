---
title: "Weapon appropriation"
type: "quest"
id: 733
status: "complete"
missing: []
sources: ["client: Quest.cdb id 733", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 704", "client: QuestTalk.cdb id 852"]
name_key: "Quest_Title_681_"
kind: 3
kind_name: "Free"
giver: {"npc": 205}
turn_in: {"npc": 205}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 15
excludes_bit: 28
owned_field: 123
prev: [16]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit_group": 10011, "units": [646, 647], "count": 10, "item": 2578, "rate": 100, "maps": [123, 123, 123], "text_key": "Quest_QuickText_681_1_"}
  - {"n": 2, "type": 1, "what": "collect", "unit_group": 10012, "units": [648, 649], "count": 5, "item": 2579, "rate": 100, "maps": [123, 123, 123], "text_key": "Quest_QuickText_681_2_"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_681_5"}
rewards:
  - {"type": 2, "what": "exp", "amount": 60000, "shown": 60000}
  - {"type": 1, "what": "item", "item": 601, "count": 25, "pick": "fixed"}
offer_talk: 704
complete_talk: 852
---
<!-- generated:start -->
<!-- generated-keys: title=6b56e0 type=eb5b2b id=bc3f9e sources=cb044e name_key=6af71c kind=77de68 kind_name=01e781 giver=37f9c0 turn_in=37f9c0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f requires_bit=f1abd6 excludes_bit=0a57cb owned_field=40bd00 prev=504845 next=97d170 stages=30caa7 objectives=08183c rewards=618b61 offer_talk=a093a3 complete_talk=2dcc38 -->
|  |  |
|---|---|
|  | ![Weapon appropriation](wiki/assets/npcs/205.png) |
| **Quest id** | `733` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/205-lewellyn\|Lewellyn]] |
| **Turn in** | [[wiki/npcs/205-lewellyn\|Lewellyn]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 15 |
| **Not after bit** | 28 |
| **Field c7@10** | [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior\|(Lv 4) Swamps of Snake Warrior]] (123) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/16-farrell-s-request|Farrell's Request]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/32-swamps-of-snake-warrior|Swamps of Snake Warrior]]

### Objectives

1. Collect [[wiki/items/2578-lizard-spear|Lizard spear]] × 10 from any unit of kill group 10011 ([[wiki/monsters/646-lizard-swordsman|Lizard Swordsman]], [[wiki/monsters/647-lizard-swordsman|Lizard Swordsman]]) (drop 100%) — tracker: “Lizard spear acquistion (0/10)” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
2. Collect [[wiki/items/2579-lizard-knife|Lizard knife]] × 5 from any unit of kill group 10012 ([[wiki/monsters/648-elite-lizard-swordsman|Elite Lizard Swordsman]], [[wiki/monsters/649-elite-lizard-lancer|Elite Lizard Lancer]]) (drop 100%) — tracker: “Lizard sword acquisition (0/5)” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
3. Report (tracker line; done by turning the quest in) — tracker: “Go back to Lewellyn”

### Rewards

- **Basic reward:** 60,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 25

### Dialogue

#### Offer (QuestTalk 704)

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
