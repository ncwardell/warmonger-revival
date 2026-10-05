---
title: "killed boss of Border area No.2"
type: "quest"
id: 762
status: "complete"
missing: []
sources: ["client: Quest.cdb id 762", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 856", "client: QuestTalk.cdb id 883"]
name_key: "Quest_Title_748"
kind: 1
kind_name: "Sub"
level: {"min": 24}
giver: {"npc": 237}
turn_in: {"npc": 237}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 67
requires_bit: 63
prev: [761]
next: [692, 759]
prerequisites:
  - {"type": 4, "what": "level", "min": 24}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit_group": 10015, "units": [674, 727, 728], "count": 1, "item": 2587, "rate": 50, "maps": [122, 122, 122], "text_key": "Quest_QuickText_761_3"}
  - {"n": 2, "type": 1, "what": "collect", "unit_group": 10016, "units": [675, 710, 711], "count": 1, "item": 2588, "rate": 50, "maps": [123, 123, 123], "text_key": "Quest_QuickText_761_4"}
  - {"n": 3, "type": 0, "what": "report", "text_key": "Quest_QuickText_F_FAREL"}
rewards:
  - {"type": 2, "what": "exp", "amount": 2400000, "shown": 2000000}
  - {"type": 1, "what": "item", "item": 9001, "count": 5, "pick": "choose", "e": 1}
  - {"type": 1, "what": "item", "item": 9000, "count": 5, "pick": "choose", "e": 1}
  - {"type": 1, "what": "item", "item": 9006, "count": 5, "pick": "choose", "e": 1}
  - {"type": 1, "what": "item", "item": 9007, "count": 5, "pick": "choose", "e": 1}
offer_talk: 856
complete_talk: 883
---
<!-- generated:start -->
<!-- generated-keys: title=a3ee91 type=eb5b2b id=c99a2a sources=0bf58c name_key=71bfb9 kind=356a19 kind_name=0bac50 level=a3b082 giver=65eab4 turn_in=65eab4 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=4d89d2 requires_bit=a17554 prev=c94718 next=daf789 prerequisites=0ab6f2 stages=30caa7 objectives=b26448 rewards=a97b23 offer_talk=efe76d complete_talk=fa9882 -->
|  |  |
|---|---|
|  | ![killed boss of Border area No.2](../assets/npcs/237.png) |
| **Quest id** | `762` |
| **Kind** | Sub (kind 1) |
| **Level** | 24+ |
| **Giver** | [[wiki/npcs/237-farrell\|Farrell]] |
| **Turn in** | [[wiki/npcs/237-farrell\|Farrell]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 67 |
| **Requires bit** | 63 |

### Chain

- **After:** [[wiki/quests/761-killed-boss-of-border-area-no-1|killed boss of Border area No.1]]
- **Next:** [[wiki/quests/692-innocence-crystal|Innocence Crystal]], [[wiki/quests/759-group-border-area-hard-mode|Group - Border Area Hard Mode]]

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 24+ |

### Objectives

1. Collect [[wiki/items/2587-the-tempest-fisher-s-pipe|The Tempest Fisher's Pipe]] from any unit of kill group 10015 ([[wiki/monsters/674-tempest-fisher|Tempest Fisher]], [[wiki/monsters/727-chepa-warrior|Chepa Warrior]], [[wiki/monsters/728-chepa-archer|Chepa Archer]]) (drop 50%) — tracker: “Acquired Fisher's Pipe (0/1)” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
2. Collect [[wiki/items/2588-the-slayer-komodo-s-pipe|The Slayer Komodo's Pipe]] from any unit of kill group 10016 ([[wiki/monsters/675-slayer-komodo|Slayer Komodo]], [[wiki/monsters/710-chepa-warrior-officer|Chepa Warrior Officer]], [[wiki/monsters/711-chepa-archer-officer|Chepa Archer Officer]]) (drop 50%) — tracker: “Acquired Komodo's Pipe (0/1)” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
3. Report (tracker line; done by turning the quest in) — tracker: “Go to Farrell”

### Rewards

- **Basic reward:** 2,400,000 exp (shown in game as 2,000,000)
- **Choose one:** [[wiki/items/9001-piece-guardian|Piece : Guardian]] × 5 (e = 1) *or* [[wiki/items/9000-piece-dark-knight-skull|Piece : Dark knight Skull]] × 5 (e = 1) *or* [[wiki/items/9006-piece-king-deathhead|Piece : King Deathhead]] × 5 (e = 1) *or* [[wiki/items/9007-piece-tempest-fisher|Piece : Tempest Fisher]] × 5 (e = 1)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 856)

Speaker: [[wiki/npcs/237-farrell|Farrell]]

> **Farrell:** There's something I'd like to have. Can you bring it? <br> The thing is... the Monster Kings have it~ Please bring it to me.  
> *(accept / continue)*

#### Completion (QuestTalk 883)

Speaker: [[wiki/npcs/237-farrell|Farrell]]

> **Farrell:** Thank you ~ Thank you! I must give you a reward! Pick one here! It's so special!  
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
