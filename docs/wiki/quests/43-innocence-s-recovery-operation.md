---
title: "Innocence's recovery operation"
type: "quest"
id: 43
status: "complete"
missing: []
sources: ["client: Quest.cdb id 43", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 824", "client: QuestTalk.cdb id 825"]
name_key: "Quest_Title_29"
kind: 0
kind_name: "Main"
giver: {"npc": 325}
turn_in: {"npc": 325}
bit: 98
requires_bit: 97
prev: [42]
next: [46]
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 0, "what": "report", "text_key": "Quest_QuickText_29_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 500000, "shown": 454545}
offer_talk: 824
complete_talk: 825
---
<!-- generated:start -->
<!-- generated-keys: title=a4656b type=eb5b2b id=0286dd sources=30537e name_key=a97fd2 kind=b6589f kind_name=b3f808 giver=ad0cc6 turn_in=ad0cc6 bit=31bd9b requires_bit=812ed4 prev=54c441 next=10537b stages=a80fa1 objectives=cb8aeb rewards=f79b21 offer_talk=5fbdc8 complete_talk=5375ef -->
|  |  |
|---|---|
|  | ![Innocence's recovery operation](wiki/assets/npcs/325.png) |
| **Quest id** | `43` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/325-joel\|Joel]] |
| **Turn in** | [[wiki/npcs/325-joel\|Joel]] |
| **Completion bit** | 98 |
| **Requires bit** | 97 |

### Chain

- **After:** [[wiki/quests/42-innocence-s-recovery-operation|Innocence's recovery operation]]
- **Next:** [[wiki/quests/46-to-oracle-of-knowledge|To Oracle of knowledge]]

### Objectives

1. Report (tracker line; done by turning the quest in) — tracker: “Chat with hero Joel : Priest  (Imprinting attempt)”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 500,000 exp (shown in game as 454,545)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 824)

Speaker: [[wiki/npcs/325-joel|Joel]]

> **Joel:** HAHA!! So I will be the best in the whole world, too!  
> *(accept / continue)*

#### Completion (QuestTalk 825)

Speaker: [[wiki/npcs/325-joel|Joel]]

> **You:** But it's still not enough to accept Innocence's power <br> I have heard Shaia recommend you, am I right?  
> **You:** Yes… is anything wrong?  
> **Joel:** Not at all. <br> Please go to Fortress.  You have a new mission now.  
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
