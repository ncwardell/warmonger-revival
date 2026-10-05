---
title: "Group - Border Area Hard Mode"
type: "quest"
id: 771
status: "partial"
missing: ["objectives"]
sources: ["client: Quest.cdb id 771", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 749", "client: QuestTalk.cdb id 750"]
name_key: "Quest_Title_771_"
kind: 1
kind_name: "Sub"
level: {"min": 24}
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 109
requires_bit: 108
prev: [760]
next: [1043]
prerequisites:
  - {"type": 4, "what": "level", "min": 24}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 129, "maps": [129, 129, 129], "text_key": "Quest_QuickText_771_1_"}
  - {"n": 2, "type": 1, "what": "kill", "target": 9999, "count": 1, "maps": [129, 129, 129], "text_key": "Quest_QuickText_771_2_"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 2000000, "shown": 1666667}
  - {"type": 1, "what": "item", "item": 688, "count": 10, "pick": "fixed"}
offer_talk: 749
complete_talk: 750
---
<!-- generated:start -->
<!-- generated-keys: title=e203c4 type=eb5b2b id=5d0fb6 sources=39674c name_key=96475c kind=356a19 kind_name=0bac50 level=a3b082 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=a1422e requires_bit=17503a prev=bed41c next=75eb62 prerequisites=0ab6f2 stages=30caa7 objectives=2be88c objectives_client=46924a rewards=8be589 offer_talk=01055f complete_talk=404c73 -->
|  |  |
|---|---|
|  | ![Group - Border Area Hard Mode](../assets/npcs/200.png) |
| **Quest id** | `771` |
| **Kind** | Sub (kind 1) |
| **Level** | 24+ |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 109 |
| **Requires bit** | 108 |

### Chain

- **After:** [[wiki/quests/760-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** [[wiki/quests/1043-thorn-s-hell-boss-hunting|Thorn's Hell : Boss Hunting]]

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 24+ |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Go to [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] (129) — tracker: “Go to the Thorn's Hell” — on [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] (129)
2. Kill target `9999` (not a unit or kill group) × 1 — tracker: “Akasha (0/1)” — on [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] (129)
3. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

- **Basic reward:** 2,000,000 exp (shown in game as 1,666,667); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 10

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 749)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** The monster king lives in the border area. Can you go and kill him?  
> *(accept / continue)*

#### Completion (QuestTalk 750)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Thank you so much.<br>The village is safe again.  
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
