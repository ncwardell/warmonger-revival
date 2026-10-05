---
title: "[Group] Ancient Ghosts"
type: "quest"
id: 21
status: "complete"
missing: []
sources: ["client: Quest.cdb id 21", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 662", "client: QuestTalk.cdb id 663"]
name_key: "Quest_Title_647"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 21
requires_bit: 16
prev: [17]
next: [23, 24, 25, 26]
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit": 827, "count": 3, "item": 2568, "rate": 70, "maps": [113, 113, 113], "text_key": "Quest_QuickText_647_1"}
  - {"n": 2, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 990000, "shown": 900000}
  - {"type": 1, "what": "item", "item": 688, "count": 4, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 885, "count": 100, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 889, "count": 100, "pick": "choose"}
offer_talk: 662
complete_talk: 663
---
<!-- generated:start -->
<!-- generated-keys: title=05c749 type=eb5b2b id=472b07 sources=6c4727 name_key=eaebb5 kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=472b07 requires_bit=1574bd prev=79d296 next=c63cb5 stages=30caa7 objectives=4bbbc4 rewards=f2f877 offer_talk=091d03 complete_talk=b66cd9 -->
|  |  |
|---|---|
|  | ![(Group) Ancient Ghosts](../assets/npcs/200.png) |
| **Quest id** | `21` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 21 |
| **Requires bit** | 16 |

### Chain

- **After:** [[wiki/quests/17-support-the-abyss-expedition|Support the Abyss expedition]]
- **Next:** [[wiki/quests/23-stepping-up-your-game|Stepping up your game]], [[wiki/quests/24-stepping-up-your-game|Stepping up your game]], [[wiki/quests/25-stepping-up-your-game|Stepping up your game]], [[wiki/quests/26-border-area-normal-mode|Border Area Normal Mode]]

### Objectives

1. Collect [[wiki/items/2568-essence-of-darkness|essence of Darkness]] × 3 from [[wiki/monsters/827-ancient-ghost|Ancient Ghost]] (drop 70%) — tracker: “Obtain the essence of darkness (0/3)” — on [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] (113)
2. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

- **Basic reward:** 990,000 exp (shown in game as 900,000); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 4
- **Choose one:** [[wiki/items/885-potion-of-health-c|Potion of Health (C)]] × 100 *or* [[wiki/items/889-potion-of-mana-c|Potion of Mana (C)]] × 100

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 662)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** You will need to create an even more powerful weapon to fight the evil. <br>For that to happen I have to complete my studies on soul energy.  
> **Freya:** You have to kill the Ancient Ghosts in the Abyss and bring me their dark essence.  
> *(accept / continue)*

#### Completion (QuestTalk 663)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **You:** Freya, the mission has been completed. Can we try to create a new weapon from the Dark Essence?  
> **Freya:** My study is not finished yet. Not all keepers use soulweapon.  
> **Freya:** If our enemies don't know about it, we will have the element of surprise. Once you are stronger, you might stand a chance. I will tell you when the weapon is complete.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 24 at [65:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=3920s)
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
