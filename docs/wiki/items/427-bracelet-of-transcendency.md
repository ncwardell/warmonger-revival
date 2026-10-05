---
title: "Bracelet of Transcendency"
type: "item"
id: 427
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 427", "image: [[gameplay/maps-and-dungeons]] §2 (2018 dungeons guide loot grids; Lv 1–4 drop T1, Lv 5–8 T2, pre-reinforced +0…+11; 2–3 rarer drops per dungeon missing)"]
name_key: "ItemName_427"
kind: 56
kind_name: "Bracelet"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 130}
cost_pair:
  - {"currency": 2, "amount": 130}
stats:
  - {"code": 2, "stat": "Ability Power", "value": 7, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "level"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 1, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "tier"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 3, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 3, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 15, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 180, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 2, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_09.png", "index": 0}
obtained_from:
  - {"how": "shop", "shop": 32}
  - {"how": "shop", "shop": 36}
  - {"how": "shop", "shop": 52}
  - {"how": "shop", "shop": 77}
  - {"how": "shop", "shop": 81}
  - {"how": "shop", "shop": 97}
  - {"how": "shop", "shop": 214}
  - {"how": "shop", "shop": 216}
  - {"how": "shop", "shop": 223}
  - {"how": "craft", "recipe": 31}
  - {"how": "craft", "recipe": 2031}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
  - {"how": "dungeon_drop", "field": 128, "tier": 1}
  - {"how": "dungeon_drop", "field": 122, "tier": 1}
  - {"how": "dungeon_drop", "field": 126, "tier": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=168ff3 type=d36ca9 id=fba7b6 sources=21f4ea name_key=bf7d7a kind=54ceb9 kind_name=c2576a classes=92d079 bind=2be88c price=05bfea cost_pair=c1b652 stats=88a052 reinforce=356a19 icon=582d6a obtained_from=dc9486 -->
|  |  |
|---|---|
|  | ![Bracelet of Transcendency](wiki/assets/items/427.png) |
| **Item id** | `427` |
| **Kind** | Bracelet (56) |
| **Category** | [[wiki/items/accessories\|Accessories]] |
| **Classes** | all |
| **Buy price** | 130 Gold |
| **Icon** | `ui/icons/Items_09.png` cell 0 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +7 | × (tier × 15 + reinforce level) | 2 |
| Mana | +10 | × (tier × 15 + reinforce level) | 33 |
| Mana Regeneration | +1 | × (tier × 15 + reinforce level) | 34 |
| Ability Power | +10 | × tier | 2 |
| Mana Regeneration | +3 | × tier | 34 |
| Mana | +3 | × tier | 33 |
| Ability Power | +15 | flat | 2 |
| Mana | +180 | flat | 33 |
| Mana Regeneration | +2 | flat | 34 |

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
| 31 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 13 | 195 | 100 |
| 2031 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 13 | 195 | 100 |

### Where to get it

- Sold in [[wiki/shops/32-shop-32-no-npc|Shop 32 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/36-shop-36-no-npc|Shop 36 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/52-shop-52-no-npc|Shop 52 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/77-shop-77-no-npc|Shop 77 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/81-shop-81-no-npc|Shop 81 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/97-shop-97-no-npc|Shop 97 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/214-shop-214-no-npc|Shop 214 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/216-shop-216-no-npc|Shop 216 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/223-shop-223-no-npc|Shop 223 (no NPC)]] (no NPC found)
- Hero gacha pool 00, grade 1 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)
- how dungeon_drop, field 128, tier 1 (hand-entered)
- how dungeon_drop, field 122, tier 1 (hand-entered)
- how dungeon_drop, field 126, tier 2 (hand-entered)
<!-- generated:end -->

## Notes

Drops in the border dungeons Skull Cemetery (128), Tsunami Lake (122), Demon Hell (126), already reinforced at a random level (+0 up to +11 seen); Lv 1–4 dungeons drop it at tier 1, Lv 5–8 at tier 2 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §2, *image*). Sockets are rolled when the item drops ([[gameplay/items-and-crafting|Items and crafting]] §2).

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
