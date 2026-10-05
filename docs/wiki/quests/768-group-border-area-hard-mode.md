---
title: "Group - Border Area Hard Mode"
type: "quest"
id: 768
status: "partial"
missing: ["rewards"]
sources: ["client: Quest.cdb id 768", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 860", "client: QuestTalk.cdb id 861"]
name_key: "Quest_Title_768_"
kind: 0
kind_name: "Main"
level: {"min": 24}
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 55
requires_bit: 56
prev: [769, 772, 773]
next: [714, 1008]
prerequisites:
  - {"type": 4, "what": "level", "min": 24}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 121, "maps": [121, 121, 121], "text_key": "Quest_QuickText_768_1_"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10013, "units": [672], "count": 1, "maps": [121, 121, 121], "text_key": "Quest_QuickText_768_2_"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards: null
rewards_client:
  - {"type": 2, "what": "exp", "amount": 715000, "shown": 650000}
  - {"type": 1, "what": "item", "item": 689, "count": 1, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 1000, "count": 3, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 688, "count": 3, "pick": "fixed"}
  - {"type": 5, "what": null, "a": 500}
offer_talk: 860
complete_talk: 861
---
<!-- generated:start -->
<!-- generated-keys: title=e203c4 type=eb5b2b id=ad2ad5 sources=5f00cd name_key=1087f5 kind=b6589f kind_name=b3f808 level=a3b082 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=8effee requires_bit=54ceb9 prev=46b5ec next=db8e83 prerequisites=0ab6f2 stages=30caa7 objectives=8a3687 rewards=2be88c rewards_client=df6ee0 offer_talk=301377 complete_talk=d5843c -->
|  |  |
|---|---|
|  | ![Group - Border Area Hard Mode](wiki/assets/npcs/200.png) |
| **Quest id** | `768` |
| **Kind** | Main (kind 0) |
| **Level** | 24+ |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 55 |
| **Requires bit** | 56 |

### Chain

- **After:** [[wiki/quests/769-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/772-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/773-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** [[wiki/quests/714-buy-time-energy|Buy time energy]], [[wiki/quests/1008-skull-temple-boss-hunting|Skull Temple : Boss Hunting]]

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 24+ |

### Objectives

1. Go to [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121) — tracker: “Go to the Skull Temple” — on [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121)
2. Kill any unit of kill group 10013 ([[wiki/monsters/672-king-deathhead|King Deathhead]]) × 1 — tracker: “King Deathhead (0/1)” — on [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121)
3. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

> [!warning] Not all reward types are decoded
> The rows below are the client's (`rewards_client`). Write the server-ready list into `rewards:` once the unclear ones are understood.

- **Basic reward:** 715,000 exp (shown in game as 650,000); [[wiki/items/689-tier-1-time-energy|Tier 1 : Time energy]]; [[wiki/items/1000-medal-bronze|Medal : Bronze]] × 3; [[wiki/items/688-dimensional-energy|Dimensional energy]] × 3
- Type 5 — fame?; values a=500

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 860)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Death Heads appeared in the Skeleton Temple. I feel bad after last time so I ask you to investigate.  
> *(accept / continue)*

#### Completion (QuestTalk 861)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** It's a big deal. The state of the dimension gate is getting worse.  
> *(accept / continue)*

### Mentioned in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]]
- [[gameplay/progression-and-economy|Progression and economy]]
<!-- generated:end -->

## Notes

A guide screenshot names the chain "Group – Border Area Hard Mode": go to a dungeon, kill its boss, talk to Freya ([[gameplay/progression-and-economy]] §1, *image*).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/progression-and-economy]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
