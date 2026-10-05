---
title: "Guardian Armor"
type: "item"
id: 482
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 482", "client: Item_Make superior column (c19 chance / fail_item, read as superior result, *guess*) + notes: [[gameplay/reinforce-and-runes]] §4 (WM 0726: crafted gear has a small chance to come out superior)"]
name_key: "ItemName_410"
kind: 51
kind_name: "Armor"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 2000}
cost_pair:
  - {"currency": 2, "amount": 2000}
rarity: 1
stats:
  - {"code": 6, "stat": "Armor", "value": 5, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 2, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 12, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 11, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 12, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 46, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 23, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 390, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 9, "scale": "flat"}
reinforce: 2
icon: {"file": "Items_09.png", "index": 37}
obtained_from:
  - {"how": "craft_superior", "recipe": 14, "chance": 5}
  - {"how": "craft_superior", "recipe": 2014, "chance": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=8c59dd type=d36ca9 id=d051bf sources=93c4d2 name_key=caf7cf kind=b7eb6c kind_name=e687cb classes=92d079 bind=883bf8 price=05563f cost_pair=ce9832 rarity=356a19 stats=db21bc reinforce=da4b92 icon=411f91 obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![Guardian Armor](wiki/assets/items/482.png) |
| **Item id** | `482` |
| **Kind** | Armor (51) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 2,000 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Items_09.png` cell 37 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +5 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +2 | × (tier × 15 + reinforce level) | 7 |
| Health | +20 | × (tier × 15 + reinforce level) | 31 |
| Armor | +12 | × tier | 6 |
| Magic Resist | +11 | × tier | 7 |
| Health | +12 | × tier | 31 |
| Armor | +46 | flat | 6 |
| Magic Resist | +23 | flat | 7 |
| Health | +390 | flat | 31 |
| Movement(%) | Movement +9% | flat | 105 |

### Reinforcement

ItemSancMet row 2 (inferred from Item_Base +0x92), 1,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 4 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 4 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 6 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 10 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 10 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 15 |

### Where to get it

- how craft_superior, recipe 14, chance 5 (hand-entered)
- how craft_superior, recipe 2014, chance 5 (hand-entered)

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]]
<!-- generated:end -->

## Notes

The superior version of the normal piece: Odin's recipe 14 (and the Training Camp copy 2014) lists this item with a 5 % chance in its superior column. Crafted gear has a small chance to come out superior from WM 0726 ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *notes*); reading the column as the superior result is a *guess*. The WM 1018 Gear gacha also lists Superior Gear ([[gameplay/events-and-schedules|Events and schedules]] §10).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- client: Item_Make superior column (c19 chance / fail_item, read as superior result, *guess*) + notes: [[gameplay/reinforce-and-runes]] §4 (WM 0726: crafted gear has a small chance to come out superior)

## Open questions

[[gameplay/gear-stats]] §4 calls ids 445–492 the "T2 rows", but in the client they are the superior result of the normal recipes; tiers are a per-item level, not a separate id ([[gameplay/items-and-crafting|Items and crafting]] §1).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
