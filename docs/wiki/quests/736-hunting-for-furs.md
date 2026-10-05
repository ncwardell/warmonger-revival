---
title: "Hunting for Furs"
type: "quest"
id: 736
status: "complete"
missing: []
sources: ["client: Quest.cdb id 736", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 702", "client: QuestTalk.cdb id 703"]
name_key: "Quest_Title_637_"
kind: 3
kind_name: "Free"
giver: {"npc": 214}
turn_in: {"npc": 214}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 26
excludes_bit: 25
owned_field: 127
prev: [26]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit": 668, "count": 5, "item": 2554, "rate": 70, "maps": [127, 127, 127], "text_key": "Quest_QuickText_637_1"}
  - {"n": 2, "type": 1, "what": "collect", "unit": 669, "count": 5, "item": 2553, "rate": 70, "maps": [127, 127, 127], "text_key": "Quest_QuickText_637_2"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_OWEN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 30000, "shown": 30000}
  - {"type": 1, "what": "item", "item": 601, "count": 15, "pick": "fixed"}
offer_talk: 702
complete_talk: 703
---
<!-- generated:start -->
<!-- generated-keys: title=adde10 type=eb5b2b id=4b14fe sources=691c6e name_key=374c8d kind=77de68 kind_name=01e781 giver=fb5a8b turn_in=fb5a8b offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f requires_bit=887309 excludes_bit=f6e112 owned_field=008451 prev=f36b47 next=97d170 stages=30caa7 objectives=305b00 rewards=2bba11 offer_talk=a08521 complete_talk=8fc1bb -->
|  |  |
|---|---|
|  | ![Hunting for Furs](wiki/assets/npcs/214.png) |
| **Quest id** | `736` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/214-owen\|Owen]] |
| **Turn in** | [[wiki/npcs/214-owen\|Owen]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 26 |
| **Not after bit** | 25 |
| **Field c7@10** | [[wiki/dungeons/127-lv-1-chepa-village\|(Lv 1) Chepa Village]] (127) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/26-border-area-normal-mode|Border Area Normal Mode]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/30-chepa-village|Chepa Village]], [[wiki/quests/1524-party-party-person|Party - Party Person]]

### Objectives

1. Collect [[wiki/items/2554-whiter-chepa-fur|Whiter Chepa Fur]] × 5 from [[wiki/monsters/668-chepa-warrior|Chepa Warrior]] (drop 70%) — tracker: “White Chepa Fur (0/5)” — on [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127)
2. Collect [[wiki/items/2553-black-chepa-fur|Black Chepa Fur]] × 5 from [[wiki/monsters/669-chepa-archer|Chepa Archer]] (drop 70%) — tracker: “Black Chepa Fur (0/5)” — on [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Owen”

### Rewards

- **Basic reward:** 30,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 15

### Dialogue

#### Offer (QuestTalk 702)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **Owen:** Do not you think it's getting cold? If you have hair, you will be able to make clothes warmly  
> **Owen:** So, can you get me the some Chepa Fur?  
> *(accept / continue)*

#### Completion (QuestTalk 703)

Speaker: [[wiki/npcs/214-owen|Owen]]

> **You:** I brought black and white Fur, here~  
> **Owen:** It's black and white~ I think I can make warm clothes this way~  
> *(accept / continue)*

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]
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
