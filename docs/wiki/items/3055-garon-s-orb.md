---
title: "Garon's Orb"
type: "item"
id: 3055
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 3055"]
name_key: "ItemName_3055"
kind: 54
kind_name: "Necklace"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 1
stats:
  - {"code": 1, "stat": "Attack", "value": 5, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 21, "scale": "level"}
  - {"code": 32, "stat": "Health Regeneration", "value": 1, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "tier"}
  - {"code": 32, "stat": "Health Regeneration", "value": 2, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 42, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 230, "scale": "flat"}
  - {"code": 32, "stat": "Health Regeneration", "value": 8, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 1, "scale": "flat"}
set: 6
reinforce: 42
icon: {"file": "Items_10.png", "index": 0}
obtained_from:
  - {"how": "craft", "recipe": 345}
  - {"how": "random_box", "box": 66}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=dcbe39 type=d36ca9 id=1762fc sources=1e0f71 name_key=03c838 kind=80e28a kind_name=7b4b74 classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=356a19 stats=5d6403 set=c1dfd9 reinforce=92cfce icon=010ba7 obtained_from=6b2bd1 -->
|  |  |
|---|---|
|  | ![Garon's Orb](../assets/items/3055.png) |
| **Item id** | `3055` |
| **Kind** | Necklace (54) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 1 |
| **Set** | Set 6 |
| **Icon** | `ui/icons/Items_10.png` cell 0 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +5 | × (tier × 15 + reinforce level) | 1 |
| Health | +21 | × (tier × 15 + reinforce level) | 31 |
| Health Regeneration | +1 | × (tier × 15 + reinforce level) | 32 |
| Health | +20 | × tier | 31 |
| Health Regeneration | +2 | × tier | 32 |
| Attack | +42 | flat | 1 |
| Health | +230 | flat | 31 |
| Health Regeneration | +8 | flat | 32 |
| Mana Regeneration | +1 | flat | 34 |

### Set bonus

Pieces: [[wiki/items/3051-garon-s-helmet|Garon's Helmet]], [[wiki/items/3052-garon-s-armor|Garon's Armor]], [[wiki/items/3053-garon-s-gloves|Garon's Gloves]], [[wiki/items/3054-garon-s-shoes|Garon's Shoes]], [[wiki/items/3055-garon-s-orb|Garon's Orb]], [[wiki/items/3056-garon-s-belt|Garon's Belt]], [[wiki/items/3057-garon-s-bracelet|Garon's Bracelet]], [[wiki/items/3058-garon-s-ring|Garon's Ring]]

| pieces | bonus | value |
|---|---|---|
| 3 | Health | +300 |
| 5 | Health | +400 |
| 5 | Health Regeneration | +50 |
| 8 | Health | +600 |
| 8 | Health Regeneration | +70 |

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
| 345 | [[wiki/items/2706-horn-of-garon\|Horn of Garon]] × 1, [[wiki/items/1934-essence-of-earth\|Essence of Earth]] × 1 | 0 | 60 |

### Where to get it

- In random box table row 66 (RandomBox.cdb; odds are server side)
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
