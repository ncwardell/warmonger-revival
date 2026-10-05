---
title: "Go to Shaia"
type: "quest"
id: 4
status: "complete"
missing: []
sources: ["client: Quest.cdb id 4", "client: QuestTalk.cdb id 713", "client: QuestTalk.cdb id 789"]
name_key: "Quest_Title_692"
kind: 0
kind_name: "Main"
giver: {"npc": 239}
turn_in: {"npc": 201}
offer_maps: [89, 93, 97]
turn_in_maps: [89, 93, 97]
bit: 4
requires_bit: 3
prev: [3]
next: [5]
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 0, "what": "report", "maps": [89, 93, 97], "text_key": "Quest_QuickText_T_SHAIA"}
rewards: []
offer_talk: 789
complete_talk: 713
---
<!-- generated:start -->
<!-- generated-keys: title=7a1949 type=eb5b2b id=1b6453 sources=4b11b4 name_key=374b60 kind=b6589f kind_name=b3f808 giver=9d96c7 turn_in=444e6c offer_maps=6e2020 turn_in_maps=6e2020 bit=1b6453 requires_bit=77de68 prev=f1e31d next=10ae24 stages=30caa7 objectives=2731e4 rewards=97d170 offer_talk=fc1200 complete_talk=84b0b5 -->
|  |  |
|---|---|
|  | ![Go to Shaia](../assets/npcs/239.png) |
| **Quest id** | `4` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/239-floyd\|Floyd]] |
| **Turn in** | [[wiki/npcs/201-shaia\|Shaia]] |
| **Offered on** | Arslan: [[wiki/fields/89-training-ground\|Training Ground]] (89) · Erion: [[wiki/fields/93-training-ground\|Training Ground]] (93) · Armia: [[wiki/fields/97-training-ground\|Training Ground]] (97) |
| **Completion bit** | 4 |
| **Requires bit** | 3 |
| **Current server** | enabled in `server/quests.py` |

### Chain

- **After:** [[wiki/quests/3-the-task-at-hand|The task at hand]]
- **Next:** [[wiki/quests/5-united-problem-solvers|United Problem Solvers]]

### Objectives

1. Report (tracker line; done by turning the quest in) — tracker: “Talk to Shaia”

### Rewards

None in the client.

### Dialogue

#### Offer (QuestTalk 789)

Speaker: [[wiki/npcs/239-floyd|Floyd]]

> **Floyd:** I will finally be able to finish my studies.  
> **You:** It was a pleasure to help you out, I better get back to Shaia.  
> **Floyd:** Yes, hurry up. We'll meet again.  
> *(accept / continue)*

#### Completion (QuestTalk 713)

Speaker: [[wiki/npcs/201-shaia|Shaia]]

> **You:** Shaia... Why is it always me who gets to do the gathering tasks?  
> **You:** I always end up doing the lousy jobs no one else wants to do ... <br>Can you please send me on a proper mission?

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: step 9 at [6:00](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=360s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 4 at [12:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=760s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 7 at [9:46](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=586s); step 8 at [10:07](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=607s)
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
