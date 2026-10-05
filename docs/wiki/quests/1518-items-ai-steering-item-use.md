---
title: "Items - AI Steering & Item Use"
type: "quest"
id: 1518
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 1518", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "client: QuestTalk.cdb id 887"]
name_key: "Quest_Title_Help_500"
kind: 12
kind_name: "Advice"
giver: {"auto": true}
turn_in: {"auto": true}
bit: 96
requires_bit: 22
automatic: true
prev: [22]
next: []
stages: [1, 2, 3, 4, 4]
objectives: null
objectives_client:
  - {"n": 1, "type": 4, "what": "talk", "npc": 207, "talk": 887, "text_key": "Quest_QuickText_725_0"}
  - {"n": 2, "type": 10, "what": "buy_item", "item": 1105, "count": 1, "maps": [120, 120, 120], "text_key": "Quest_QuickText_Help_500_1"}
  - {"n": 3, "type": 14, "what": null, "a": 2, "text_key": "Quest_QuickText_Help_500_2"}
  - {"n": 4, "type": 13, "what": "use_item", "item": 1105, "count": 1, "text_key": "Quest_QuickText_Help_500_3"}
rewards: []
help: {"text_key": "Quest_Title_Help_String_500"}
---
<!-- generated:start -->
<!-- generated-keys: title=98e7d3 type=eb5b2b id=c8ec39 sources=cb61c9 name_key=08180d kind=7b5200 kind_name=ec7dd4 giver=847ad4 turn_in=847ad4 bit=6fb84a requires_bit=12c6fc automatic=5ffe53 prev=5c6c1d next=97d170 stages=fabb9c objectives=2be88c objectives_client=1c07ef rewards=97d170 help=6a3a4b -->
|  |  |
|---|---|
| **Quest id** | `1518` |
| **Kind** | Advice (kind 12) |
| **Giver** | automatic |
| **Turn in** | automatic |
| **Completion bit** | 96 |
| **Requires bit** | 22 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 96 with:** [[wiki/quests/691-items-ai-steering-item-use|Items - AI Steering & Item Use]] (completing one closes the others)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Talk to [[wiki/npcs/207-athan|Athan]] (dialogue 887) — tracker: “Return to Athan”
2. Buy [[wiki/items/1105-pyrotechnics|Pyrotechnics]] — tracker: “Pyrotechnics Item Buy (0/1)” — on [[wiki/fields/120-fortress|Fortress]] (120)
3. Type 14 — move to battlefield / monster area?; values a=2 — tracker: “Moving the battlefield”
4. Use [[wiki/items/1105-pyrotechnics|Pyrotechnics]] — tracker: “Use the Pyrotechnics Item (0/1) (Quick Slot Registration or Right-click an item in inventory and click Ground)”

Stages (`flag1..5` = [1, 2, 3, 4, 4]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

None in the client.

### Dialogue

#### Objective 1 (QuestTalk 887)

Speaker: [[wiki/npcs/207-athan|Athan]]

> **Athan:** Going to war?? Then you will need this item! It's called Pyrotechnics, which means you can control AI! Use it well!  
> *(end)*

### Tip window

> You can play and control the AI when using the Pyrotechnics item.
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
