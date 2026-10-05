---
title: "Mushrooms in the Komodo area"
type: "quest"
id: 786
status: "complete"
missing: []
sources: ["client: Quest.cdb id 786", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 874", "client: QuestTalk.cdb id 875"]
name_key: "Quest_Title_784"
kind: 1
kind_name: "Sub"
giver: {"npc": 204}
turn_in: {"npc": 204}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 87
requires_bit: 84
prev: [781, 782]
next: []
stages: [3, 4, 5, 5, 5]
objectives:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 123, "maps": [123, 123, 123], "text_key": "Quest_QuickText_784_1"}
  - {"n": 2, "type": 5, "what": "gadget", "gadget": 18, "extra": {"c": 2591}, "maps": [123, 123, 123], "text_key": "Quest_QuickText_784_2"}
  - {"n": 3, "type": 0, "what": "report", "text_key": "Quest_QuickText_CB_REN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 130000, "shown": 108333}
  - {"type": 1, "what": "item", "item": 890, "count": 50, "pick": "fixed"}
offer_talk: 874
complete_talk: 875
---
<!-- generated:start -->
<!-- generated-keys: title=d94cd6 type=eb5b2b id=40bc26 sources=2b34f7 name_key=31cc72 kind=356a19 kind_name=0bac50 giver=4518d0 turn_in=4518d0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=e62d7f requires_bit=be461a prev=49296a next=97d170 stages=260252 objectives=7c8f00 rewards=a50786 offer_talk=7d9f2b complete_talk=c08d99 -->
|  |  |
|---|---|
|  | ![Mushrooms in the Komodo area](wiki/assets/npcs/204.png) |
| **Quest id** | `786` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/204-wren\|Wren]] |
| **Turn in** | [[wiki/npcs/204-wren\|Wren]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 87 |
| **Requires bit** | 84 |

### Chain

- **After:** [[wiki/quests/781-tsunami-lake|Tsunami Lake]], [[wiki/quests/782-tsunami-lake|Tsunami Lake]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Go to [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123) — tracker: “Go to the Swamps of the Snake Warrior” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
2. Talk to [[wiki/nodes/12318-swamp-mushroom|Swamp mushroom]] (gadget 18) (also c=2591) — tracker: “Mushroom” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Wren”

Stages (`flag1..5` = [3, 4, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 130,000 exp (shown in game as 108,333); [[wiki/items/890-potion-of-mana-b|Potion of Mana (B)]] × 50

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 874)

Speaker: [[wiki/npcs/204-wren|Wren]]

> **Wren:** If you use mushrooms, which grow in the Swamps of the Snake Warrior, as a medicine, the medicine will work better. Could you please get some?  
> *(accept / continue)*  
> *(accept / continue)*

#### Completion (QuestTalk 875)

Speaker: [[wiki/npcs/204-wren|Wren]]

> **Wren:** Thank you for bringing these.  
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
