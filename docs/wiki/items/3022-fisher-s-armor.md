---
title: "Fisher's Armor"
type: "item"
id: 3022
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 3022"]
name_key: "ItemName_3022"
kind: 51
kind_name: "Armor"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 1
stats:
  - {"code": 6, "stat": "Armor", "value": 3, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 6, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 42, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 21, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 500, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 11, "scale": "flat"}
set: 3
reinforce: 42
icon: {"file": "Items_09.png", "index": 29}
obtained_from:
  - {"how": "craft", "recipe": 318}
  - {"how": "random_box", "box": 63}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=04fd4f type=d36ca9 id=8dfb87 sources=8954c4 name_key=261997 kind=b7eb6c kind_name=e687cb classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=356a19 stats=93b750 set=77de68 reinforce=92cfce icon=e32c67 obtained_from=24891c -->
|  |  |
|---|---|
|  | ![Fisher's Armor](wiki/assets/items/3022.png) |
| **Item id** | `3022` |
| **Kind** | Armor (51) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 1 |
| **Set** | Set 3 |
| **Icon** | `ui/icons/Items_09.png` cell 29 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +3 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +6 | × (tier × 15 + reinforce level) | 7 |
| Mana | +10 | × (tier × 15 + reinforce level) | 33 |
| Armor | +10 | × tier | 6 |
| Magic Resist | +10 | × tier | 7 |
| Mana | +10 | × tier | 33 |
| Armor | +42 | flat | 6 |
| Magic Resist | +21 | flat | 7 |
| Health | +500 | flat | 31 |
| Movement(%) | Movement +11% | flat | 105 |

### Set bonus

Pieces: [[wiki/items/3021-fisher-s-helmet|Fisher's Helmet]], [[wiki/items/3022-fisher-s-armor|Fisher's Armor]], [[wiki/items/3023-fisher-s-gloves|Fisher's Gloves]], [[wiki/items/3024-fisher-s-shoes|Fisher's Shoes]], [[wiki/items/3025-fisher-s-necklace|Fisher's Necklace]], [[wiki/items/3026-fisher-s-belt|Fisher's Belt]], [[wiki/items/3027-fisher-s-bracelet|Fisher's Bracelet]], [[wiki/items/3028-fisher-s-ring|Fisher's Ring]]

| pieces | bonus | value |
|---|---|---|
| 3 | Ability Power | +30 |
| 5 | Ability Power | +40 |
| 5 | Magic resist Penetration | +20 |
| 8 | Ability Power | +60 |
| 8 | Magic resist Penetration | +30 |

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
| 318 | [[wiki/items/2703-fin-of-fisher\|Fin of Fisher]] × 1, [[wiki/items/1933-essence-of-water\|Essence of Water]] × 1 | 0 | 60 |

### Where to get it

- In random box table row 63 (RandomBox.cdb; odds are server side)
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
