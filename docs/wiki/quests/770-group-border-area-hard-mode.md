---
title: "Group - Border Area Hard Mode"
type: "quest"
id: 770
status: "complete"
missing: []
sources: ["client: Quest.cdb id 770", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 862", "client: QuestTalk.cdb id 863"]
name_key: "Quest_Title_770_"
kind: 0
kind_name: "Main"
level: {"min": 24}
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 36
requires_bit: 7
prev: [714]
next: [697, 781, 782, 785, 1013]
prerequisites:
  - {"type": 4, "what": "level", "min": 24}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 128, "maps": [128, 128, 128], "text_key": "Quest_QuickText_700_1"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10014, "units": [673], "count": 1, "maps": [128, 128, 128], "text_key": "Quest_QuickText_770_2_"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 825000, "shown": 750000}
  - {"type": 1, "what": "item", "item": 7002, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 7012, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 688, "count": 4, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 1000, "count": 3, "pick": "fixed"}
offer_talk: 862
complete_talk: 863
---
<!-- generated:start -->
<!-- generated-keys: title=e203c4 type=eb5b2b id=5b5b33 sources=8bb632 name_key=dc15ea kind=b6589f kind_name=b3f808 level=a3b082 giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=fc074d requires_bit=902ba3 prev=b3e901 next=821415 prerequisites=0ab6f2 stages=30caa7 objectives=44634f rewards=4a55d4 offer_talk=5753ab complete_talk=c2145e -->
|  |  |
|---|---|
|  | ![Group - Border Area Hard Mode](../assets/npcs/200.png) |
| **Quest id** | `770` |
| **Kind** | Main (kind 0) |
| **Level** | 24+ |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 36 |
| **Requires bit** | 7 |

### Chain

- **After:** [[wiki/quests/714-buy-time-energy|Buy time energy]]
- **Next:** [[wiki/quests/697-create-rune|Create Rune]], [[wiki/quests/781-tsunami-lake|Tsunami Lake]], [[wiki/quests/782-tsunami-lake|Tsunami Lake]], [[wiki/quests/785-the-strange-flowers-in-the-lake|The strange flowers in the lake]], [[wiki/quests/1013-skull-cemetery-boss-hunting|Skull Cemetery : Boss Hunting]]

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 24+ |

### Objectives

1. Go to [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128) — tracker: “Move to the Skull Cemetery” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
2. Kill any unit of kill group 10014 ([[wiki/monsters/673-dark-knight-skull|Dark Knight Skull]]) × 1 — tracker: “Dark Knight Skull (0/1)” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
3. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

- **Basic reward:** 825,000 exp (shown in game as 750,000); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 4; [[wiki/items/1000-medal-bronze|Medal : Bronze]] × 3
- **Choose one:** [[wiki/items/7002-attack-rune|Attack Rune]] *or* [[wiki/items/7012-ability-power-rune|Ability Power Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 862)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** The Skull Cemetery has a bad aura. I don't know the cause of it yet, however. Kill Skull to stabilize the area.  
> *(accept / continue)*

#### Completion (QuestTalk 863)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **You:** I have killed Skull. The Dimension Gate still looks bad.  
> *(accept / continue)*

### Mentioned in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]]
- [[gameplay/progression-and-economy|Progression and economy]]
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
