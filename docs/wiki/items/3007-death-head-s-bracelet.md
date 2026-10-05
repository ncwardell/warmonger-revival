---
title: "Death Head's Bracelet"
type: "item"
id: 3007
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 3007"]
name_key: "ItemName_3007"
kind: 56
kind_name: "Bracelet"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 1
stats:
  - {"code": 1, "stat": "Attack", "value": 5, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 17, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
  - {"code": 32, "stat": "Health Regeneration", "value": 3, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 25, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 250, "scale": "flat"}
  - {"code": 32, "stat": "Health Regeneration", "value": 4, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 1, "scale": "flat"}
set: 1
reinforce: 42
icon: {"file": "Items_09.png", "index": 24}
obtained_from:
  - {"how": "craft", "recipe": 307}
  - {"how": "random_box", "box": 61}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=67d908 type=d36ca9 id=eb25f6 sources=08a103 name_key=d8e052 kind=54ceb9 kind_name=c2576a classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=356a19 stats=e856d4 set=356a19 reinforce=92cfce icon=e0e781 obtained_from=d2ee6f -->
|  |  |
|---|---|
|  | ![Death Head's Bracelet](../assets/items/3007.png) |
| **Item id** | `3007` |
| **Kind** | Bracelet (56) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 1 |
| **Set** | Set 1 |
| **Icon** | `ui/icons/Items_09.png` cell 24 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +5 | × (tier × 15 + reinforce level) | 1 |
| Health | +17 | × (tier × 15 + reinforce level) | 31 |
| Attack | +10 | × tier | 1 |
| Health Regeneration | +3 | × tier | 32 |
| Health | +20 | × tier | 31 |
| Attack | +25 | flat | 1 |
| Health | +250 | flat | 31 |
| Health Regeneration | +4 | flat | 32 |
| Mana Regeneration | +1 | flat | 34 |

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
| 307 | [[wiki/items/2701-deathhead-horn\|DeathHead Horn]] × 1, [[wiki/items/1930-essence-of-darkness\|essence of Darkness]] × 1 | 0 | 60 |

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
