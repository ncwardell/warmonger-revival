---
title: "Acquire materials"
type: "quest"
id: 747
status: "complete"
missing: []
sources: ["client: Quest.cdb id 747", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 829", "client: QuestTalk.cdb id 830"]
name_key: "Quest_Title_769"
kind: 3
kind_name: "Free"
giver: {"npc": 214}
turn_in: {"npc": 214}
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
  - {"n": 1, "type": 3, "what": "acquire_item", "item": 849, "count": 3, "maps": [129, 129, 129], "text_key": "Quest_QuickText_769_1"}
  - {"n": 2, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 135000, "shown": 135000}
  - {"type": 1, "what": "item", "item": 611, "count": 40, "pick": "fixed"}
offer_talk: 829
complete_talk: 830
---
<!-- generated:start -->
<!-- generated-keys: title=66283e type=eb5b2b id=5c1dc0 sources=08635a name_key=5debb6 kind=77de68 kind_name=01e781 giver=fb5a8b turn_in=fb5a8b offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f requires_bit=632667 excludes_bit=cb4e52 owned_field=8b7471 prev=5c3c3a next=97d170 stages=30caa7 objectives=d83537 rewards=3d8dbe offer_talk=459b50 complete_talk=201921 -->
|  |  |
|---|---|
|  | ![Acquire materials](wiki/assets/npcs/214.png) |
| **Quest id** | `747` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/214-owen\|Owen]] |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
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

1. Acquire [[wiki/items/849-burning-water|Burning water]] × 3 — tracker: “Acquire Burning water (0/3)” — on [[wiki/dungeons/129-lv-8-thorn-s-hell|(Lv 8) Thorn's Hell]] (129)
2. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen”

### Rewards

- **Basic reward:** 135,000 exp; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 40

### Dialogue

#### Offer (QuestTalk 829)

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
