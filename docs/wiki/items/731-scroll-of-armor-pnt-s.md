---
title: "Scroll of Armor PNT [S]"
type: "item"
id: 731
status: "partial"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb id 731"]
name_key: "ItemName_731"
kind: 11
kind_name: "Normal"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 24}
cost_pair:
  - {"currency": 2, "amount": 24}
flags: 1
no_sell: false
period: 1500
use_buff: 2104
cooldown_s: 2
cooldown_group: 25
stats: []
options:
  - {"code": 301, "value": 2104}
  - {"code": 261, "value": 2}
  - {"code": 262, "value": 25}
icon: {"file": "Items_04.png", "index": 15}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=583864 type=d36ca9 id=77895c sources=30c986 name_key=dd1e76 kind=17ba07 kind_name=6f63d6 classes=92d079 bind=2be88c price=81b208 cost_pair=a530a9 flags=356a19 no_sell=7cb6ef period=7841fb use_buff=a8c97e cooldown_s=da4b92 cooldown_group=f6e112 stats=97d170 options=0035d9 icon=a68b30 obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![Scroll of Armor PNT (S)](../assets/items/731.png) |
| **Item id** | `731` |
| **Kind** | Normal (11) |
| **Classes** | all |
| **Buy price** | 24 Gold |
| **Period** | 1500 (unit unknown; costume duration) |
| **Cooldown** | 2 s (group 25) |
| **On use: buff** | [[wiki/buffs/2104-tome-of-armor-penetration-s-armor-penetration-8\|Tome of Armor Penetration (S) : Armor Penetration +8]] |
| **Icon** | `ui/icons/Items_04.png` cell 15 |

### Tooltip

> Gain 8 Armor Penetration for 5 minutes.

### Other options

| code | value | meaning |
|---|---|---|
| 301 | 2104 | buff applied on use |
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
