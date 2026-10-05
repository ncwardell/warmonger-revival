---
title: "Fame warrior Helmet"
type: "item"
id: 3511
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 3511"]
name_key: "ItemName_3511"
kind: 50
kind_name: "Helmet"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 1
stats:
  - {"code": 6, "stat": "Armor", "value": 6, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 3, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 40, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 20, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 75, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 9, "scale": "flat"}
set: 8
reinforce: 42
icon: {"file": "Items_08.png", "index": 36}
obtained_from:
  - {"how": "craft", "recipe": 357}
  - {"how": "random_box", "box": 68}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=65b875 type=d36ca9 id=ba4234 sources=8372e6 name_key=c19af6 kind=e1822d kind_name=c90f98 classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=356a19 stats=8dba95 set=fe5dbb reinforce=92cfce icon=ce9e12 obtained_from=ab524c -->
|  |  |
|---|---|
|  | ![Fame warrior Helmet](../assets/items/3511.png) |
| **Item id** | `3511` |
| **Kind** | Helmet (50) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 1 |
| **Set** | Set 8 |
| **Icon** | `ui/icons/Items_08.png` cell 36 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +6 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +3 | × (tier × 15 + reinforce level) | 7 |
| Health | +20 | × (tier × 15 + reinforce level) | 31 |
| Armor | +10 | × tier | 6 |
| Magic Resist | +10 | × tier | 7 |
| Health | +10 | × tier | 31 |
| Armor | +40 | flat | 6 |
| Magic Resist | +20 | flat | 7 |
| Mana | +75 | flat | 33 |
| Movement(%) | Movement +9% | flat | 105 |

### Set bonus

Pieces: [[wiki/items/3511-fame-warrior-helmet|Fame warrior Helmet]], [[wiki/items/3512-fame-warrior-armor|Fame warrior Armor]], [[wiki/items/3513-fame-warrior-gloves|Fame warrior Gloves]], [[wiki/items/3514-fame-warrior-shoes|Fame warrior Shoes]], [[wiki/items/3515-fame-warrior-necklace|Fame warrior Necklace]], [[wiki/items/3516-fame-warrior-belt|Fame warrior Belt]], [[wiki/items/3517-fame-warrior-bracelet|Fame warrior Bracelet]], [[wiki/items/3518-fame-warrior-ring|Fame warrior Ring]]

| pieces | bonus | value |
|---|---|---|
| 3 | Armor | +30 |
| 5 | Magic Resist | +30 |
| 8 | Armor | +40 |
| 8 | Magic Resist | +40 |
| 8 | PvP Armor | +30 |

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
| 357 | [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 2, [[wiki/items/854-shining-passion\|Shining Passion]] × 2 | 0 | 60 |

### Where to get it

- In random box table row 68 (RandomBox.cdb; odds are server side)
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
