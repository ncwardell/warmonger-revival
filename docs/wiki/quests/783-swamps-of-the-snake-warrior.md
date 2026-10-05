---
title: "Swamps of the Snake Warrior"
type: "quest"
id: 783
status: "complete"
missing: []
sources: ["client: Quest.cdb id 783", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 869", "client: QuestTalk.cdb id 877", "client: QuestTalk.cdb id 896"]
name_key: "Quest_Title_782"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 85
requires_bit: 84
automatic: true
prev: [781, 782]
next: [37, 106]
stages: [4, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 99, "talk": 896, "maps": [120, 120, 120], "text_key": "Quest_QuickText_Area"}
  - {"n": 2, "type": 12, "what": "reach_map", "map": 123, "maps": [123, 123, 123], "text_key": "Quest_QuickText_782_1"}
  - {"n": 3, "type": 5, "what": "gadget", "gadget": 16, "talk": 869, "maps": [123, 123, 123], "text_key": "Quest_QuickText_782_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 120000, "shown": 109091}
offer_talk: 877
---
<!-- generated:start -->
<!-- generated-keys: title=cc1830 type=eb5b2b id=43095d sources=53ee05 name_key=16edee kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=847ad4 offer_maps=15f2a7 bit=135224 requires_bit=be461a automatic=5ffe53 prev=49296a next=e29c34 stages=17e0b1 objectives=68a119 rewards=a843e5 offer_talk=d24b13 -->
|  |  |
|---|---|
|  | ![Swamps of the Snake Warrior](wiki/assets/npcs/200.png) |
| **Quest id** | `783` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 85 |
| **Requires bit** | 84 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/781-tsunami-lake|Tsunami Lake]], [[wiki/quests/782-tsunami-lake|Tsunami Lake]]
- **Next:** [[wiki/quests/37-call-tempest|Call Tempest]], [[wiki/quests/106-talk-to-krister|Talk to Krister]]
- **Shares completion bit 85 with:** [[wiki/quests/784-swamps-of-the-snake-warrior|Swamps of the Snake Warrior]] (completing one closes the others)

### Objectives

1. Talk to Dimension Gate (dialogue 896) — tracker: “Go to Dimension Gate”
2. Go to [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123) — tracker: “Go to the Swamps of the Snake Warrior” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
3. Talk to [[wiki/nodes/12316-a-doubtful-character|A Doubtful character]] (gadget 16) (dialogue 869) — tracker: “Find A doubtful character” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)

Stages (`flag1..5` = [4, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 120,000 exp (shown in game as 109,091)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 877)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** It's time for you to know. They're doing secret mission now. if you help they. I'll tell you everything  
> *(accept / continue)*  
> *(accept / continue)*

#### Objective 1 (QuestTalk 896)

Speaker: NPC

> *(end)*

#### Objective 3 (QuestTalk 869)

Speaker: [[wiki/nodes/12316-a-doubtful-character|A Doubtful character]] (gadget 16)

> **You:** Hey, guys. Wake up!  
> **A Doubtful character:** Hmm … who are you?  
> **You:** I am the Keeper who came here after hearing from the OracleI was asked to help you with your mission.  
> **A Doubtful character:** Ah! You're the Keeper. Well, I'm lucky to have you here.  
> **A Doubtful character:** I'm sorry, but I was seriously injured doing the mission here. <br> Could you bring me out?  
> *(accept / continue)*

### Mentioned in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]]
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]]
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
