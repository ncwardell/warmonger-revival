---
title: "Life saviour (Premium)"
type: "item"
id: 1801
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 1801", "notes: [[gameplay/events-and-schedules]] §11 (Crush Online: Premium Life Saviour, bundle of 25 for 1,000 jewels in the auction house)"]
name_key: "ItemName_1801"
kind: 11
kind_name: "Normal"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 0}
cost_pair:
  - {"currency": 2, "amount": 0}
flags: 7
no_sell: true
use_skill: 5276
cooldown_s: 120
cooldown_group: 15
stats: []
options:
  - {"code": 210, "value": 5276}
  - {"code": 261, "value": 120}
  - {"code": 262, "value": 15}
icon: {"file": "Items_07.png", "index": 58}
obtained_from:
  - {"how": "auction_house_bundle", "count": 25, "price": 1000, "currency": "jewels"}
---
<!-- generated:start -->
<!-- generated-keys: title=3ac1c7 type=d36ca9 id=775ea0 sources=82677b name_key=6885ce kind=17ba07 kind_name=6f63d6 classes=92d079 bind=883bf8 price=32a324 cost_pair=395e20 flags=902ba3 no_sell=5ffe53 use_skill=11c5ea cooldown_s=775bc5 cooldown_group=f1abd6 stats=97d170 options=0f51d7 icon=0afb33 obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![Life saviour (Premium)](wiki/assets/items/1801.png) |
| **Item id** | `1801` |
| **Kind** | Normal (11) |
| **Category** | [[wiki/items/consumables\|Consumables]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 0 Gold |
| **Sell** | cannot be sold (flags bit 1) |
| **Cooldown** | 120 s (group 15) |
| **On use: skill** | [[wiki/skills/5276\|Skill 5276]] |
| **Icon** | `ui/icons/Items_07.png` cell 58 |

### Tooltip

> Fill 50% of Max HP
> immediately.
>
> (But, If your Max HP is over 2000,
> you will be healed max 2,000)
>
> Can't use in battle arena

### Other options

| code | value | meaning |
|---|---|---|
| 210 | 5276 | skill cast on use |
| 261 | 120 | cooldown (s) |
| 262 | 15 | cooldown group |

### Where to get it

- how auction_house_bundle, count 25, price 1000, currency jewels (hand-entered)
<!-- generated:end -->

## Notes

Crush Online sold the Premium Life Saviour in bundles of 25 for **1,000 jewels** in the auction house; it heals 50 % of max HP, cannot be used in the battle arena and has a **120 s** cooldown (the client's cooldown is 120 s too) ([[gameplay/events-and-schedules|Events and schedules]] §11, *notes*). The fame version (1802) cost 1,000 fame at the merits merchant.

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- notes: [[gameplay/events-and-schedules]] §11 (Crush Online: Premium Life Saviour, bundle of 25 for 1,000 jewels in the auction house)

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
