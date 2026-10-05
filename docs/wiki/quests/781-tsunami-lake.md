---
title: "Tsunami Lake"
type: "quest"
id: 781
status: "complete"
missing: []
sources: ["client: Quest.cdb id 781", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 864", "client: QuestTalk.cdb id 865", "client: QuestTalk.cdb id 896"]
name_key: "Quest_Title_781"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 84
requires_bit: 36
automatic: true
prev: [770]
next: [783, 784, 786]
stages: [4, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 99, "talk": 896, "maps": [120, 120, 120], "text_key": "Quest_QuickText_Area"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 122, "maps": [122, 122, 122], "text_key": "Quest_QuickText_749_0"}
  - {"n": 3, "type": 5, "what": "gadget", "gadget": 13, "talk": 865, "maps": [122, 122, 122], "text_key": "Quest_QuickText_781_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 110000, "shown": 100000}
offer_talk: 864
---
<!-- generated:start -->
<!-- generated-keys: title=b98456 type=eb5b2b id=c7e47b sources=5d9fb8 name_key=9272ec kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=847ad4 offer_maps=15f2a7 bit=be461a requires_bit=fc074d automatic=5ffe53 prev=d8e285 next=09f263 stages=17e0b1 objectives=0558e4 rewards=8974c1 offer_talk=de1592 -->
|  |  |
|---|---|
|  | ![Tsunami Lake](wiki/assets/npcs/200.png) |
| **Quest id** | `781` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 84 |
| **Requires bit** | 36 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/770-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** [[wiki/quests/783-swamps-of-the-snake-warrior|Swamps of the Snake Warrior]], [[wiki/quests/784-swamps-of-the-snake-warrior|Swamps of the Snake Warrior]], [[wiki/quests/786-mushrooms-in-the-komodo-area|Mushrooms in the Komodo area]]
- **Shares completion bit 84 with:** [[wiki/quests/782-tsunami-lake|Tsunami Lake]] (completing one closes the others)

### Objectives

1. Talk to Dimension Gate (dialogue 896) — tracker: “Go to Dimension Gate”
2. Go to [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122) — tracker: “Go to the Tsunami Lake” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
3. Talk to [[wiki/nodes/12213-a-doubtful-character|A Doubtful character]] (gadget 13) (dialogue 865) — tracker: “Find A doubtful character” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)

Stages (`flag1..5` = [4, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 110,000 exp (shown in game as 100,000)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 864)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** There's a rumor that there's a suspicious person coming out of Tsunami Lake. Go meet him.  
> *(accept / continue)*

#### Objective 1 (QuestTalk 896)

Speaker: NPC

> *(end)*

#### Objective 3 (QuestTalk 865)

Speaker: [[wiki/nodes/12213-a-doubtful-character|A Doubtful character]] (gadget 13)

> **You:** Who are you? I heard you keep going to the Tsunami Lake these days. Is that you? You'r suspicious. Identify yourself!  
> **A Doubtful character:** Who's there? I only came and went once or twice! Now then, who are you ??  
> **You:** I'm the Keeper.  
> **A Doubtful character:** You? If you're Keeper, prove it! If you can get rid of the Fisher here, I can trust you.  
> *(accept / continue)*

### Mentioned in

- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/npc-locations|NPC and point-of-interest locations]]
- [[gameplay/patch-history|Patch notes and other sources]]
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
