---
title: "Spector's Bracelet"
type: "item"
id: 3047
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 3047"]
name_key: "ItemName_3047"
kind: 56
kind_name: "Bracelet"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 1
stats:
  - {"code": 2, "stat": "Ability Power", "value": 9, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 8, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 9, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 15, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 75, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 125, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 125, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 1, "scale": "flat"}
set: 5
reinforce: 42
icon: {"file": "Items_09.png", "index": 58}
obtained_from:
  - {"how": "craft", "recipe": 339}
  - {"how": "random_box", "box": 65}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=c94a2e type=d36ca9 id=e956d3 sources=3df86e name_key=e97573 kind=54ceb9 kind_name=c2576a classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=356a19 stats=036c9e set=ac3478 reinforce=92cfce icon=828e5d obtained_from=1ac9e8 -->
|  |  |
|---|---|
|  | ![Spector's Bracelet](wiki/assets/items/3047.png) |
| **Item id** | `3047` |
| **Kind** | Bracelet (56) |
| **Category** | [[wiki/items/accessories\|Accessories]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 1 |
| **Set** | Set 5 |
| **Icon** | `ui/icons/Items_09.png` cell 58 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +9 | × (tier × 15 + reinforce level) | 2 |
| Mana | +8 | × (tier × 15 + reinforce level) | 33 |
| Health | +9 | × (tier × 15 + reinforce level) | 31 |
| Ability Power | +15 | × tier | 2 |
| Mana | +10 | × tier | 33 |
| Ability Power | +75 | flat | 2 |
| Mana | +125 | flat | 33 |
| Health | +125 | flat | 31 |
| Mana Regeneration | +1 | flat | 34 |

### Set bonus

Pieces: [[wiki/items/3041-spector-s-earring|Spector's Earring]], [[wiki/items/3042-spector-s-armor|Spector's Armor]], [[wiki/items/3043-spector-s-gloves|Spector's Gloves]], [[wiki/items/3044-spector-s-shoes|Spector's Shoes]], [[wiki/items/3045-spector-s-necklace|Spector's Necklace]], [[wiki/items/3046-spector-s-belt|Spector's Belt]], [[wiki/items/3047-spector-s-bracelet|Spector's Bracelet]], [[wiki/items/3048-spector-s-ring|Spector's Ring]]

| pieces | bonus | value |
|---|---|---|
| 3 | Ability Power | +30 |
| 5 | Ability Power | +40 |
| 5 | Cooldown Reduction(%) | Cooldown Reduction +10% |
| 8 | Ability Power | +60 |
| 8 | Cooldown Reduction(%) | Cooldown Reduction +10% |

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
| 339 | [[wiki/items/2705-bone-of-spector\|Bone of Spector]] × 1, [[wiki/items/1935-essence-of-light\|Essence of Light]] × 1 | 0 | 60 |

### Where to get it

- In random box table row 65 (RandomBox.cdb; odds are server side)
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
