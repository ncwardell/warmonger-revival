---
title: "Bandolier Ring"
type: "item"
id: 432
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 432"]
name_key: "ItemName_432"
kind: 57
kind_name: "Ring"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 120}
cost_pair:
  - {"currency": 2, "amount": 120}
stats:
  - {"code": 1, "stat": "Attack", "value": 4, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "tier"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 1, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 80, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 250, "scale": "flat"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 3, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_09.png", "index": 5}
obtained_from:
  - {"how": "shop", "shop": 44}
  - {"how": "shop", "shop": 60}
  - {"how": "shop", "shop": 93}
  - {"how": "shop", "shop": 105}
  - {"how": "shop", "shop": 113}
  - {"how": "shop", "shop": 117}
  - {"how": "craft", "recipe": 36}
  - {"how": "craft", "recipe": 2036}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=606bda type=d36ca9 id=a2092f sources=8832a1 name_key=f8b49c kind=9109c8 kind_name=8ad6b7 classes=92d079 bind=2be88c price=401276 cost_pair=7638f4 stats=84f907 reinforce=356a19 icon=eb30cb obtained_from=e5fcff -->
|  |  |
|---|---|
|  | ![Bandolier Ring](wiki/assets/items/432.png) |
| **Item id** | `432` |
| **Kind** | Ring (57) |
| **Classes** | all |
| **Buy price** | 120 Gold |
| **Icon** | `ui/icons/Items_09.png` cell 5 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +4 | × (tier × 15 + reinforce level) | 1 |
| Health | +10 | × (tier × 15 + reinforce level) | 31 |
| Attack | +10 | × tier | 1 |
| Health | +20 | × tier | 31 |
| Attack Speed(%) | Attack Speed +1% | × tier | 103 |
| Attack | +80 | flat | 1 |
| Health | +250 | flat | 31 |
| Attack Speed(%) | Attack Speed +3% | flat | 103 |

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
| 36 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 11 | 165 | 100 |
| 2036 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 11 | 165 | 100 |

### Where to get it

- Sold in [[wiki/shops/44-shop-44-no-npc|Shop 44 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/60-shop-60-no-npc|Shop 60 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/93-shop-93-no-npc|Shop 93 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/105-shop-105-no-npc|Shop 105 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/113-shop-113-no-npc|Shop 113 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/117-shop-117-no-npc|Shop 117 (no NPC)]] (no NPC found)
- Hero gacha pool 00, grade 1 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)
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
