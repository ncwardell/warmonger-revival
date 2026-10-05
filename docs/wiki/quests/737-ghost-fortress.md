---
title: "Ghost Fortress"
type: "quest"
id: 737
status: "complete"
missing: []
sources: ["client: Quest.cdb id 737", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 751", "client: QuestTalk.cdb id 848"]
name_key: "Quest_Title_754"
kind: 3
kind_name: "Free"
giver: {"npc": 205}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 0
requires_bit: 123
excludes_bit: 29
owned_field: 124
automatic: true
prev: [47]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 124, "maps": [124, 124, 124], "text_key": "Quest_QuickText_754_1"}
  - {"n": 2, "type": 5, "what": "gadget", "gadget": 9, "talk": 848, "maps": [124, 124, 124], "text_key": "Quest_QuickText_754_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 22500, "shown": 22500}
offer_talk: 751
---
<!-- generated:start -->
<!-- generated-keys: title=13d702 type=eb5b2b id=4cae59 sources=b75040 name_key=7cf8f4 kind=77de68 kind_name=01e781 giver=37f9c0 turn_in=847ad4 offer_maps=15f2a7 bit=b6589f requires_bit=40bd00 excludes_bit=7719a1 owned_field=f38cfe automatic=5ffe53 prev=80af3c next=97d170 stages=30caa7 objectives=b3f6a3 rewards=cc625e offer_talk=758a25 -->
|  |  |
|---|---|
|  | ![Ghost Fortress](wiki/assets/npcs/205.png) |
| **Quest id** | `737` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/205-lewellyn\|Lewellyn]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 123 |
| **Not after bit** | 29 |
| **Field c7@10** | [[wiki/dungeons/124-lv-6-ghost-fortress\|(Lv 6) Ghost Fortress]] (124) (contract: fort the nation must own) |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/47-create-potion|Create Potion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/33-ghost-fortress|Ghost Fortress]]

### Objectives

1. Go to [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124) — tracker: “Move to the Boundary of the Haunted Fortress” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)
2. Talk to [[wiki/nodes/12409-ghost-soldier|Ghost soldier]] (gadget 9) (dialogue 848) — tracker: “Talk to a ghosted soldier” — on [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] (124)

### Rewards

- **Basic reward:** 22,500 exp

### Dialogue

#### Offer (QuestTalk 751)

Speaker: [[wiki/npcs/205-lewellyn|Lewellyn]]

> **Lewellyn:** There was a soldier dispatched to the Ghost Fortress and he still hasn't returned. Could you go to the Ghost Fortress and find the soldier?  
> **Lewellyn:** When you find it, please bring the soldier ~  
> *(accept / continue)*

#### Objective 2 (QuestTalk 848)

Speaker: [[wiki/nodes/12409-ghost-soldier|Ghost soldier]] (gadget 9)

> **You:** I came to hear from Lewellyn, what happened?  
> **Ghost Soldier:** I died without being able to kill all the Ghosts ... Can you take care of the Ghosts here for me?  
> **You:** Leave it to me.  
> *(accept / continue)*

### Mentioned in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]]
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/npc-locations|NPC and point-of-interest locations]]
- [[gameplay/patch-history|Patch notes and other sources]]
- [[gameplay/precept-shop|Precept shop and precept quests]]
- [[gameplay/server-rules|Server rules checklist]]
- [[gameplay/video-dungeon-run|Video notes: Nas Village dungeon run (ZonderCoRe)]]
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
