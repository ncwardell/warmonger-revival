---
title: "killed boss of Border area No.1"
type: "quest"
id: 761
status: "complete"
missing: []
sources: ["client: Quest.cdb id 761", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 856", "client: QuestTalk.cdb id 857"]
name_key: "Quest_Title_761"
kind: 1
kind_name: "Sub"
level: {"min": 24}
giver: {"npc": 237}
turn_in: {"npc": 237}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 63
requires_bit: 28
prev: [32]
next: [756, 762]
prerequisites:
  - {"type": 4, "what": "level", "min": 24}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit_group": 10000, "units": [870], "count": 1, "item": 2589, "rate": 50, "maps": [127, 127, 127], "text_key": "Quest_QuickText_761_0"}
  - {"n": 2, "type": 1, "what": "collect", "unit_group": 10013, "units": [672], "count": 1, "item": 2585, "rate": 50, "maps": [121, 121, 121], "text_key": "Quest_QuickText_761_1_"}
  - {"n": 3, "type": 1, "what": "collect", "unit_group": 10014, "units": [673], "count": 1, "item": 2586, "rate": 50, "maps": [128, 128, 128], "text_key": "Quest_QuickText_761_2"}
  - {"n": 4, "type": 0, "what": "report", "text_key": "Quest_QuickText_F_FAREL"}
rewards:
  - {"type": 2, "what": "exp", "amount": 2400000, "shown": 2000000}
  - {"type": 1, "what": "item", "item": 641, "count": 1, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 8500, "count": 1, "pick": "choose", "e": 1}
  - {"type": 1, "what": "item", "item": 8506, "count": 1, "pick": "choose", "e": 1}
  - {"type": 1, "what": "item", "item": 8507, "count": 1, "pick": "choose", "e": 1}
offer_talk: 856
complete_talk: 857
---
<!-- generated:start -->
<!-- generated-keys: title=be7ff1 type=eb5b2b id=8d1218 sources=f2d583 name_key=d0da9d kind=356a19 kind_name=0bac50 level=a3b082 giver=65eab4 turn_in=65eab4 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=a17554 requires_bit=0a57cb prev=b891b8 next=4f2426 prerequisites=0ab6f2 stages=30caa7 objectives=6dad98 rewards=792da4 offer_talk=efe76d complete_talk=c44201 -->
|  |  |
|---|---|
|  | ![killed boss of Border area No.1](../assets/npcs/237.png) |
| **Quest id** | `761` |
| **Kind** | Sub (kind 1) |
| **Level** | 24+ |
| **Giver** | [[wiki/npcs/237-farrell\|Farrell]] |
| **Turn in** | [[wiki/npcs/237-farrell\|Farrell]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 63 |
| **Requires bit** | 28 |

### Chain

- **After:** [[wiki/quests/32-swamps-of-snake-warrior|Swamps of Snake Warrior]]
- **Next:** [[wiki/quests/756-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/762-killed-boss-of-border-area-no-2|killed boss of Border area No.2]]

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 24+ |

### Objectives

1. Collect [[wiki/items/2589-the-chepa-sorcerer-s-pipe|The Chepa Sorcerer's Pipe]] from any unit of kill group 10000 ([[wiki/monsters/870-chepa-sorcerer|Chepa Sorcerer]]) (drop 50%) — tracker: “Acquired Chepa Sorcerer's Pipe (0/1)” — on [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] (127)
2. Collect [[wiki/items/2585-the-death-head-s-pipe|The Death Head's Pipe]] from any unit of kill group 10013 ([[wiki/monsters/672-king-deathhead|King Deathhead]]) (drop 50%) — tracker: “Acquired Deathhead's Pipe (0/1)” — on [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] (121)
3. Collect [[wiki/items/2586-the-dark-knight-s-pipe|The Dark Knight's Pipe]] from any unit of kill group 10014 ([[wiki/monsters/673-dark-knight-skull|Dark Knight Skull]]) (drop 50%) — tracker: “Acquired Skull's Pipe (0/1)” — on [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] (128)
4. Report (tracker line; done by turning the quest in) — tracker: “Go to Farrell”

### Rewards

- **Basic reward:** 2,400,000 exp (shown in game as 2,000,000); [[wiki/items/641-rainbow-reinforcing-stone-weapon|Rainbow Reinforcing Stone (Weapon)]]
- **Choose one:** [[wiki/items/8500-crystal-dark-knight-skull|Crystal : Dark knight Skull]] (e = 1) *or* [[wiki/items/8506-crystal-king-deathhead|Crystal : King Deathhead]] (e = 1) *or* [[wiki/items/8507-crystal-tempest-fisher|Crystal : Tempest Fisher]] (e = 1)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 856)

Speaker: [[wiki/npcs/237-farrell|Farrell]]

> **Farrell:** There's something I'd like to have. Can you bring it? <br> The thing is... the Monster Kings have it~ Please bring it to me.  
> *(accept / continue)*

#### Completion (QuestTalk 857)

Speaker: [[wiki/npcs/237-farrell|Farrell]]

> **Farrell:** Oh, I brought the goods ~ I'll give you a great deal~ <br> You can use it to enhance your rating~  
> *(accept / continue)*
<!-- generated:end -->

## Notes

The guide screenshot of the quest window lists "killed boss of Border area No.3", a later quest of this series ([[gameplay/progression-and-economy]] §1, *image*).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/progression-and-economy]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
