---
title: "Skull Temple : Hunting"
type: "quest"
id: 1006
status: "stub"
missing: ["giver"]
sources: ["client: Quest.cdb id 1006", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 694", "client: QuestTalk.cdb id 695"]
name_key: "Quest_Title_1006"
kind: 3
kind_name: "Free"
giver: null
turn_in: {"npc": 204}
turn_in_maps: [120, 120, 120]
bit: 0
requires_bit: 25
excludes_bit: 14
prev: [30, 1524]
next: []
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 204, "talk": 694, "maps": [120, 120, 120], "text_key": "Quest_QuickText_F_REN"}
  - {"n": 2, "type": 1, "what": "collect", "unit_group": 10009, "units": [640, 641], "count": 10, "item": 2655, "rate": 100, "maps": [121, 121, 121], "text_key": "Quest_QuickText_1006_1"}
  - {"n": 3, "type": 1, "what": "collect", "unit": 10010, "count": 5, "item": 2657, "rate": 100, "maps": [121, 121, 121], "text_key": "Quest_QuickText_1006_2"}
  - {"n": 4, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_CB_REN"}
rewards:
  - {"type": 2, "what": "exp", "amount": 25000, "shown": 25000}
  - {"type": 1, "what": "item", "item": 601, "count": 20, "pick": "fixed"}
complete_talk: 695
---
<!-- generated:start -->
<!-- generated-keys: title=41296c type=eb5b2b id=8554fe sources=b1c4ca name_key=0688ca kind=77de68 kind_name=01e781 giver=2be88c turn_in=4518d0 turn_in_maps=15f2a7 bit=b6589f requires_bit=f6e112 excludes_bit=fa35e1 prev=71a868 next=97d170 stages=a80fa1 objectives=f56ae0 rewards=580311 complete_talk=00a691 -->
|  |  |
|---|---|
| **Quest id** | `1006` |
| **Kind** | Free (kind 3) |
| **Giver** | **unknown** |
| **Turn in** | [[wiki/npcs/204-wren\|Wren]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 25 |
| **Not after bit** | 14 |

### Chain

- **After:** [[wiki/quests/30-chepa-village|Chepa Village]], [[wiki/quests/1524-party-party-person|Party - Party Person]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/15-repel-the-skeleton-invasion|Repel the Skeleton Invasion]]

### Objectives

1. Talk to [[wiki/npcs/204-wren|Wren]] (dialogue 694) — tracker: “Go to Wren” — on [[wiki/fields/120-fortress|Fortress]] (120)
2. Collect [[wiki/items/2655-skeleton-bone|Skeleton bone]] × 10 from any unit of kill group 10009 ([[wiki/monsters/640-skeleton-warrior|Skeleton Warrior]], [[wiki/monsters/641-skeleton-archer|Skeleton Archer]]) (drop 100%) — tracker: “Skeleton bone (0/10)” — on [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121)
3. Collect [[wiki/items/2657-elite-skeleton-bone|Elite Skeleton bone]] × 5 from Object 10010 (drop 100%) — tracker: “Elite Skeleton bone (0/5)” — on [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121)
4. Report (tracker line; done by turning the quest in) — tracker: “Return to Wren” — on [[wiki/fields/120-fortress|Fortress]] (120)

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 25,000 exp; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 20

### Dialogue

#### Objective 1 (QuestTalk 694)

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
