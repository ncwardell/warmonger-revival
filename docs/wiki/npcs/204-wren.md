---
title: "Wren"
type: "npc"
id: 204
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 204", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §3"]
name_key: "TitleName_3"
title_key: "UnitName_204"
npc_title: "Merchant"
category: 50
class_mask: 2
model: 40
scale: 1.5
functions:
  - {"code": 1, "function": "shop", "label": "Shop"}
role: "Merchant"
shop: 281
talk_key: "Quest_Talk_Default_Hawker"
portrait: "ui/NPCProfile/Hawker.dds"
quests: {"gives": [26, 727, 740, 785, 786], "receives": [26, 727, 779, 785, 786, 1006, 1032], "talk_objective": [26, 102, 691, 1006, 1031]}
quest_fields: [120]
map: 120
x: 1983.2
z: 1709.8
positions:
  - {"field": 120, "x": 1983.2, "z": 1709.8, "source": "gameplay/npc-locations §3", "confidence": "video"}
  - {"field": 120, "x": 2239.2, "z": 1709.8, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2495.2, "z": 1709.8, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=60ea71 type=3664ce id=1cc641 sources=11b11a name_key=7d155d title_key=ee2258 npc_title=b0845f category=e1822d class_mask=da4b92 model=af3e13 scale=aa8f28 functions=7dac55 role=b0845f shop=d8502b talk_key=2634be portrait=399d90 quests=3079bf quest_fields=6c3da9 map=775bc5 x=ad06d3 z=ce86c4 positions=29049f -->
|  |  |
|---|---|
|  | ![Wren](wiki/assets/npcs/204.png) |
| **Unit id** | `204` |
| **Title** | Merchant |
| **Category** | NPC (category 50) |
| **Menu** | Shop (`1`) |
| **Shop** | [[wiki/shops/281-wren-s-shop-merchant-281\|Wren's shop (Merchant) 281]] |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1983.2, 1709.8) |
| **Model** | ObjectList `40`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Hawker.dds` |

### Greeting

> Welcome back friend!  Is there anything you need?

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1983.2 | 1709.8 | video | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2239.2 | 1709.8 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2495.2 | 1709.8 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Shop

Sells 14 items (`Npc_Carry` row 281; full list on [[wiki/shops/281-wren-s-shop-merchant-281|Wren's shop (Merchant) 281]]): [[wiki/items/883-potion-of-health-d|Potion of Health (D)]], [[wiki/items/884-potion-of-mana-d|Potion of Mana (D)]], [[wiki/items/906-scroll-return|Scroll : Return]], [[wiki/items/909-scroll-gaia|Scroll : Gaia]], [[wiki/items/908-scroll-castle|Scroll : Castle]], [[wiki/items/688-dimensional-energy|Dimensional energy]], [[wiki/items/945-auto-decomposition-hammer-d|Auto decomposition hammer (D)]], [[wiki/items/946-auto-decomposition-hammer-c|Auto decomposition hammer (C)]], [[wiki/items/947-auto-decomposition-hammer-b|Auto decomposition hammer (B)]], [[wiki/items/949-auto-decomposition-hammer-a|Auto decomposition hammer (A)]], [[wiki/items/1105-pyrotechnics|Pyrotechnics]], [[wiki/items/2909-flare|Flare]] ….

### Quests

- **Gives:** [[wiki/quests/26-border-area-normal-mode|Border Area Normal Mode]], [[wiki/quests/727-the-necessary-materials|The necessary materials]], [[wiki/quests/740-tow-canyon|Tow Canyon]], [[wiki/quests/785-the-strange-flowers-in-the-lake|The strange flowers in the lake]], [[wiki/quests/786-mushrooms-in-the-komodo-area|Mushrooms in the Komodo area]]
- **Takes the turn-in of:** [[wiki/quests/26-border-area-normal-mode|Border Area Normal Mode]], [[wiki/quests/727-the-necessary-materials|The necessary materials]], [[wiki/quests/779-request-of-dispatch-knight|Request of dispatch knight]], [[wiki/quests/785-the-strange-flowers-in-the-lake|The strange flowers in the lake]], [[wiki/quests/786-mushrooms-in-the-komodo-area|Mushrooms in the Komodo area]], [[wiki/quests/1006-skull-temple-hunting|Skull Temple : Hunting]], [[wiki/quests/1032-tow-canyon-hunting|Tow Canyon : Hunting]]
- **Must be talked to in:** [[wiki/quests/26-border-area-normal-mode|Border Area Normal Mode]], [[wiki/quests/102-wren-s-sister-wren|Wren's sister Wren?]], [[wiki/quests/691-items-ai-steering-item-use|Items - AI Steering & Item Use]], [[wiki/quests/1006-skull-temple-hunting|Skull Temple : Hunting]], [[wiki/quests/1031-tow-canyon-hunting|Tow Canyon : Hunting]]

Dialogue rows (`QuestTalk`; full text on the quest pages):

| quest | QuestTalk | speaker | first line |
|---|---|---|---|
| [[wiki/quests/740-tow-canyon\|Tow Canyon]] | 757 | Wren : Merchant | Knights were dispatched to the Tow Canyon   but Knights alone will not be able to kill monsters in the Tow Canyon. Go he |
| [[wiki/quests/779-request-of-dispatch-knight\|Request of dispatch knight]] | 757 | Wren : Merchant | Knights were dispatched to the Tow Canyon   but Knights alone will not be able to kill monsters in the Tow Canyon. Go he |

### Other units with this name

The client has one unit row per placement or variant: [[wiki/npcs/238-wren|Wren (238)]], [[wiki/npcs/319-wren|Wren (319)]].

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/consumables|Consumables and clickables]] (5. Where the inputs come from)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 37:00 (Fortress (levels 12–20))
<!-- generated:end -->

## Notes

- Wren is the Fortress merchant on the upper-right stairs ([[gameplay/npc-locations|NPC locations]] §3, guide). Her shop (`Npc_Carry` 281) sells potions, scrolls (Return, Gaia, Castle), Dimensional Energy, auto-decomposition hammers and Pyrotechnics ([[gameplay/maps-and-dungeons|Maps and dungeons]] §5). *image*
- Prices shown in one fortress in spring 2018: D potions 79, Scroll: Castle 19,800, Dimensional energy 5,500, hammers D/C/B/A 158,400 / 285,120 / 1,346,400 / 3,960,000, Pyrotechnics 3,960. Gold items cost 7.92 × the `Item_Base` price and Dimensional Energy 1.1 × ([[gameplay/progression-and-economy|Progression and economy]] §4, [[gameplay/server-rules|Server rules]] Economy). *image*
- Pyrotechnics were sold for gold from WM 0404 ([[gameplay/patch-history|Patch history]]). She also sells the Flare and Ward items 2909–2911 ([[gameplay/reinforce-and-runes|Reinforce and runes]] §7). *notes + client*
- In Crush Online she sold the Magic Crafting Stone (37,000 → 48,000 → 42,500 gold); from 15 Dec 2016 it came only from the Diamond medal box ([[gameplay/crush-mechanics|Crush Online mechanics]] §3). *player*

## Behaviour

- Her twin in the Training Camp (unit 238) sends the player to her with the "Hawker letter" (quest 102 "Wren's sister Wren?"), finished at about 40:05 ([[gameplay/video-early-quests|Video notes: first session]] §2 step 14). *video*

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/npc-locations|NPC locations]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/progression-and-economy|Progression and economy]]
- [[gameplay/server-rules|Server rules]]
- [[gameplay/patch-history|Patch history]]
- [[gameplay/reinforce-and-runes|Reinforce and runes]]
- [[gameplay/crush-mechanics|Crush Online mechanics]]
- [[gameplay/video-early-quests|Video notes: first session]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
