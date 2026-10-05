---
title: "Thorn's Hell : Collecting material"
type: "quest"
id: 1042
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1042", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 829", "client: QuestTalk.cdb id 830"]
name_key: "Quest_Title_1042"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 214}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 31
excludes_bit: 32
prev: [35]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 214, "talk": 829, "maps": [120, 120, 120], "text_key": "Quest_QuickText_C_OWEN"}
  - {"n": 2, "type": 3, "what": "acquire_item", "item": 849, "count": 3, "maps": [129, 129, 129], "text_key": "Quest_QuickText_1042_1"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 90000, "shown": 90000}
  - {"type": 1, "what": "item", "item": 611, "count": 40, "pick": "fixed"}
complete_talk: 830
---
<!-- generated:start -->
<!-- generated-keys: title=72301e type=eb5b2b id=8b2dd0 sources=7242d5 name_key=04e663 kind=77de68 kind_name=01e781 giver=2be88c turn_in=fb5a8b turn_in_maps=15f2a7 bit=b6589f requires_bit=632667 excludes_bit=cb4e52 prev=5c3c3a next=97d170 stages=a80fa1 objectives=dcd837 rewards=f28039 complete_talk=201921 -->
|  |  |
|---|---|
| **Quest id** | `1042` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 31 |
| **Not after bit** | 32 |

### Chain

- **After:** [[wiki/quests/35-demon-hell|Demon Hell]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/36-thorn-s-hell|Thorn's Hell]]

### Objectives

1. Talk to [[wiki/npcs/214-owen|Owen]] (dialogue 829) — tracker: “Go to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Acquire [[wiki/items/849-burning-water|Burning water]] × 3 — tracker: “Acquire Burning water (0/3) (Elite monster hunting)” — on [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] (129)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 90,000 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 40

### Dialogue

#### Objective 1 (QuestTalk 829)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** The war is getting tougher and there are a lot of requests coming in. <br> Could you please get me some important ingredients from the Dimension Gate in Thorn's Hell?  
> *(accept / continue)*

#### Completion (QuestTalk 830)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** You got me some wonderful ingredients. Thank you very much.  
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
