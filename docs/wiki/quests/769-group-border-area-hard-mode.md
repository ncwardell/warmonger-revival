---
title: "Group - Border Area Hard Mode"
type: "quest"
id: 769
status: "complete"
missing: []
sources: ["client: Quest.cdb id 769", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 858", "client: QuestTalk.cdb id 859"]
name_key: "Quest_Title_769_"
kind: 0
kind_name: "Main"
level: {"min": 24}
classes: ["Saint"]
giver: {"npc": 200}
turn_in: {"npc": 200}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 56
requires_bit: 28
prev: [32]
next: [114, 768, 1003]
prerequisites:
  - {"type": 4, "what": "level", "min": 24}
  - {"type": 1, "what": "class", "classes": ["Saint"], "mask": 1}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 127, "maps": [127, 127, 127], "text_key": "Quest_QuickText_769_1_"}
  - {"n": 2, "type": 1, "what": "kill", "unit_group": 10000, "units": [870], "count": 1, "maps": [127, 127, 127], "text_key": "Quest_QuickText_769_2_"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 1, "what": "item", "item": 10002, "count": 1, "pick": "choose", "e": 15}
  - {"type": 1, "what": "item", "item": 10017, "count": 1, "pick": "choose", "e": 15}
  - {"type": 1, "what": "item", "item": 10011, "count": 1, "pick": "choose", "e": 15}
  - {"type": 1, "what": "item", "item": 10001, "count": 1, "pick": "choose", "e": 15}
  - {"type": 2, "what": "exp", "amount": 605000, "shown": 550000}
offer_talk: 858
complete_talk: 859
---
<!-- generated:start -->
<!-- generated-keys: title=e203c4 type=eb5b2b id=98079d sources=2eec1c name_key=d930dd kind=b6589f kind_name=b3f808 level=a3b082 classes=30141f giver=1caac0 turn_in=1caac0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=54ceb9 requires_bit=0a57cb prev=b891b8 next=d09211 prerequisites=ad4268 stages=30caa7 objectives=808850 rewards=4d193b offer_talk=fe39d9 complete_talk=812cd8 -->
|  |  |
|---|---|
|  | ![Group - Border Area Hard Mode](wiki/assets/npcs/200.png) |
| **Quest id** | `769` |
| **Kind** | Main (kind 0) |
| **Level** | 24+ |
| **Classes** | Saint |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 56 |
| **Requires bit** | 28 |

### Chain

- **After:** [[wiki/quests/32-swamps-of-snake-warrior|Swamps of Snake Warrior]]
- **Next:** [[wiki/quests/114-weapon-tier-reinforce|Weapon tier reinforce]], [[wiki/quests/768-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/1003-chepa-village-boss-hunting|Chepa Village : Boss Hunting]]
- **Shares completion bit 56 with:** [[wiki/quests/772-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/773-group-border-area-hard-mode|Group - Border Area Hard Mode]] (completing one closes the others)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 24+ |
| 1 | class | Saint (mask 1) |

### Objectives

1. Go to [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127) — tracker: “Go to the Chepa Village” — on [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127)
2. Kill any unit of kill group 10000 ([[wiki/monsters/870-chepa-sorcerer|Chepa Sorcerer]]) × 1 — tracker: “Chepa Sorcerer (0/1)” — on [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127)
3. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

### Rewards

- **Basic reward:** 605,000 exp (shown in game as 550,000)
- **Choose one:** [[wiki/items/10002-magical-life-wand|Magical Life Wand]] (e = 15) *or* [[wiki/items/10017-magical-wrath-blade|Magical Wrath Blade]] (e = 15) *or* [[wiki/items/10011-magical-adapted-dual-gun|Magical adapted Dual Gun]] (e = 15) *or* [[wiki/items/10001-magical-thunder-wand|Magical Thunder Wand]] (e = 15)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 858)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Chepa Village is now saturated. I don't know what happened all of a sudden, but I need you to clean up Chepa Village to stabilize it.  
> *(accept / continue)*

#### Completion (QuestTalk 859)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **You:** The conditions in the Chepa Village are not good. There's even a Chepa Sorcerer now.  
> **Freya:** Chepa sorcerer...Umm.. A big change is likely to happen.  
> *(accept / continue)*

### Seen in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]]

### Mentioned in

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
