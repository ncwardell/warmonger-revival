---
title: "Gloves of Honor"
type: "item"
id: 492
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 492", "client: Item_Make superior column (c19 chance / fail_item, read as superior result, *guess*) + notes: [[gameplay/reinforce-and-runes]] §4 (WM 0726: crafted gear has a small chance to come out superior)"]
name_key: "ItemName_420"
kind: 52
kind_name: "Gloves"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 1100}
cost_pair:
  - {"currency": 2, "amount": 1100}
rarity: 1
stats:
  - {"code": 6, "stat": "Armor", "value": 3, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 3, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 11, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 11, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 15, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 43, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 23, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 50, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 13, "scale": "flat"}
reinforce: 2
icon: {"file": "Items_06.png", "index": 26}
obtained_from:
  - {"how": "craft_superior", "recipe": 24, "chance": 5}
  - {"how": "craft_superior", "recipe": 2024, "chance": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=007156 type=d36ca9 id=77d67a sources=f86ca1 name_key=8adb94 kind=a93349 kind_name=f6564c classes=92d079 bind=883bf8 price=ec494a cost_pair=bf2342 rarity=356a19 stats=7db2fe reinforce=da4b92 icon=8ad561 obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![Gloves of Honor](wiki/assets/items/492.png) |
| **Item id** | `492` |
| **Kind** | Gloves (52) |
| **Category** | [[wiki/items/armor-gloves\|Gloves]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 1,100 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Items_06.png` cell 26 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +3 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +3 | × (tier × 15 + reinforce level) | 7 |
| Mana | +10 | × (tier × 15 + reinforce level) | 33 |
| Armor | +11 | × tier | 6 |
| Magic Resist | +11 | × tier | 7 |
| Mana | +15 | × tier | 33 |
| Armor | +43 | flat | 6 |
| Magic Resist | +23 | flat | 7 |
| Mana | +50 | flat | 33 |
| Movement(%) | Movement +13% | flat | 105 |

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

- how craft_superior, recipe 24, chance 5 (hand-entered)
- how craft_superior, recipe 2024, chance 5 (hand-entered)
<!-- generated:end -->

## Notes

The superior version of the normal piece: Odin's recipe 24 (and the Training Camp copy 2024) lists this item with a 5 % chance in its superior column. Crafted gear has a small chance to come out superior from WM 0726 ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *notes*); reading the column as the superior result is a *guess*. The WM 1018 Gear gacha also lists Superior Gear ([[gameplay/events-and-schedules|Events and schedules]] §10).

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
