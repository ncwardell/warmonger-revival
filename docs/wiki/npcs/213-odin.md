---
title: "Odin"
type: "npc"
id: 213
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 213", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §3"]
name_key: "TitleName_10"
title_key: "UnitName_213"
npc_title: "Member of Blue Union"
category: 50
class_mask: 2
model: 187
scale: 1.3
functions:
  - {"code": 20, "function": "craft", "label": "Create"}
role: "Member of Blue Union"
talk_key: "Quest_Talk_Default_Blue"
portrait: "ui/NPCProfile/Quest_MetalPartner.dds"
quests: {"gives": [110, 726, 728, 730, 734, 739, 741, 743, 746], "receives": [110, 726, 728, 730, 734, 739, 741, 746, 1033, 1041], "talk_objective": [780, 1033, 1036, 1037, 1041]}
quest_fields: [120]
map: 120
x: 1991.9
z: 1703.6
positions:
  - {"field": 120, "x": 1991.9, "z": 1703.6, "source": "gameplay/npc-locations §3", "confidence": "video"}
  - {"field": 120, "x": 2247.9, "z": 1703.6, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2503.9, "z": 1703.6, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=aa5e60 type=3664ce id=19187d sources=a43186 name_key=239d7b title_key=27670d npc_title=8543b1 category=e1822d class_mask=da4b92 model=f67462 scale=2afe7d functions=8b6f7e role=8543b1 talk_key=8dc755 portrait=a30bd7 quests=e41896 quest_fields=6c3da9 map=775bc5 x=37114f z=da850b positions=89ff24 -->
|  |  |
|---|---|
|  | ![Odin](../assets/npcs/213.png) |
| **Unit id** | `213` |
| **Title** | Member of Blue Union |
| **Category** | NPC (category 50) |
| **Menu** | Create (`20`) |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1991.9, 1703.6) |
| **Model** | ObjectList `187`, scale 1.3 |
| **Portrait** | `ui/NPCProfile/Quest_MetalPartner.dds` |

### Greeting

> If you want to get stronger, you need better Gears. 
> You can create them with my help.

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1991.9 | 1703.6 | video | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2247.9 | 1703.6 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2503.9 | 1703.6 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Quests

- **Gives:** [[wiki/quests/110-gear-manufacturing|Gear manufacturing]], [[wiki/quests/726-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/728-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/730-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/734-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/739-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/741-collecting-material|Collecting material]], [[wiki/quests/743-demon-hell|Demon Hell]], [[wiki/quests/746-devil-s-material|Devil's material]]
- **Takes the turn-in of:** [[wiki/quests/110-gear-manufacturing|Gear manufacturing]], [[wiki/quests/726-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/728-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/730-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/734-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/739-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/741-collecting-material|Collecting material]], [[wiki/quests/746-devil-s-material|Devil's material]], [[wiki/quests/1033-tow-canyon-collecting-material|Tow Canyon : Collecting material]], [[wiki/quests/1041-thorn-s-hell-hunting|Thorn's Hell : Hunting]]
- **Must be talked to in:** [[wiki/quests/780-bring-the-demon-crystals|Bring the Demon Crystals]], [[wiki/quests/1033-tow-canyon-collecting-material|Tow Canyon : Collecting material]], [[wiki/quests/1036-demon-hell-hunting|Demon Hell : Hunting]], [[wiki/quests/1037-demon-hell-hunting|Demon Hell : Hunting]], [[wiki/quests/1041-thorn-s-hell-hunting|Thorn's Hell : Hunting]]

Dialogue rows (`QuestTalk`; full text on the quest pages):

| quest | QuestTalk | speaker | first line |
|---|---|---|---|
| [[wiki/quests/739-gathering-plant-and-ore\|Gathering plant and ore]] | 756 | Odin : Blue Union | Do you have the materials I asked for? |
| [[wiki/quests/743-demon-hell\|Demon Hell]] | 760 | Odin : Blue Union | Do you have the materials I asked for? |
| [[wiki/quests/780-bring-the-demon-crystals\|Bring the Demon Crystals]] | 760 | Odin : Blue Union | Do you have the materials I asked for? |

### Other units with this name

The client has one unit row per placement or variant: [[wiki/npcs/313-odin|Odin (313)]], [[wiki/npcs/335-odin|Odin (335)]].

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 42:35, 48:20, 48:40, 49:20, 50:05 (Fortress (levels 12–20); 3. NPCs)
<!-- generated:end -->

## Notes

- Blue Union crafter for gear (armour and accessories) in the east arm of the Fortress ([[gameplay/npc-locations|NPC locations]] §3; [[gameplay/maps-and-dungeons|Maps and dungeons]] §5). Life gear costs 0 gold to craft and Honor / Rise gear 15,000 gold ([[gameplay/video-early-quests|Video notes: first session]] §3). *video*
- Normal gear takes 10–30 Blue Crystals per piece, for example Ring of Spell for 10 Blue Crystals and 15,000 gold ([[gameplay/items-and-crafting|Items and crafting]] §3). Courage and Rise gear can only be crafted here, never dropped ([[gameplay/items-and-crafting|Items and crafting]] §1). *guide*

## Behaviour

- Quest 110 "Gear manufacturing": craft one piece of gear here; the panel shows 10,000 exp and 30,000 gold ([[gameplay/video-early-quests|Video notes: first session]] §2 step 19, [42:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=2555s)). *video*
- A Crush-era screenshot shows his repeat quest "Destroy the hell of demon" (10 Demon Hunters and 10 Elite Demon Hunters) ([[gameplay/lords-of-the-land|Lords of the Land]] §5). A repeatable Refined Oils quest unlocks after an Odin quest that asks for 2 Garnet and 2 Bloodstone ([[gameplay/warmonger-forum|Warmonger forum]] §4). *image / forum*

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/npc-locations|NPC locations]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/video-early-quests|Video notes: first session]]
- [[gameplay/items-and-crafting|Items and crafting]]
- [[gameplay/lords-of-the-land|Lords of the Land]]
- [[gameplay/warmonger-forum|Warmonger forum]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
