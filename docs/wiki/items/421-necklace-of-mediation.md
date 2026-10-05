---
title: "Necklace of Mediation"
type: "item"
id: 421
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 421"]
name_key: "ItemName_421"
kind: 54
kind_name: "Necklace"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 100}
cost_pair:
  - {"currency": 2, "amount": 100}
stats:
  - {"code": 2, "stat": "Ability Power", "value": 5, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 7, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 7, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 15, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 70, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 125, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 125, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_08.png", "index": 56}
obtained_from:
  - {"how": "shop", "shop": 27}
  - {"how": "shop", "shop": 47}
  - {"how": "shop", "shop": 72}
  - {"how": "shop", "shop": 88}
  - {"how": "shop", "shop": 211}
  - {"how": "craft", "recipe": 25}
  - {"how": "craft", "recipe": 2025}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=623426 type=d36ca9 id=1c76c4 sources=1789b5 name_key=63e5f0 kind=80e28a kind_name=7b4b74 classes=92d079 bind=2be88c price=936627 cost_pair=ebf7c2 stats=3dba2f reinforce=356a19 icon=46fa1a obtained_from=e67239 -->
|  |  |
|---|---|
|  | ![Necklace of Mediation](wiki/assets/items/421.png) |
| **Item id** | `421` |
| **Kind** | Necklace (54) |
| **Classes** | all |
| **Buy price** | 100 Gold |
| **Icon** | `ui/icons/Items_08.png` cell 56 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +5 | × (tier × 15 + reinforce level) | 2 |
| Mana | +7 | × (tier × 15 + reinforce level) | 33 |
| Health | +7 | × (tier × 15 + reinforce level) | 31 |
| Ability Power | +15 | × tier | 2 |
| Mana | +10 | × tier | 33 |
| Ability Power | +70 | flat | 2 |
| Mana | +125 | flat | 33 |
| Health | +125 | flat | 31 |

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
| 25 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 15 | 225 | 100 |
| 2025 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 15 | 225 | 100 |

### Where to get it

- Sold in [[wiki/shops/27-shop-27-no-npc|Shop 27 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/47-shop-47-no-npc|Shop 47 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/72-shop-72-no-npc|Shop 72 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/88-shop-88-no-npc|Shop 88 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/211-shop-211-no-npc|Shop 211 (no NPC)]] (no NPC found)
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
