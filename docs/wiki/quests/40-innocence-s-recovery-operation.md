---
title: "Innocence's recovery operation"
type: "quest"
id: 40
status: "stub"
missing: ["rewards"]
sources: ["client: Quest.cdb id 40", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 819", "client: QuestTalk.cdb id 820"]
name_key: "Quest_Title_26"
kind: 0
kind_name: "Main"
giver: {"gadget": 6}
turn_in: {"gadget": 6}
offer_maps: [114, 114, 114]
turn_in_maps: [114, 114, 114]
bit: 93
requires_bit: 39
prev: [39]
next: [41]
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit": 829, "count": 4, "item": 2548, "rate": 30, "maps": [114, 114, 114], "text_key": "Quest_QuickText_26_1"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_26_2"}
rewards: null
rewards_client:
  - {"type": 6, "what": null, "a": -100000}
  - {"type": 2, "what": "exp", "amount": 500000, "shown": 454545}
offer_talk: 819
complete_talk: 820
---
<!-- generated:start -->
<!-- generated-keys: title=a4656b type=eb5b2b id=af3e13 sources=23f1fd name_key=30c31c kind=b6589f kind_name=b3f808 giver=dbc19e turn_in=dbc19e offer_maps=91194d turn_in_maps=91194d bit=08a352 requires_bit=ca3512 prev=44b878 next=8f80dd stages=a80fa1 objectives=831397 rewards=2be88c rewards_client=4a5e56 offer_talk=6ef2c7 complete_talk=4b68e4 -->
|  |  |
|---|---|
| **Quest id** | `40` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/nodes/11406-knightage-s-leader\|Knightage's Leader]] / [[wiki/nodes/11407-knightage-s-leader\|Knightage's Leader]] / [[wiki/nodes/11408-knightage-s-leader\|Knightage's Leader]] (gadget 6) |
| **Turn in** | [[wiki/nodes/11406-knightage-s-leader\|Knightage's Leader]] / [[wiki/nodes/11407-knightage-s-leader\|Knightage's Leader]] / [[wiki/nodes/11408-knightage-s-leader\|Knightage's Leader]] (gadget 6) |
| **Offered on** | [[wiki/fields/114-the-way-go-to-devildom\|The way go to devildom]] (114) |
| **Completion bit** | 93 |
| **Requires bit** | 39 |

### Chain

- **After:** [[wiki/quests/39-innocence-s-recovery-operation|Innocence's recovery operation]]
- **Next:** [[wiki/quests/41-innocence-s-recovery-operation|Innocence's recovery operation]]

### Objectives

1. Collect [[wiki/items/2548-broken-innocence|Broken Innocence]] × 4 from [[wiki/monsters/829-fragile-elite-demon-hunter|Fragile Elite Demon Hunter]] (drop 30%) — tracker: “Kill the Fragile Demon Hunter (0/4) (Find Innocence)”
2. Report (tracker line; done by turning the quest in) — tracker: “Find out with knightage's leader”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

> [!warning] Not all reward types are decoded
> The rows below are the client's (`rewards_client`). Write the server-ready list into `rewards:` once the unclear ones are understood.

- **Basic reward:** 500,000 exp (shown in game as 454,545)
- Type 6 — negative value (cost?); values a=-100000

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 819)

Speaker: [[wiki/nodes/11406-knightage-s-leader|Knightage's Leader]] / [[wiki/nodes/11407-knightage-s-leader|Knightage's Leader]] / [[wiki/nodes/11408-knightage-s-leader|Knightage's Leader]] (gadget 6)

> **Scout:** One of the Demons in here has Inoocence.  
> **You:** I will find it.  
> *(accept / continue)*  
> *(accept / continue)*

#### Completion (QuestTalk 820)

Speaker: [[wiki/nodes/11406-knightage-s-leader|Knightage's Leader]] / [[wiki/nodes/11407-knightage-s-leader|Knightage's Leader]] / [[wiki/nodes/11408-knightage-s-leader|Knightage's Leader]] (gadget 6)

> **Scout:** No!! That's enough!! Thanks!  
> **You:** Oh my goodness!  Why me…  
> **Scout:** I am sorry about what happened.  You will meet me later.  
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
