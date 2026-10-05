---
title: "Buy time energy"
type: "quest"
id: 714
status: "complete"
missing: []
sources: ["client: Quest.cdb id 714", "client: QuestTalk.cdb id 836", "client: QuestTalk.cdb id 837", "client: QuestTalk.cdb id 898"]
name_key: "Quest_Title_725"
kind: 0
kind_name: "Main"
giver: {"npc": 207}
turn_in: {"npc": 207}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 7
requires_bit: 55
prev: [768]
next: [770]
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 207, "talk": 836, "maps": [120, 120, 120], "text_key": "Quest_QuickText_725_0"}
  - {"n": 2, "type": 10, "what": "buy_item", "item": 689, "count": 1, "maps": [120, 120, 120], "text_key": "Quest_QuickText_725_1"}
  - {"n": 3, "type": 0, "what": "report", "text_key": "Quest_QuickText_725_2"}
rewards: []
offer_talk: 898
complete_talk: 837
---
<!-- generated:start -->
<!-- generated-keys: title=f9eac7 type=eb5b2b id=3acc03 sources=48ea3d name_key=e1ea16 kind=b6589f kind_name=b3f808 giver=7e080a turn_in=7e080a offer_maps=15f2a7 turn_in_maps=15f2a7 bit=902ba3 requires_bit=8effee prev=d571f1 next=d8e285 stages=30caa7 objectives=011fc0 rewards=97d170 offer_talk=6b2e24 complete_talk=9b41f9 -->
|  |  |
|---|---|
|  | ![Buy time energy](../assets/npcs/207.png) |
| **Quest id** | `714` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/207-athan\|Athan]] |
| **Turn in** | [[wiki/npcs/207-athan\|Athan]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 7 |
| **Requires bit** | 55 |

### Chain

- **After:** [[wiki/quests/768-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** [[wiki/quests/770-group-border-area-hard-mode|Group - Border Area Hard Mode]]

### Objectives

1. Talk to [[wiki/npcs/207-athan|Athan]] (dialogue 836) — tracker: “Return to Athan”
2. Buy [[wiki/items/689-tier-1-time-energy|Tier 1 : Time energy]] — tracker: “Tier 1 : Time energy Buy”
3. Report (tracker line; done by turning the quest in) — tracker: “Talk to Athan”

### Rewards

None in the client.

### Dialogue

#### Offer (QuestTalk 898)

Speaker: [[wiki/npcs/207-athan|Athan]]

> **Athan:** Come on, you can buy medals and fame items from me.  
> *(accept / continue)*

#### Objective 1 (QuestTalk 836)

Speaker: [[wiki/npcs/207-athan|Athan]]

> **Athan:** This item is the best in the border area! Try it once and do not forget that the required number depends on the border area -  
> *(end)*

#### Completion (QuestTalk 837)

Speaker: [[wiki/npcs/207-athan|Athan]]

> **Athan:** Did you buy the ingredients you needed? I wish you luck with them.  
> *(accept / continue)*

### Seen in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]]
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
