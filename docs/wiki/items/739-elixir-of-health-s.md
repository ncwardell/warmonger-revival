---
title: "Elixir of Health [S]"
type: "item"
id: 739
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 739", "notes: [[gameplay/reinforce-and-runes]] §7 (WM 0124)"]
name_key: "ItemName_739"
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
use_buff: 2112
cooldown_s: 2
cooldown_group: 27
stats: []
options:
  - {"code": 301, "value": 2112}
  - {"code": 261, "value": 2}
  - {"code": 262, "value": 27}
icon: {"file": "Items_03.png", "index": 31}
obtained_from:
  - {"how": "craft", "recipe": 527}
---
<!-- generated:start -->
<!-- generated-keys: title=a61a08 type=d36ca9 id=1c710b sources=f5fcbb name_key=7158ae kind=17ba07 kind_name=6f63d6 classes=92d079 bind=2be88c price=81b208 cost_pair=a530a9 flags=356a19 no_sell=7cb6ef period=7841fb use_buff=612d9e cooldown_s=da4b92 cooldown_group=bc33ea stats=97d170 options=b0bd3e icon=49820a obtained_from=ab253b -->
|  |  |
|---|---|
|  | ![Elixir of Health (S)](../assets/items/739.png) |
| **Item id** | `739` |
| **Kind** | Normal (11) |
| **Classes** | all |
| **Buy price** | 24 Gold |
| **Period** | 1500 (unit unknown; costume duration) |
| **Cooldown** | 2 s (group 27) |
| **On use: buff** | [[wiki/buffs/2112-elixir-of-health-s-health-regeneration-8-maximum-health-400\|Elixir of Health (S) : Health Regeneration +8, Maximum Health 400]] |
| **Icon** | `ui/icons/Items_03.png` cell 31 |

### Tooltip

> Gain 8 Health Regeneration and 400 Max Health for 5 minutes.

### Other options

| code | value | meaning |
|---|---|---|
| 301 | 2112 | buff applied on use |
| 261 | 2 | cooldown (s) |
| 262 | 27 | cooldown group |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 527 | [[wiki/items/819-lavender-powder\|Lavender powder]] × 40, [[wiki/items/837-empty-flask-s\|Empty Flask (S)]] × 1, [[wiki/items/844-dried-flower\|Dried flower]] × 3 | 0 | 100 |

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.
<!-- generated:end -->

## Notes

WM 0124 doubled the Elixir of Health's HP regen from 1/2/3/4 to **2/4/6/8** (C/B/A/S); the client buffs 2109–2112 already carry the new values plus max HP +100…+400 ([[gameplay/reinforce-and-runes|Reinforce and runes]] §7, *notes + client*). One active elixir at a time ([[gameplay/consumables|Consumables]] §1).

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
