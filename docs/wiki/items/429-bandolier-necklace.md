---
title: "Bandolier Necklace"
type: "item"
id: 429
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 429"]
name_key: "ItemName_429"
kind: 54
kind_name: "Necklace"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 100}
cost_pair:
  - {"currency": 2, "amount": 100}
stats:
  - {"code": 1, "stat": "Attack", "value": 7, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "tier"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 1, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 80, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 250, "scale": "flat"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 3, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_08.png", "index": 54}
obtained_from:
  - {"how": "shop", "shop": 43}
  - {"how": "shop", "shop": 59}
  - {"how": "shop", "shop": 92}
  - {"how": "shop", "shop": 104}
  - {"how": "shop", "shop": 112}
  - {"how": "shop", "shop": 116}
  - {"how": "craft", "recipe": 33}
  - {"how": "craft", "recipe": 2033}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=30ded9 type=d36ca9 id=75988f sources=1c739c name_key=35f780 kind=80e28a kind_name=7b4b74 classes=92d079 bind=2be88c price=936627 cost_pair=ebf7c2 stats=84b784 reinforce=356a19 icon=4aaf5d obtained_from=f03cf3 -->
|  |  |
|---|---|
|  | ![Bandolier Necklace](../assets/items/429.png) |
| **Item id** | `429` |
| **Kind** | Necklace (54) |
| **Classes** | all |
| **Buy price** | 100 Gold |
| **Icon** | `ui/icons/Items_08.png` cell 54 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +7 | × (tier × 15 + reinforce level) | 1 |
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
| 33 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 15 | 225 | 100 |
| 2033 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 15 | 225 | 100 |

### Where to get it

- Sold in [[wiki/shops/43-shop-43-no-npc|Shop 43 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/59-shop-59-no-npc|Shop 59 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/92-shop-92-no-npc|Shop 92 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/104-shop-104-no-npc|Shop 104 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/112-shop-112-no-npc|Shop 112 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/116-shop-116-no-npc|Shop 116 (no NPC)]] (no NPC found)
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
