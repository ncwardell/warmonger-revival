---
title: "Ashley"
type: "npc"
id: 206
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 206", "gameplay/npc-locations §3"]
name_key: "TitleName_8"
title_key: "UnitName_206"
npc_title: "Merits Costume Merchant"
category: 50
class_mask: 2
model: 194
scale: 1.5
functions:
  - {"code": 1, "function": "shop", "label": "Shop"}
  - {"code": 30, "function": "costume_lock", "label": "Carve Costume"}
role: "Merits Costume Merchant"
shop: 284
talk_key: "Quest_Talk_Default_Coustume"
portrait: "ui/NPCProfile/Quest_ItemShop.dds"
map: 120
x: 1888.5
z: 1704.5
positions:
  - {"field": 120, "x": 1888.5, "z": 1704.5, "source": "gameplay/npc-locations §3", "confidence": "video"}
  - {"field": 120, "x": 2144.5, "z": 1704.5, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2400.5, "z": 1704.5, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=8bb19e type=3664ce id=4afa8f sources=3dcb13 name_key=4a7a05 title_key=f5f511 npc_title=e9cdd2 category=e1822d class_mask=da4b92 model=2a79f1 scale=aa8f28 functions=ff474b role=e9cdd2 shop=7f3541 talk_key=48ccbb portrait=71efa1 map=775bc5 x=a9df41 z=73bf7b positions=468f56 -->
|  |  |
|---|---|
|  | ![Ashley](../assets/npcs/206.png) |
| **Unit id** | `206` |
| **Title** | Merits Costume Merchant |
| **Category** | NPC (category 50) |
| **Menu** | Shop (`1`), Carve Costume (`30`) |
| **Shop** | [[wiki/shops/284-ashley-s-shop-merits-costume-merchant\|Ashley's shop (Merits Costume Merchant)]] |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1888.5, 1704.5) |
| **Model** | ObjectList `194`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Quest_ItemShop.dds` |

### Greeting

> Hello there, do you want to change your appearance?  I can help you with that. 
>  Take a look at all those costumes.

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1888.5 | 1704.5 | video | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2144.5 | 1704.5 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2400.5 | 1704.5 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Shop

Sells 16 items (`Npc_Carry` row 284; full list on [[wiki/shops/284-ashley-s-shop-merits-costume-merchant|Ashley's shop (Merits Costume Merchant)]]): [[wiki/items/2027-twisted-wind-set|Twisted Wind Set]], [[wiki/items/2028-twisted-wind-set|Twisted Wind Set]], [[wiki/items/2029-twisted-wind-set|Twisted Wind Set]], [[wiki/items/2015-crown-set|Crown Set]], [[wiki/items/2016-crown-set|Crown Set]], [[wiki/items/2017-crown-set|Crown Set]], [[wiki/items/2018-helios-set|Helios Set]], [[wiki/items/2019-helios-set|Helios Set]], [[wiki/items/2020-helios-set|Helios Set]], [[wiki/items/2079-haple-set|Haple Set]], [[wiki/items/2080-haple-set|Haple Set]], [[wiki/items/2081-haple-set|Haple Set]] ….

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
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
