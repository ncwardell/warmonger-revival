---
title: "Tow Canyon : Hunting"
type: "quest"
id: 1031
status: "partial"
missing: ["giver"]
sources: ["client: Quest.cdb id 1031", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 757", "client: QuestTalk.cdb id 849"]
name_key: "Quest_Title_1031"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"auto": true}
bit: 0
requires_bit: 29
excludes_bit: 30
automatic: true
prev: [33]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 204, "talk": 757, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_REN"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 125, "maps": [125, 125, 125], "text_key": "Quest_QuickText_1031_1"}
  - {"n": 3, "type": 5, "what": "gadget", "gadget": 11, "talk": 849, "maps": [125, 125, 125], "text_key": "Quest_QuickText_1031_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 25000, "shown": 25000}
---
<!-- generated:start -->
<!-- generated-keys: title=06f38d type=eb5b2b id=45ce12 sources=bc62d0 name_key=f2213b kind=77de68 kind_name=01e781 giver=2be88c turn_in=847ad4 bit=b6589f requires_bit=7719a1 excludes_bit=22d200 automatic=5ffe53 prev=78415f next=97d170 stages=a80fa1 objectives=f969c3 rewards=412979 -->
|  |  |
|---|---|
| **Quest id** | `1031` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | automatic |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 29 |
| **Not after bit** | 30 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/33-ghost-fortress|Ghost Fortress]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/34-tow-canyon|Tow Canyon]]

### Objectives

1. Talk to [[wiki/npcs/204-wren|Wren]] (dialogue 757) — tracker: “Go to Wren” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Go to [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125) — tracker: “Move to the Tow Canyon Border” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)
3. Talk to [[wiki/nodes/12511-dispatch-knight|Dispatch Knight]] (gadget 11) (dialogue 849) — tracker: “Talk with dispatch knight” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 25,000 exp

### Dialogue

#### Objective 1 (QuestTalk 757)

Speaker: [[wiki/npcs/204-wren|Wren]]

> **Wren:** Knights were dispatched to the Tow Canyon <br> but Knights alone will not be able to kill monsters in the Tow Canyon. Go help them!  
> *(accept / continue)*

#### Objective 3 (QuestTalk 849)

Speaker: [[wiki/nodes/12511-dispatch-knight|Dispatch Knight]] (gadget 11)

> **Dispatch knight:** How did you get here? This is very dangerous.  
> **You:** I listened to Wren. I came to help you organize the Tow Canyon.  
> **Dispatch knight:** Oh~! i See! Thank you so much for killing the tows inside.  
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
