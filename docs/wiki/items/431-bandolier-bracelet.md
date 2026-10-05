---
title: "Bandolier Bracelet"
type: "item"
id: 431
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 431", "image: [[gameplay/maps-and-dungeons]] §2 (2018 dungeons guide loot grids; Lv 1–4 drop T1, Lv 5–8 T2, pre-reinforced +0…+11; 2–3 rarer drops per dungeon missing)"]
name_key: "ItemName_431"
kind: 56
kind_name: "Bracelet"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 130}
cost_pair:
  - {"currency": 2, "amount": 130}
stats:
  - {"code": 1, "stat": "Attack", "value": 5, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "tier"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 1, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 80, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 250, "scale": "flat"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 3, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_08.png", "index": 62}
obtained_from:
  - {"how": "shop", "shop": 44}
  - {"how": "shop", "shop": 60}
  - {"how": "shop", "shop": 93}
  - {"how": "shop", "shop": 105}
  - {"how": "shop", "shop": 113}
  - {"how": "shop", "shop": 117}
  - {"how": "shop", "shop": 223}
  - {"how": "craft", "recipe": 35}
  - {"how": "craft", "recipe": 2035}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
  - {"how": "dungeon_drop", "field": 121, "tier": 1}
  - {"how": "dungeon_drop", "field": 125, "tier": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=8c38f6 type=d36ca9 id=6c0ac7 sources=31e8e0 name_key=37737c kind=54ceb9 kind_name=c2576a classes=92d079 bind=2be88c price=05bfea cost_pair=c1b652 stats=5a9e73 reinforce=356a19 icon=6a1367 obtained_from=1cb3b5 -->
|  |  |
|---|---|
|  | ![Bandolier Bracelet](wiki/assets/items/431.png) |
| **Item id** | `431` |
| **Kind** | Bracelet (56) |
| **Category** | [[wiki/items/accessories\|Accessories]] |
| **Classes** | all |
| **Buy price** | 130 Gold |
| **Icon** | `ui/icons/Items_08.png` cell 62 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +5 | × (tier × 15 + reinforce level) | 1 |
| Health | +10 | × (tier × 15 + reinforce level) | 31 |
| Attack | +10 | × tier | 1 |
| Health | +20 | × tier | 31 |
| Attack Speed(%) | Attack Speed +1% | × tier | 103 |
| Attack | +80 | flat | 1 |
| Health | +250 | flat | 31 |
| Attack Speed(%) | Attack Speed +3% | flat | 103 |

### Reinforcement

ItemSancMet row 1 (inferred from Item_Base +0x92), 1,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 1 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 1 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 1 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 2 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 5 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 7 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 35 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 13 | 195 | 100 |
| 2035 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 13 | 195 | 100 |

### Where to get it

- Sold in [[wiki/shops/44-shop-44-no-npc|Shop 44 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/60-shop-60-no-npc|Shop 60 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/93-shop-93-no-npc|Shop 93 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/105-shop-105-no-npc|Shop 105 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/113-shop-113-no-npc|Shop 113 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/117-shop-117-no-npc|Shop 117 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/223-shop-223-no-npc|Shop 223 (no NPC)]] (no NPC found)
- Hero gacha pool 00, grade 1 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)
- how dungeon_drop, field 121, tier 1 (hand-entered)
- how dungeon_drop, field 125, tier 2 (hand-entered)
<!-- generated:end -->

## Notes

Drops in the border dungeons Skull Temple (121), Tow Canyon (125), already reinforced at a random level (+0 up to +11 seen); Lv 1–4 dungeons drop it at tier 1, Lv 5–8 at tier 2 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §2, *image*). Sockets are rolled when the item drops ([[gameplay/items-and-crafting|Items and crafting]] §2).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- image: [[gameplay/maps-and-dungeons]] §2 (2018 dungeons guide loot grids; Lv 1–4 drop T1, Lv 5–8 T2, pre-reinforced +0…+11; 2–3 rarer drops per dungeon missing)

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
