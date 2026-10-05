---
title: "Bring the Demon Crystals"
type: "quest"
id: 780
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 780", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 764"]
name_key: "Quest_Title_760_"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"auto": true}
bit: 0
requires_bit: 31
automatic: true
prev: [35]
next: []
prerequisites:
  - {"type": 6, "what": "item", "item": 2575, "count": 1}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 213, "talk": 764, "maps": [120, 120, 120], "text_key": "Quest_QuickText_B_ODIN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 50000, "shown": 50000}
  - {"type": 1, "what": "item", "item": 611, "count": 35, "pick": "fixed"}
---
<!-- generated:start -->
<!-- generated-keys: title=dbde19 type=eb5b2b id=1dd4b9 sources=7568b4 name_key=ddab61 kind=77de68 kind_name=01e781 giver=2be88c turn_in=847ad4 bit=b6589f requires_bit=632667 automatic=5ffe53 prev=5c3c3a next=97d170 prerequisites=af527d stages=30caa7 objectives=edb81f rewards=7ad9bd -->
|  |  |
|---|---|
| **Quest id** | `780` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | automatic |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 31 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/35-demon-hell|Demon Hell]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/2575-demon-crystals\|Demon Crystals]] |

### Objectives

1. Talk to [[wiki/npcs/213-odin|Odin]] (dialogue 764) — tracker: “Return to Odin” — on [[wiki/fields/120-fortress|Fortress]] (120)

### Rewards

- **Basic reward:** 50,000 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 35

### Dialogue

#### Objective 1 (QuestTalk 764)

Speaker: [[wiki/npcs/213-odin|Odin]]

> **You:** When I gathered the unknown crystals, they became the crystals of the devils. Can you analyze this?  
> **Odin:** Of course .. But ... I think that there are stronger monsters.  
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
