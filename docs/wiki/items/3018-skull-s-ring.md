---
title: "Skull's Ring"
type: "item"
id: 3018
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 3018", "image: [[gameplay/skull-artifact-set]] (Crush Online tooltips, Feb 2017)"]
name_key: "ItemName_3018"
kind: 57
kind_name: "Ring"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rarity: 1
stats:
  - {"code": 6, "stat": "Armor", "value": 2, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 5, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 57, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 42, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 140, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 1, "scale": "flat"}
set: 2
reinforce: 42
icon: {"file": "Items_09.png", "index": 27}
obtained_from:
  - {"how": "craft", "recipe": 316}
  - {"how": "random_box", "box": 62}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=02c811 type=d36ca9 id=f5e707 sources=a9dc5f name_key=6a7159 kind=9109c8 kind_name=8ad6b7 classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rarity=356a19 stats=225ab5 set=da4b92 reinforce=92cfce icon=c28d91 obtained_from=57ae3d -->
|  |  |
|---|---|
|  | ![Skull's Ring](wiki/assets/items/3018.png) |
| **Item id** | `3018` |
| **Kind** | Ring (57) |
| **Category** | [[wiki/items/accessories\|Accessories]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rarity (guessed column)** | 1 |
| **Set** | Set 2 |
| **Icon** | `ui/icons/Items_09.png` cell 27 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +2 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +5 | × (tier × 15 + reinforce level) | 7 |
| Mana | +10 | × (tier × 15 + reinforce level) | 33 |
| Armor | +10 | × tier | 6 |
| Magic Resist | +10 | × tier | 7 |
| Mana | +10 | × tier | 33 |
| Armor | +57 | flat | 6 |
| Magic Resist | +42 | flat | 7 |
| Mana | +140 | flat | 33 |
| Mana Regeneration | +1 | flat | 34 |

### Set bonus

Pieces: [[wiki/items/3011-skull-s-helmet|Skull's Helmet]], [[wiki/items/3012-skull-s-armor|Skull's Armor]], [[wiki/items/3013-skull-s-gloves|Skull's Gloves]], [[wiki/items/3014-skull-s-shoes|Skull's Shoes]], [[wiki/items/3015-skull-s-necklace|Skull's Necklace]], [[wiki/items/3016-skull-s-belt|Skull's Belt]], [[wiki/items/3017-skull-s-bracelet|Skull's Bracelet]], [[wiki/items/3018-skull-s-ring|Skull's Ring]]

| pieces | bonus | value |
|---|---|---|
| 3 | Armor | +30 |
| 5 | Magic Resist | +30 |
| 8 | Armor | +50 |
| 8 | Magic Resist | +50 |

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
| 316 | [[wiki/items/2702-skull-horn\|Skull Horn]] × 1, [[wiki/items/1930-essence-of-darkness\|essence of Darkness]] × 1 | 0 | 60 |

### Where to get it

- In random box table row 62 (RandomBox.cdb; odds are server side)
- Hero gacha pool 04, grade 2 (Gacha_04.cdb; odds are server side)

### Mentioned in

- [[gameplay/skull-artifact-set|Skull artifact set tooltips (Crush Online, Feb 2017)]]
<!-- generated:end -->

## Notes

Crush Online called this piece **Ring of Skull** (Feb 2017 tooltip). The Crush set bonus was offensive (3 pieces Attack +30, which a bug report said pushed players to the 1,000 Attack cap); Warmonger made it Armor / Magic Resist ([[gameplay/skull-artifact-set|Skull artifact set]], *image*; WM 0809 values in [[gameplay/reinforce-and-runes|Reinforce and runes]] §6).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- image: [[gameplay/skull-artifact-set]] (Crush Online tooltips, Feb 2017)

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
