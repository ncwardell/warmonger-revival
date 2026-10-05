---
title: "Aenes"
type: "npc"
id: 327
status: "partial"
missing: ["x", "z"]
sources: ["client: UnitDB.cdb id 327", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "client: Quest.cdb giver/receiver field (map only; no position)"]
name_key: "TitleName_35"
title_key: "UnitName_327"
npc_title: "The Oracle of Protection"
category: 50
class_mask: 2
model: 375
scale: 1.5
functions:
  - {"code": 39, "function": "move_to_temple", "label": "Move to Temple"}
role: "The Oracle of Protection"
talk_key: "Quest_Talk_Guadian_Oracle"
portrait: "ui/NPCProfile/Oracle_Aenes_Illust.dds"
quests: {"gives": [38], "receives": [37], "talk_objective": [41, 44, 692]}
quest_fields: [90, 94, 98]
map: 90
x: null
z: null
---
<!-- generated:start -->
<!-- generated-keys: title=80b189 type=3664ce id=076e5a sources=4350cb name_key=829565 title_key=97b127 npc_title=c75e8c category=e1822d class_mask=da4b92 model=348763 scale=aa8f28 functions=62c1e4 role=c75e8c talk_key=e79dbd portrait=32d74b quests=91841c quest_fields=18e60d map=2d0c8a x=2be88c z=2be88c -->
|  |  |
|---|---|
|  | ![Aenes](wiki/assets/npcs/327.png) |
| **Unit id** | `327` |
| **Title** | The Oracle of Protection |
| **Category** | NPC (category 50) |
| **Menu** | Move to Temple (`39`) |
| **Stands in** | [[wiki/fields/90-castle\|Castle]] (position unknown) |
| **Model** | ObjectList `375`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Oracle_Aenes_Illust.dds` |

### Greeting

> Do you want to go to the Temple? I will send you~

### Where it stands

No measured position yet. The client's quests put this NPC in [[wiki/fields/90-castle|Castle]], [[wiki/fields/94-castle|Castle]], [[wiki/fields/98-castle|Castle]] (giver/receiver fields, one per nation).

### Quests

- **Gives:** [[wiki/quests/38-innocence-s-recovery-operation|Innocence's recovery operation]]
- **Takes the turn-in of:** [[wiki/quests/37-call-tempest|Call Tempest]]
- **Must be talked to in:** [[wiki/quests/41-innocence-s-recovery-operation|Innocence's recovery operation]], [[wiki/quests/44-innocence-report|Innocence report]], [[wiki/quests/692-innocence-crystal|Innocence Crystal]]

### Other units with this name

The client has one unit row per placement or variant: [[wiki/npcs/328-aenes|Aenes (328)]].

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (6. Village (87/91/95), Castle (90/94/98), tutorial (117); 8. Still unplaced)
<!-- generated:end -->

## Notes

- Oracle of Protection; the client's quests put her in the Castle (90/94/98), but no position has been measured ([[gameplay/npc-locations|NPC locations]] §6, §8). *client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/npc-locations|NPC locations]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
