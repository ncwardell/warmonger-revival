---
title: "Lewellyn"
type: "npc"
id: 205
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 205", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §3"]
name_key: "TitleName_4"
title_key: "UnitName_205"
npc_title: "Scroll Merchant"
category: 50
class_mask: 2
model: 36
scale: 1.5
functions:
  - {"code": 1, "function": "shop", "label": "Shop"}
role: "Scroll Merchant"
shop: 282
talk_key: "Quest_Talk_Default_Artifacts"
portrait: "ui/NPCProfile/Quest_ItemShop.dds"
quests: {"gives": [119, 724, 733, 737], "receives": [724, 733, 778, 1011, 1021, 1027], "talk_objective": [1011, 1021, 1026]}
quest_fields: [120]
map: 120
x: 1987.0
z: 1712.4
positions:
  - {"field": 120, "x": 1987.0, "z": 1712.4, "source": "gameplay/npc-locations §3", "confidence": "video"}
  - {"field": 120, "x": 2243.0, "z": 1712.4, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2499.0, "z": 1712.4, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=ef0630 type=3664ce id=5f1cd7 sources=69228a name_key=ba31e5 title_key=f11c2d npc_title=4bc26f category=e1822d class_mask=da4b92 model=fc074d scale=aa8f28 functions=7dac55 role=4bc26f shop=267b97 talk_key=daeeaf portrait=71efa1 quests=68d9db quest_fields=6c3da9 map=775bc5 x=646a91 z=7904c5 positions=b38101 -->
|  |  |
|---|---|
|  | ![Lewellyn](wiki/assets/npcs/205.png) |
| **Unit id** | `205` |
| **Title** | Scroll Merchant |
| **Category** | NPC (category 50) |
| **Menu** | Shop (`1`) |
| **Shop** | [[wiki/shops/282-lewellyn-s-shop-scroll-merchant\|Lewellyn's shop (Scroll Merchant)]] |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1987.0, 1712.4) |
| **Model** | ObjectList `36`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Quest_ItemShop.dds` |

### Greeting

> Nice to meet you, I sell Scroll. would you be interested?

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1987.0 | 1712.4 | video | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2243.0 | 1712.4 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2499.0 | 1712.4 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Shop

Sells 12 items (`Npc_Carry` row 282; full list on [[wiki/shops/282-lewellyn-s-shop-scroll-merchant|Lewellyn's shop (Scroll Merchant)]]): [[wiki/items/704-scroll-of-the-warrior-c|Scroll of the Warrior (C)]], [[wiki/items/708-scroll-of-the-magician-c|Scroll of the Magician (C)]], [[wiki/items/712-tome-of-attack-spd-c|Tome of Attack SPD (C)]], [[wiki/items/716-tome-of-cooldown-c|Tome of Cooldown (C)]], [[wiki/items/720-tome-of-patience-c|Tome of Patience (C)]], [[wiki/items/724-tome-of-critical-c|Tome of Critical (C)]], [[wiki/items/736-elixir-of-health-c|Elixir of Health (C)]], [[wiki/items/740-flask-of-mana-c|Flask of Mana (C)]], [[wiki/items/744-elixir-of-vampirism-c|Elixir of Vampirism (C)]], [[wiki/items/748-flask-of-devour-c|Flask of Devour (C)]], [[wiki/items/752-elixir-of-tenacity-c|Elixir of Tenacity (C)]], [[wiki/items/756-flask-of-tenacity-c|Flask of Tenacity (C)]].

### Quests

- **Gives:** [[wiki/quests/119-monster-area-wars|Monster area wars]], [[wiki/quests/724-find-lost-item|Find lost item]], [[wiki/quests/733-weapon-appropriation|Weapon appropriation]], [[wiki/quests/737-ghost-fortress|Ghost Fortress]]
- **Takes the turn-in of:** [[wiki/quests/724-find-lost-item|Find lost item]], [[wiki/quests/733-weapon-appropriation|Weapon appropriation]], [[wiki/quests/778-ghost-soldier|Ghost soldier]], [[wiki/quests/1011-skull-cemetery-hunting|Skull Cemetery : Hunting]], [[wiki/quests/1021-swamps-of-the-snake-warrior-hunting|Swamps of the Snake Warrior : Hunting]], [[wiki/quests/1027-ghost-fortress-hunting|Ghost Fortress : Hunting]]
- **Must be talked to in:** [[wiki/quests/1011-skull-cemetery-hunting|Skull Cemetery : Hunting]], [[wiki/quests/1021-swamps-of-the-snake-warrior-hunting|Swamps of the Snake Warrior : Hunting]], [[wiki/quests/1026-ghost-fortress-hunting|Ghost Fortress : Hunting]]

### Other units with this name

The client has one unit row per placement or variant: [[wiki/npcs/315-lewellyn|Lewellyn (315)]], [[wiki/npcs/316-lewellyn|Lewellyn (316)]].

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/consumables|Consumables and clickables]] (5. Where the inputs come from)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 48:20, 48:40, 49:20, 50:05 (3. NPCs)
<!-- generated:end -->

## Notes

- Fortress scroll merchant (shop 282; one guide spells it "Llewellyn") ([[gameplay/maps-and-dungeons|Maps and dungeons]] §5). Shop 282 sells the C-grade clickables 704, 708, 712, 716, 720, 724, 736, 740, 744, 748, 752 and 756; B, A and S grades are only crafted at Owen ([[gameplay/consumables|Consumables]] §5, §4). *client*
- She does not sell C-grade Armor PNT or Magic PNT scrolls, so those were probably unobtainable or drop-only ([[gameplay/consumables|Consumables]] §4.1). *client + guess*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/consumables|Consumables]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
