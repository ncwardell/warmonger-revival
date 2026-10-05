---
title: "Barrier Ring"
type: "item"
id: 436
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 436"]
name_key: "ItemName_436"
kind: 57
kind_name: "Ring"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 120}
cost_pair:
  - {"currency": 2, "amount": 120}
stats:
  - {"code": 1, "stat": "Attack", "value": 3, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 15, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
  - {"code": 32, "stat": "Health Regeneration", "value": 3, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 20, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 250, "scale": "flat"}
  - {"code": 32, "stat": "Health Regeneration", "value": 4, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_06.png", "index": 8}
obtained_from:
  - {"how": "shop", "shop": 32}
  - {"how": "shop", "shop": 40}
  - {"how": "shop", "shop": 56}
  - {"how": "shop", "shop": 77}
  - {"how": "shop", "shop": 85}
  - {"how": "shop", "shop": 101}
  - {"how": "shop", "shop": 109}
  - {"how": "shop", "shop": 216}
  - {"how": "craft", "recipe": 40}
  - {"how": "craft", "recipe": 2040}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=2e1e0b type=d36ca9 id=6c4c04 sources=d0a9ba name_key=8944b3 kind=9109c8 kind_name=8ad6b7 classes=92d079 bind=2be88c price=401276 cost_pair=7638f4 stats=80adb2 reinforce=356a19 icon=b7bbb0 obtained_from=e6ab3a -->
|  |  |
|---|---|
|  | ![Barrier Ring](../assets/items/436.png) |
| **Item id** | `436` |
| **Kind** | Ring (57) |
| **Classes** | all |
| **Buy price** | 120 Gold |
| **Icon** | `ui/icons/Items_06.png` cell 8 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +3 | × (tier × 15 + reinforce level) | 1 |
| Health | +15 | × (tier × 15 + reinforce level) | 31 |
| Attack | +10 | × tier | 1 |
| Health Regeneration | +3 | × tier | 32 |
| Health | +20 | × tier | 31 |
| Attack | +20 | flat | 1 |
| Health | +250 | flat | 31 |
| Health Regeneration | +4 | flat | 32 |

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
| 40 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 11 | 165 | 100 |
| 2040 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 11 | 165 | 100 |

### Where to get it

- Sold in [[wiki/shops/32-shop-32-no-npc|Shop 32 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/40-shop-40-no-npc|Shop 40 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/56-shop-56-no-npc|Shop 56 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/77-shop-77-no-npc|Shop 77 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/85-shop-85-no-npc|Shop 85 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/101-shop-101-no-npc|Shop 101 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/109-shop-109-no-npc|Shop 109 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/216-shop-216-no-npc|Shop 216 (no NPC)]] (no NPC found)
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
