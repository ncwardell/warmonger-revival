---
title: "Devil's material"
type: "quest"
id: 746
status: "complete"
missing: []
sources: ["client: Quest.cdb id 746", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 827", "client: QuestTalk.cdb id 828"]
name_key: "Quest_Title_768"
kind: 3
kind_name: "Free"
giver: {"npc": 213}
turn_in: {"npc": 213}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 31
excludes_bit: 32
owned_field: 129
prev: [35]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit_group": 10035, "units": [679, 680], "count": 10, "item": 2580, "rate": 100, "maps": [129, 129, 129], "text_key": "Quest_QuickText_768_1"}
  - {"n": 2, "type": 1, "what": "collect", "unit_group": 10036, "units": [681, 682], "count": 5, "item": 2581, "rate": 100, "maps": [129, 129, 129], "text_key": "Quest_QuickText_768_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_B_ODIN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 120000, "shown": 120000}
  - {"type": 1, "what": "item", "item": 601, "count": 40, "pick": "fixed"}
offer_talk: 827
complete_talk: 828
---
<!-- generated:start -->
<!-- generated-keys: title=bccae0 type=eb5b2b id=9b3aa2 sources=18a992 name_key=d1a442 kind=77de68 kind_name=01e781 giver=91ad7d turn_in=91ad7d offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f requires_bit=632667 excludes_bit=cb4e52 owned_field=8b7471 prev=5c3c3a next=97d170 stages=30caa7 objectives=0a6419 rewards=8cb638 offer_talk=1d57cc complete_talk=0da8cb -->
|  |  |
|---|---|
|  | ![Devil's material](wiki/assets/npcs/213.png) |
| **Quest id** | `746` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/213-odin\|Odin]] |
| **Turn in** | [[wiki/npcs/213-odin\|Odin]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 31 |
| **Not after bit** | 32 |
| **Field c7@10** | [[wiki/dungeons/129-lv-8-thorn-s-hell\|(Lv 8) Thorn's Hell]] (129) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/35-demon-hell|Demon Hell]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/36-thorn-s-hell|Thorn's Hell]]

### Objectives

1. Collect [[wiki/items/2580-red-demon-hunter-tooth|Red Demon Hunter Tooth]] × 10 from any unit of kill group 10035 ([[wiki/monsters/679-demon-hunter|Demon Hunter]], [[wiki/monsters/680-devil-miner|Devil Miner]]) (drop 100%) — tracker: “Red Devil's Tooth (0/10)” — on [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] (129)
2. Collect [[wiki/items/2581-red-demon-hunter-horn|Red Demon Hunter Horn]] × 5 from any unit of kill group 10036 ([[wiki/monsters/681-elite-demon-hunter|Elite Demon Hunter]], [[wiki/monsters/682-elite-devil-miner|Elite Devil Miner]]) (drop 100%) — tracker: “Red Devil's Horn (0/5)” — on [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] (129)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Odin”

### Rewards

- **Basic reward:** 120,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 40

### Dialogue

#### Offer (QuestTalk 827)

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
