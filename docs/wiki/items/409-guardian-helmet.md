---
title: "Guardian Helmet"
type: "item"
id: 409
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 409"]
name_key: "ItemName_409"
kind: 50
kind_name: "Helmet"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 100}
cost_pair:
  - {"currency": 2, "amount": 100}
stats:
  - {"code": 6, "stat": "Armor", "value": 4, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 3, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 40, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 20, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 75, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 9, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_09.png", "index": 36}
obtained_from:
  - {"how": "shop", "shop": 27}
  - {"how": "shop", "shop": 35}
  - {"how": "shop", "shop": 47}
  - {"how": "shop", "shop": 72}
  - {"how": "shop", "shop": 80}
  - {"how": "shop", "shop": 88}
  - {"how": "shop", "shop": 211}
  - {"how": "shop", "shop": 213}
  - {"how": "shop", "shop": 221}
  - {"how": "craft", "recipe": 13}
  - {"how": "craft", "recipe": 2013}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=03b69b type=d36ca9 id=3352d0 sources=3e4e41 name_key=c0157e kind=e1822d kind_name=c90f98 classes=92d079 bind=2be88c price=936627 cost_pair=ebf7c2 stats=51114c reinforce=356a19 icon=8a212e obtained_from=f06fea -->
|  |  |
|---|---|
|  | ![Guardian Helmet](wiki/assets/items/409.png) |
| **Item id** | `409` |
| **Kind** | Helmet (50) |
| **Classes** | all |
| **Buy price** | 100 Gold |
| **Icon** | `ui/icons/Items_09.png` cell 36 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +4 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +3 | × (tier × 15 + reinforce level) | 7 |
| Health | +20 | × (tier × 15 + reinforce level) | 31 |
| Armor | +10 | × tier | 6 |
| Magic Resist | +10 | × tier | 7 |
| Health | +10 | × tier | 31 |
| Armor | +40 | flat | 6 |
| Magic Resist | +20 | flat | 7 |
| Mana | +75 | flat | 33 |
| Movement(%) | Movement +9% | flat | 105 |

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
| 13 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |
| 2013 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |

### Where to get it

- Sold in [[wiki/shops/27-shop-27-no-npc|Shop 27 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/35-shop-35-no-npc|Shop 35 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/47-shop-47-no-npc|Shop 47 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/72-shop-72-no-npc|Shop 72 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/80-shop-80-no-npc|Shop 80 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/88-shop-88-no-npc|Shop 88 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/211-shop-211-no-npc|Shop 211 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/213-shop-213-no-npc|Shop 213 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/221-shop-221-no-npc|Shop 221 (no NPC)]] (no NPC found)
- Hero gacha pool 00, grade 2 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]]
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
