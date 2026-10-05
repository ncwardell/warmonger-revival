---
title: "Swamps of the Snake Warrior"
type: "quest"
id: 784
status: "complete"
missing: []
sources: ["client: Quest.cdb id 784", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 871", "client: QuestTalk.cdb id 876"]
name_key: "Quest_Title_782"
kind: 0
kind_name: "Main"
giver: {"auto": true}
turn_in: {"npc": 200}
turn_in_maps: [120, 120, 120]
bit: 85
requires_bit: 84
prev: [781, 782]
next: [37, 106]
stages: [1, 2, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "unit": 81, "count": 1, "maps": [123, 123, 123], "text_key": "Quest_QuickText_782_3"}
  - {"n": 2, "type": 5, "what": "gadget", "gadget": 17, "talk": 876, "maps": [123, 123, 123], "text_key": "Quest_QuickText_782_4"}
  - {"n": 3, "type": 0, "what": "report", "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1100000, "shown": 1000000}
  - {"type": 1, "what": "item", "item": 688, "count": 4, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 621, "count": 5, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 7062, "count": 1, "pick": "choose"}
  - {"type": 1, "what": "item", "item": 7072, "count": 1, "pick": "choose"}
complete_talk: 871
---
<!-- generated:start -->
<!-- generated-keys: title=cc1830 type=eb5b2b id=aa5076 sources=b6eba3 name_key=16edee kind=b6589f kind_name=b3f808 giver=847ad4 turn_in=1caac0 turn_in_maps=15f2a7 bit=135224 requires_bit=be461a prev=49296a next=e29c34 stages=642aaf objectives=ab6d2e rewards=b06af0 complete_talk=edc10c -->
|  |  |
|---|---|
| **Quest id** | `784` |
| **Kind** | Main (kind 0) |
| **Giver** | automatic |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 85 |
| **Requires bit** | 84 |

### Chain

- **After:** [[wiki/quests/781-tsunami-lake|Tsunami Lake]], [[wiki/quests/782-tsunami-lake|Tsunami Lake]]
- **Next:** [[wiki/quests/37-call-tempest|Call Tempest]], [[wiki/quests/106-talk-to-krister|Talk to Krister]]
- **Shares completion bit 85 with:** [[wiki/quests/783-swamps-of-the-snake-warrior|Swamps of the Snake Warrior]] (completing one closes the others)

### Objectives

1. Kill [[wiki/npcs/81-transmission-equipment|Transmission equipment]] × 1 — tracker: “Destroy the Transmission equipment” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
2. Talk to [[wiki/nodes/12317-a-doubtful-character|A Doubtful character]] (gadget 17) (dialogue 876) — tracker: “Talk A doubtful character” — on [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] (123)
3. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

Stages (`flag1..5` = [1, 2, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 1,100,000 exp (shown in game as 1,000,000); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 4; [[wiki/items/621-orange-passion-fragments-d|Orange Passion Fragments (D)]] × 5
- **Choose one:** [[wiki/items/7062-health-regeneration-rune|Health Regeneration Rune]] *or* [[wiki/items/7072-mana-regeneration-rune|Mana Regeneration Rune]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Objective 2 (QuestTalk 876)

Speaker: [[wiki/nodes/12317-a-doubtful-character|A Doubtful character]] (gadget 17)

> **You:** You can go out through the portal here.. See you later  
> *(accept / continue)*  
> *(accept / continue)*

#### Completion (QuestTalk 871)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **You:** She was down in theSwamps of Snake Warrior. <br> Now that you've helped me, let me know.  
> *(accept / continue)*  
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
