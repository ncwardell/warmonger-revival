---
title: "Scroll of Magic PNT [B]"
type: "item"
id: 733
status: "partial"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb id 733"]
name_key: "ItemName_733"
kind: 11
kind_name: "Normal"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 9}
cost_pair:
  - {"currency": 2, "amount": 9}
flags: 1
no_sell: false
period: 1500
use_buff: 2106
cooldown_s: 2
cooldown_group: 25
stats: []
options:
  - {"code": 301, "value": 2106}
  - {"code": 261, "value": 2}
  - {"code": 262, "value": 25}
icon: {"file": "Items_04.png", "index": 17}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=05a411 type=d36ca9 id=bc3f9e sources=7e43b2 name_key=d2d986 kind=17ba07 kind_name=6f63d6 classes=92d079 bind=2be88c price=2d93d3 cost_pair=632317 flags=356a19 no_sell=7cb6ef period=7841fb use_buff=02e0a5 cooldown_s=da4b92 cooldown_group=f6e112 stats=97d170 options=2bd789 icon=88e6a0 obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![Scroll of Magic PNT (B)](wiki/assets/items/733.png) |
| **Item id** | `733` |
| **Kind** | Normal (11) |
| **Category** | [[wiki/items/consumables\|Consumables]] |
| **Classes** | all |
| **Buy price** | 9 Gold |
| **Period** | 1500 (unit unknown) |
| **Cooldown** | 2 s (group 25) |
| **On use: buff** | [[wiki/buffs/2106-tome-of-magic-penetration-b-magic-penetration-4\|Tome of Magic Penetration (B) : Magic Penetration +4]] |
| **Icon** | `ui/icons/Items_04.png` cell 17 |

### Tooltip

> Gain 4 Magic Penetration for 5 minutes.

### Other options

| code | value | meaning |
|---|---|---|
| 301 | 2106 | buff applied on use |
| 261 | 2 | cooldown (s) |
| 262 | 25 | cooldown group |

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.
<!-- generated:end -->

## Notes

Scrolls of Armor and Magic Penetration were removed from the game in WM 0420 ([[gameplay/reinforce-and-runes|Reinforce and runes]] §7, *notes*). No recipe makes them (Owen's matching rows 519–524 have result 0) and Lewellyn does not sell the C grade ([[gameplay/consumables|Consumables]] §4.1, *client*).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

Map Owen's rows 519–521 (Topaz) to Armor PNT and 522–524 (Jasmine) to Magic PNT, or leave the scrolls unobtainable as after WM 0420? ([[gameplay/consumables|Consumables]] §4.1, *guess*)

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
