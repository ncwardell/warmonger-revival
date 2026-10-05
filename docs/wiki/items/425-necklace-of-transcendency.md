---
title: "Necklace of Transcendency"
type: "item"
id: 425
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 425"]
name_key: "ItemName_425"
kind: 54
kind_name: "Necklace"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 100}
cost_pair:
  - {"currency": 2, "amount": 100}
stats:
  - {"code": 2, "stat": "Ability Power", "value": 4, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "level"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 1, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "tier"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 3, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 3, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 15, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 180, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 2, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_08.png", "index": 30}
obtained_from:
  - {"how": "shop", "shop": 31}
  - {"how": "shop", "shop": 35}
  - {"how": "shop", "shop": 51}
  - {"how": "shop", "shop": 76}
  - {"how": "shop", "shop": 80}
  - {"how": "shop", "shop": 96}
  - {"how": "shop", "shop": 212}
  - {"how": "shop", "shop": 213}
  - {"how": "craft", "recipe": 29}
  - {"how": "craft", "recipe": 2029}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=c40c0a type=d36ca9 id=7a6986 sources=d8c3b8 name_key=425820 kind=80e28a kind_name=7b4b74 classes=92d079 bind=2be88c price=936627 cost_pair=ebf7c2 stats=2f2ab5 reinforce=356a19 icon=639600 obtained_from=92a51b -->
|  |  |
|---|---|
|  | ![Necklace of Transcendency](wiki/assets/items/425.png) |
| **Item id** | `425` |
| **Kind** | Necklace (54) |
| **Classes** | all |
| **Buy price** | 100 Gold |
| **Icon** | `ui/icons/Items_08.png` cell 30 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +4 | × (tier × 15 + reinforce level) | 2 |
| Mana | +10 | × (tier × 15 + reinforce level) | 33 |
| Mana Regeneration | +1 | × (tier × 15 + reinforce level) | 34 |
| Ability Power | +10 | × tier | 2 |
| Mana Regeneration | +3 | × tier | 34 |
| Mana | +3 | × tier | 33 |
| Ability Power | +15 | flat | 2 |
| Mana | +180 | flat | 33 |
| Mana Regeneration | +2 | flat | 34 |

### Reinforcement

ItemSancMet row 1 (inferred from Item_Base +0x92), 1,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 1 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 1 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 1 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 2 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 5 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 7 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 29 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 15 | 225 | 100 |
| 2029 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 15 | 225 | 100 |

### Where to get it

- Sold in [[wiki/shops/31-shop-31-no-npc|Shop 31 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/35-shop-35-no-npc|Shop 35 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/51-shop-51-no-npc|Shop 51 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/76-shop-76-no-npc|Shop 76 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/80-shop-80-no-npc|Shop 80 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/96-shop-96-no-npc|Shop 96 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/212-shop-212-no-npc|Shop 212 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/213-shop-213-no-npc|Shop 213 (no NPC)]] (no NPC found)
- Hero gacha pool 00, grade 1 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)

### Mentioned in

- [[gameplay/gear-stats|Gear stats (Crush Online artifacts)]]
- [[gameplay/warmonger-forum|Warmonger forum (2018)]]
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
