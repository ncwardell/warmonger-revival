---
title: "Barrier Necklace"
type: "item"
id: 433
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 433"]
name_key: "ItemName_433"
kind: 54
kind_name: "Necklace"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 100}
cost_pair:
  - {"currency": 2, "amount": 100}
stats:
  - {"code": 1, "stat": "Attack", "value": 7, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 15, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
  - {"code": 32, "stat": "Health Regeneration", "value": 3, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 20, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 250, "scale": "flat"}
  - {"code": 32, "stat": "Health Regeneration", "value": 4, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_08.png", "index": 32}
obtained_from:
  - {"how": "shop", "shop": 39}
  - {"how": "shop", "shop": 55}
  - {"how": "shop", "shop": 84}
  - {"how": "shop", "shop": 100}
  - {"how": "shop", "shop": 108}
  - {"how": "shop", "shop": 221}
  - {"how": "craft", "recipe": 37}
  - {"how": "craft", "recipe": 2037}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=25f56f type=d36ca9 id=82ad38 sources=e25cbe name_key=cd578d kind=80e28a kind_name=7b4b74 classes=92d079 bind=2be88c price=936627 cost_pair=ebf7c2 stats=010735 reinforce=356a19 icon=ede490 obtained_from=50fd0f -->
|  |  |
|---|---|
|  | ![Barrier Necklace](../assets/items/433.png) |
| **Item id** | `433` |
| **Kind** | Necklace (54) |
| **Classes** | all |
| **Buy price** | 100 Gold |
| **Icon** | `ui/icons/Items_08.png` cell 32 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +7 | × (tier × 15 + reinforce level) | 1 |
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
| 37 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 15 | 225 | 100 |
| 2037 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 15 | 225 | 100 |

### Where to get it

- Sold in [[wiki/shops/39-shop-39-no-npc|Shop 39 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/55-shop-55-no-npc|Shop 55 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/84-shop-84-no-npc|Shop 84 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/100-shop-100-no-npc|Shop 100 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/108-shop-108-no-npc|Shop 108 (no NPC)]] (no NPC found)
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
