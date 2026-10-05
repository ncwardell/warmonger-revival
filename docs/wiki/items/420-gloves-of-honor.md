---
title: "Gloves of Honor"
type: "item"
id: 420
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 420"]
name_key: "ItemName_420"
kind: 52
kind_name: "Gloves"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 120}
cost_pair:
  - {"currency": 2, "amount": 120}
stats:
  - {"code": 6, "stat": "Armor", "value": 3, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 3, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 40, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 20, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 30, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 13, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_06.png", "index": 26}
obtained_from:
  - {"how": "shop", "shop": 32}
  - {"how": "shop", "shop": 36}
  - {"how": "shop", "shop": 52}
  - {"how": "shop", "shop": 77}
  - {"how": "shop", "shop": 81}
  - {"how": "shop", "shop": 97}
  - {"how": "shop", "shop": 214}
  - {"how": "shop", "shop": 216}
  - {"how": "craft", "recipe": 24}
  - {"how": "craft", "recipe": 2024}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=007156 type=d36ca9 id=7a9556 sources=152559 name_key=8adb94 kind=a93349 kind_name=f6564c classes=92d079 bind=2be88c price=401276 cost_pair=7638f4 stats=0ca990 reinforce=356a19 icon=8ad561 obtained_from=2d14dc -->
|  |  |
|---|---|
|  | ![Gloves of Honor](wiki/assets/items/420.png) |
| **Item id** | `420` |
| **Kind** | Gloves (52) |
| **Classes** | all |
| **Buy price** | 120 Gold |
| **Icon** | `ui/icons/Items_06.png` cell 26 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +3 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +3 | × (tier × 15 + reinforce level) | 7 |
| Mana | +10 | × (tier × 15 + reinforce level) | 33 |
| Armor | +10 | × tier | 6 |
| Magic Resist | +10 | × tier | 7 |
| Mana | +10 | × tier | 33 |
| Armor | +40 | flat | 6 |
| Magic Resist | +20 | flat | 7 |
| Mana | +30 | flat | 33 |
| Movement(%) | Movement +13% | flat | 105 |

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
| 24 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 12 | 180 | 100 |
| 2024 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 12 | 180 | 100 |

### Where to get it

- Sold in [[wiki/shops/32-shop-32-no-npc|Shop 32 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/36-shop-36-no-npc|Shop 36 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/52-shop-52-no-npc|Shop 52 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/77-shop-77-no-npc|Shop 77 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/81-shop-81-no-npc|Shop 81 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/97-shop-97-no-npc|Shop 97 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/214-shop-214-no-npc|Shop 214 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/216-shop-216-no-npc|Shop 216 (no NPC)]] (no NPC found)
- Hero gacha pool 00, grade 2 (Gacha_00.cdb; odds are server side)
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
