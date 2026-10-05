---
title: "Skull Cemetery : Hunting"
type: "quest"
id: 1011
status: "partial"
missing: ["giver"]
sources: ["client: Quest.cdb id 1011", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 705", "client: QuestTalk.cdb id 732"]
name_key: "Quest_Title_1011"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 205}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 14
excludes_bit: 22
prev: [15]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 205, "talk": 732, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_Lewe"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 128, "maps": [128, 128, 128], "text_key": "Quest_QuickText_1011_1"}
  - {"n": 3, "type": 1, "what": "collect", "unit_group": 10027, "units": [664, 665], "count": 1, "item": 2673, "rate": 10, "maps": [128, 128, 128], "text_key": "Quest_QuickText_1011_2"}
  - {"n": 4, "type": 0, "what": "report", "text_key": "Quest_QuickText_CB_Lewe"}
rewards:
  - {"type": 2, "what": "exp", "amount": 40000, "shown": 40000}
  - {"type": 1, "what": "item", "item": 601, "count": 20, "pick": "fixed"}
complete_talk: 705
---
<!-- generated:start -->
<!-- generated-keys: title=8c7a64 type=eb5b2b id=dd2dfa sources=62e453 name_key=a8815f kind=77de68 kind_name=01e781 giver=2be88c turn_in=37f9c0 turn_in_maps=15f2a7 bit=b6589f requires_bit=fa35e1 excludes_bit=12c6fc prev=017b8e next=97d170 stages=a80fa1 objectives=137aac rewards=7d28c7 complete_talk=794bb3 -->
|  |  |
|---|---|
| **Quest id** | `1011` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/205-lewellyn\|Lewellyn]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 14 |
| **Not after bit** | 22 |

### Chain

- **After:** [[wiki/quests/15-repel-the-skeleton-invasion|Repel the Skeleton Invasion]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]

### Objectives

1. Talk to [[wiki/npcs/205-lewellyn|Lewellyn]] (dialogue 732) — tracker: “Go to Lewellyn” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Go to [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128) — tracker: “Move to the Skull Cemetery” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
3. Collect [[wiki/items/2673-toy-ring|Toy Ring]] from any unit of kill group 10027 ([[wiki/monsters/664-black-skeleton-warrior|Black Skeleton Warrior]], [[wiki/monsters/665-black-skeleton-archer|Black Skeleton Archer]]) (drop 10%) — tracker: “Find lost items (0/1)” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
4. Report (tracker line; done by turning the quest in) — tracker: “Return to Lewellyn”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 40,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 20

### Dialogue

#### Objective 1 (QuestTalk 732)

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

Repeatable ("Free") quest. The WM 0110 patch moved repeatable quests to a "Free Quests" tab on the quest board, and WM 0124 removed that tab again ([[gameplay/patch-history]]). *patch notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/patch-history]]

## Open questions

The client names no giver for this row. Whether it was offered from the quest board or by the NPC of its first "talk" step is not known ([[gameplay/patch-history]] 0110/0124).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
