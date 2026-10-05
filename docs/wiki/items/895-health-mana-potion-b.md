---
title: "Health Mana Potion [B]"
type: "item"
id: 895
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 895"]
name_key: "ItemName_895"
kind: 11
kind_name: "Normal"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 100}
cost_pair:
  - {"currency": 2, "amount": 100}
flags: 1
no_sell: false
use_buff: 2070
cooldown_s: 15
cooldown_group: 3
stats: []
options:
  - {"code": 301, "value": 2070}
  - {"code": 261, "value": 15}
  - {"code": 262, "value": 3}
icon: {"file": "Items_01.png", "index": 12}
obtained_from:
  - {"how": "craft", "recipe": 710}
  - {"how": "craft", "recipe": 2506}
---
<!-- generated:start -->
<!-- generated-keys: title=7fc198 type=d36ca9 id=f1c6fe sources=e57f02 name_key=e6c0d8 kind=17ba07 kind_name=6f63d6 classes=92d079 bind=2be88c price=936627 cost_pair=ebf7c2 flags=356a19 no_sell=7cb6ef use_buff=0164a5 cooldown_s=f1abd6 cooldown_group=77de68 stats=97d170 options=bad210 icon=be594a obtained_from=400706 -->
|  |  |
|---|---|
|  | ![Health Mana Potion (B)](wiki/assets/items/895.png) |
| **Item id** | `895` |
| **Kind** | Normal (11) |
| **Category** | [[wiki/items/consumables\|Consumables]] |
| **Classes** | all |
| **Buy price** | 100 Gold |
| **Cooldown** | 15 s (group 3) |
| **On use: buff** | [[wiki/buffs/2070-omni-potion-b-strong-omni-regeneration\|Omni Potion (B) : Strong Omni Regeneration]] |
| **Icon** | `ui/icons/Items_01.png` cell 12 |

### Tooltip

> Regenerates Health and Mana for 16 seconds. 
> Restores a total of 400 Health and 80 Mana.

### Other options

| code | value | meaning |
|---|---|---|
| 301 | 2070 | buff applied on use |
| 261 | 15 | cooldown (s) |
| 262 | 3 | cooldown group |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 710 | [[wiki/items/835-empty-flask-b\|Empty Flask (B)]] × 100, [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 4 | 0 | 100 |
| 2506 | [[wiki/items/835-empty-flask-b\|Empty Flask (B)]] × 100, [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 4 | 0 | 100 |

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

### Mentioned in

- [[gameplay/potion-regen|Potion regeneration ticks]]
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
