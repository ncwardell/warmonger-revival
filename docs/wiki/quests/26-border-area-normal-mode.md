---
title: "Border Area Normal Mode"
type: "quest"
id: 26
status: "complete"
missing: []
sources: ["client: Quest.cdb id 26", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 834", "client: QuestTalk.cdb id 835", "client: QuestTalk.cdb id 884"]
name_key: "Quest_Title_724"
kind: 0
kind_name: "Main"
giver: {"npc": 204}
turn_in: {"npc": 204}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 26
requires_bit: 21
prev: [21]
next: [30, 736, 1001, 1002]
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 204, "talk": 834, "maps": [120, 120, 120], "text_key": "Quest_QuickText_724_0"}
  - {"n": 2, "type": 10, "what": "buy_item", "item": 688, "count": 1, "text_key": "Quest_QuickText_724_1"}
  - {"n": 3, "type": 0, "what": "report", "text_key": "Quest_QuickText_656_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 11000, "shown": 10000}
offer_talk: 884
complete_talk: 835
---
<!-- generated:start -->
<!-- generated-keys: title=9e43fd type=eb5b2b id=887309 sources=5891dc name_key=2be012 kind=b6589f kind_name=b3f808 giver=4518d0 turn_in=4518d0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=887309 requires_bit=472b07 prev=6c9878 next=9d849e stages=30caa7 objectives=fd4b93 rewards=a7fbfc offer_talk=8cc981 complete_talk=d449b2 -->
|  |  |
|---|---|
|  | ![Border Area Normal Mode](../assets/npcs/204.png) |
| **Quest id** | `26` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/204-wren\|Wren]] |
| **Turn in** | [[wiki/npcs/204-wren\|Wren]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 26 |
| **Requires bit** | 21 |

### Chain

- **After:** [[wiki/quests/21-group-ancient-ghosts|(Group) Ancient Ghosts]]
- **Next:** [[wiki/quests/30-chepa-village|Chepa Village]], [[wiki/quests/736-hunting-for-furs|Hunting for Furs]], [[wiki/quests/1001-chepa-village-hunting|Chepa Village : Hunting]], [[wiki/quests/1002-chepa-village-collecting-material|Chepa Village : Collecting material]]

### Objectives

1. Talk to [[wiki/npcs/204-wren|Wren]] (dialogue 834) — tracker: “Return to Wren”
2. Buy [[wiki/items/688-dimensional-energy|Dimensional energy]] — tracker: “Dimensional energy Buy”
3. Report (tracker line; done by turning the quest in) — tracker: “Talk to Wren”

### Rewards

- **Basic reward:** 11,000 exp (shown in game as 10,000)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 884)

Speaker: [[wiki/npcs/204-wren|Wren]]

> **Wren:** Did you come to buy it in my shop? Let's buy it soon ~  
> *(accept / continue)*

#### Objective 1 (QuestTalk 834)

Speaker: [[wiki/npcs/204-wren|Wren]]

> **Wren:** Hi~ Are you going to go outside of Gaia now? Then there are items that you absolutely need to take with you. <br> You can buy them here!  
> *(end)*

#### Completion (QuestTalk 835)

Speaker: [[wiki/npcs/204-wren|Wren]]

> **Wren:** Dimensional energy is a necessary item when entering the border area!  
> *(accept / continue)*
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
