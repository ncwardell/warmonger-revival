---
title: "Athan"
type: "npc"
id: 207
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 207", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §3"]
name_key: "TitleName_7"
title_key: "UnitName_207"
npc_title: "Merits Merchant"
category: 50
class_mask: 2
model: 234
scale: 1.5
functions:
  - {"code": 1, "function": "shop", "label": "Shop"}
role: "Merits Merchant"
shop: 283
talk_key: "Quest_Talk_Default_Medal"
portrait: "ui/NPCProfile/NPC_Instructor.dds"
quests: {"gives": [714], "receives": [714, 749, 750, 751, 841, 1101, 1102, 1103], "talk_objective": [714, 1101, 1102, 1103, 1518]}
quest_fields: [120]
map: 120
x: 1910.6
z: 1666.7
positions:
  - {"field": 120, "x": 1910.6, "z": 1666.7, "source": "gameplay/npc-locations §3", "confidence": "video"}
  - {"field": 120, "x": 2166.6, "z": 1666.7, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2422.6, "z": 1666.7, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=9e0248 type=3664ce id=3be76c sources=5aebd5 name_key=9afd73 title_key=36b546 npc_title=bc697c category=e1822d class_mask=da4b92 model=0ec09e scale=aa8f28 functions=7dac55 role=bc697c shop=3032a4 talk_key=630967 portrait=6aa998 quests=bd0b79 quest_fields=6c3da9 map=775bc5 x=c3a2bf z=f4f2e4 positions=262929 -->
|  |  |
|---|---|
|  | ![Athan](wiki/assets/npcs/207.png) |
| **Unit id** | `207` |
| **Title** | Merits Merchant |
| **Category** | NPC (category 50) |
| **Menu** | Shop (`1`) |
| **Shop** | [[wiki/shops/283-athan-s-shop-merits-merchant\|Athan's shop (Merits Merchant)]] |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1910.6, 1666.7) |
| **Model** | ObjectList `234`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/NPC_Instructor.dds` |

### Greeting

> Nice to meet you! The greatest honor is to fight on the battlefield.

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1910.6 | 1666.7 | video | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2166.6 | 1666.7 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2422.6 | 1666.7 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Shop

Sells 16 items (`Npc_Carry` row 283; full list on [[wiki/shops/283-athan-s-shop-merits-merchant|Athan's shop (Merits Merchant)]]): [[wiki/items/854-shining-passion|Shining Passion]], [[wiki/items/855-mysterious-passion|Mysterious Passion]], [[wiki/items/856-brilliant-passion|Brilliant Passion]], [[wiki/items/857-amplifying-passion|Amplifying Passion]], [[wiki/items/1051-bronze-medal-reward-box|(Bronze) Medal Reward Box]], [[wiki/items/1052-silver-medal-reward-box|(Silver) Medal Reward Box]], [[wiki/items/1053-gold-medal-reward-box|(Gold) Medal Reward Box]], [[wiki/items/1054-mithril-medal-reward-box|(Mithril) Medal Reward Box]], [[wiki/items/1057-random-box-of-dye|Random box of dye]], [[wiki/items/1058-random-box-of-dye|Random box of dye]], [[wiki/items/1059-random-box-of-dye|Random box of dye]], [[wiki/items/689-tier-1-time-energy|Tier 1 : Time energy]] ….

### Quests

- **Gives:** [[wiki/quests/714-buy-time-energy|Buy time energy]]
- **Takes the turn-in of:** [[wiki/quests/714-buy-time-energy|Buy time energy]], [[wiki/quests/749-kill-monster-of-the-land-of-greed|Kill monster of The land of Greed]], [[wiki/quests/750-kill-monster-of-the-avenue-of-spirit|Kill monster of The avenue of spirit]], [[wiki/quests/751-kill-monster-of-the-way-go-to-devildom|Kill monster of The way go to devildom]], [[wiki/quests/841-gather-resourses-at-connected-world|Gather resourses at Connected World]], [[wiki/quests/1101-the-land-of-greed-kill-monster|The Land of Greed : Kill monster]], [[wiki/quests/1102-the-avenue-of-spirit-kill-monster|The Avenue of spirit : Kill monster]], [[wiki/quests/1103-the-way-go-to-devildom-kill-monster|The Way go to devildom : Kill monster]]
- **Must be talked to in:** [[wiki/quests/714-buy-time-energy|Buy time energy]], [[wiki/quests/1101-the-land-of-greed-kill-monster|The Land of Greed : Kill monster]], [[wiki/quests/1102-the-avenue-of-spirit-kill-monster|The Avenue of spirit : Kill monster]], [[wiki/quests/1103-the-way-go-to-devildom-kill-monster|The Way go to devildom : Kill monster]], [[wiki/quests/1518-items-ai-steering-item-use|Items - AI Steering & Item Use]]

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/consumables|Consumables and clickables]] (5. Where the inputs come from)
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] (3. Artifacts: additional effects, crafting, reinforcing)
- [[gameplay/items-and-crafting|Items, upgrades and crafting]] (3. Crafting; 5. Where gear comes from)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (5. Fortress layout (town))
- [[gameplay/patch-history|Patch notes and other sources]] (Numbers pass (October 2026))
- [[gameplay/progression-and-economy|Progression and economy]] (3. Currencies)
- [[gameplay/server-rules|Server rules checklist]] (Economy)
- [[gameplay/sources|Sources and gaps]] (3. Player screenshots (image sets that still load))
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] (After the tutorial (Fortress, from 22:00))
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 41:50, 48:20, 48:40, 49:20, 50:05, 2:22:30 (Fortress (levels 12–20); 3. NPCs; 4. Levelling)
<!-- generated:end -->

## Notes

- Merits (medal) merchant, in the middle of the Fortress opposite the auction house ([[gameplay/maps-and-dungeons|Maps and dungeons]] §5). *image*
- Medal prices from a guide screenshot include Shining Passion 2 silver, Mysterious Passion 5 bronze, Brilliant Passion 5 silver, medal reward boxes 4 bronze / 3 silver / 2 gold / 1 mithril, Tier 1/2/3 Time Energy 1 bronze / 1 silver / 1 gold ([[gameplay/progression-and-economy|Progression and economy]] §4). Weapon materials cost 2 bronze medals each ([[gameplay/items-and-crafting|Items and crafting]] §3). *image + guide*
- He also sells Crystal: Blue and Yellow (shop 283) ([[gameplay/consumables|Consumables]] §5). *client*
- The 0329 patch added three repeatable Abyss quests at Athan ([[gameplay/patch-history|Patch history]]). In Crush Online he sold reinforcement adjuvants for Mithril medals ([[gameplay/crush-mechanics|Crush Online mechanics]] §3). *notes / player*

## Behaviour

- Quest 749 "Kill monster of The land of Greed": 50 Tow and 50 Elite Tow, back to Athan, for 50,000 exp, 50,000 gold, 50/50 fragments and 20 Crystal: Blue. He then offers the ghost version (750 / 1102): 70,000 exp, 70,000 gold, 60/60 fragments and Crystal: Yellow ([[gameplay/video-early-quests|Video notes: first session]] §2 step 17, [41:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=2515s), [2:22:32](https://www.youtube.com/watch?v=s04CSN16w1s&t=8552s)). *video*

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/progression-and-economy|Progression and economy]]
- [[gameplay/items-and-crafting|Items and crafting]]
- [[gameplay/consumables|Consumables]]
- [[gameplay/patch-history|Patch history]]
- [[gameplay/crush-mechanics|Crush Online mechanics]]
- [[gameplay/video-early-quests|Video notes: first session]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
