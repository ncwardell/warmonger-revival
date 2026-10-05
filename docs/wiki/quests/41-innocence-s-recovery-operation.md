---
title: "Innocence's recovery operation"
type: "quest"
id: 41
status: "complete"
missing: []
sources: ["client: Quest.cdb id 41", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 821", "client: QuestTalk.cdb id 886"]
name_key: "Quest_Title_27"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"npc": 325}
offer_maps: [120, 120, 120]
bit: 95
requires_bit: 93
prev: [40]
next: [42]
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 327, "text_key": "Quest_QuickText_23_2_"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_24_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 500000, "shown": 454545}
  - {"type": 1, "what": "item", "item": 7022, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 7032, "count": 1, "pick": "choose"}
offer_talk: 886
complete_talk: 821
---
<!-- generated:start -->
<!-- generated-keys: title=a4656b type=eb5b2b id=761f22 sources=344fe6 name_key=e0d023 kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=ad0cc6 offer_maps=15f2a7 bit=8e63fd requires_bit=08a352 prev=7b279c next=54c441 stages=a80fa1 objectives=4e43af rewards=c13c21 offer_talk=f2d28e complete_talk=fbbf19 -->
|  |  |
|---|---|
|  | ![Innocence's recovery operation](../assets/npcs/200.png) |
| **Quest id** | `41` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/325-joel\|Joel]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 95 |
| **Requires bit** | 93 |

### Chain

- **After:** [[wiki/quests/40-innocence-s-recovery-operation|Innocence's recovery operation]]
- **Next:** [[wiki/quests/42-innocence-s-recovery-operation|Innocence's recovery operation]]

### Objectives

1. Talk to [[wiki/npcs/327-aenes|Aenes]] — tracker: “Go to castle's the Oracle of Protect (Use Scroll : Castle )”
2. Report (tracker line; done by turning the quest in) — tracker: “Go to Joel: (Moving the Temple through the Oracle of the Protection)”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 500,000 exp (shown in game as 454,545)
- **Choose one:** [[wiki/items/7022-armor-rune|Armor Rune]] *or* [[wiki/items/7032-magic-resist-rune|Magic Resist Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 886)

Speaker: [[wiki/npcs/325-joel|Joel]]

> **Joel:** Why did you come back here? We should go to the Castle soon and meet the Priest! Please go quickly ~  
> *(accept / continue)*

#### Completion (QuestTalk 821)

Speaker: [[wiki/npcs/325-joel|Joel]]

> **You:** The Scout Leader just attacted me and left with Innocence.  
> *(accept / continue)*  
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
