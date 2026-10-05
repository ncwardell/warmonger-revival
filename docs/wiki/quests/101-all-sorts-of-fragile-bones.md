---
title: "All sorts of Fragile bones"
type: "quest"
id: 101
status: "complete"
missing: []
sources: ["client: Quest.cdb id 101", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 645", "client: QuestTalk.cdb id 649"]
name_key: "Quest_Title_638"
kind: 1
kind_name: "Sub"
giver: {"npc": 335}
turn_in: {"npc": 335}
offer_maps: [88, 92, 96]
turn_in_maps: [88, 92, 96]
bit: 41
requires_bit: 99
prev: [7]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit_group": 10003, "units": [700, 701], "count": 10, "item": 2571, "rate": 100, "maps": [99, 100, 101], "text_key": "Quest_QuickText_638_1"}
  - {"n": 2, "type": 1, "what": "collect", "unit_group": 10004, "units": [702, 703], "count": 10, "item": 2572, "rate": 100, "maps": [99, 100, 101], "text_key": "Quest_QuickText_638_2"}
  - {"n": 5, "type": 0, "what": "report", "maps": [88, 92, 96], "text_key": "Quest_QuickText_G_ODIN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 17400, "shown": 14500}
  - {"type": 4, "what": "gold", "amount": 10000}
  - {"type": 1, "what": "item", "item": 398, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 406, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 700, "count": 10, "pick": "fixed"}
offer_talk: 645
complete_talk: 649
---
<!-- generated:start -->
<!-- generated-keys: title=79494b type=eb5b2b id=dbc0f0 sources=db56b9 name_key=5b8fde kind=356a19 kind_name=0bac50 giver=5e775e turn_in=5e775e offer_maps=46bf0f turn_in_maps=46bf0f bit=761f22 requires_bit=9a79be prev=bd703d next=97d170 stages=30caa7 objectives=bff8c2 rewards=e45275 offer_talk=f7b41d complete_talk=491173 -->
|  |  |
|---|---|
|  | ![All sorts of Fragile bones](../assets/npcs/335.png) |
| **Quest id** | `101` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/335-odin\|Odin]] |
| **Turn in** | [[wiki/npcs/335-odin\|Odin]] |
| **Offered on** | Arslan: [[wiki/fields/88-training-camp\|Training Camp]] (88) · Erion: [[wiki/fields/92-training-camp\|Training Camp]] (92) · Armia: [[wiki/fields/96-training-camp\|Training Camp]] (96) |
| **Completion bit** | 41 |
| **Requires bit** | 99 |

### Chain

- **After:** [[wiki/quests/7-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Collect [[wiki/items/2571-weak-skeleton-bone|Weak Skeleton bone]] × 10 from any unit of kill group 10003 ([[wiki/monsters/700-skeleton-warrior|Skeleton Warrior]], [[wiki/monsters/701-skeleton-archer|Skeleton Archer]]) (drop 100%) — tracker: “Fragile Weak Skeleton bone (0/10)” — on Arslan: [[wiki/fields/99-corpse-incineration|Corpse incineration]] (99) · Erion: [[wiki/fields/100-corpse-incineration|Corpse incineration]] (100) · Armia: [[wiki/fields/101-corpse-incineration|Corpse incineration]] (101)
2. Collect [[wiki/items/2572-weak-elite-skeleton-bone|Weak Elite Skeleton bone]] × 10 from any unit of kill group 10004 ([[wiki/monsters/702-elite-skeleton-warrior|Elite Skeleton Warrior]], [[wiki/monsters/703-elite-skeleton-archer|Elite Skeleton Archer]]) (drop 100%) — tracker: “Fragile Weak Elite Skeleton bone (0/10)” — on Arslan: [[wiki/fields/99-corpse-incineration|Corpse incineration]] (99) · Erion: [[wiki/fields/100-corpse-incineration|Corpse incineration]] (100) · Armia: [[wiki/fields/101-corpse-incineration|Corpse incineration]] (101)
5. Report (tracker line; done by turning the quest in) — tracker: “Deliver them to Odin”

### Rewards

- **Basic reward:** 17,400 exp (shown in game as 14,500); 10,000 gold; [[wiki/items/700-crystal-blue|Crystal : Blue]] × 10
- **Choose one:** [[wiki/items/398-spell-belt|Spell Belt]] *or* [[wiki/items/406-belt-of-life|Belt of Life]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 645)

Speaker: [[wiki/npcs/335-odin|Odin]]

> **Odin:** Are you on your way into the Abyss?  
> **Odin:** I'm in need of skeleton bones, are you up for the task?  
> **Odin:** I will reward you properly for them!  
> *(accept / continue)*

#### Completion (QuestTalk 649)

Speaker: [[wiki/npcs/335-odin|Odin]]

> **Odin:** You made it! Take this as a reward.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: step 18 at [15:55](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=955s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 10 at [22:45](https://www.youtube.com/watch?v=s04CSN16w1s&t=1368s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 26 at [29:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1770s)
<!-- generated:end -->

## Notes

Odin (335, Blue Union, Training Camp) needs 10 Weak Skeleton bone (2571) and 10 Weak Elite Skeleton bone (2572) from the skeleton groups 10003/10004 (units 700–703) in Corpse incineration ([22:45](https://www.youtube.com/watch?v=s04CSN16w1s&t=1365s), [29:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1770s), [15:55](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=955s)). Panel: 14,500 exp, 10,000 gold, Crystal: Blue ×10, then Spell Belt (398) or Belt of Life (406). Turned in at [36:10](https://www.youtube.com/watch?v=s04CSN16w1s&t=2170s) and [20:25](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1225s). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
