---
title: "The task at hand"
type: "quest"
id: 3
status: "complete"
missing: []
sources: ["client: Quest.cdb id 3", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 633", "client: QuestTalk.cdb id 636"]
name_key: "Quest_Title_632"
kind: 0
kind_name: "Main"
giver: {"npc": 239}
turn_in: {"npc": 239}
offer_maps: [89, 93, 97]
turn_in_maps: [89, 93, 97]
bit: 3
requires_bit: 2
prev: [2]
next: [4]
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit": 731, "count": 5, "item": 2552, "rate": 100, "maps": [89, 93, 97], "text_key": "Quest_QuickText_632_1"}
  - {"n": 2, "type": 1, "what": "collect", "unit": 732, "count": 5, "item": 2551, "rate": 100, "maps": [89, 93, 97], "text_key": "Quest_QuickText_632_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [89, 93, 97], "text_key": "Quest_QuickText_G_FLOYD"}
rewards:
  - {"type": 2, "what": "exp", "amount": 3850, "shown": 3500}
  - {"type": 1, "what": "item", "item": 401, "count": 1, "pick": "fixed"}
offer_talk: 636
complete_talk: 633
---
<!-- generated:start -->
<!-- generated-keys: title=372f51 type=eb5b2b id=77de68 sources=0a45ad name_key=390214 kind=b6589f kind_name=b3f808 giver=9d96c7 turn_in=9d96c7 offer_maps=6e2020 turn_in_maps=6e2020 bit=77de68 requires_bit=da4b92 prev=249983 next=8f4e34 stages=30caa7 objectives=fda49d rewards=8df38b offer_talk=bc6020 complete_talk=43b4d1 -->
|  |  |
|---|---|
|  | ![The task at hand](wiki/assets/npcs/239.png) |
| **Quest id** | `3` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/239-floyd\|Floyd]] |
| **Turn in** | [[wiki/npcs/239-floyd\|Floyd]] |
| **Offered on** | Arslan: [[wiki/fields/89-training-ground\|Training Ground]] (89) · Erion: [[wiki/fields/93-training-ground\|Training Ground]] (93) · Armia: [[wiki/fields/97-training-ground\|Training Ground]] (97) |
| **Completion bit** | 3 |
| **Requires bit** | 2 |
| **Current server** | enabled in `server/quests.py` |

### Chain

- **After:** [[wiki/quests/2-the-slime-is-mine|The Slime is mine]]
- **Next:** [[wiki/quests/4-go-to-shaia|Go to Shaia]]

### Objectives

1. Collect [[wiki/items/2552-bee-needle|Bee Needle]] × 5 from [[wiki/monsters/731-bee|Bee]] (drop 100%) — tracker: “Bee Needle (0/5)”
2. Collect [[wiki/items/2551-snake-leather|Snake Leather]] × 5 from [[wiki/monsters/732-cobra|Cobra]] (drop 100%) — tracker: “Cobra Leather (0/5)”
3. Report (tracker line; done by turning the quest in) — tracker: “Bring them to Floyd”

### Rewards

- **Basic reward:** 3,850 exp (shown in game as 3,500); [[wiki/items/401-helmet-of-life|Helmet of Life]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 636)

Speaker: [[wiki/npcs/239-floyd|Floyd]]

> **Floyd:** I need a couple more things for my research.<br>Are you up to the task?  
> **Floyd:** Hunt the bees and snakes around here in the training hill.<br>You will get Bee Stings and Snake Leather.<br>I need both for my research.  
> *(accept / continue)*

#### Completion (QuestTalk 633)

Speaker: [[wiki/npcs/239-floyd|Floyd]]

> **Floyd:** Thank you. Now I can continue my research.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: step 7 at [4:25](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=265s); step 8 at [5:45](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=345s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 3 at [7:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=420s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 5 at [7:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=450s); step 7 at [9:46](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=586s)
<!-- generated:end -->

## Notes

From Floyd: 5 Bee Needle (2552) from Bees (731) and 5 Snake Leather (2551) from Cobras (732), both dropped on every kill; the tracker calls the second item "Cobra Leather" ([7:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=450s), [[gameplay/video-tutorial-walkthrough]] step 6). Panel: 3,500 exp + Helmet of Life (401) ([7:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=420s)). Turned in at [12:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=755s), [9:46](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=586s) and [5:45](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=345s). Lesson 704 (Equip Gear) starts with it ([[gameplay/video-character-creation-and-tutorial]] §3 step 7). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-tutorial-walkthrough]]
- [[gameplay/video-character-creation-and-tutorial]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
