---
title: "Support the Abyss expedition"
type: "quest"
id: 17
status: "complete"
missing: []
sources: ["client: Quest.cdb id 17", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 657", "client: QuestTalk.cdb id 658"]
name_key: "Quest_Title_16"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"gadget": 3}
offer_maps: [120, 120, 120]
turn_in_maps: [108, 109, 111]
bit: 16
requires_bit: 13
prev: [14]
next: [19, 21, 108, 109]
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 0, "what": "report", "text_key": "Quest_QuickText_16_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 198000, "shown": 180000}
  - {"type": 1, "what": "item", "item": 885, "count": 100, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 889, "count": 100, "pick": "choose"}
offer_talk: 657
complete_talk: 658
---
<!-- generated:start -->
<!-- generated-keys: title=59867a type=eb5b2b id=0716d9 sources=26865a name_key=58198d kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=ab1fa2 offer_maps=15f2a7 turn_in_maps=20d88d bit=1574bd requires_bit=bd307a prev=76cdc5 next=bb20ec stages=a80fa1 objectives=58646c rewards=693b24 offer_talk=f90a34 complete_talk=f597ae -->
|  |  |
|---|---|
|  | ![Support the Abyss expedition](wiki/assets/npcs/200.png) |
| **Quest id** | `17` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/nodes/10803-scout-leader\|Scout Leader]] / [[wiki/nodes/10904-scout-leader\|Scout Leader]] / [[wiki/nodes/11105-scout-leader\|Scout Leader]] (gadget 3) |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Turned in on** | Arslan: [[wiki/fields/108-the-land-of-greed\|The land of Greed]] (108) · Erion: [[wiki/fields/109-the-land-of-greed\|The land of Greed]] (109) · Armia: [[wiki/fields/111-the-land-of-greed\|The land of Greed]] (111) |
| **Completion bit** | 16 |
| **Requires bit** | 13 |

### Chain

- **After:** [[wiki/quests/14-battle-preparations|Battle preparations]]
- **Next:** [[wiki/quests/19-meeting-freya|Meeting Freya]], [[wiki/quests/21-group-ancient-ghosts|(Group) Ancient Ghosts]], [[wiki/quests/108-hunting-ghosts-spirit-avenue|Hunting Ghosts (Spirit Avenue)]], [[wiki/quests/109-for-the-honor|For the honor]]

### Objectives

1. Report (tracker line; done by turning the quest in) — tracker: “Meet with the Scout Leader”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 198,000 exp (shown in game as 180,000)
- **Choose one:** [[wiki/items/885-potion-of-health-c|Potion of Health (C)]] × 100 *or* [[wiki/items/889-potion-of-mana-c|Potion of Mana (C)]] × 100

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 657)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Since the last time we spoke, I have heard concerning reports from our expedition force <br>in the Abyss.  
> **Freya:** The Tow Chief is gathering his tribe for an uprising and is giving our expedition force <br>a lot of trouble.  
> **Freya:** They need all the support they can get. <br>Speak to the leader of our scouts in the Abyss and take care of our tow problem.  
> *(accept / continue)*

#### Completion (QuestTalk 658)

Speaker: [[wiki/nodes/10803-scout-leader|Scout Leader]] / [[wiki/nodes/10904-scout-leader|Scout Leader]] / [[wiki/nodes/11105-scout-leader|Scout Leader]] (gadget 3)

> **You:** I'm the one they sent to take care of your Tow problem.  
> **Scout Leader:** All by yourself? Good luck my friend.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 16 at [41:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=2490s)
- [[gameplay/warmonger-forum|Warmonger forum (2018)]]

### Mentioned in

- [[gameplay/server-rules|Server rules checklist]]
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
