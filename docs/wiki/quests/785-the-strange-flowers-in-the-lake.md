---
title: "The strange flowers in the lake"
type: "quest"
id: 785
status: "complete"
missing: []
sources: ["client: Quest.cdb id 785", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 872", "client: QuestTalk.cdb id 873"]
name_key: "Quest_Title_783"
kind: 1
kind_name: "Sub"
giver: {"npc": 204}
turn_in: {"npc": 204}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 86
requires_bit: 36
prev: [770]
next: []
stages: [3, 4, 5, 5, 5]
objectives:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 122, "maps": [122, 122, 122], "text_key": "Quest_QuickText_749_0"}
  - {"n": 2, "type": 5, "what": "gadget", "gadget": 15, "extra": {"c": 2590}, "maps": [122, 122, 122], "text_key": "Quest_QuickText_783_2"}
  - {"n": 3, "type": 0, "what": "report", "text_key": "Quest_QuickText_CB_REN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 130000, "shown": 108333}
  - {"type": 1, "what": "item", "item": 886, "count": 50, "pick": "fixed"}
offer_talk: 872
complete_talk: 873
---
<!-- generated:start -->
<!-- generated-keys: title=d0b721 type=eb5b2b id=298f93 sources=1e0225 name_key=d4df09 kind=356a19 kind_name=0bac50 giver=4518d0 turn_in=4518d0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=3c26df requires_bit=fc074d prev=d8e285 next=97d170 stages=260252 objectives=f9d131 rewards=eb5d23 offer_talk=389b4f complete_talk=eab06f -->
|  |  |
|---|---|
|  | ![The strange flowers in the lake](../assets/npcs/204.png) |
| **Quest id** | `785` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/204-wren\|Wren]] |
| **Turn in** | [[wiki/npcs/204-wren\|Wren]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 86 |
| **Requires bit** | 36 |

### Chain

- **After:** [[wiki/quests/770-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Go to [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122) — tracker: “Go to the Tsunami Lake” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
2. Talk to [[wiki/nodes/12215-tsunami-lake-flower|Tsunami Lake flower]] (gadget 15) (also c=2590) — tracker: “Obtain the Unknow Flowers” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Wren”

Stages (`flag1..5` = [3, 4, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 130,000 exp (shown in game as 108,333); [[wiki/items/886-potion-of-health-b|Potion of Health (B)]] × 50

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 872)

Speaker: [[wiki/npcs/204-wren|Wren]]

> **Wren:** They say there are flowers that grow only in the Tsunami Lake. If you can get this flower, I can make a potion. Please get it.  
> *(accept / continue)*  
> *(accept / continue)*

#### Completion (QuestTalk 873)

Speaker: [[wiki/npcs/204-wren|Wren]]

> **Wren:** Thank you! I think I can make good medicine from this~  
> *(accept / continue)*  
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
