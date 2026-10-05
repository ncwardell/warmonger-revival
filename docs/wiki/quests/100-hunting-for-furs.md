---
title: "Hunting for Furs"
type: "quest"
id: 100
status: "complete"
missing: []
sources: ["client: Quest.cdb id 100", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 644", "client: QuestTalk.cdb id 648"]
name_key: "Quest_Title_637"
kind: 1
kind_name: "Sub"
giver: {"npc": 315}
turn_in: {"npc": 315}
offer_maps: [88, 92, 96]
turn_in_maps: [88, 92, 96]
bit: 40
prev: []
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit": 727, "count": 5, "item": 2554, "rate": 100, "maps": [89, 93, 97], "text_key": "Quest_QuickText_637_1"}
  - {"n": 2, "type": 1, "what": "collect", "unit": 728, "count": 5, "item": 2553, "rate": 100, "maps": [89, 93, 97], "text_key": "Quest_QuickText_637_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [88, 92, 96], "text_key": "Quest_QuickText_681_5"}
rewards:
  - {"type": 2, "what": "exp", "amount": 8880, "shown": 7400}
  - {"type": 4, "what": "gold", "amount": 5000}
  - {"type": 1, "what": "item", "item": 397, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 405, "count": 1, "pick": "choose"}
offer_talk: 644
complete_talk: 648
---
<!-- generated:start -->
<!-- generated-keys: title=adde10 type=eb5b2b id=310b86 sources=ad6e68 name_key=2b0f6b kind=356a19 kind_name=0bac50 giver=a5beda turn_in=a5beda offer_maps=46bf0f turn_in_maps=46bf0f bit=af3e13 prev=97d170 next=97d170 stages=30caa7 objectives=1a6263 rewards=f925fb offer_talk=4c8596 complete_talk=4de62d -->
|  |  |
|---|---|
|  | ![Hunting for Furs](wiki/assets/npcs/315.png) |
| **Quest id** | `100` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/315-lewellyn\|Lewellyn]] |
| **Turn in** | [[wiki/npcs/315-lewellyn\|Lewellyn]] |
| **Offered on** | Arslan: [[wiki/fields/88-training-camp\|Training Camp]] (88) · Erion: [[wiki/fields/92-training-camp\|Training Camp]] (92) · Armia: [[wiki/fields/96-training-camp\|Training Camp]] (96) |
| **Completion bit** | 40 |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Collect [[wiki/items/2554-whiter-chepa-fur|Whiter Chepa Fur]] × 5 from [[wiki/monsters/727-chepa-warrior|Chepa Warrior]] (drop 100%) — tracker: “White Chepa Fur (0/5)” — on Arslan: [[wiki/fields/89-training-ground|Training Ground]] (89) · Erion: [[wiki/fields/93-training-ground|Training Ground]] (93) · Armia: [[wiki/fields/97-training-ground|Training Ground]] (97)
2. Collect [[wiki/items/2553-black-chepa-fur|Black Chepa Fur]] × 5 from [[wiki/monsters/728-chepa-archer|Chepa Archer]] (drop 100%) — tracker: “Black Chepa Fur (0/5)” — on Arslan: [[wiki/fields/89-training-ground|Training Ground]] (89) · Erion: [[wiki/fields/93-training-ground|Training Ground]] (93) · Armia: [[wiki/fields/97-training-ground|Training Ground]] (97)
3. Report (tracker line; done by turning the quest in) — tracker: “Go back to Lewellyn”

### Rewards

- **Basic reward:** 8,880 exp (shown in game as 7,400); 5,000 gold
- **Choose one:** [[wiki/items/397-spell-necklace|Spell Necklace]] *or* [[wiki/items/405-necklace-of-life|Necklace of Life]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 644)

Speaker: [[wiki/npcs/315-lewellyn|Lewellyn]]

> **Lewellyn:** I heard about you. Floyd said that you're trustworthy.<br>I would like to ask you for a favour.  
> **Lewellyn:** Rumour is you are on your way to kill Chepas.<br>Their fur is worth a lot.  
> **Lewellyn:** Could you bring me five of each colour?  
> *(accept / continue)*

#### Completion (QuestTalk 648)

Speaker: [[wiki/npcs/315-lewellyn|Lewellyn]]

> **Lewellyn:** Thank you. Your reward will not only be my gratitude. <br>Take a look at those fine shoes I made for you.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: step 13 at [8:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=530s); step 17 at [15:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=950s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 8 at [17:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=1022s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 12 at [15:10](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=910s); step 14 at [19:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1170s)
<!-- generated:end -->

## Notes

Lewellyn (315, Scroll Merchant, Training Camp) wants 5 White Chepa Fur (2554, from Chepa Warrior 727) and 5 Black Chepa Fur (2553, from Chepa Archer 728); both drop at 100% in the round clearings of the northern Training Ground ([[gameplay/video-tutorial-walkthrough]] steps 12–13). The tracker spells the first "Whiter Chepa Fur". Panel: 7,400 exp, 5,000 gold, then Spell Necklace (397) or Necklace of Life (405) ([17:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=1020s), [8:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=530s)). Turned in at [22:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=1320s), [19:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1170s) and [15:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=950s). Her dialogue mentions shoes although the reward is a necklace ([[gameplay/video-early-quests]] step 8). Lesson 706 (Expand your Inventory) starts at the turn-in. *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-tutorial-walkthrough]]
- [[gameplay/video-early-quests]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
