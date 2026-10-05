---
title: "Fame knight Armor"
type: "item"
id: 3502
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 3502"]
name_key: "ItemName_3502"
kind: 51
kind_name: "Armor"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 1
stats:
  - {"code": 6, "stat": "Armor", "value": 4, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 5, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 15, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 42, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 21, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 395, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 13, "scale": "flat"}
set: 7
reinforce: 42
icon: {"file": "Items_06.png", "index": 38}
obtained_from:
  - {"how": "craft", "recipe": 350}
  - {"how": "random_box", "box": 67}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=db296f type=d36ca9 id=60fddb sources=625130 name_key=60d982 kind=b7eb6c kind_name=e687cb classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=356a19 stats=1ae44d set=902ba3 reinforce=92cfce icon=14a29f obtained_from=131533 -->
|  |  |
|---|---|
|  | ![Fame knight Armor](../assets/items/3502.png) |
| **Item id** | `3502` |
| **Kind** | Armor (51) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 1 |
| **Set** | Set 7 |
| **Icon** | `ui/icons/Items_06.png` cell 38 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +4 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +5 | × (tier × 15 + reinforce level) | 7 |
| Health | +15 | × (tier × 15 + reinforce level) | 31 |
| Armor | +10 | × tier | 6 |
| Magic Resist | +10 | × tier | 7 |
| Health | +10 | × tier | 31 |
| Armor | +42 | flat | 6 |
| Magic Resist | +21 | flat | 7 |
| Health | +395 | flat | 31 |
| Movement(%) | Movement +13% | flat | 105 |

### Set bonus

Pieces: [[wiki/items/3501-fame-knight-helmet|Fame knight Helmet]], [[wiki/items/3502-fame-knight-armor|Fame knight Armor]], [[wiki/items/3503-fame-knight-gloves|Fame knight Gloves]], [[wiki/items/3504-fame-knight-shoes|Fame knight Shoes]], [[wiki/items/3505-fame-knight-necklace|Fame knight Necklace]], [[wiki/items/3506-fame-knight-belt|Fame knight Belt]], [[wiki/items/3507-fame-knight-bracelet|Fame knight Bracelet]], [[wiki/items/3508-fame-knight-ring|Fame knight Ring]]

| pieces | bonus | value |
|---|---|---|
| 3 | Attack | +30 |
| 5 | Attack | +40 |
| 5 | Attack Speed(%) | Attack Speed +20% |
| 8 | Attack | +60 |
| 8 | PvP Attack | +30 |

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
| 350 | [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 2, [[wiki/items/854-shining-passion\|Shining Passion]] × 2 | 0 | 60 |

### Where to get it

- In random box table row 67 (RandomBox.cdb; odds are server side)
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
