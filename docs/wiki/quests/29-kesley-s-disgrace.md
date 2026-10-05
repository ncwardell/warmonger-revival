---
title: "Kesley's Disgrace"
type: "quest"
id: 29
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 29", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 676", "client: QuestTalk.cdb id 885"]
name_key: "Quest_Title_652"
kind: 0
kind_name: "Main"
giver: {"npc": 210}
turn_in: {"npc": 210}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 52
requires_bit: 44
prev: [105]
next: [48, 117, 120]
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 3, "b": 1, "text_key": "Quest_QuickText_652_2"}
  - {"n": 2, "type": 0, "what": "report", "maps": [90, 90, 90], "text_key": "Quest_QuickText_650_3"}
rewards:
  - {"type": 2, "what": "exp", "amount": 500000, "shown": 454545}
offer_talk: 885
complete_talk: 676
---
<!-- generated:start -->
<!-- generated-keys: title=64c742 type=eb5b2b id=7719a1 sources=39294f name_key=c2d13e kind=b6589f kind_name=b3f808 giver=7abdb8 turn_in=7abdb8 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=a93349 requires_bit=98fbc4 prev=355b7f next=d998ae stages=30caa7 objectives=2be88c objectives_client=4bf360 rewards=f79b21 offer_talk=c5f248 complete_talk=c6cf93 -->
|  |  |
|---|---|
|  | ![Kesley's Disgrace](wiki/assets/npcs/210.png) |
| **Quest id** | `29` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 52 |
| **Requires bit** | 44 |

### Chain

- **After:** [[wiki/quests/105-kesley-s-disgrace|Kesley's Disgrace]]
- **Next:** [[wiki/quests/48-doping-create|Doping Create]], [[wiki/quests/117-lords-of-the-land|Lords of the Land]], [[wiki/quests/120-enemy-territory|Enemy territory]]

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 15 — monster-area war / occupation?; values a=3, b=1 — tracker: “Invade monster lands. Kill Officers and build Nexus to summon the boss. Kill the territory boss.”
2. Report (tracker line; done by turning the quest in) — tracker: “Return to Kesley” — on [[wiki/fields/90-castle|Castle]] (90)

### Rewards

- **Basic reward:** 500,000 exp (shown in game as 454,545)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 885)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** Did you miss out on a mission? I can give you the mission again.  
> *(accept / continue)*

#### Completion (QuestTalk 676)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** Great job!  
> **Kesley:** We'll meet again.  
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
