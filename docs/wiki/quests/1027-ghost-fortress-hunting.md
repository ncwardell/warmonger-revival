---
title: "Ghost Fortress : Hunting"
type: "quest"
id: 1027
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1027", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 752", "client: QuestTalk.cdb id 850"]
name_key: "Quest_Title_1027"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 205}
turn_in_maps: [120, 120, 120]
bit: 0
prev: []
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "unit_group": 10029, "units": [654, 655], "count": 30, "maps": [124, 124, 124], "text_key": "Quest_QuickText_1027_1"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10030, "units": [656, 657], "count": 8, "maps": [124, 124, 124], "text_key": "Quest_QuickText_1027_2"}
  - {"n": 3, "type": 5, "what": "gadget", "gadget": 10, "talk": 850, "maps": [124, 124, 124], "text_key": "Quest_QuickText_1027_3"}
  - {"n": 4, "type": 0, "what": "report", "text_key": "Quest_QuickText_CB_Lewe"}
rewards:
  - {"type": 2, "what": "exp", "amount": 35000, "shown": 35000}
  - {"type": 1, "what": "item", "item": 601, "count": 30, "pick": "fixed"}
complete_talk: 752
---
<!-- generated:start -->
<!-- generated-keys: title=c86430 type=eb5b2b id=e194ee sources=f8c776 name_key=354d01 kind=77de68 kind_name=01e781 giver=2be88c turn_in=37f9c0 turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 stages=30caa7 objectives=7217ff rewards=12877f complete_talk=b7ecf1 -->
|  |  |
|---|---|
| **Quest id** | `1027` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/205-lewellyn\|Lewellyn]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Kill any unit of kill group 10029 ([[wiki/monsters/654-black-ghost|Black Ghost]], [[wiki/monsters/655-red-ghost|Red Ghost]]) × 30 — tracker: “Killed ghost (0/30)” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
2. Kill any unit of kill group 10030 ([[wiki/monsters/656-elite-black-ghost|Elite Black Ghost]], [[wiki/monsters/657-elite-red-ghost|Elite Red Ghost]]) × 8 — tracker: “Killed Elite ghost (0/8)” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
3. Talk to [[wiki/nodes/12410-ghost-soldier|Ghost soldier]] (gadget 10) (dialogue 850) — tracker: “Go to the Ghost soldier” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
4. Report (tracker line; done by turning the quest in) — tracker: “Return to Lewellyn”

### Rewards

- **Basic reward:** 35,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 30

### Dialogue

#### Objective 3 (QuestTalk 850)

Speaker: [[wiki/nodes/12410-ghost-soldier|Ghost soldier]] (gadget 10)

> **You:** I have come to kill all the ghosts.  
> **Ghost Soldier:** Thank you. Now I can go to Heaven and find peace ~ Well... Goodbye  
> *(accept / continue)*

#### Completion (QuestTalk 752)

Speaker: [[wiki/npcs/205-lewellyn|Lewellyn]]

> **Lewellyn:** What happened to the dispatched soldier?  
> **You:** The dispatched soldier is dead… I have released one of the dispatched soldiers, so you can stop worrying.  
> **Lewellyn:** Okay.. Thank you. Thank you.  
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
