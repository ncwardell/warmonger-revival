---
title: "Shoes of Honor"
type: "item"
id: 419
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 419"]
name_key: "ItemName_419"
kind: 53
kind_name: "Shoes"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 130}
cost_pair:
  - {"currency": 2, "amount": 130}
stats:
  - {"code": 6, "stat": "Armor", "value": 2, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 2, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 40, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 20, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 280, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 26, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_07.png", "index": 53}
obtained_from:
  - {"how": "shop", "shop": 32}
  - {"how": "shop", "shop": 36}
  - {"how": "shop", "shop": 52}
  - {"how": "shop", "shop": 77}
  - {"how": "shop", "shop": 81}
  - {"how": "shop", "shop": 97}
  - {"how": "shop", "shop": 214}
  - {"how": "shop", "shop": 216}
  - {"how": "shop", "shop": 223}
  - {"how": "craft", "recipe": 23}
  - {"how": "craft", "recipe": 2023}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=48182a type=d36ca9 id=1f0037 sources=0eb174 name_key=9da94e kind=c5b76d kind_name=a64daf classes=92d079 bind=2be88c price=05bfea cost_pair=c1b652 stats=dee974 reinforce=356a19 icon=dbd5a1 obtained_from=985213 -->
|  |  |
|---|---|
|  | ![Shoes of Honor](../assets/items/419.png) |
| **Item id** | `419` |
| **Kind** | Shoes (53) |
| **Classes** | all |
| **Buy price** | 130 Gold |
| **Icon** | `ui/icons/Items_07.png` cell 53 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +2 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +2 | × (tier × 15 + reinforce level) | 7 |
| Armor | +10 | × tier | 6 |
| Magic Resist | +10 | × tier | 7 |
| Armor | +40 | flat | 6 |
| Magic Resist | +20 | flat | 7 |
| Health | +280 | flat | 31 |
| Movement(%) | Movement +26% | flat | 105 |

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
| 23 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 13 | 195 | 100 |
| 2023 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 13 | 195 | 100 |

### Where to get it

- Sold in [[wiki/shops/32-shop-32-no-npc|Shop 32 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/36-shop-36-no-npc|Shop 36 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/52-shop-52-no-npc|Shop 52 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/77-shop-77-no-npc|Shop 77 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/81-shop-81-no-npc|Shop 81 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/97-shop-97-no-npc|Shop 97 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/214-shop-214-no-npc|Shop 214 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/216-shop-216-no-npc|Shop 216 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/223-shop-223-no-npc|Shop 223 (no NPC)]] (no NPC found)
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
