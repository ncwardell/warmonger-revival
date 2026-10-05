---
title: "Items - AI Steering & Item Use"
type: "quest"
id: 691
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 691", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "video: [[gameplay/video-tutorial-walkthrough]] steps 3-5 (lesson exp shown = table value)", "client: QuestTalk.cdb id 887"]
name_key: "Quest_Title_500"
kind: 2
kind_name: "Guide"
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
  - {"n": 1, "type": 4, "what": "talk", "npc": 204, "talk": 887, "text_key": "Quest_QuickText_724_0"}
  - {"n": 2, "type": 10, "what": "buy_item", "item": 1105, "count": 1, "maps": [120, 120, 120], "text_key": "Quest_QuickText_500_1"}
  - {"n": 3, "type": 14, "what": null, "b": 1, "text_key": "Quest_QuickText_500_2"}
  - {"n": 4, "type": 13, "what": "use_item", "item": 1105, "count": 1, "text_key": "Quest_QuickText_500_3"}
rewards:
  - {"type": 2, "what": "exp", "amount": 50000, "shown": 50000}
---
<!-- generated:start -->
<!-- generated-keys: title=98e7d3 type=eb5b2b id=3da7e2 sources=1a2497 name_key=5d0569 kind=da4b92 kind_name=875cc6 giver=847ad4 turn_in=847ad4 bit=6fb84a requires_bit=12c6fc automatic=5ffe53 prev=5c6c1d next=97d170 stages=fabb9c objectives=2be88c objectives_client=951b24 rewards=e7ec17 -->
|  |  |
|---|---|
| **Quest id** | `691` |
| **Kind** | Guide (kind 2) |
| **Giver** | automatic |
| **Turn in** | automatic |
| **Completion bit** | 96 |
| **Requires bit** | 22 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 96 with:** [[wiki/quests/1518-items-ai-steering-item-use|Items - AI Steering & Item Use]] (completing one closes the others)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Talk to [[wiki/npcs/204-wren|Wren]] (dialogue 887) — tracker: “Return to Wren”
2. Buy [[wiki/items/1105-pyrotechnics|Pyrotechnics]] — tracker: “Pyrotechnics Item Buy (0/1)” — on [[wiki/fields/120-fortress|Fortress]] (120)
3. Type 14 — move to battlefield / monster area?; values b=1 — tracker: “Moving the battlefield”
4. Use [[wiki/items/1105-pyrotechnics|Pyrotechnics]] — tracker: “Use the Pyrotechnics Item (0/1) (Quick Slot Registration or Right-click an item in inventory and click Ground)”

Stages (`flag1..5` = [1, 2, 3, 4, 4]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 50,000 exp

### Dialogue

#### Objective 1 (QuestTalk 887)

Speaker: [[wiki/npcs/207-athan|Athan]]

> **Athan:** Going to war?? Then you will need this item! It's called Pyrotechnics, which means you can control AI! Use it well!  
> *(end)*
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
