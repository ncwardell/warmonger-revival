---
title: "legion - Create Core"
type: "quest"
id: 1530
status: "stub"
missing: ["turn_in"]
sources: ["client: Quest.cdb id 1530", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "client: QuestTalk.cdb id 844", "client: QuestTalk.cdb id 845"]
name_key: "Quest_Title_Help_774"
kind: 12
kind_name: "Advice"
giver: {"auto": true}
turn_in: null
bit: 80
prev: []
next: [705]
stages: [1, 2, 3, 5, 5]
objectives:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 90, "maps": [90, 90, 90], "text_key": "Quest_QuickText_Help_774_1"}
  - {"n": 2, "type": 4, "what": "talk", "npc": 242, "talk": 844, "maps": [90, 90, 90], "text_key": "Quest_QuickText_Help_774_2"}
  - {"n": 3, "type": 11, "what": "craft_item", "item": 1401, "count": 1, "maps": [90, 90, 90], "text_key": "Quest_QuickText_Help_774_3"}
  - {"n": 4, "type": 4, "what": "talk", "npc": 242, "talk": 845, "maps": [90, 90, 90]}
rewards: []
help: {"text_key": "Quest_Title_Help_String_774"}
---
<!-- generated:start -->
<!-- generated-keys: title=606601 type=eb5b2b id=0ad54e sources=7b67f5 name_key=031816 kind=7b5200 kind_name=ec7dd4 giver=847ad4 turn_in=2be88c bit=b888b2 prev=97d170 next=46b74f stages=0f733e objectives=45d1cf rewards=97d170 help=d6955c -->
|  |  |
|---|---|
| **Quest id** | `1530` |
| **Kind** | Advice (kind 12) |
| **Giver** | automatic |
| **Turn in** | **unknown** |
| **Completion bit** | 80 |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** [[wiki/quests/705-legion-how-to-use-add-on|Legion - How to use add-on]]
- **Shares completion bit 80 with:** [[wiki/quests/774-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]], [[wiki/quests/775-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]], [[wiki/quests/776-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]] (completing one closes the others)

### Objectives

1. Go to [[wiki/fields/90-castle|Castle]] (90) — tracker: “Move to castle” — on [[wiki/fields/90-castle|Castle]] (90)
2. Talk to [[wiki/npcs/242-raon|Raon]] (dialogue 844) — tracker: “Making legion cores through NPC raon” — on [[wiki/fields/90-castle|Castle]] (90)
3. Craft [[wiki/items/1401-siege-minion|Siege Minion]] — tracker: “Core installed through legion core window” — on [[wiki/fields/90-castle|Castle]] (90)
4. Talk to [[wiki/npcs/242-raon|Raon]] (dialogue 845) — on [[wiki/fields/90-castle|Castle]] (90)

Stages (`flag1..5` = [1, 2, 3, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

None in the client.

### Dialogue

#### Objective 2 (QuestTalk 844)

Speaker: [[wiki/npcs/242-raon|Raon]]

> **You:** I came to listen to Legion Manager Kesley. I heard that you can build Legion Cores.  
> **Raon:** Kesley? You found me! Which Core would you like to produce? Take a look around!  
> *(end)*

#### Objective 4 (QuestTalk 845)

Speaker: [[wiki/npcs/242-raon|Raon]]

> **Raon:** Did you produce what you wanted? Good use of Cores will be very beneficial for war! Try it!  
> *(accept / continue)*

### Tip window

> You can build legion cores through NPC raons in your nature and mount them through the legion core window. &lt;N&gt; You can use TP skills on the cores attached to the core when equipped with cores.
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
