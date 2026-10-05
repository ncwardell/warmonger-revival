---
title: "Find lost item"
type: "quest"
id: 724
status: "complete"
missing: []
sources: ["client: Quest.cdb id 724", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 705", "client: QuestTalk.cdb id 732"]
name_key: "Quest_Title_700"
kind: 3
kind_name: "Free"
giver: {"npc": 205}
turn_in: {"npc": 205}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 14
excludes_bit: 22
owned_field: 128
prev: [15]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 128, "maps": [128, 128, 128], "text_key": "Quest_QuickText_700_1"}
  - {"n": 2, "type": 1, "what": "collect", "unit_group": 10027, "units": [664, 665], "count": 1, "item": 2573, "rate": 10, "maps": [128, 128, 128], "text_key": "Quest_QuickText_700_3"}
  - {"n": 5, "type": 0, "what": "report", "text_key": "Quest_QuickText_681_5"}
rewards:
  - {"type": 2, "what": "exp", "amount": 60000, "shown": 60000}
  - {"type": 1, "what": "item", "item": 601, "count": 20, "pick": "fixed"}
offer_talk: 732
complete_talk: 705
---
<!-- generated:start -->
<!-- generated-keys: title=76581d type=eb5b2b id=b19dc1 sources=4bfc46 name_key=25aaad kind=77de68 kind_name=01e781 giver=37f9c0 turn_in=37f9c0 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b6589f requires_bit=fa35e1 excludes_bit=12c6fc owned_field=b4182b prev=017b8e next=97d170 stages=30caa7 objectives=c25c18 rewards=795576 offer_talk=9deb86 complete_talk=794bb3 -->
|  |  |
|---|---|
|  | ![Find lost item](../assets/npcs/205.png) |
| **Quest id** | `724` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/205-lewellyn\|Lewellyn]] |
| **Turn in** | [[wiki/npcs/205-lewellyn\|Lewellyn]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 14 |
| **Not after bit** | 22 |
| **Field c7@10** | [[wiki/dungeons/128-lv-2-skull-cemetery\|(Lv 2) Skull Cemetery]] (128) (contract: fort the nation must own) |

### Chain

- **After:** [[wiki/quests/15-repel-the-skeleton-invasion|Repel the Skeleton Invasion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]

### Objectives

1. Go to [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128) — tracker: “Move to the Skull Cemetery” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
2. Collect [[wiki/items/2573-toy-ring|Toy Ring]] from any unit of kill group 10027 ([[wiki/monsters/664-black-skeleton-warrior|Black Skeleton Warrior]], [[wiki/monsters/665-black-skeleton-archer|Black Skeleton Archer]]) (drop 10%) — tracker: “Find lost items (0/1)” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
5. Report (tracker line; done by turning the quest in) — tracker: “Go back to Lewellyn”

### Rewards

- **Basic reward:** 60,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 20

### Dialogue

#### Offer (QuestTalk 732)

Speaker: [[wiki/npcs/205-lewellyn|Lewellyn]]

> **Lewellyn:** Will you go to the Skull Cemetery? There's a request for you~  
> **Lewellyn:** The soldier who has gone to the cemetery of the skeleton says he has lost his belongings.  
> **Lewellyn:** Could you find a belongings?  
> *(accept / continue)*

#### Completion (QuestTalk 705)

Speaker: [[wiki/npcs/205-lewellyn|Lewellyn]]

> **Lewellyn:** You found me ~ I'm glad. This ring belonged to a soldier's child.  
> **Lewellyn:** I am glad to find it.~ I have a keeper, so it is safe~ I'll let you know when other missions arrive~  
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
