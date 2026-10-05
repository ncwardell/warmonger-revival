---
title: "Leviathan's Necklace"
type: "item"
id: 3065
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 3065"]
name_key: "ItemName_3065"
kind: 54
kind_name: "Necklace"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 1
stats:
  - {"code": 1, "stat": "Attack", "value": 7, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 5, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 12, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 8, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 13, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 15, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 25, "scale": "flat"}
  - {"code": 2, "stat": "Ability Power", "value": 75, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 200, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 125, "scale": "flat"}
set: 9
reinforce: 42
icon: {"file": "Items_10.png", "index": 40}
obtained_from:
  - {"how": "craft", "recipe": 369}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=853e21 type=d36ca9 id=aa5006 sources=f689c8 name_key=30010b kind=80e28a kind_name=7b4b74 classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=356a19 stats=0a826d set=0ade7c reinforce=92cfce icon=4f938b obtained_from=42e1f6 -->
|  |  |
|---|---|
|  | ![Leviathan's Necklace](wiki/assets/items/3065.png) |
| **Item id** | `3065` |
| **Kind** | Necklace (54) |
| **Category** | [[wiki/items/accessories\|Accessories]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 1 |
| **Set** | Set 9 |
| **Icon** | `ui/icons/Items_10.png` cell 40 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +7 | × (tier × 15 + reinforce level) | 1 |
| Ability Power | +5 | × (tier × 15 + reinforce level) | 2 |
| Health | +12 | × (tier × 15 + reinforce level) | 31 |
| Attack | +8 | × tier | 1 |
| Ability Power | +13 | × tier | 2 |
| Health | +15 | × tier | 31 |
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
| 369 | [[wiki/items/2707-horn-of-leviathan\|Horn of Leviathan]] × 1, [[wiki/items/1935-essence-of-light\|Essence of Light]] × 1 | 0 | 60 |

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
