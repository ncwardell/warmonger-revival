---
title: "Ghost Fortress : Hunting"
type: "quest"
id: 1026
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1026", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 751", "client: QuestTalk.cdb id 848"]
name_key: "Quest_Title_1026"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"auto": true}
bit: 0
requires_bit: 123
excludes_bit: 29
automatic: true
prev: [47]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 205, "talk": 751, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_Lewe"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 124, "maps": [124, 124, 124], "text_key": "Quest_QuickText_1026_1"}
  - {"n": 3, "type": 5, "what": "gadget", "gadget": 9, "talk": 848, "maps": [124, 124, 124], "text_key": "Quest_QuickText_1026_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 15000, "shown": 15000}
---
<!-- generated:start -->
<!-- generated-keys: title=c86430 type=eb5b2b id=183723 sources=9c4f60 name_key=101d17 kind=77de68 kind_name=01e781 giver=2be88c turn_in=847ad4 bit=b6589f requires_bit=40bd00 excludes_bit=7719a1 automatic=5ffe53 prev=80af3c next=97d170 stages=a80fa1 objectives=aabbe9 rewards=0db38f -->
|  |  |
|---|---|
| **Quest id** | `1026` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | automatic |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 123 |
| **Not after bit** | 29 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/47-create-potion|Create Potion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/33-ghost-fortress|Ghost Fortress]]

### Objectives

1. Talk to [[wiki/npcs/205-lewellyn|Lewellyn]] (dialogue 751) — tracker: “Go to Lewellyn” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Go to [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124) — tracker: “Move to the Boundary of the Haunted Fortress” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
3. Talk to [[wiki/nodes/12409-ghost-soldier|Ghost soldier]] (gadget 9) (dialogue 848) — tracker: “Talk to a ghosted soldier” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 15,000 exp

### Dialogue

#### Objective 1 (QuestTalk 751)

Speaker: [[wiki/npcs/205-lewellyn|Lewellyn]]

> **Lewellyn:** There was a soldier dispatched to the Ghost Fortress and he still hasn't returned. Could you go to the Ghost Fortress and find the soldier?  
> **Lewellyn:** When you find it, please bring the soldier ~  
> *(accept / continue)*

#### Objective 3 (QuestTalk 848)

Speaker: [[wiki/nodes/12409-ghost-soldier|Ghost soldier]] (gadget 9)

> **You:** I came to hear from Lewellyn, what happened?  
> **Ghost Soldier:** I died without being able to kill all the Ghosts ... Can you take care of the Ghosts here for me?  
> **You:** Leave it to me.  
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
