---
title: "Spector's Shoes"
type: "item"
id: 3044
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 3044"]
name_key: "ItemName_3044"
kind: 53
kind_name: "Shoes"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 1
stats:
  - {"code": 6, "stat": "Armor", "value": 1, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 3, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 40, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 20, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 290, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 22, "scale": "flat"}
set: 5
reinforce: 42
icon: {"file": "Items_09.png", "index": 55}
obtained_from:
  - {"how": "craft", "recipe": 336}
  - {"how": "random_box", "box": 65}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=85f4a1 type=d36ca9 id=9753e6 sources=ddbc00 name_key=482741 kind=c5b76d kind_name=a64daf classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=356a19 stats=70c2ae set=ac3478 reinforce=92cfce icon=da0c86 obtained_from=9dfdb3 -->
|  |  |
|---|---|
|  | ![Spector's Shoes](wiki/assets/items/3044.png) |
| **Item id** | `3044` |
| **Kind** | Shoes (53) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 1 |
| **Set** | Set 5 |
| **Icon** | `ui/icons/Items_09.png` cell 55 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +1 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +3 | × (tier × 15 + reinforce level) | 7 |
| Armor | +10 | × tier | 6 |
| Magic Resist | +10 | × tier | 7 |
| Armor | +40 | flat | 6 |
| Magic Resist | +20 | flat | 7 |
| Health | +290 | flat | 31 |
| Movement(%) | Movement +22% | flat | 105 |

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
| 336 | [[wiki/items/2705-bone-of-spector\|Bone of Spector]] × 1, [[wiki/items/1935-essence-of-light\|Essence of Light]] × 1 | 0 | 60 |

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
