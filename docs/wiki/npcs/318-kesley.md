---
title: "Kesley"
type: "npc"
id: 318
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 318", "video: [[gameplay/video-early-quests]] §3 at 59:00, Castle (90) Kesley, ±5; the notes give the unit as '210 (318?)', so the match to 318 is a guess"]
manual: ["map", "x", "z"]
name_key: "TitleName_5"
title_key: "UnitName_210"
npc_title: "Legion Administrator"
category: 50
class_mask: 2
model: 235
scale: 1.7
functions:
  - {"code": 6, "function": "legion_create", "label": "Legion Create"}
  - {"code": 28, "function": "legion_warehouse", "label": "Warehouse"}
role: "Legion Administrator"
talk_key: "Quest_Talk_Default_Guild"
portrait: "ui/NPCProfile/NPC_Guild.dds"
map: 90
x: 480.8
z: 4146.2
---
<!-- generated:start -->
<!-- generated-keys: title=f6e385 type=3664ce id=154a31 sources=ee9c99 name_key=ca5d69 title_key=7696fa npc_title=63326e category=e1822d class_mask=da4b92 model=0b7f5a scale=58e6d3 functions=13674d role=63326e talk_key=9314f1 portrait=69c286 map=2be88c x=2be88c z=2be88c -->
|  |  |
|---|---|
|  | ![Kesley](../assets/npcs/318.png) |
| **Unit id** | `318` |
| **Title** | Legion Administrator |
| **Category** | NPC (category 50) |
| **Menu** | Legion Create (`6`), Warehouse (`28`) |
| **Model** | ObjectList `235`, scale 1.7 |
| **Portrait** | `ui/NPCProfile/NPC_Guild.dds` |

### Greeting

> Do you want to create your own Legion? I'm the person that will make that happen.

### Other units with this name

The client has one unit row per placement or variant: [[wiki/npcs/210-kesley|Kesley (210)]].

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 59:00 (3. NPCs)
<!-- generated:end -->

## Notes

- A second Legion Administrator stands in the Castle at (480.8, 4146.2), ±5 units, besides the Fortress Kesley (210) ([[gameplay/video-early-quests|Video notes: first session]] §3, [59:01](https://www.youtube.com/watch?v=s04CSN16w1s&t=3541s)). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/video-early-quests|Video notes: first session]]

## Open questions

- The video notes write the unit as "210 (318?)". This page assumes the Castle Kesley is 318, the second `UnitDB` row with the same name and menu. The Erion and Armia castles (94, 98) would need their own positions; whether they share the Arslan layout is not checked.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
