---
title: "Meeting Freya"
type: "quest"
id: 19
status: "complete"
missing: []
sources: ["client: Quest.cdb id 19", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 666"]
name_key: "Quest_Title_645"
kind: 0
kind_name: "Main"
giver: {"auto": true}
turn_in: {"npc": 224}
turn_in_maps: [90, 94, 98]
bit: 19
requires_bit: 16
prev: [17]
next: [20]
prerequisites:
  - {"type": 6, "what": "item", "item": 911, "count": 1}
stages: [1, 2, 3, 3, 3]
objectives:
  - {"n": 1, "type": 13, "what": "use_item", "item": 911, "count": 1, "text_key": "Quest_QuickText_645_2"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_F_BERNICE"}
rewards:
  - {"type": 2, "what": "exp", "amount": 220000, "shown": 200000}
complete_talk: 666
---
<!-- generated:start -->
<!-- generated-keys: title=a9e78b type=eb5b2b id=b3f0c7 sources=faae23 name_key=d930dd kind=b6589f kind_name=b3f808 giver=847ad4 turn_in=c2dfa7 turn_in_maps=18e60d bit=b3f0c7 requires_bit=1574bd prev=79d296 next=6a5bf6 prerequisites=154ad3 stages=8f1a2c objectives=d9b961 rewards=0256a4 complete_talk=cd3f0c -->
|  |  |
|---|---|
| **Quest id** | `19` |
| **Kind** | Main (kind 0) |
| **Giver** | automatic |
| **Turn in** | [[wiki/npcs/224-bernice\|Bernice]] |
| **Turned in on** | Arslan: [[wiki/fields/90-castle\|Castle]] (90) · Erion: [[wiki/fields/94-castle\|Castle]] (94) · Armia: [[wiki/fields/98-castle\|Castle]] (98) |
| **Completion bit** | 19 |
| **Requires bit** | 16 |

### Chain

- **After:** [[wiki/quests/17-support-the-abyss-expedition|Support the Abyss expedition]]
- **Next:** [[wiki/quests/20-talk-to-freya|Talk to Freya]]

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/911-scroll-castle\|Scroll : Castle]] |

### Objectives

1. Use [[wiki/items/911-scroll-castle|Scroll : Castle]] — tracker: “Use the Castle Scroll”
2. Report (tracker line; done by turning the quest in) — tracker: “Go to Bernice”

Stages (`flag1..5` = [1, 2, 3, 3, 3]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 220,000 exp (shown in game as 200,000)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Completion (QuestTalk 666)

Speaker: [[wiki/npcs/224-bernice|Bernice]]

> **Bernice:** You are well-known in all the land for your bravery. But this mission is even more difficult than the ones you faced before.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: at [57:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=3445s); step 22 at [56:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=3417s)
<!-- generated:end -->

## Notes

Freya: meet Bernice on the plaza first ([56:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=3415s)). The player used the Castle scroll and talked to Bernice (224, Oracle of Judgment) in the Castle at [57:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=3475s). Panel: 200,000 exp. Bernice also offers unhappy players a change of nation ([[gameplay/video-early-quests]] step 22). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-early-quests]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
