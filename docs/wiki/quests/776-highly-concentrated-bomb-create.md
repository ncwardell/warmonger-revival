---
title: "Highly Concentrated Bomb Create"
type: "quest"
id: 776
status: "complete"
missing: []
sources: ["client: Quest.cdb id 776", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 842", "client: QuestTalk.cdb id 843", "client: QuestTalk.cdb id 844", "client: QuestTalk.cdb id 845"]
name_key: "Quest_Title_774"
kind: 1
kind_name: "Sub"
giver: {"npc": 210}
turn_in: {"npc": 210}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 80
requires_bit: 101
prev: [753, 1526]
next: [705]
prerequisites:
  - {"type": 7, "what": "legion?", "a": 4, "b": 2}
  - {"type": 3, "what": null, "a": 3}
stages: [1, 2, 3, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 242, "talk": 844, "maps": [120, 120, 120], "text_key": "Quest_QuickText_774_2"}
  - {"n": 2, "type": 11, "what": "craft_item", "item": 1408, "count": 1, "maps": [120, 120, 120], "text_key": "Quest_QuickText_774_3"}
  - {"n": 3, "type": 4, "what": "talk", "npc": 242, "talk": 845, "maps": [120, 120, 120], "text_key": "Quest_QuickText_774_2"}
  - {"n": 4, "type": 0, "what": "report", "text_key": "Quest_QuickText_650_3"}
rewards:
  - {"type": 2, "what": "exp", "amount": 3000, "shown": 2500}
offer_talk: 842
complete_talk: 843
---
<!-- generated:start -->
<!-- generated-keys: title=953445 type=eb5b2b id=0aed85 sources=e2fd63 name_key=b65f8a kind=356a19 kind_name=0bac50 giver=7abdb8 turn_in=7abdb8 offer_maps=15f2a7 turn_in_maps=15f2a7 bit=b888b2 requires_bit=dbc0f0 prev=efaebd next=46b74f prerequisites=46da25 stages=0f733e objectives=470ba8 rewards=f31fb4 offer_talk=62362f complete_talk=c02b74 -->
|  |  |
|---|---|
|  | ![Highly Concentrated Bomb Create](../assets/npcs/210.png) |
| **Quest id** | `776` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 80 |
| **Requires bit** | 101 |

### Chain

- **After:** [[wiki/quests/753-join-the-legion|Join the Legion]], [[wiki/quests/1526-legion-invite-or-join|legion - Invite or join]]
- **Next:** [[wiki/quests/705-legion-how-to-use-add-on|Legion - How to use add-on]]
- **Shares completion bit 80 with:** [[wiki/quests/774-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]], [[wiki/quests/775-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]], [[wiki/quests/1530-legion-create-core|legion - Create Core]] (completing one closes the others)

### Requirements

| type | meaning | value |
|---|---|---|
| 7 | legion? | a=4, b=2 |
| 3 | unknown | a=3 |

### Objectives

1. Talk to [[wiki/npcs/242-raon|Raon]] (dialogue 844) — tracker: “Go to Raon”
2. Craft [[wiki/items/1408-highly-concentrated-bomb|Highly Concentrated Bomb]] — tracker: “Creating a Highly Concentrated Bomb through Raon”
3. Talk to [[wiki/npcs/242-raon|Raon]] (dialogue 845) — tracker: “Go to Raon”
4. Report (tracker line; done by turning the quest in) — tracker: “Return to Kesley”

Stages (`flag1..5` = [1, 2, 3, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 3,000 exp (shown in game as 2,500)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 842)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** Let me tell you about the legion Core! You can use the legion core to add strategic skills that you can use in the war. <br> If you install a good core, it will be advantageous in war. <br> Go to Raon in Castle  
> *(accept / continue)*

#### Objective 1 (QuestTalk 844)

Speaker: [[wiki/npcs/242-raon|Raon]]

> **You:** I came to listen to Legion Manager Kesley. I heard that you can build Legion Cores.  
> **Raon:** Kesley? You found me! Which Core would you like to produce? Take a look around!  
> *(end)*

#### Objective 3 (QuestTalk 845)

Speaker: [[wiki/npcs/242-raon|Raon]]

> **Raon:** Did you produce what you wanted? Good use of Cores will be very beneficial for war! Try it!  
> *(accept / continue)*

#### Completion (QuestTalk 843)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** Have you seen Raon? I hope you win the war with various Cores~  
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
