---
title: "Tsunami Lake"
type: "quest"
id: 782
status: "complete"
missing: []
sources: ["client: Quest.cdb id 782", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 867", "client: QuestTalk.cdb id 868"]
name_key: "Quest_Title_781"
kind: 0
kind_name: "Main"
giver: {"auto": true}
turn_in: {"npc": 200}
turn_in_maps: [120, 120, 120]
bit: 84
requires_bit: 36
prev: [770]
next: [783, 784, 786]
stages: [4, 4, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "unit": 644, "count": 20, "maps": [122, 122, 122], "text_key": "Quest_QuickText_650_1"}
  - {"n": 2, "type": 1, "what": "kill", "unit": 645, "count": 10, "maps": [122, 122, 122], "text_key": "Quest_QuickText_650_2"}
  - {"n": 3, "type": 5, "what": "gadget", "gadget": 14, "talk": 867, "maps": [122, 122, 122], "text_key": "Quest_QuickText_781_5"}
  - {"n": 4, "type": 0, "what": "report", "text_key": "Quest_QuickText_R_FREYA"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1000000, "shown": 909091}
  - {"type": 1, "what": "item", "item": 688, "count": 4, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 601, "count": 100, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 100, "pick": "fixed"}
complete_talk: 868
---
<!-- generated:start -->
<!-- generated-keys: title=b98456 type=eb5b2b id=281785 sources=11c79c name_key=9272ec kind=b6589f kind_name=b3f808 giver=847ad4 turn_in=1caac0 turn_in_maps=15f2a7 bit=be461a requires_bit=fc074d prev=d8e285 next=09f263 stages=66d7ee objectives=54aeeb rewards=012df3 complete_talk=0b93ca -->
|  |  |
|---|---|
| **Quest id** | `782` |
| **Kind** | Main (kind 0) |
| **Giver** | automatic |
| **Turn in** | [[wiki/npcs/200-freya\|Freya]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 84 |
| **Requires bit** | 36 |

### Chain

- **After:** [[wiki/quests/770-group-border-area-hard-mode|Group - Border Area Hard Mode]]
- **Next:** [[wiki/quests/783-swamps-of-the-snake-warrior|Swamps of the Snake Warrior]], [[wiki/quests/784-swamps-of-the-snake-warrior|Swamps of the Snake Warrior]], [[wiki/quests/786-mushrooms-in-the-komodo-area|Mushrooms in the Komodo area]]
- **Shares completion bit 84 with:** [[wiki/quests/781-tsunami-lake|Tsunami Lake]] (completing one closes the others)

### Objectives

1. Kill [[wiki/monsters/644-fisher|Fisher]] × 20 — tracker: “Kill Fisher (0/20)” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
2. Kill [[wiki/monsters/645-elite-fisher|Elite Fisher]] × 10 — tracker: “Kill Elite Fisher (0/10)” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
3. Talk to [[wiki/nodes/12214-a-doubtful-character|A Doubtful character]] (gadget 14) (dialogue 867) — tracker: “Talk A doubtful character” — on [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] (122)
4. Report (tracker line; done by turning the quest in) — tracker: “Talk to Freya”

Stages (`flag1..5` = [4, 4, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 1,000,000 exp (shown in game as 909,091); [[wiki/items/688-dimensional-energy|Dimensional energy]] × 4; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 100; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 100

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Objective 3 (QuestTalk 867)

Speaker: [[wiki/nodes/12214-a-doubtful-character|A Doubtful character]] (gadget 14)

> **You:** Do you believe it now? Then tell me who you are!  
> **A Doubtful character:** If there's a connection, we will know some day. See you later.

#### Completion (QuestTalk 868)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **You:** I saw a suspicious man, as you said. he was wearing a strange robe with a golden motif.  
> **Freya:** Gold patterns? Then... I think it's them.  
> **You:** Do you know who that is?  
> **Freya:** I'll let you know when it's time. It won't be long.  
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
