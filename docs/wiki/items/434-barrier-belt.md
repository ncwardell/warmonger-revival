---
title: "Barrier Belt"
type: "item"
id: 434
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 434"]
name_key: "ItemName_434"
kind: 55
kind_name: "Belt"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 150}
cost_pair:
  - {"currency": 2, "amount": 150}
stats:
  - {"code": 1, "stat": "Attack", "value": 6, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 15, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
  - {"code": 32, "stat": "Health Regeneration", "value": 3, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 20, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 250, "scale": "flat"}
  - {"code": 32, "stat": "Health Regeneration", "value": 4, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_08.png", "index": 21}
obtained_from:
  - {"how": "shop", "shop": 31}
  - {"how": "shop", "shop": 39}
  - {"how": "shop", "shop": 55}
  - {"how": "shop", "shop": 76}
  - {"how": "shop", "shop": 84}
  - {"how": "shop", "shop": 100}
  - {"how": "shop", "shop": 108}
  - {"how": "shop", "shop": 212}
  - {"how": "shop", "shop": 221}
  - {"how": "craft", "recipe": 38}
  - {"how": "craft", "recipe": 2038}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=756bd6 type=d36ca9 id=8949eb sources=0dfc2c name_key=b30b68 kind=8effee kind_name=ddf027 classes=92d079 bind=2be88c price=6d19d1 cost_pair=ca8a4e stats=40809f reinforce=356a19 icon=63228f obtained_from=343ae7 -->
|  |  |
|---|---|
|  | ![Barrier Belt](../assets/items/434.png) |
| **Item id** | `434` |
| **Kind** | Belt (55) |
| **Classes** | all |
| **Buy price** | 150 Gold |
| **Icon** | `ui/icons/Items_08.png` cell 21 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +6 | × (tier × 15 + reinforce level) | 1 |
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
| 38 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 20 | 300 | 100 |
| 2038 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 20 | 300 | 100 |

### Where to get it

- Sold in [[wiki/shops/31-shop-31-no-npc|Shop 31 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/39-shop-39-no-npc|Shop 39 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/55-shop-55-no-npc|Shop 55 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/76-shop-76-no-npc|Shop 76 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/84-shop-84-no-npc|Shop 84 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/100-shop-100-no-npc|Shop 100 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/108-shop-108-no-npc|Shop 108 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/212-shop-212-no-npc|Shop 212 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/221-shop-221-no-npc|Shop 221 (no NPC)]] (no NPC found)
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
