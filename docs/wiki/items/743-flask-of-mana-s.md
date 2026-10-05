---
title: "Flask of Mana [S]"
type: "item"
id: 743
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 743", "notes: [[gameplay/reinforce-and-runes]] §7 (WM 0124)"]
name_key: "ItemName_743"
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
use_buff: 2116
cooldown_s: 2
cooldown_group: 28
stats: []
options:
  - {"code": 301, "value": 2116}
  - {"code": 261, "value": 2}
  - {"code": 262, "value": 28}
icon: {"file": "Items_30.png", "index": 32}
obtained_from:
  - {"how": "craft", "recipe": 530}
---
<!-- generated:start -->
<!-- generated-keys: title=54e07a type=d36ca9 id=f032e5 sources=d1d55a name_key=7a5838 kind=17ba07 kind_name=6f63d6 classes=92d079 bind=2be88c price=81b208 cost_pair=a530a9 flags=356a19 no_sell=7cb6ef period=7841fb use_buff=397423 cooldown_s=da4b92 cooldown_group=0a57cb stats=97d170 options=7a8f29 icon=16039e obtained_from=702655 -->
|  |  |
|---|---|
|  | ![Flask of Mana (S)](wiki/assets/items/743.png) |
| **Item id** | `743` |
| **Kind** | Normal (11) |
| **Category** | [[wiki/items/consumables\|Consumables]] |
| **Classes** | all |
| **Buy price** | 24 Gold |
| **Period** | 1500 (unit unknown) |
| **Cooldown** | 2 s (group 28) |
| **On use: buff** | [[wiki/buffs/2116-flask-of-mana-s-mana-regeneration-8-maximum-mana-200\|Flask of Mana (S) : Mana Regeneration +8, Maximum Mana +200]] |
| **Icon** | `ui/icons/Items_30.png` cell 32 |

### Tooltip

> Gain 8 Mana Regeneration and 200 Max Mana for 5 minutes.

### Other options

| code | value | meaning |
|---|---|---|
| 301 | 2116 | buff applied on use |
| 261 | 2 | cooldown (s) |
| 262 | 28 | cooldown group |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 530 | [[wiki/items/821-peppermint-powder\|Peppermint powder]] × 40, [[wiki/items/837-empty-flask-s\|Empty Flask (S)]] × 1, [[wiki/items/844-dried-flower\|Dried flower]] × 3 | 0 | 100 |

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.
<!-- generated:end -->

## Notes

WM 0124 doubled the Flask of Mana's MP regen from 1/2/3/4 to **2/4/6/8** (C/B/A/S); the client buffs 2113–2116 match, plus max MP +50…+200 ([[gameplay/reinforce-and-runes|Reinforce and runes]] §7, *notes + client*). One active flask at a time ([[gameplay/consumables|Consumables]] §1).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- notes: [[gameplay/reinforce-and-runes]] §7 (WM 0124)

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
