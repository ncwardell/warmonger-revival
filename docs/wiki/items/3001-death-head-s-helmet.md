---
title: "Death Head's Helmet"
type: "item"
id: 3001
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 3001"]
name_key: "ItemName_3001"
kind: 50
kind_name: "Helmet"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 1
stats:
  - {"code": 6, "stat": "Armor", "value": 5, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 4, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 40, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 20, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 85, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 13, "scale": "flat"}
set: 1
reinforce: 42
icon: {"file": "Items_09.png", "index": 12}
obtained_from:
  - {"how": "craft", "recipe": 301}
  - {"how": "random_box", "box": 61}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=bd0c0e type=d36ca9 id=49042c sources=43355b name_key=87bcb0 kind=e1822d kind_name=c90f98 classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=356a19 stats=5d0217 set=356a19 reinforce=92cfce icon=788408 obtained_from=0f1c06 -->
|  |  |
|---|---|
|  | ![Death Head's Helmet](../assets/items/3001.png) |
| **Item id** | `3001` |
| **Kind** | Helmet (50) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 1 |
| **Set** | Set 1 |
| **Icon** | `ui/icons/Items_09.png` cell 12 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +5 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +4 | × (tier × 15 + reinforce level) | 7 |
| Health | +10 | × (tier × 15 + reinforce level) | 31 |
| Armor | +10 | × tier | 6 |
| Magic Resist | +10 | × tier | 7 |
| Health | +10 | × tier | 31 |
| Armor | +40 | flat | 6 |
| Magic Resist | +20 | flat | 7 |
| Mana | +85 | flat | 33 |
| Movement(%) | Movement +13% | flat | 105 |

### Set bonus

Pieces: [[wiki/items/3001-death-head-s-helmet|Death Head's Helmet]], [[wiki/items/3002-death-head-s-armor|Death Head's Armor]], [[wiki/items/3003-death-head-s-gloves|Death Head's Gloves]], [[wiki/items/3004-death-head-s-shoes|Death Head's Shoes]], [[wiki/items/3005-death-head-s-necklace|Death Head's Necklace]], [[wiki/items/3006-death-head-s-belt|Death Head's Belt]], [[wiki/items/3007-death-head-s-bracelet|Death Head's Bracelet]], [[wiki/items/3008-death-head-s-ring|Death Head's Ring]]

| pieces | bonus | value |
|---|---|---|
| 3 | Attack | +30 |
| 5 | Attack | +40 |
| 5 | Critical Strike Deal | +20 |
| 8 | Attack | +60 |
| 8 | Critical Strike +(%) | Critical Strike +40% |

### Reinforcement

ItemSancMet row 42 (inferred from Item_Base +0x92), 5,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 6 |
| 2 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 8 |
| 3 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 8 |
| 4 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 10 |
| 5 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 10 |
| 6 | [[wiki/items/607-blue-passion-fragments-a\|Blue Passion Fragments (A)]] × 15 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 301 | [[wiki/items/2701-deathhead-horn\|DeathHead Horn]] × 1, [[wiki/items/1930-essence-of-darkness\|essence of Darkness]] × 1 | 0 | 60 |

### Where to get it

- In random box table row 61 (RandomBox.cdb; odds are server side)
- Hero gacha pool 04, grade 2 (Gacha_04.cdb; odds are server side)
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
