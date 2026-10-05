---
title: "Health Mana Potion [C]"
type: "item"
id: 894
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 894"]
name_key: "ItemName_894"
kind: 11
kind_name: "Normal"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 80}
cost_pair:
  - {"currency": 2, "amount": 80}
flags: 1
no_sell: false
use_buff: 2069
cooldown_s: 15
cooldown_group: 3
stats: []
options:
  - {"code": 301, "value": 2069}
  - {"code": 261, "value": 15}
  - {"code": 262, "value": 3}
icon: {"file": "Items_01.png", "index": 11}
obtained_from:
  - {"how": "craft", "recipe": 709}
  - {"how": "craft", "recipe": 2505}
---
<!-- generated:start -->
<!-- generated-keys: title=b34189 type=d36ca9 id=1ecaeb sources=4f675e name_key=d8f9cf kind=17ba07 kind_name=6f63d6 classes=92d079 bind=2be88c price=c4f310 cost_pair=809c9f flags=356a19 no_sell=7cb6ef use_buff=100b22 cooldown_s=f1abd6 cooldown_group=77de68 stats=97d170 options=25b3e2 icon=f46d20 obtained_from=9d851d -->
|  |  |
|---|---|
|  | ![Health Mana Potion (C)](wiki/assets/items/894.png) |
| **Item id** | `894` |
| **Kind** | Normal (11) |
| **Classes** | all |
| **Buy price** | 80 Gold |
| **Cooldown** | 15 s (group 3) |
| **On use: buff** | [[wiki/buffs/2069-omni-potion-c-minor-omni-regeneration\|Omni Potion (C) : Minor Omni Regeneration]] |
| **Icon** | `ui/icons/Items_01.png` cell 11 |

### Tooltip

> Regenerates Mana for 16 seconds. 
> Restores a total of 300 Health, 60 Mana.

### Other options

| code | value | meaning |
|---|---|---|
| 301 | 2069 | buff applied on use |
| 261 | 15 | cooldown (s) |
| 262 | 3 | cooldown group |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 709 | [[wiki/items/834-empty-flask-c\|Empty Flask (C)]] × 100, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 4 | 0 | 100 |
| 2505 | [[wiki/items/834-empty-flask-c\|Empty Flask (C)]] × 100, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 4 | 0 | 100 |

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
