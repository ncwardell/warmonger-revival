---
title: "Tow Canyon : Hunting"
type: "quest"
id: 1032
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1032", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 758", "client: QuestTalk.cdb id 851"]
name_key: "Quest_Title_1032"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 204}
turn_in_maps: [120, 120, 120]
bit: 0
prev: []
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "unit_group": 10023, "units": [658, 659], "count": 15, "maps": [125, 125, 125], "text_key": "Quest_QuickText_1032_1"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10024, "units": [660, 661], "count": 5, "maps": [125, 125, 125], "text_key": "Quest_QuickText_1032_2"}
  - {"n": 3, "type": 5, "what": "gadget", "gadget": 12, "talk": 851, "maps": [125, 125, 125], "text_key": "Quest_QuickText_1032_3"}
  - {"n": 4, "type": 0, "what": "report", "text_key": "Quest_QuickText_CB_REN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 50000, "shown": 50000}
  - {"type": 1, "what": "item", "item": 611, "count": 30, "pick": "fixed"}
complete_talk: 758
---
<!-- generated:start -->
<!-- generated-keys: title=06f38d type=eb5b2b id=842205 sources=ab35b8 name_key=a9765a kind=77de68 kind_name=01e781 giver=2be88c turn_in=4518d0 turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 stages=30caa7 objectives=6860da rewards=f3b612 complete_talk=82a506 -->
|  |  |
|---|---|
| **Quest id** | `1032` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/204-wren\|Wren]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Kill any unit of kill group 10023 ([[wiki/monsters/658-tow-warrior|Tow Warrior]], [[wiki/monsters/659-tow-sorcerer|Tow Sorcerer]]) × 15 — tracker: “Killed Tow (0/15)” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)
2. Kill any unit of kill group 10024 ([[wiki/monsters/660-elite-tow-warrior|Elite Tow Warrior]], [[wiki/monsters/661-elite-tow-sorcerer|Elite Tow Sorcerer]]) × 5 — tracker: “Killed Elite Tow (0/5)” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)
3. Talk to [[wiki/nodes/12512-dispatch-knight|Dispatch Knight]] (gadget 12) (dialogue 851) — tracker: “Go to the Dispatch knight” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)
4. Report (tracker line; done by turning the quest in) — tracker: “Return to Wren”

### Rewards

- **Basic reward:** 50,000 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30

### Dialogue

#### Objective 3 (QuestTalk 851)

Speaker: [[wiki/nodes/12512-dispatch-knight|Dispatch Knight]] (gadget 12)

> **Dispatch knight:** I arranged all the inside ~  
> **Dispatch knight:** It's very fast~ I think I know why you sent it to me ~ Thank you so much for telling us about Wren.  
> **Dispatch knight:** I will finish this and go. Goodbye  
> *(accept / continue)*

#### Completion (QuestTalk 758)

Speaker: [[wiki/npcs/204-wren|Wren]]

> **Wren:** Did you go to the Tow Canyon. Did it go well?  
> **You:** Yes~ The knight says he's staying in the Tow Canyon to finish what he started.  
> **Wren:** Thank you very much for your next visit.  
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
