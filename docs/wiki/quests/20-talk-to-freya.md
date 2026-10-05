---
title: "Talk to Freya"
type: "quest"
id: 20
status: "stub"
missing: ["next"]
sources: ["client: Quest.cdb id 20", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 667"]
name_key: "Quest_Title_646"
kind: 0
kind_name: "Main"
giver: {"auto": true}
turn_in: {"npc": 200}
turn_in_maps: [120, 120, 120]
bit: 20
requires_bit: 19
prev: [19]
next: []
prerequisites:
  - {"type": 6, "what": "item", "item": 912, "count": 1}
  - {"type": 6, "what": "item", "item": 2564, "count": 1}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 13, "what": "use_item", "item": 912, "count": 1, "text_key": "Quest_QuickText_646_2"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 330000, "shown": 300000}
  - {"type": 1, "what": "item", "item": 706, "count": 5, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 714, "count": 5, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 710, "count": 5, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 718, "count": 5, "pick": "choose"}
complete_talk: 667
---
<!-- generated:start -->
<!-- generated-keys: title=86fe5d type=eb5b2b id=91032a sources=0c14bb name_key=b65ea5 kind=b6589f kind_name=b3f808 giver=847ad4 turn_in=1caac0 turn_in_maps=15f2a7 bit=91032a requires_bit=b3f0c7 prev=49534d next=97d170 prerequisites=c28417 stages=30caa7 objectives=046eb3 rewards=9db639 complete_talk=74da61 -->
|  |  |
|---|---|
| **Quest id** | `20` |
| **Kind** | Main (kind 0) |
| **Giver** | automatic |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 20 |
| **Requires bit** | 19 |

### Chain

- **After:** [[wiki/quests/19-meeting-freya|Meeting Freya]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/912-scroll-gaia\|Scroll : Gaia]] |
| 6 | item | carries [[wiki/items/2564-letter-to-oracle-of-knowledge\|Letter to Oracle of Knowledge]] |

### Objectives

1. Use [[wiki/items/912-scroll-gaia|Scroll : Gaia]] — tracker: “Use the Gaia Scroll”
2. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

- **Basic reward:** 330,000 exp (shown in game as 300,000)
- **Choose one:** [[wiki/items/706-scroll-of-the-warrior-a|Scroll of the Warrior (A)]] × 5 *or* [[wiki/items/714-tome-of-attack-spd-a|Tome of Attack SPD (A)]] × 5 *or* [[wiki/items/710-scroll-of-the-magician-a|Scroll of the Magician (A)]] × 5 *or* [[wiki/items/718-tome-of-cooldown-a|Tome of Cooldown (A)]] × 5

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Completion (QuestTalk 667)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** You already went to see the Oracle in the plaza?  
> **You:** Yes, they already heard about me and recognised my efforts. They gave me this letter for you.  
> **Freya:** Alright. It seems you have earned their trust with your relentless efforts to support our great Nation. Before that, I'll show you the convenient features before you can use the disassembly function in the inventory.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 23 at [58:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=3502s)

### Mentioned in

- [[gameplay/precept-shop|Precept shop and precept quests]]
- [[gameplay/progression-and-economy|Progression and economy]]
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]
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
