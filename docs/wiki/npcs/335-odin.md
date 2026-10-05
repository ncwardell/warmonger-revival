---
title: "Odin"
type: "npc"
id: 335
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 335", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §4", "gameplay/video-tutorial-walkthrough §2"]
name_key: "TitleName_10"
title_key: "UnitName_213"
npc_title: "Member of Blue Union"
category: 50
class_mask: 2
model: 187
scale: 1.3
functions:
  - {"code": 3, "function": "craft", "label": "Create"}
role: "Member of Blue Union"
shop: 6
talk_key: "Quest_Talk_Default_Blue"
portrait: "ui/NPCProfile/Quest_MetalPartner.dds"
quests: {"gives": [101], "receives": [101]}
quest_fields: [88, 92, 96]
map: 88
x: 387.1
z: 3478.9
positions:
  - {"field": 88, "x": 387.1, "z": 3478.9, "source": "gameplay/npc-locations §4", "confidence": "video"}
  - {"field": 88, "x": 385.9, "z": 3478.8, "source": "gameplay/video-tutorial-walkthrough §2", "confidence": "video"}
  - {"field": 92, "x": 643.1, "z": 3478.9, "source": "derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 96, "x": 899.1, "z": 3478.9, "source": "derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=aa5e60 type=3664ce id=4728a2 sources=68d296 name_key=239d7b title_key=27670d npc_title=8543b1 category=e1822d class_mask=da4b92 model=f67462 scale=2afe7d functions=7d0bc3 role=8543b1 shop=c1dfd9 talk_key=8dc755 portrait=a30bd7 quests=ad1cbc quest_fields=46bf0f map=b37f6d x=187cc9 z=202cb5 positions=b73861 -->
|  |  |
|---|---|
|  | ![Odin](../assets/npcs/335.png) |
| **Unit id** | `335` |
| **Title** | Member of Blue Union |
| **Category** | NPC (category 50) |
| **Menu** | Create (`3`) |
| **Shop** | [[wiki/shops/6-odin-s-shop-member-of-blue-union\|Odin's shop (Member of Blue Union)]] |
| **Stands in** | [[wiki/fields/88-training-camp\|Training Camp]] at (387.1, 3478.9) |
| **Model** | ObjectList `187`, scale 1.3 |
| **Portrait** | `ui/NPCProfile/Quest_MetalPartner.dds` |

### Greeting

> If you want to get stronger, you need better Gears. 
> You can create them with my help.

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/88-training-camp\|Training Camp]] | 387.1 | 3478.9 | video | [[gameplay/npc-locations\|npc-locations]] §4 |
| [[wiki/fields/88-training-camp\|Training Camp]] | 385.9 | 3478.8 | video | [[gameplay/video-tutorial-walkthrough\|video-tutorial-walkthrough]] §2 |
| [[wiki/fields/92-training-camp\|Training Camp]] | 643.1 | 3478.9 | derived | derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/96-training-camp\|Training Camp]] | 899.1 | 3478.9 | derived | derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2) |

### Shop

Sells 25 items (`Npc_Carry` row 6; full list on [[wiki/shops/6-odin-s-shop-member-of-blue-union|Odin's shop (Member of Blue Union)]]): [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]], [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]], [[wiki/items/1900-faded-passion-fragments|Faded Passion fragments]], [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]], [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]], [[wiki/items/1900-faded-passion-fragments|Faded Passion fragments]], [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]], [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]], [[wiki/items/1900-faded-passion-fragments|Faded Passion fragments]], [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]], [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]], [[wiki/items/1900-faded-passion-fragments|Faded Passion fragments]] ….

### Quests

- **Gives:** [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]
- **Takes the turn-in of:** [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]

### Other units with this name

The client has one unit row per placement or variant: [[wiki/npcs/213-odin|Odin (213)]], [[wiki/npcs/313-odin|Odin (313)]].

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (4. Training Camp (fields 88 / 92 / 96))
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] at 15:55 (Training Camp (field 92) and back)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 22:45, 36:10, 48:20, 48:40, 49:20, 50:05 (Training Ground and Camp (levels 1–11); 3. NPCs)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] at 29:30 (Steps; 2. NPC positions)
<!-- generated:end -->

## Notes

- Training Camp Odin. His menu is Quest / Create / Close ([[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough]] step 26). His craft list (6) is a copy of the Fortress list, category 0 ([[gameplay/consumables|Consumables]] §4). *video + client*

## Behaviour

- Side quest 101 "All sorts of Fragile bones": 10 Weak Skeleton bone and 10 Weak Elite Skeleton bone from the skeletons in Corpse incineration (kill groups 10003 / 10004). The panel shows 14,500 exp (table 17,400), 10,000 gold and 10 Crystal: Blue, then Spell Belt (398) or Belt of Life (406) ([[gameplay/video-early-quests|Video notes: first session]] §2 step 10, [22:48](https://www.youtube.com/watch?v=s04CSN16w1s&t=1368s); [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough]] step 26, [29:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1770s); [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial]] step 18). *video*

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough]]
- [[gameplay/consumables|Consumables]]
- [[gameplay/video-early-quests|Video notes: first session]]
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
