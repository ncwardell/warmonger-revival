---
title: "Lewellyn"
type: "npc"
id: 315
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 315", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §4", "gameplay/video-tutorial-walkthrough §2"]
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
quests: {"gives": [100], "receives": [100]}
quest_fields: [88, 92, 96]
map: 88
x: 378.9
z: 3478.9
positions:
  - {"field": 88, "x": 378.9, "z": 3478.9, "source": "gameplay/npc-locations §4", "confidence": "video"}
  - {"field": 88, "x": 380.3, "z": 3478.6, "source": "gameplay/video-tutorial-walkthrough §2", "confidence": "video"}
  - {"field": 92, "x": 634.9, "z": 3478.9, "source": "derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 96, "x": 890.9, "z": 3478.9, "source": "derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=ef0630 type=3664ce id=f6b9b6 sources=b4fb16 name_key=ba31e5 title_key=f11c2d npc_title=4bc26f category=e1822d class_mask=da4b92 model=fc074d scale=aa8f28 functions=7dac55 role=4bc26f shop=267b97 talk_key=daeeaf portrait=71efa1 quests=759050 quest_fields=46bf0f map=b37f6d x=0076cc z=202cb5 positions=7b1280 -->
|  |  |
|---|---|
|  | ![Lewellyn](../assets/npcs/315.png) |
| **Unit id** | `315` |
| **Title** | Scroll Merchant |
| **Category** | NPC (category 50) |
| **Menu** | Shop (`1`) |
| **Shop** | [[wiki/shops/282-lewellyn-s-shop-scroll-merchant\|Lewellyn's shop (Scroll Merchant)]] |
| **Stands in** | [[wiki/fields/88-training-camp\|Training Camp]] at (378.9, 3478.9) |
| **Model** | ObjectList `36`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Quest_ItemShop.dds` |

### Greeting

> Nice to meet you, I sell Scroll. would you be interested?

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/88-training-camp\|Training Camp]] | 378.9 | 3478.9 | video | [[gameplay/npc-locations\|npc-locations]] §4 |
| [[wiki/fields/88-training-camp\|Training Camp]] | 380.3 | 3478.6 | video | [[gameplay/video-tutorial-walkthrough\|video-tutorial-walkthrough]] §2 |
| [[wiki/fields/92-training-camp\|Training Camp]] | 634.9 | 3478.9 | derived | derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/96-training-camp\|Training Camp]] | 890.9 | 3478.9 | derived | derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2) |

### Shop

Sells 12 items (`Npc_Carry` row 282; full list on [[wiki/shops/282-lewellyn-s-shop-scroll-merchant|Lewellyn's shop (Scroll Merchant)]]): [[wiki/items/704-scroll-of-the-warrior-c|Scroll of the Warrior (C)]], [[wiki/items/708-scroll-of-the-magician-c|Scroll of the Magician (C)]], [[wiki/items/712-tome-of-attack-spd-c|Tome of Attack SPD (C)]], [[wiki/items/716-tome-of-cooldown-c|Tome of Cooldown (C)]], [[wiki/items/720-tome-of-patience-c|Tome of Patience (C)]], [[wiki/items/724-tome-of-critical-c|Tome of Critical (C)]], [[wiki/items/736-elixir-of-health-c|Elixir of Health (C)]], [[wiki/items/740-flask-of-mana-c|Flask of Mana (C)]], [[wiki/items/744-elixir-of-vampirism-c|Elixir of Vampirism (C)]], [[wiki/items/748-flask-of-devour-c|Flask of Devour (C)]], [[wiki/items/752-elixir-of-tenacity-c|Elixir of Tenacity (C)]], [[wiki/items/756-flask-of-tenacity-c|Flask of Tenacity (C)]].

### Quests

- **Gives:** [[wiki/quests/100-hunting-for-furs|Hunting for Furs]]
- **Takes the turn-in of:** [[wiki/quests/100-hunting-for-furs|Hunting for Furs]]

### Other units with this name

The client has one unit row per placement or variant: [[wiki/npcs/205-lewellyn|Lewellyn (205)]], [[wiki/npcs/316-lewellyn|Lewellyn (316)]].

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (4. Training Camp (fields 88 / 92 / 96))
- [[gameplay/consumables|Consumables and clickables]] (5. Where the inputs come from)
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] at 8:50 (Training Camp (field 92) and back)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 17:00, 22:00, 23:00 (Training Ground and Camp (levels 1–11); 3. NPCs)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] at 15:10 (Steps; 2. NPC positions)
<!-- generated:end -->

## Notes

- Training Camp scroll merchant, also on shop 282 ([[gameplay/consumables|Consumables]] §5). *client*
- Video checks place her within 2 units of the listed point: (378.7, 3477.4) ([[gameplay/video-early-quests|Video notes: first session]] §3) and (380.3, 3478.6) ([[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough]] §2). *video*

## Behaviour

- Side quest 100 "Hunting for Furs": 5 White Chepa Fur (Chepa Warrior 727) and 5 Black Chepa Fur (Chepa Archer 728). The panel shows 7,400 exp (table 8,880) and 5,000 gold, then a choice of Spell Necklace (397) or Necklace of Life (405). Her line mentions shoes, but the reward is a necklace ([[gameplay/video-early-quests|Video notes: first session]] §2 step 8, [17:02](https://www.youtube.com/watch?v=s04CSN16w1s&t=1022s); [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough]] step 12, [15:10](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=910s); [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial]] step 13). *video*

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/consumables|Consumables]]
- [[gameplay/video-early-quests|Video notes: first session]]
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough]]
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
