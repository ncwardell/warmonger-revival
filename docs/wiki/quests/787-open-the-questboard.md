---
title: "Open The QuestBoard"
type: "quest"
id: 787
status: "complete"
missing: []
sources: ["client: Quest.cdb id 787", "client: QuestTalk.cdb id 916"]
name_key: "Quest_Title_787"
kind: 2
kind_name: "Guide"
level: {"min": 27}
giver: {"npc": 200}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 129
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 27}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 10004, "what": "client_open_panel", "panel": 4, "text_key": "Quest_QuickText_787_1"}
rewards: []
offer_talk: 916
help: {"image": "ui/HelpImage/Help_8.png", "text_key": "Quest_HelpText_787"}
---
<!-- generated:start -->
<!-- generated-keys: title=98b4de type=eb5b2b id=e00988 sources=e07288 name_key=b71482 kind=da4b92 kind_name=875cc6 level=8c32e3 giver=1caac0 turn_in=847ad4 offer_maps=15f2a7 bit=8b7471 automatic=5ffe53 prev=97d170 next=97d170 prerequisites=eb6b9f stages=30caa7 objectives=4c4ad6 rewards=97d170 offer_talk=5a4b36 help=8a17b6 -->
|  |  |
|---|---|
|  | ![Open The QuestBoard](wiki/assets/quests/787.png) |
| **Quest id** | `787` |
| **Kind** | Guide (kind 2) |
| **Level** | 27+ |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 129 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 27+ |

### Objectives

1. client event: panel opened (a: 1 world map, 2 reinforce, 3 TP panel, 4 quest board) (a = 4) — tracker: “Click icon to open the Questboard”

### Rewards

None in the client.

### Dialogue

#### Offer (QuestTalk 916)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** I am going to tell you about the quest board function.<br>It tells the quest information that can be performed through the quest board.<br>I hope that you will use it well as it provides the rewards you need for growth.  
> *(accept / continue)*

### Tip window

> Click on the icon to open the quest board window.

Image `ui/HelpImage/Help_8.png`.
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
