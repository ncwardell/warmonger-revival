---
title: "On to a promising start"
type: "quest"
id: 1
status: "complete"
missing: []
sources: ["client: Quest.cdb id 1", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 630", "client: QuestTalk.cdb id 684"]
name_key: "Quest_Title_630"
kind: 0
kind_name: "Main"
giver: {"npc": 201}
turn_in: {"auto": true}
offer_maps: [89, 93, 97]
turn_in_maps: [89, 93, 97]
bit: 1
automatic: true
prev: []
next: [2]
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 201, "talk": 630, "maps": [89, 93, 97], "text_key": "Quest_QuickText_T_SHAIA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 550, "shown": 500}
offer_talk: 684
help: {"image": "ui/HelpImage/Help_02.png", "text_key": "Quest_HelpText_1"}
---
<!-- generated:start -->
<!-- generated-keys: title=07df90 type=eb5b2b id=356a19 sources=ccf428 name_key=2d5a68 kind=b6589f kind_name=b3f808 giver=444e6c turn_in=847ad4 offer_maps=6e2020 turn_in_maps=6e2020 bit=356a19 automatic=5ffe53 prev=97d170 next=249983 stages=30caa7 objectives=b10c30 rewards=0247a1 offer_talk=a79e9a help=a61787 -->
|  |  |
|---|---|
|  | ![On to a promising start](wiki/assets/quests/1.png) |
| **Quest id** | `1` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/201-shaia\|Shaia]] |
| **Turn in** | automatic |
| **Offered on** | Arslan: [[wiki/fields/89-training-ground\|Training Ground]] (89) · Erion: [[wiki/fields/93-training-ground\|Training Ground]] (93) · Armia: [[wiki/fields/97-training-ground\|Training Ground]] (97) |
| **Completion bit** | 1 |
| **Automatic flag** | set (c14@11) |
| **Current server** | enabled in `server/quests.py` |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** [[wiki/quests/2-the-slime-is-mine|The Slime is mine]]
- **Shares completion bit 1 with:** [[wiki/quests/1501-basic-function-move-character|Basic function - Move character]] (completing one closes the others)

### Objectives

1. Talk to [[wiki/npcs/201-shaia|Shaia]] (dialogue 630) — tracker: “Talk to Shaia”

### Rewards

- **Basic reward:** 550 exp (shown in game as 500)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 684)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **You:** Oops! I'm late again, I can already hear Shaia grumbling.  
> **You:** I better hurry up and explain myself to her.  
> *(accept / continue)*

#### Objective 1 (QuestTalk 630)

Speaker: [[wiki/npcs/201-shaia|Shaia]]

> **Shaia:** Why are you always late?  
> **Shaia:** Gather a couple of Slime Mucus from the Slimes around here and hurry up. You are already late as it is.  
> **You:** Why should the best fighter in the world gather slime mucus?  
> **Shaia:** The best fighter in the world? Hahaha.<br>At least you have a good sense of humour.<br>You have a long way to go before you can call yourself that.<br>Now stop fooling around and get going, Biologist Floyd needs them for her research.  
> **You:** But... but.... never mind. I'll get the job done!<br>Don't you worry Shaia, the Slimes won't know what hit them!  
> *(accept / continue)*

### Tip window

> You can talk to Shaia with right mouse button click.

Image `ui/HelpImage/Help_02.png`.

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: at [6:35](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=395s); step 1 at [2:33](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=153s); step 2 at [3:00](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=180s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: at [3:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=210s); step 1 at [3:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=220s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 2 at [3:20](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=200s); step 3 at [4:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=240s); step 4 at [4:55](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=295s)
<!-- generated:end -->

## Notes

Already active when a new character first enters the Training Ground; there is no tutorial map in the 2018 builds ([[gameplay/video-early-quests]] §1 note, [[gameplay/video-character-creation-and-tutorial]] §3 step 1). The offer dialogue (684, the character's own lines) opens by itself with a reward panel showing 500 exp ([2:33](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=153s), [3:20](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=200s)). A tip window then says to right-click Shaia ([3:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=220s)). Talking to Shaia completes it and starts quest 2 and lesson 700 at once ([3:00](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=180s), [[gameplay/video-tutorial-walkthrough]] step 3). *video*

## Behaviour

The new character spawns about 14 units south of Shaia: about (435.5, 3648) in the Arslan copy ([[gameplay/video-tutorial-walkthrough]] §2), local (174.3, 68.3) in the Erion copy ([[gameplay/video-character-creation-and-tutorial]] §4). Quest 1's 500 exp plus lesson 700's 200 exp give exactly the 700 exp needed for level 2 ([4:55](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=295s), [3:25](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=205s)). *video + client*

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-early-quests]]
- [[gameplay/video-character-creation-and-tutorial]]
- [[gameplay/video-tutorial-walkthrough]]

## Open questions

The table grants 550 exp; every video shows 500. Levelling in the June 2018 video adds up with the shown value ([[gameplay/video-character-creation-and-tutorial]] §3 step 3, §6), so the original server may have granted the shown amount. *video vs client*

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
