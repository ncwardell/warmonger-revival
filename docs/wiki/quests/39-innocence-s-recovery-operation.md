---
title: "Innocence's recovery operation"
type: "quest"
id: 39
status: "complete"
missing: []
sources: ["client: Quest.cdb id 39", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 817", "client: QuestTalk.cdb id 833"]
name_key: "Quest_Title_25"
kind: 0
kind_name: "Main"
giver: {"npc": 325}
turn_in: {"auto": true}
bit: 39
requires_bit: 38
automatic: true
prev: [38]
next: [40]
prerequisites:
  - {"type": 6, "what": "item", "item": 912, "count": 1}
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 13, "what": "use_item", "item": 912, "count": 1, "text_key": "Quest_QuickText_25_3"}
  - {"n": 2, "type": 4, "what": "talk", "npc": 200, "talk": 833, "maps": [120, 120, 120], "text_key": "Quest_QuickText_25_0"}
  - {"n": 3, "type": 12, "what": "reach_map", "map": 114, "maps": [114, 114, 114], "text_key": "Quest_QuickText_25_1"}
  - {"n": 4, "type": 5, "what": "gadget", "gadget": 6, "talk": 818, "maps": [114, 114, 114], "text_key": "Quest_QuickText_25_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 500000, "shown": 454545}
offer_talk: 817
---
<!-- generated:start -->
<!-- generated-keys: title=a4656b type=eb5b2b id=ca3512 sources=ba0bf6 name_key=0c3ef0 kind=b6589f kind_name=b3f808 giver=ad0cc6 turn_in=847ad4 bit=ca3512 requires_bit=5b384c automatic=5ffe53 prev=429a2a next=7b279c prerequisites=fda3f1 stages=a80fa1 objectives=ebb875 rewards=f79b21 offer_talk=2e946d -->
|  |  |
|---|---|
|  | ![Innocence's recovery operation](../assets/npcs/325.png) |
| **Quest id** | `39` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/325-joel\|Joel]] |
| **Turn in** | automatic |
| **Completion bit** | 39 |
| **Requires bit** | 38 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/38-innocence-s-recovery-operation|Innocence's recovery operation]]
- **Next:** [[wiki/quests/40-innocence-s-recovery-operation|Innocence's recovery operation]]

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/912-scroll-gaia\|Scroll : Gaia]] |

### Objectives

1. Use [[wiki/items/912-scroll-gaia|Scroll : Gaia]] — tracker: “Use the Gaia Scroll in your inventory.”
2. Talk to [[wiki/npcs/200-freya|Freya]] (dialogue 833) — tracker: “Go to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)
3. Go to [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]] (114) — tracker: “Move to Devildom” — on [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]] (114)
4. Talk to [[wiki/nodes/11406-knightage-s-leader|Knightage's Leader]] / [[wiki/nodes/11407-knightage-s-leader|Knightage's Leader]] / [[wiki/nodes/11408-knightage-s-leader|Knightage's Leader]] (gadget 6) (dialogue 818) — tracker: “Chat with knightage's leader” — on [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]] (114)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 500,000 exp (shown in game as 454,545)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 817)

Speaker: [[wiki/npcs/325-joel|Joel]]

> **You:** I am on my way now!!  
> *(accept / continue)*  
> *(accept / continue)*

#### Objective 2 (QuestTalk 833)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Are you on your way to see the Scout Leader? When you are done looking for the innocence, please come to me ~  
> *(accept / continue)*

#### Objective 4 (QuestTalk 818)

*QuestTalk 818 is not in the client.*
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
