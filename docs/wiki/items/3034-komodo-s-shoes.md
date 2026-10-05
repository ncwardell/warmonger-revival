---
title: "Komodo's Shoes"
type: "item"
id: 3034
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 3034"]
name_key: "ItemName_3034"
kind: 53
kind_name: "Shoes"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 1
stats:
  - {"code": 6, "stat": "Armor", "value": 2, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 2, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 40, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 20, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 280, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 26, "scale": "flat"}
set: 4
reinforce: 42
icon: {"file": "Items_09.png", "index": 47}
obtained_from:
  - {"how": "craft", "recipe": 328}
  - {"how": "random_box", "box": 64}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=9b338c type=d36ca9 id=62263d sources=305d56 name_key=b9ffbc kind=c5b76d kind_name=a64daf classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=356a19 stats=dee974 set=1b6453 reinforce=92cfce icon=3e9c72 obtained_from=e0f4f0 -->
|  |  |
|---|---|
|  | ![Komodo's Shoes](wiki/assets/items/3034.png) |
| **Item id** | `3034` |
| **Kind** | Shoes (53) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 1 |
| **Set** | Set 4 |
| **Icon** | `ui/icons/Items_09.png` cell 47 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +2 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +2 | × (tier × 15 + reinforce level) | 7 |
| Armor | +10 | × tier | 6 |
| Magic Resist | +10 | × tier | 7 |
| Armor | +40 | flat | 6 |
| Magic Resist | +20 | flat | 7 |
| Health | +280 | flat | 31 |
| Movement(%) | Movement +26% | flat | 105 |

### Set bonus

Pieces: [[wiki/items/3031-komodo-s-helmet|Komodo's Helmet]], [[wiki/items/3032-komodo-s-armor|Komodo's Armor]], [[wiki/items/3033-komodo-s-gloves|Komodo's Gloves]], [[wiki/items/3034-komodo-s-shoes|Komodo's Shoes]], [[wiki/items/3035-komodo-s-necklace|Komodo's Necklace]], [[wiki/items/3036-komodo-s-belt|Komodo's Belt]], [[wiki/items/3037-komodo-s-bracelet|Komodo's Bracelet]], [[wiki/items/3038-komodo-s-ring|Komodo's Ring]]

| pieces | bonus | value |
|---|---|---|
| 3 | Attack | +30 |
| 5 | Attack | +40 |
| 5 | Attack Speed(%) | Attack Speed +20% |
| 8 | Attack | +60 |
| 8 | Life Steal(%) | Life Steal +30% |

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
| 328 | [[wiki/items/2704-horn-of-komodo\|Horn of Komodo]] × 1, [[wiki/items/1932-essence-of-fire\|Essence of Fire]] × 1 | 0 | 60 |

### Where to get it

- In random box table row 64 (RandomBox.cdb; odds are server side)
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
