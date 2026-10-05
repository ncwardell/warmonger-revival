---
title: "Leviathan's Bracelet"
type: "item"
id: 3067
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 3067"]
name_key: "ItemName_3067"
kind: 56
kind_name: "Bracelet"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 1
stats:
  - {"code": 1, "stat": "Attack", "value": 4, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 8, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 5, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 8, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 13, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 7, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 25, "scale": "flat"}
  - {"code": 2, "stat": "Ability Power", "value": 75, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 200, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 125, "scale": "flat"}
set: 9
reinforce: 42
icon: {"file": "Items_10.png", "index": 42}
obtained_from:
  - {"how": "craft", "recipe": 371}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=8f69c3 type=d36ca9 id=7d7a2c sources=28a929 name_key=0fe2c4 kind=54ceb9 kind_name=c2576a classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=356a19 stats=e3c6fa set=0ade7c reinforce=92cfce icon=9c820d obtained_from=31a8fc -->
|  |  |
|---|---|
|  | ![Leviathan's Bracelet](../assets/items/3067.png) |
| **Item id** | `3067` |
| **Kind** | Bracelet (56) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 1 |
| **Set** | Set 9 |
| **Icon** | `ui/icons/Items_10.png` cell 42 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +4 | × (tier × 15 + reinforce level) | 1 |
| Ability Power | +8 | × (tier × 15 + reinforce level) | 2 |
| Mana | +5 | × (tier × 15 + reinforce level) | 33 |
| Attack | +8 | × tier | 1 |
| Ability Power | +13 | × tier | 2 |
| Mana | +7 | × tier | 33 |
| Attack | +25 | flat | 1 |
| Ability Power | +75 | flat | 2 |
| Health | +200 | flat | 31 |
| Mana | +125 | flat | 33 |

### Set bonus

Pieces: [[wiki/items/3061-leviathan-s-helmet|Leviathan's Helmet]], [[wiki/items/3062-leviathan-s-armor|Leviathan's Armor]], [[wiki/items/3063-leviathan-s-gloves|Leviathan's Gloves]], [[wiki/items/3064-leviathan-s-shoes|Leviathan's Shoes]], [[wiki/items/3065-leviathan-s-necklace|Leviathan's Necklace]], [[wiki/items/3066-leviathan-s-belt|Leviathan's Belt]], [[wiki/items/3067-leviathan-s-bracelet|Leviathan's Bracelet]], [[wiki/items/3068-leviathan-s-ring|Leviathan's Ring]]

| pieces | bonus | value |
|---|---|---|
| 3 | Attack | +40 |
| 3 | Ability Power | +40 |
| 5 | Attack | +60 |
| 5 | Ability Power | +60 |
| 8 | Armor Penetration | +25 |
| 8 | Magic resist Penetration | +25 |

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
| 371 | [[wiki/items/2707-horn-of-leviathan\|Horn of Leviathan]] × 1, [[wiki/items/1935-essence-of-light\|Essence of Light]] × 1 | 0 | 60 |

### Where to get it

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
