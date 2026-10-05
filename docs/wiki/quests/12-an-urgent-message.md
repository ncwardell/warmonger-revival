---
title: "An urgent message"
type: "quest"
id: 12
status: "complete"
missing: []
sources: ["client: Quest.cdb id 12", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 650"]
name_key: "Quest_Title_639"
kind: 0
kind_name: "Main"
giver: {"auto": true}
turn_in: {"auto": true}
offer_maps: [0, 0, 120]
bit: 11
requires_bit: 10
automatic: true
prev: [11]
next: [122]
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 200, "talk": 650, "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 44000, "shown": 40000}
  - {"type": 1, "what": "item", "item": 601, "count": 20, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 20, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 700, "count": 10, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 7022, "count": 1, "pick": "fixed"}
---
<!-- generated:start -->
<!-- generated-keys: title=1e6f8b type=eb5b2b id=7b5200 sources=b5df11 name_key=a386ad kind=b6589f kind_name=b3f808 giver=847ad4 turn_in=847ad4 offer_maps=5e7629 bit=17ba07 requires_bit=b1d578 automatic=5ffe53 prev=3ad009 next=d4ee27 stages=a80fa1 objectives=cb520a rewards=46c527 -->
|  |  |
|---|---|
| **Quest id** | `12` |
| **Kind** | Main (kind 0) |
| **Giver** | automatic |
| **Turn in** | automatic |
| **Offered on** | Arslan: — · Erion: — · Armia: [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 11 |
| **Requires bit** | 10 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/11-an-urgent-message|An urgent message]]
- **Next:** [[wiki/quests/122-rune-equipment|Rune Equipment.]]

### Objectives

1. Talk to [[wiki/npcs/200-freya|Freya]] (dialogue 650) — tracker: “Talk to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 44,000 exp (shown in game as 40,000); [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 20; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 20; [[wiki/items/700-crystal-blue|Crystal : Blue]] × 10; [[wiki/items/7022-armor-rune|Armor Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Objective 1 (QuestTalk 650)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** You look like you had one hell of a journey ...  
> **You:** Frei asked me to deliver this letter to you.  
> **Freya:** A letter?? Thank you. You must be tired. You should rest now.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: step 23 at [21:35](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1295s); at [22:05](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1325s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 13 at [36:45](https://www.youtube.com/watch?v=s04CSN16w1s&t=2205s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 30 at [32:25](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1945s); step 32 at [33:05](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1985s)
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
