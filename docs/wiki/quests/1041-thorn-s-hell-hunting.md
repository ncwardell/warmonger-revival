---
title: "Thorn's Hell : Hunting"
type: "quest"
id: 1041
status: "partial"
missing: ["giver"]
sources: ["client: Quest.cdb id 1041", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 827", "client: QuestTalk.cdb id 828"]
name_key: "Quest_Title_1041"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 213}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 31
excludes_bit: 32
prev: [35]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 213, "talk": 827, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_ODIN"}
  - {"n": 2, "type": 1, "what": "collect", "unit_group": 10035, "units": [679, 680], "count": 10, "item": 2680, "rate": 100, "maps": [129, 129, 129], "text_key": "Quest_QuickText_1041_1"}
  - {"n": 3, "type": 1, "what": "collect", "unit_group": 10036, "units": [681, 682], "count": 5, "item": 2681, "rate": 100, "maps": [129, 129, 129], "text_key": "Quest_QuickText_1041_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_B_ODIN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 80000, "shown": 80000}
  - {"type": 1, "what": "item", "item": 601, "count": 40, "pick": "fixed"}
complete_talk: 828
---
<!-- generated:start -->
<!-- generated-keys: title=72714c type=eb5b2b id=8a8ec4 sources=6370a1 name_key=89d370 kind=77de68 kind_name=01e781 giver=2be88c turn_in=91ad7d turn_in_maps=15f2a7 bit=b6589f requires_bit=632667 excludes_bit=cb4e52 prev=5c3c3a next=97d170 stages=a80fa1 objectives=66cacb rewards=e12473 complete_talk=0da8cb -->
|  |  |
|---|---|
| **Quest id** | `1041` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/213-odin\|Odin]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 31 |
| **Not after bit** | 32 |

### Chain

- **After:** [[wiki/quests/35-demon-hell|Demon Hell]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/36-thorn-s-hell|Thorn's Hell]]

### Objectives

1. Talk to [[wiki/npcs/213-odin|Odin]] (dialogue 827) — tracker: “Go to Odin” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Collect [[wiki/items/2680-red-demon-hunter-tooth|Red Demon Hunter Tooth]] × 10 from any unit of kill group 10035 ([[wiki/monsters/679-demon-hunter|Demon Hunter]], [[wiki/monsters/680-devil-miner|Devil Miner]]) (drop 100%) — tracker: “Red Devil's Tooth (0/10)” — on [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] (129)
3. Collect [[wiki/items/2681-red-demon-hunter-horn|Red Demon Hunter Horn]] × 5 from any unit of kill group 10036 ([[wiki/monsters/681-elite-demon-hunter|Elite Demon Hunter]], [[wiki/monsters/682-elite-devil-miner|Elite Devil Miner]]) (drop 100%) — tracker: “Red Devil's Horn (0/5)” — on [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] (129)
4. Report (tracker line; done by turning the quest in) — tracker: “Return to Odin” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 80,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 40

### Dialogue

#### Objective 1 (QuestTalk 827)

Speaker: [[wiki/npcs/213-odin|Odin]]

> **Odin:** Can you bring some loot from the top Demon?  
> **Odin:** If you bring the loot, I'll find it in myself to reward you.  
> *(accept / continue)*

#### Completion (QuestTalk 828)

Speaker: [[wiki/npcs/213-odin|Odin]]

> **Odin:** You're always get things done so quickly!  
> **Odin:** If you can save more…  
> *(accept / continue)*
<!-- generated:end -->

## Notes

Repeatable ("Free") quest. The WM 0110 patch moved repeatable quests to a "Free Quests" tab on the quest board, and WM 0124 removed that tab again ([[gameplay/patch-history]]). *patch notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/patch-history]]

## Open questions

The client names no giver for this row. Whether it was offered from the quest board or by the NPC of its first "talk" step is not known ([[gameplay/patch-history]] 0110/0124).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
