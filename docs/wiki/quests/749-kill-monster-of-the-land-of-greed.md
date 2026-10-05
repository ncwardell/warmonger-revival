---
title: "Kill monster of The land of Greed"
type: "quest"
id: 749
status: "complete"
missing: []
sources: ["client: Quest.cdb id 749", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 889", "video: [[gameplay/video-early-quests]] step 17 (accepted from Athan 207 in the Fortress)"]
manual: ["giver"]
name_key: "Quest_Title_662"
kind: 3
kind_name: "Free"
level: {"min": 15, "max": 20}
giver: {"npc": 207}
turn_in: {"npc": 207}
turn_in_maps: [120, 120, 120]
bit: 0
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 15, "max": 20}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "unit_group": 10001, "units": [721, 722], "count": 50, "maps": [108, 109, 111], "text_key": "Quest_QuickText_662_1"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10002, "units": [723, 724], "count": 50, "maps": [108, 109, 111], "text_key": "Quest_QuickText_662_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_725_0"}
rewards:
  - {"type": 2, "what": "exp", "amount": 50000, "shown": 50000}
  - {"type": 4, "what": "gold", "amount": 50000}
  - {"type": 1, "what": "item", "item": 601, "count": 50, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 50, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 700, "count": 20, "pick": "fixed"}
complete_talk: 889
---
<!-- generated:start -->
<!-- generated-keys: title=98a457 type=eb5b2b id=01055f sources=a21e73 name_key=7f6128 kind=77de68 kind_name=01e781 level=fe8783 giver=2be88c turn_in=7e080a turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 prerequisites=a89597 stages=30caa7 objectives=174367 rewards=e04a61 complete_talk=4d7adc -->
|  |  |
|---|---|
| **Quest id** | `749` |
| **Kind** | Free (kind 3) |
| **Level** | 15–20 |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/207-athan\|Athan]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 15–20 |

### Objectives

1. Kill any unit of kill group 10001 ([[wiki/monsters/721-fragile-tow-warrior|Fragile Tow Warrior]], [[wiki/monsters/722-fragile-tow-sorcerer|Fragile Tow Sorcerer]]) × 50 — tracker: “Fragile Kill Tow (0/50)” — on Arslan: [[wiki/fields/108-the-land-of-greed|The land of Greed]] (108) · Erion: [[wiki/fields/109-the-land-of-greed|The land of Greed]] (109) · Armia: [[wiki/fields/111-the-land-of-greed|The land of Greed]] (111)
2. Kill any unit of kill group 10002 ([[wiki/monsters/723-fragile-elite-tow-warrior|Fragile Elite Tow Warrior]], [[wiki/monsters/724-fragile-elite-tow-sorcerer|Fragile Elite Tow Sorcerer]]) × 50 — tracker: “Fragile Kill Elite Tow  (0/50)” — on Arslan: [[wiki/fields/108-the-land-of-greed|The land of Greed]] (108) · Erion: [[wiki/fields/109-the-land-of-greed|The land of Greed]] (109) · Armia: [[wiki/fields/111-the-land-of-greed|The land of Greed]] (111)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Athan” — on [[wiki/fields/120-fortress|Fortress]] (120)

### Rewards

- **Basic reward:** 50,000 exp; 50,000 gold; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 50; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 50; [[wiki/items/700-crystal-blue|Crystal : Blue]] × 20

### Dialogue

#### Completion (QuestTalk 889)

Speaker: [[wiki/npcs/207-athan|Athan]]

> **Athan:** I'll give you this! Can you kill the tow?  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 17 at [41:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=2515s)
- [[gameplay/warmonger-forum|Warmonger forum (2018)]]
<!-- generated:end -->

## Notes

Accepted from Athan (207) in the Fortress at [41:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=2510s): kill 50 Tow and 50 Elite Tow in The land of Greed, then return to Athan. Turned in at [2:22:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=8545s). Panel: 50,000 exp + 50,000 gold + 50/50 Passion Fragments + Crystal: Blue ×20; the exp is shown unchanged for this kind ([[gameplay/video-early-quests]] step 17 and §4). The three repeatable Abyss quests at Athan were added in the WM 0329 patch ([[gameplay/patch-history]]). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-early-quests]]
- [[gameplay/patch-history]]
- [[gameplay/warmonger-forum]]

## Open questions

Quest 1101 has the same kills and rewards ([[gameplay/warmonger-forum]] §3); the video does not show which of the two rows Athan offered.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
