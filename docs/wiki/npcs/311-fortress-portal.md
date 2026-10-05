---
title: "Fortress Portal"
type: "npc"
id: 311
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 311", "gameplay/npc-locations §3", "guide: [[gameplay/maps-and-dungeons]] §1 (noob guide): the bottom-right Fortress portal sends you to a dungeon matched to your level"]
manual: ["teleport_to"]
name_key: "UnitName_311"
category: 50
class_mask: 2
model: 3009
scale: 3.0
functions:
  - {"code": 4, "function": "teleport", "label": "Teleport"}
role: "Teleport"
map: 120
x: 1981.0
z: 1561.0
positions:
  - {"field": 120, "x": 1981.0, "z": 1561.0, "source": "gameplay/npc-locations §3", "confidence": "image + guide"}
  - {"field": 120, "x": 2237.0, "z": 1561.0, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2493.0, "z": 1561.0, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
teleport_to: [{"name": "Dungeon matched to the player's level"}]
---
<!-- generated:start -->
<!-- generated-keys: title=fb0229 type=3664ce id=cd6d91 sources=3f455d name_key=6cc383 category=e1822d class_mask=da4b92 model=269f4f scale=bdc140 functions=b85d7e role=6b2147 map=775bc5 x=9154fe z=09f217 positions=5aa78b teleport_to=2be88c -->
|  |  |
|---|---|
| **Unit id** | `311` |
| **Role** | Teleport |
| **Category** | NPC (category 50) |
| **Menu** | Teleport (`4`) |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1981.0, 1561.0) |
| **Model** | ObjectList `3009`, scale 3.0 |

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1981.0 | 1561.0 | image + guide | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2237.0 | 1561.0 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2493.0 | 1561.0 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 51:25 (1. Map order)
<!-- generated:end -->

## Notes

- The portal in the south-east (bottom-right) of the Fortress sends the player to a dungeon that matches the player's level ([[gameplay/maps-and-dungeons|Maps and dungeons]] §1, noob guide). *guide*
- On the minimap it is the blue portal icon just south of Freya, at the top of the long tail toward the south-east ([[gameplay/precept-shop|Precept shop]] §5). *image*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/precept-shop|Precept shop]]
- [[gameplay/video-early-quests|Video notes: first session]]

## Open questions

- The guides do not name the destination fields, so `teleport_to` has no field ids. How the level is matched to a dungeon is unknown.
- In [[gameplay/video-early-quests|Video notes: first session]] §1 the player reached Place for Scattered troops (103) from the Fortress at [51:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=3085s), by this portal or by Haley's "Abyss" option. The notes do not say which.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
