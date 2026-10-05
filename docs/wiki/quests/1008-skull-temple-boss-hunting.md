---
title: "Skull Temple : Boss Hunting"
type: "quest"
id: 1008
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1008", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 860", "client: QuestTalk.cdb id 861"]
name_key: "Quest_Title_1008"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 200}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 55
prev: [768]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 200, "talk": 860, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_FREYA"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 121, "maps": [121, 121, 121], "text_key": "Quest_QuickText_1008_1"}
  - {"n": 3, "type": 1, "what": "kill", "unit_group": 10013, "units": [672], "count": 1, "maps": [121, 121, 121], "text_key": "Quest_QuickText_1008_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 75000, "shown": 75000}
  - {"type": 1, "what": "item", "item": 601, "count": 40, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 40, "pick": "fixed"}
complete_talk: 861
---
<!-- generated:start -->
<!-- generated-keys: title=bda1a8 type=eb5b2b id=ff1eb8 sources=c1d259 name_key=d3e9e6 kind=77de68 kind_name=01e781 giver=2be88c turn_in=1caac0 turn_in_maps=15f2a7 bit=b6589f requires_bit=8effee prev=d571f1 next=97d170 stages=a80fa1 objectives=da2d22 rewards=2f2ce7 complete_talk=d5843c -->
|  |  |
|---|---|
| **Quest id** | `1008` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 55 |

### Chain

- **After:** [[wiki/quests/768-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Talk to [[wiki/npcs/200-freya|Freya]] (dialogue 860) — tracker: “Go to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Go to [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121) — tracker: “Go to the Skull Temple” — on [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121)
3. Kill any unit of kill group 10013 ([[wiki/monsters/672-king-deathhead|King Deathhead]]) × 1 — tracker: “King Deathhead (0/1)” — on [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121)
4. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 75,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 40; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 40

### Dialogue

#### Objective 1 (QuestTalk 860)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** Death Heads appeared in the Skeleton Temple. I feel bad after last time so I ask you to investigate.  
> *(accept / continue)*

#### Completion (QuestTalk 861)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** It's a big deal. The state of the dimension gate is getting worse.  
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
