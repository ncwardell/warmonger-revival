---
title: "Owen"
type: "npc"
id: 337
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 337", "gameplay/npc-locations §4", "gameplay/video-tutorial-walkthrough §2"]
name_key: "TitleName_11"
title_key: "UnitName_214"
npc_title: "Member of Red Union"
category: 50
class_mask: 2
model: 297
scale: 1.5
functions:
  - {"code": 3, "function": "craft", "label": "Create"}
role: "Member of Red Union"
shop: 8
talk_key: "Quest_Talk_Default_Red"
portrait: "ui/NPCProfile/Quest_RedFlames.dds"
map: 88
x: 393.7
z: 3470.4
positions:
  - {"field": 88, "x": 393.7, "z": 3470.4, "source": "gameplay/npc-locations §4", "confidence": "video"}
  - {"field": 88, "x": 392.3, "z": 3475.1, "source": "gameplay/video-tutorial-walkthrough §2", "confidence": "video", "seen": ["20:05"]}
  - {"field": 92, "x": 649.7, "z": 3470.4, "source": "derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 96, "x": 905.7, "z": 3470.4, "source": "derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=2a0552 type=3664ce id=0588f5 sources=91f6be name_key=47bcc5 title_key=9f8371 npc_title=1bd231 category=e1822d class_mask=da4b92 model=dd500e scale=aa8f28 functions=7d0bc3 role=1bd231 shop=fe5dbb talk_key=12d6a8 portrait=7348e7 map=b37f6d x=f85af8 z=37c15b positions=f098d0 -->
|  |  |
|---|---|
|  | ![Owen](wiki/assets/npcs/337.png) |
| **Unit id** | `337` |
| **Title** | Member of Red Union |
| **Category** | NPC (category 50) |
| **Menu** | Create (`3`) |
| **Shop** | [[wiki/shops/8-owen-s-shop-member-of-red-union\|Owen's shop (Member of Red Union)]] |
| **Stands in** | [[wiki/fields/88-training-camp\|Training Camp]] at (393.7, 3470.4) |
| **Model** | ObjectList `297`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Quest_RedFlames.dds` |

### Greeting

> Hello. Do you need anything? Take your time and look around.

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/88-training-camp\|Training Camp]] | 393.7 | 3470.4 | video | [[gameplay/npc-locations\|npc-locations]] §4 |
| [[wiki/fields/88-training-camp\|Training Camp]] | 392.3 | 3475.1 | video | [[gameplay/video-tutorial-walkthrough\|video-tutorial-walkthrough]] §2 at 20:05 |
| [[wiki/fields/92-training-camp\|Training Camp]] | 649.7 | 3470.4 | derived | derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/96-training-camp\|Training Camp]] | 905.7 | 3470.4 | derived | derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2) |

### Shop

Sells 25 items (`Npc_Carry` row 8; full list on [[wiki/shops/8-owen-s-shop-member-of-red-union|Owen's shop (Member of Red Union)]]): [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]], [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]], [[wiki/items/1900-faded-passion-fragments|Faded Passion fragments]], [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]], [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]], [[wiki/items/1900-faded-passion-fragments|Faded Passion fragments]], [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]], [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]], [[wiki/items/1900-faded-passion-fragments|Faded Passion fragments]], [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]], [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]], [[wiki/items/1900-faded-passion-fragments|Faded Passion fragments]] ….

### Other units with this name

The client has one unit row per placement or variant: [[wiki/npcs/214-owen|Owen (214)]], [[wiki/npcs/314-owen|Owen (314)]].

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (4. Training Camp (fields 88 / 92 / 96))
- [[gameplay/consumables|Consumables and clickables]] (4. Recipes (Owen, Red Union))
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 48:20, 48:40, 49:20, 50:05 (3. NPCs)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] at 20:05 (2. NPC positions)
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
