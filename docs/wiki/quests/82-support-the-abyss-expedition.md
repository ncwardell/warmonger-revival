---
title: "Support the Abyss expedition"
type: "quest"
id: 82
status: "stub"
missing: ["next"]
sources: ["client: Quest.cdb id 82", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 659", "client: QuestTalk.cdb id 737"]
name_key: "Quest_Title_16"
kind: 0
kind_name: "Main"
classes: ["Guardian"]
giver: {"gadget": 3}
turn_in: {"npc": 200}
offer_maps: [108, 109, 111]
turn_in_maps: [120, 120, 120]
bit: 17
prev: []
next: []
prerequisites:
  - {"type": 1, "what": "class", "classes": ["Guardian"], "mask": 16}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "unit_group": 10001, "units": [721, 722], "count": 10, "maps": [108, 109, 111], "text_key": "Quest_QuickText_644_1"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10002, "units": [723, 724], "count": 10, "maps": [108, 109, 111], "text_key": "Quest_QuickText_644_2"}
  - {"n": 3, "type": 1, "what": "kill", "unit": 826, "count": 1, "maps": [108, 109, 111], "text_key": "Quest_QuickText_16_4"}
  - {"n": 4, "type": 0, "what": "report", "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 220000, "shown": 200000}
  - {"type": 1, "what": "item", "item": 20001, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 20021, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 20003, "count": 1, "pick": "choose"}
offer_talk: 737
complete_talk: 659
---
<!-- generated:start -->
<!-- generated-keys: title=59867a type=eb5b2b id=76546f sources=5d1820 name_key=58198d kind=b6589f kind_name=b3f808 classes=2160c0 giver=ab1fa2 turn_in=1caac0 offer_maps=20d88d turn_in_maps=15f2a7 bit=0716d9 prev=97d170 next=97d170 prerequisites=9bef0c stages=30caa7 objectives=f41117 rewards=f8de19 offer_talk=4cae59 complete_talk=9dbb7f -->
|  |  |
|---|---|
| **Quest id** | `82` |
| **Kind** | Main (kind 0) |
| **Classes** | Guardian |
| **Giver** | [[wiki/nodes/10803-scout-leader\|Scout Leader]] / [[wiki/nodes/10904-scout-leader\|Scout Leader]] / [[wiki/nodes/11105-scout-leader\|Scout Leader]] (gadget 3) |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | Arslan: [[wiki/fields/108-the-land-of-greed\|The land of Greed]] (108) · Erion: [[wiki/fields/109-the-land-of-greed\|The land of Greed]] (109) · Armia: [[wiki/fields/111-the-land-of-greed\|The land of Greed]] (111) |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 17 |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 17 with:** [[wiki/quests/80-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/81-support-the-abyss-expedition|Support the Abyss expedition]] (completing one closes the others)

### Requirements

| type | meaning | value |
|---|---|---|
| 1 | class | Guardian (mask 16) |

### Objectives

1. Kill any unit of kill group 10001 ([[wiki/monsters/721-fragile-tow-warrior|Fragile Tow Warrior]], [[wiki/monsters/722-fragile-tow-sorcerer|Fragile Tow Sorcerer]]) × 10 — tracker: “Fragile Kill Tow (0/10)”
2. Kill any unit of kill group 10002 ([[wiki/monsters/723-fragile-elite-tow-warrior|Fragile Elite Tow Warrior]], [[wiki/monsters/724-fragile-elite-tow-sorcerer|Fragile Elite Tow Sorcerer]]) × 10 — tracker: “Fragile Kill Elite Tow (0/10)”
3. Kill [[wiki/monsters/826-tow-chief|Tow Chief]] × 1 — tracker: “Kill the Tow's Chief (0/1)”
4. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

- **Basic reward:** 220,000 exp (shown in game as 200,000)
- **Choose one:** [[wiki/items/20001-magical-demolition-hammer|Magical Demolition Hammer]] *or* [[wiki/items/20021-magical-protect-cannon|Magical Protect Cannon]] *or* [[wiki/items/20003-magical-crush-hammer|Magical Crush Hammer]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 737)

Speaker: [[wiki/nodes/10803-scout-leader|Scout Leader]] / [[wiki/nodes/10904-scout-leader|Scout Leader]] / [[wiki/nodes/11105-scout-leader|Scout Leader]] (gadget 3)

> **Scout Leader:** Hey, Use this ring and don't forget equip that..<br>The Tows are gathering around their chief, I'll better be careful.  
> **Scout Leader:** Return to the Oracle of Knowledge, when you completed your mission.  
> *(accept / continue)*  
> *(accept / continue)*

#### Completion (QuestTalk 659)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Thank you for your service.  
> **You:** By the way, how is the exploring of the Abyss going?  
> **Freya:** Talk to the other oracles for more information.  
> **Freya:** Will you go look for them?  
> *(accept / continue)*

### Seen in

- [[gameplay/server-rules|Server rules checklist]]
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 21 at [52:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=3147s)

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/warmonger-forum|Warmonger forum (2018)]]
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
