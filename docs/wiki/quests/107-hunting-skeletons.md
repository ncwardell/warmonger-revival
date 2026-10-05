---
title: "Hunting Skeletons"
type: "quest"
id: 107
status: "complete"
missing: []
sources: ["client: Quest.cdb id 107", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 646", "client: QuestTalk.cdb id 647"]
name_key: "Quest_Title_665"
kind: 1
kind_name: "Sub"
giver: {"gadget": 1}
turn_in: {"npc": 198}
offer_maps: [99, 100, 101]
turn_in_maps: [88, 92, 96]
bit: 46
requires_bit: 99
prev: [7]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "unit": 704, "count": 1, "maps": [99, 100, 101], "text_key": "Quest_QuickText_665_1"}
  - {"n": 2, "type": 1, "what": "kill", "unit": 705, "count": 1, "maps": [99, 100, 101], "text_key": "Quest_QuickText_665_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [99, 100, 96], "text_key": "Quest_QuickText_CB_FREI"}
rewards:
  - {"type": 2, "what": "exp", "amount": 12000, "shown": 10000}
  - {"type": 1, "what": "item", "item": 601, "count": 20, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 20, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 700, "count": 10, "pick": "fixed"}
offer_talk: 646
complete_talk: 647
---
<!-- generated:start -->
<!-- generated-keys: title=65a5cd type=eb5b2b id=524e05 sources=feab76 name_key=c20de0 kind=356a19 kind_name=0bac50 giver=bc802c turn_in=f8f324 offer_maps=0f349c turn_in_maps=46bf0f bit=fe2ef4 requires_bit=9a79be prev=bd703d next=97d170 stages=30caa7 objectives=9a9340 rewards=2efb5e offer_talk=961cc9 complete_talk=17820a -->
|  |  |
|---|---|
| **Quest id** | `107` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/nodes/9901-scout\|Scout]] / [[wiki/nodes/10001-scout\|Scout]] / [[wiki/nodes/10101-scout\|Scout]] (gadget 1) |
| **Turn in** | [[wiki/npcs/198-frei\|Frei]] |
| **Offered on** | Arslan: [[wiki/fields/99-corpse-incineration\|Corpse incineration]] (99) · Erion: [[wiki/fields/100-corpse-incineration\|Corpse incineration]] (100) · Armia: [[wiki/fields/101-corpse-incineration\|Corpse incineration]] (101) |
| **Turned in on** | Arslan: [[wiki/fields/88-training-camp\|Training Camp]] (88) · Erion: [[wiki/fields/92-training-camp\|Training Camp]] (92) · Armia: [[wiki/fields/96-training-camp\|Training Camp]] (96) |
| **Completion bit** | 46 |
| **Requires bit** | 99 |

### Chain

- **After:** [[wiki/quests/7-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Kill [[wiki/monsters/704-skeleton-warrior-officer|Skeleton Warrior Officer]] × 1 — tracker: “Kill Skeleton Warrior Leader (0/1)”
2. Kill [[wiki/monsters/705-skeleton-archer-officer|Skeleton Archer Officer]] × 1 — tracker: “Kill Skeleton Archer Leader (0/1)”
3. Report (tracker line; done by turning the quest in) — tracker: “Report back to Frei” — on Arslan: [[wiki/fields/99-corpse-incineration|Corpse incineration]] (99) · Erion: [[wiki/fields/100-corpse-incineration|Corpse incineration]] (100) · Armia: [[wiki/fields/96-training-camp|Training Camp]] (96)

### Rewards

- **Basic reward:** 12,000 exp (shown in game as 10,000); [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 20; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 20; [[wiki/items/700-crystal-blue|Crystal : Blue]] × 10

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 646)

Speaker: [[wiki/nodes/9901-scout|Scout]] / [[wiki/nodes/10001-scout|Scout]] / [[wiki/nodes/10101-scout|Scout]] (gadget 1)

> **Scout:** You look like it's your first time here in the Abyss.  
> **Scout:** Its a dangerous place. I recommend you leave it as soon as possible.  
> **You:** I'm tougher than I look.  
> **Scout:** Could you kill some more skeletons for me? Report back to Freya when you're done.  
> *(accept / continue)*

#### Completion (QuestTalk 647)

Speaker: Scout

> **You:** I also killed the leaders of the skeletons.  
> **Scout:** I see, we are in your debt. Exploring the Abyss will be a lot easier,<br>now that those menaces are gone.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: step 20 at [19:20](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1160s); step 21 at [20:00](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1200s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 12 at [26:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=1590s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 23 at [26:45](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1605s); step 27 at [29:50](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1790s)

### Mentioned in

- [[gameplay/sources|Sources and gaps]]
<!-- generated:end -->

## Notes

From the Scout at [26:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=1590s): kill the Skeleton Warrior Leader (704) and the Skeleton Archer Leader (705), which stand in the south of Corpse incineration guarded by elites, then report to Frei ([36:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=2195s), [28:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1680s)–[30:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1830s)). Panel: 10,000 exp, 20 Blue and 20 Red Passion Fragments [D] (601/611), Crystal: Blue ×10 ([[gameplay/video-early-quests]] step 12, [[gameplay/video-tutorial-walkthrough]] step 27). A Crush Online forum screenshot of this quest shows the leaders' spawn area on the minimap ([[gameplay/sources]], "Hunting Skeletons" row). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-early-quests]]
- [[gameplay/video-tutorial-walkthrough]]
- [[gameplay/sources]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
