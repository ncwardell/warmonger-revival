---
title: "Skull Cemetery : Boss Hunting"
type: "quest"
id: 1013
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1013", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 862", "client: QuestTalk.cdb id 863"]
name_key: "Quest_Title_1013"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 200}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 36
prev: [770]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 200, "talk": 862, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_FREYA"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 128, "maps": [128, 128, 128], "text_key": "Quest_QuickText_1013_1"}
  - {"n": 3, "type": 1, "what": "kill", "unit_group": 10014, "units": [673], "count": 1, "maps": [128, 128, 128], "text_key": "Quest_QuickText_1013_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 100000, "shown": 100000}
  - {"type": 1, "what": "item", "item": 601, "count": 40, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 40, "pick": "fixed"}
complete_talk: 863
---
<!-- generated:start -->
<!-- generated-keys: title=57970c type=eb5b2b id=ba5bfc sources=2e49de name_key=c971d1 kind=77de68 kind_name=01e781 giver=2be88c turn_in=1caac0 turn_in_maps=15f2a7 bit=b6589f requires_bit=fc074d prev=d8e285 next=97d170 stages=a80fa1 objectives=d707a6 rewards=1993dc complete_talk=c2145e -->
|  |  |
|---|---|
| **Quest id** | `1013` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 36 |

### Chain

- **After:** [[wiki/quests/770-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Talk to [[wiki/npcs/200-freya|Freya]] (dialogue 862) — tracker: “Go to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Go to [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128) — tracker: “Move to the Skull Cemetery” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
3. Kill any unit of kill group 10014 ([[wiki/monsters/673-dark-knight-skull|Dark Knight Skull]]) × 1 — tracker: “Dark Knight Skull (0/1)” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
4. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 100,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 40; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 40

### Dialogue

#### Objective 1 (QuestTalk 862)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** The Skull Cemetery has a bad aura. I don't know the cause of it yet, however. Kill Skull to stabilize the area.  
> *(accept / continue)*

#### Completion (QuestTalk 863)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **You:** I have killed Skull. The Dimension Gate still looks bad.  
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
