---
title: "Spirit Shoes"
type: "item"
id: 415
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 415"]
name_key: "ItemName_415"
kind: 53
kind_name: "Shoes"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 130}
cost_pair:
  - {"currency": 2, "amount": 130}
stats:
  - {"code": 6, "stat": "Armor", "value": 1, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 3, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 40, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 20, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 290, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 22, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_02.png", "index": 42}
obtained_from:
  - {"how": "shop", "shop": 44}
  - {"how": "shop", "shop": 55}
  - {"how": "shop", "shop": 60}
  - {"how": "shop", "shop": 93}
  - {"how": "shop", "shop": 100}
  - {"how": "shop", "shop": 105}
  - {"how": "shop", "shop": 108}
  - {"how": "shop", "shop": 113}
  - {"how": "shop", "shop": 117}
  - {"how": "shop", "shop": 222}
  - {"how": "craft", "recipe": 19}
  - {"how": "craft", "recipe": 2019}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=0cb41d type=d36ca9 id=8749f5 sources=b57fb2 name_key=a46ace kind=c5b76d kind_name=a64daf classes=92d079 bind=2be88c price=05bfea cost_pair=c1b652 stats=70c2ae reinforce=356a19 icon=fa8ae0 obtained_from=aa9b0e -->
|  |  |
|---|---|
|  | ![Spirit Shoes](wiki/assets/items/415.png) |
| **Item id** | `415` |
| **Kind** | Shoes (53) |
| **Classes** | all |
| **Buy price** | 130 Gold |
| **Icon** | `ui/icons/Items_02.png` cell 42 |

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
| 19 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 13 | 195 | 100 |
| 2019 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 13 | 195 | 100 |

### Where to get it

- Sold in [[wiki/shops/44-shop-44-no-npc|Shop 44 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/55-shop-55-no-npc|Shop 55 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/60-shop-60-no-npc|Shop 60 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/93-shop-93-no-npc|Shop 93 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/100-shop-100-no-npc|Shop 100 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/105-shop-105-no-npc|Shop 105 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/108-shop-108-no-npc|Shop 108 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/113-shop-113-no-npc|Shop 113 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/117-shop-117-no-npc|Shop 117 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/222-shop-222-no-npc|Shop 222 (no NPC)]] (no NPC found)
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
