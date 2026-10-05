---
title: "United Problem Solvers"
type: "quest"
id: 5
status: "complete"
missing: []
sources: ["client: Quest.cdb id 5", "video: [[gameplay/video-character-creation-and-tutorial]] step 11 and [[gameplay/video-tutorial-walkthrough]] steps 10 and 16 (quests 6 and 28 start at the quest 5 turn-in)", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 634", "client: QuestTalk.cdb id 635"]
name_key: "Quest_Title_633"
kind: 0
kind_name: "Main"
giver: {"npc": 201}
turn_in: {"npc": 198}
offer_maps: [89, 93, 97]
turn_in_maps: [88, 92, 96]
bit: 5
requires_bit: 4
prev: [4]
next: [6, 28]
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 0, "what": "report", "maps": [0, 92, 96], "text_key": "Quest_QuickText_633_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 2750, "shown": 2500}
  - {"type": 1, "what": "item", "item": 402, "count": 1, "pick": "fixed"}
  - {"type": 4, "what": "gold", "amount": 500}
offer_talk: 634
complete_talk: 635
---
<!-- generated:start -->
<!-- generated-keys: title=ceb419 type=eb5b2b id=ac3478 sources=f68362 name_key=24b466 kind=b6589f kind_name=b3f808 giver=444e6c turn_in=f8f324 offer_maps=6e2020 turn_in_maps=46bf0f bit=ac3478 requires_bit=1b6453 prev=8f4e34 next=e6a0b3 stages=30caa7 objectives=8e6ab4 rewards=a8e717 offer_talk=08ec2e complete_talk=83a002 -->
|  |  |
|---|---|
|  | ![United Problem Solvers](../assets/npcs/201.png) |
| **Quest id** | `5` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/201-shaia\|Shaia]] |
| **Turn in** | [[wiki/npcs/198-frei\|Frei]] |
| **Offered on** | Arslan: [[wiki/fields/89-training-ground\|Training Ground]] (89) · Erion: [[wiki/fields/93-training-ground\|Training Ground]] (93) · Armia: [[wiki/fields/97-training-ground\|Training Ground]] (97) |
| **Turned in on** | Arslan: [[wiki/fields/88-training-camp\|Training Camp]] (88) · Erion: [[wiki/fields/92-training-camp\|Training Camp]] (92) · Armia: [[wiki/fields/96-training-camp\|Training Camp]] (96) |
| **Completion bit** | 5 |
| **Requires bit** | 4 |
| **Current server** | enabled in `server/quests.py` |

### Chain

- **After:** [[wiki/quests/4-go-to-shaia|Go to Shaia]]
- **Next:** [[wiki/quests/6-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]], [[wiki/quests/28-what-does-wren-do|What does Wren do?]]

### Objectives

1. Report (tracker line; done by turning the quest in) — tracker: “Talk to Frei, you can find her  in the training camp.” — on Arslan: — · Erion: [[wiki/fields/92-training-camp|Training Camp]] (92) · Armia: [[wiki/fields/96-training-camp|Training Camp]] (96)

### Rewards

- **Basic reward:** 2,750 exp (shown in game as 2,500); [[wiki/items/402-armor-of-life|Armor of Life]]; 500 gold

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 634)

Speaker: [[wiki/npcs/201-shaia|Shaia]]

> **You:** Do you have any important missions for a  real warrior?  
> **You:** Do you remember when you told me it was my destiny<br>to change the world?  
> **Shaia:** Yes I do, I saw the potential in you when no one else did. But you need more training first!  
> **You:** Training?? What sort of training is hunting snakes, slimes and bees ?!?!  
> **Shaia:** Ok… If you feel that way we will step it up a notch. Deliver this letter to Frei.  
> **You:** Delivering a letter, really?<br>Do I look like the postman to you?<br>Whatever hand me that stupid piece of paper, I'll get it done.  
> *(accept / continue)*

#### Completion (QuestTalk 635)

Speaker: [[wiki/npcs/198-frei|Frei]]

> **You:** Are you Frei? Shaia has sent me to deliver this letter to you.  
> **Frei:** Hmmmmm… Shaia sent you?<br>Usually she wouldn't send one of her apprentices to deliver<br>such an important letter.  
> **You:** Important letter? Hmmm… <br>I guess Shaia finally recognised me for the warrior I am! <br>If you ask me, it was about time my talents got put to better use<br>and don't get me started on slime mucus and bee stings …  
> **Frei:** Stop babbling, I'm trying to read here. <br>..... <br><br>I don't know if you're up for the task, so I will have to test you first!  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: step 10 at [6:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=370s); step 11 at [8:30](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=510s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 5 at [13:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=812s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 8 at [10:07](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=607s); step 10 at [12:50](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=770s)
<!-- generated:end -->

## Notes

Shaia hands over a letter for Frei, the Oracle of Knowledge (198), in the Training Camp; tracker "Talk to Frei, you can find her in the training camp" ([13:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=810s), [10:07](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=607s)). Turned in at [16:05](https://www.youtube.com/watch?v=s04CSN16w1s&t=965s), [12:50](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=770s) and [8:30](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=510s): the panel and a "+2500" popup show 2,500 exp, and the chat shows Armor of Life (402) and a Faded Passion fragment (1900). Quests 6 and 28 start at the turn-in ([[gameplay/video-character-creation-and-tutorial]] §3 step 11). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-character-creation-and-tutorial]]
- [[gameplay/video-tutorial-walkthrough]]
- [[gameplay/video-early-quests]]

## Open questions

Gold: the table lists 500 gold (reward type 4), but no video shows it. The panel had no gold row and the player's gold stayed 0 until the first sale ([[gameplay/video-tutorial-walkthrough]] §3 Shop and economy, [[gameplay/video-character-creation-and-tutorial]] §6, [[gameplay/video-early-quests]] step 5). The Faded Passion fragment that arrived instead is not in the table; quest 28 needs it. Whether the relaunch server swapped the reward is not known. *video vs client*

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
