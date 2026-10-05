---
title: "Fame knight Ring"
type: "item"
id: 3508
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 3508"]
name_key: "ItemName_3508"
kind: 57
kind_name: "Ring"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 1
stats:
  - {"code": 1, "stat": "Attack", "value": 5, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "tier"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 1, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 85, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 250, "scale": "flat"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 4, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 1, "scale": "flat"}
set: 7
reinforce: 42
icon: {"file": "Items_06.png", "index": 43}
obtained_from:
  - {"how": "craft", "recipe": 356}
  - {"how": "random_box", "box": 67}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=89312b type=d36ca9 id=fb77ce sources=ceec93 name_key=f93882 kind=9109c8 kind_name=8ad6b7 classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=356a19 stats=a7195f set=902ba3 reinforce=92cfce icon=5ae6b3 obtained_from=3200d0 -->
|  |  |
|---|---|
|  | ![Fame knight Ring](wiki/assets/items/3508.png) |
| **Item id** | `3508` |
| **Kind** | Ring (57) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 1 |
| **Set** | Set 7 |
| **Icon** | `ui/icons/Items_06.png` cell 43 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +5 | × (tier × 15 + reinforce level) | 1 |
| Health | +10 | × (tier × 15 + reinforce level) | 31 |
| Attack | +10 | × tier | 1 |
| Health | +20 | × tier | 31 |
| Attack Speed(%) | Attack Speed +1% | × tier | 103 |
| Attack | +85 | flat | 1 |
| Health | +250 | flat | 31 |
| Attack Speed(%) | Attack Speed +4% | flat | 103 |
| Mana Regeneration | +1 | flat | 34 |

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
| 356 | [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 2, [[wiki/items/854-shining-passion\|Shining Passion]] × 2 | 0 | 60 |

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
