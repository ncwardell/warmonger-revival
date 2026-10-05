---
title: "Potion of Health [S]"
type: "item"
id: 888
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 888"]
name_key: "ItemName_888"
kind: 11
kind_name: "Normal"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 182}
cost_pair:
  - {"currency": 2, "amount": 182}
flags: 1
no_sell: false
use_buff: 2063
cooldown_s: 15
cooldown_group: 1
stats: []
options:
  - {"code": 301, "value": 2063}
  - {"code": 261, "value": 15}
  - {"code": 262, "value": 1}
icon: {"file": "Items_01.png", "index": 4}
obtained_from:
  - {"how": "craft", "recipe": 704}
---
<!-- generated:start -->
<!-- generated-keys: title=897d47 type=d36ca9 id=eaa67f sources=fd4340 name_key=cf5989 kind=17ba07 kind_name=6f63d6 classes=92d079 bind=2be88c price=43df00 cost_pair=439d8b flags=356a19 no_sell=7cb6ef use_buff=c7131f cooldown_s=f1abd6 cooldown_group=356a19 stats=97d170 options=c8db48 icon=96b2eb obtained_from=3e789a -->
|  |  |
|---|---|
|  | ![Potion of Health (S)](wiki/assets/items/888.png) |
| **Item id** | `888` |
| **Kind** | Normal (11) |
| **Classes** | all |
| **Buy price** | 182 Gold |
| **Cooldown** | 15 s (group 1) |
| **On use: buff** | [[wiki/buffs/2063-hp-potion-s-supreme-hp-regeneration\|HP Potion (S): Supreme HP Regeneration]] |
| **Icon** | `ui/icons/Items_01.png` cell 4 |

### Tooltip

> Regenerates Health for 16 seconds. 
> Restores a total of 1200 Health.

### Other options

| code | value | meaning |
|---|---|---|
| 301 | 2063 | buff applied on use |
| 261 | 15 | cooldown (s) |
| 262 | 1 | cooldown group |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 704 | [[wiki/items/837-empty-flask-s\|Empty Flask (S)]] × 100, [[wiki/items/703-crystal-black\|Crystal : Black]] × 2 | 0 | 100 |

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
