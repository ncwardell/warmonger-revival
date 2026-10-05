---
title: "Bandolier Belt"
type: "item"
id: 430
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 430"]
name_key: "ItemName_430"
kind: 55
kind_name: "Belt"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 150}
cost_pair:
  - {"currency": 2, "amount": 150}
stats:
  - {"code": 1, "stat": "Attack", "value": 8, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "tier"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 1, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 80, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 250, "scale": "flat"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 3, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_03.png", "index": 4}
obtained_from:
  - {"how": "shop", "shop": 43}
  - {"how": "shop", "shop": 59}
  - {"how": "shop", "shop": 92}
  - {"how": "shop", "shop": 104}
  - {"how": "shop", "shop": 112}
  - {"how": "shop", "shop": 116}
  - {"how": "shop", "shop": 223}
  - {"how": "craft", "recipe": 34}
  - {"how": "craft", "recipe": 2034}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=c599bf type=d36ca9 id=f8c024 sources=10e076 name_key=b3f63b kind=8effee kind_name=ddf027 classes=92d079 bind=2be88c price=6d19d1 cost_pair=ca8a4e stats=f18b5e reinforce=356a19 icon=bd3edc obtained_from=5d1e0d -->
|  |  |
|---|---|
|  | ![Bandolier Belt](../assets/items/430.png) |
| **Item id** | `430` |
| **Kind** | Belt (55) |
| **Classes** | all |
| **Buy price** | 150 Gold |
| **Icon** | `ui/icons/Items_03.png` cell 4 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +8 | × (tier × 15 + reinforce level) | 1 |
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
| 34 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 20 | 300 | 100 |
| 2034 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 20 | 300 | 100 |

### Where to get it

- Sold in [[wiki/shops/43-shop-43-no-npc|Shop 43 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/59-shop-59-no-npc|Shop 59 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/92-shop-92-no-npc|Shop 92 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/104-shop-104-no-npc|Shop 104 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/112-shop-112-no-npc|Shop 112 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/116-shop-116-no-npc|Shop 116 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/223-shop-223-no-npc|Shop 223 (no NPC)]] (no NPC found)
- Hero gacha pool 00, grade 1 (Gacha_00.cdb; odds are server side)
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
