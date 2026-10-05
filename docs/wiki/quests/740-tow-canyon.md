---
title: "Tow Canyon"
type: "quest"
id: 740
status: "complete"
missing: []
sources: ["client: Quest.cdb id 740", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 757", "client: QuestTalk.cdb id 849"]
name_key: "Quest_Title_757"
kind: 3
kind_name: "Free"
giver: {"npc": 204}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 0
requires_bit: 29
excludes_bit: 30
owned_field: 125
automatic: true
prev: [33]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 125, "maps": [125, 125, 125], "text_key": "Quest_QuickText_20_0"}
  - {"n": 2, "type": 5, "what": "gadget", "gadget": 11, "talk": 849, "maps": [125, 125, 125], "text_key": "Quest_QuickText_757_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 37500, "shown": 37500}
offer_talk: 757
---
<!-- generated:start -->
<!-- generated-keys: title=30a3eb type=eb5b2b id=2e0ab5 sources=9a5a30 name_key=e138c5 kind=77de68 kind_name=01e781 giver=4518d0 turn_in=847ad4 offer_maps=15f2a7 bit=b6589f requires_bit=7719a1 excludes_bit=22d200 owned_field=0ca927 automatic=5ffe53 prev=78415f next=97d170 stages=30caa7 objectives=06941f rewards=7af226 offer_talk=d64ce8 -->
|  |  |
|---|---|
|  | ![Tow Canyon](../assets/npcs/204.png) |
| **Quest id** | `740` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/204-wren\|Wren]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 29 |
| **Not after bit** | 30 |
| **Field c7@10** | [[wiki/dungeons/125-lv-5-tow-canyon\|(Lv 5) Tow Canyon]] (125) (contract: fort the nation must own) |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/33-ghost-fortress|Ghost Fortress]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/34-tow-canyon|Tow Canyon]]

### Objectives

1. Go to [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125) — tracker: “Move to the Tow Canyon Border” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)
2. Talk to [[wiki/nodes/12511-dispatch-knight|Dispatch Knight]] (gadget 11) (dialogue 849) — tracker: “Talk with dispatch knight” — on [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] (125)

### Rewards

- **Basic reward:** 37,500 exp

### Dialogue

#### Offer (QuestTalk 757)

Speaker: [[wiki/npcs/204-wren|Wren]]

> **Wren:** Knights were dispatched to the Tow Canyon <br> but Knights alone will not be able to kill monsters in the Tow Canyon. Go help them!  
> *(accept / continue)*

#### Objective 2 (QuestTalk 849)

Speaker: [[wiki/nodes/12511-dispatch-knight|Dispatch Knight]] (gadget 11)

> **Dispatch knight:** How did you get here? This is very dangerous.  
> **You:** I listened to Wren. I came to help you organize the Tow Canyon.  
> **Dispatch knight:** Oh~! i See! Thank you so much for killing the tows inside.  
> *(accept / continue)*

### Mentioned in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]]
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/npc-locations|NPC and point-of-interest locations]]
- [[gameplay/patch-history|Patch notes and other sources]]
- [[gameplay/server-rules|Server rules checklist]]
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
