---
title: "The necessary materials"
type: "quest"
id: 727
status: "complete"
missing: []
sources: ["client: Quest.cdb id 727", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 694", "client: QuestTalk.cdb id 695"]
name_key: "Quest_Title_727"
kind: 3
kind_name: "Free"
giver: {"npc": 204}
turn_in: {"npc": 204}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 25
excludes_bit: 14
owned_field: 121
prev: [30, 1524]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit_group": 10009, "units": [640, 641], "count": 10, "item": 2555, "rate": 100, "maps": [121, 121, 121], "text_key": "Quest_QuickText_727"}
  - {"n": 2, "type": 1, "what": "collect", "unit": 10010, "count": 5, "item": 2557, "rate": 100, "maps": [121, 121, 121], "text_key": "Quest_QuickText_727_1"}
  - {"n": 3, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_REN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 37500, "shown": 37500}
  - {"type": 1, "what": "item", "item": 601, "count": 20, "pick": "fixed"}
offer_talk: 694
complete_talk: 695
---
<!-- generated:start -->
<!-- generated-keys: title=0909e2 type=eb5b2b id=90f98c sources=913d4e name_key=876cd5 kind=77de68 kind_name=01e781 giver=4518d0 turn_in=4518d0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f requires_bit=f6e112 excludes_bit=fa35e1 owned_field=8bd795 prev=71a868 next=97d170 stages=30caa7 objectives=214329 rewards=b49a38 offer_talk=d2e19c complete_talk=00a691 -->
|  |  |
|---|---|
|  | ![The necessary materials](wiki/assets/npcs/204.png) |
| **Quest id** | `727` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/204-wren\|Wren]] |
| **Turn in** | [[wiki/npcs/204-wren\|Wren]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 25 |
| **Not after bit** | 14 |
| **Field c7@10** | [[wiki/dungeons/121-lv-1-skull-temple\|(Lv 1) Skull Temple]] (121) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/30-chepa-village|Chepa Village]], [[wiki/quests/1524-party-party-person|Party - Party Person]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/15-repel-the-skeleton-invasion|Repel the Skeleton Invasion]]

### Objectives

1. Collect [[wiki/items/2555-skeleton-bone|Skeleton bone]] × 10 from any unit of kill group 10009 ([[wiki/monsters/640-skeleton-warrior|Skeleton Warrior]], [[wiki/monsters/641-skeleton-archer|Skeleton Archer]]) (drop 100%) — tracker: “Skeleton bone (0/10)” — on [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121)
2. Collect [[wiki/items/2557-elite-skeleton-bone|Elite Skeleton bone]] × 5 from Object 10010 (drop 100%) — tracker: “Elite Skeleton bone (0/5)” — on [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121)
3. Report (tracker line; done by turning the quest in) — tracker: “Return to Wren”

### Rewards

- **Basic reward:** 37,500 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 20

### Dialogue

#### Offer (QuestTalk 694)

Speaker: [[wiki/npcs/204-wren|Wren]]

> **Wren:** I need ingredients~You can acquire bones by killing skeletons that exist in the skeleton's temple.  
> **Wren:** Please save the bones of the skeletons ~  
> *(accept / continue)*

#### Completion (QuestTalk 695)

Speaker: [[wiki/npcs/204-wren|Wren]]

> **Wren:** This is the bone of the skeletons. Hmm .. I guess this is not enough~ I would appreciate it if you could save me more.  
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
