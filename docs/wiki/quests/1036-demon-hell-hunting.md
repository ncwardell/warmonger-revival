---
title: "Demon Hell : Hunting"
type: "quest"
id: 1036
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1036", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 763"]
name_key: "Quest_Title_1036"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"auto": true}
bit: 0
requires_bit: 30
excludes_bit: 31
automatic: true
prev: [34]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 213, "talk": 763, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_ODIN"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 126, "maps": [126, 126, 126], "text_key": "Quest_QuickText_1036_1"}
  - {"n": 3, "type": 1, "what": "collect", "unit_group": 10031, "units": [662], "count": 10, "item": 2674, "rate": 70, "maps": [126, 126, 126], "text_key": "Quest_QuickText_1036_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 30000, "shown": 30000}
---
<!-- generated:start -->
<!-- generated-keys: title=35624f type=eb5b2b id=3d41b7 sources=004b99 name_key=d4fae6 kind=77de68 kind_name=01e781 giver=2be88c turn_in=847ad4 bit=b6589f requires_bit=22d200 excludes_bit=632667 automatic=5ffe53 prev=91a33c next=97d170 stages=a80fa1 objectives=2a7e19 rewards=cf1f3c -->
|  |  |
|---|---|
| **Quest id** | `1036` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | automatic |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 30 |
| **Not after bit** | 31 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/34-tow-canyon|Tow Canyon]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/35-demon-hell|Demon Hell]]

### Objectives

1. Talk to [[wiki/npcs/213-odin|Odin]] (dialogue 763) — tracker: “Go to Odin” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Go to [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] (126) — tracker: “Move to the Demonic Hell Boundary Area” — on [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] (126)
3. Collect [[wiki/items/2674-unknown-crystal|Unknown Crystal]] × 10 from any unit of kill group 10031 ([[wiki/monsters/662-demon-hunter|Demon Hunter]]) (drop 70%) — tracker: “Kill a demon and collect decisions (0/10)” — on [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] (126)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 30,000 exp

### Dialogue

#### Objective 1 (QuestTalk 763)

Speaker: [[wiki/npcs/213-odin|Odin]]

> **Odin:** The Demon living in the Devildom are coming to our world. Please go to the Demon Hell and kill them. If you kill the Demons, please bring some drop items aswell.  
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
