---
title: "An urgent message"
type: "quest"
id: 11
status: "complete"
missing: []
sources: ["client: Quest.cdb id 11", "client: QuestTalk.cdb id 643"]
name_key: "Quest_Title_639"
kind: 0
kind_name: "Main"
giver: {"npc": 198}
turn_in: {"auto": true}
offer_maps: [88, 92, 96]
bit: 10
requires_bit: 9
automatic: true
prev: [10]
next: [12]
prerequisites:
  - {"type": 6, "what": "item", "item": 912, "count": 1}
  - {"type": 6, "what": "item", "item": 2567, "count": 1}
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 13, "what": "use_item", "item": 912, "count": 1, "text_key": "Quest_QuickText_639_2"}
rewards: []
offer_talk: 643
---
<!-- generated:start -->
<!-- generated-keys: title=1e6f8b type=eb5b2b id=17ba07 sources=d4e81f name_key=a386ad kind=b6589f kind_name=b3f808 giver=f8f324 turn_in=847ad4 offer_maps=46bf0f bit=b1d578 requires_bit=0ade7c automatic=5ffe53 prev=e9310b next=707bff prerequisites=303313 stages=a80fa1 objectives=413905 rewards=97d170 offer_talk=dcd7d0 -->
|  |  |
|---|---|
|  | ![An urgent message](wiki/assets/npcs/198.png) |
| **Quest id** | `11` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/198-frei\|Frei]] |
| **Turn in** | automatic |
| **Offered on** | Arslan: [[wiki/fields/88-training-camp\|Training Camp]] (88) · Erion: [[wiki/fields/92-training-camp\|Training Camp]] (92) · Armia: [[wiki/fields/96-training-camp\|Training Camp]] (96) |
| **Completion bit** | 10 |
| **Requires bit** | 9 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/10-find-the-secret-document|Find the Secret Document]]
- **Next:** [[wiki/quests/12-an-urgent-message|An urgent message]]

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/912-scroll-gaia\|Scroll : Gaia]] |
| 6 | item | carries [[wiki/items/2567-urgent-letter\|Urgent Letter]] |

### Objectives

1. Use [[wiki/items/912-scroll-gaia|Scroll : Gaia]] — tracker: “Use the Gaia Scroll in your inventory.”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

None in the client.

### Dialogue

#### Offer (QuestTalk 643)

Speaker: [[wiki/npcs/198-frei|Frei]]

> **Frei:** According to reports from our scouts the Undead are preparing to invade Gaia.  
> **Frei:** We can't waste any time, deliver this message to Freya in the Fortress.  
> **Frei:** These are Gaia's Scrolls. Use this and use the Nexus to move to the Fortress.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: step 21 at [20:00](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1200s); step 23 at [21:20](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1280s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 13 at [36:45](https://www.youtube.com/watch?v=s04CSN16w1s&t=2205s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 27 at [30:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1830s); step 30 at [32:25](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1945s)
<!-- generated:end -->

## Notes

From Frei: use Scroll: Gaia (912), then the nexus, to reach the Fortress ([36:45](https://www.youtube.com/watch?v=s04CSN16w1s&t=2205s)). Using the scroll completes it and starts quest 12 and lesson 719. The scroll's landing field differed by nation: Eternal River – Upper Region (14) for Arslan ([32:25](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1945s), [37:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=2260s)) and Cracked Earth (63) for Erion ([21:20](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1280s)); both times the player stood beside a nexus. *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-tutorial-walkthrough]]
- [[gameplay/video-character-creation-and-tutorial]]

## Open questions

Where the scroll lands for Armia was not seen, and whether the landing field is fixed per nation is not known ([[gameplay/video-tutorial-walkthrough]] step 30, [[gameplay/video-character-creation-and-tutorial]] §3 step 23).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
