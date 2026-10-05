---
title: "Bracelet of Mediation"
type: "item"
id: 423
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 423", "image: [[gameplay/maps-and-dungeons]] §2 (2018 dungeons guide loot grids; Lv 1–4 drop T1, Lv 5–8 T2, pre-reinforced +0…+11; 2–3 rarer drops per dungeon missing)"]
name_key: "ItemName_423"
kind: 56
kind_name: "Bracelet"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 130}
cost_pair:
  - {"currency": 2, "amount": 130}
stats:
  - {"code": 2, "stat": "Ability Power", "value": 8, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 7, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 7, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 15, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 70, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 125, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 125, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_09.png", "index": 7}
obtained_from:
  - {"how": "shop", "shop": 28}
  - {"how": "shop", "shop": 48}
  - {"how": "shop", "shop": 73}
  - {"how": "shop", "shop": 89}
  - {"how": "shop", "shop": 215}
  - {"how": "shop", "shop": 222}
  - {"how": "craft", "recipe": 27}
  - {"how": "craft", "recipe": 2027}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
  - {"how": "dungeon_drop", "field": 127, "tier": 1}
  - {"how": "dungeon_drop", "field": 124, "tier": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=dd1888 type=d36ca9 id=a785bd sources=ec05b7 name_key=903fdb kind=54ceb9 kind_name=c2576a classes=92d079 bind=2be88c price=05bfea cost_pair=c1b652 stats=c9f209 reinforce=356a19 icon=12e00f obtained_from=cb9f40 -->
|  |  |
|---|---|
|  | ![Bracelet of Mediation](../assets/items/423.png) |
| **Item id** | `423` |
| **Kind** | Bracelet (56) |
| **Classes** | all |
| **Buy price** | 130 Gold |
| **Icon** | `ui/icons/Items_09.png` cell 7 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +8 | × (tier × 15 + reinforce level) | 2 |
| Mana | +7 | × (tier × 15 + reinforce level) | 33 |
| Health | +7 | × (tier × 15 + reinforce level) | 31 |
| Ability Power | +15 | × tier | 2 |
| Mana | +10 | × tier | 33 |
| Ability Power | +70 | flat | 2 |
| Mana | +125 | flat | 33 |
| Health | +125 | flat | 31 |

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
| 27 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 13 | 195 | 100 |
| 2027 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 13 | 195 | 100 |

### Where to get it

- Sold in [[wiki/shops/28-shop-28-no-npc|Shop 28 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/48-shop-48-no-npc|Shop 48 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/73-shop-73-no-npc|Shop 73 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/89-shop-89-no-npc|Shop 89 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/215-shop-215-no-npc|Shop 215 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/222-shop-222-no-npc|Shop 222 (no NPC)]] (no NPC found)
- Hero gacha pool 00, grade 1 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)
<!-- generated:end -->

## Notes

Drops in the border dungeons Chepa Village (127), Ghost Fortress (124), already reinforced at a random level (+0 up to +11 seen); Lv 1–4 dungeons drop it at tier 1, Lv 5–8 at tier 2 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §2, *image*). Sockets are rolled when the item drops ([[gameplay/items-and-crafting|Items and crafting]] §2).

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
