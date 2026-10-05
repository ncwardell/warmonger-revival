---
title: "Elixir of Health [A]"
type: "item"
id: 738
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 738", "notes: [[gameplay/reinforce-and-runes]] §7 (WM 0124)"]
name_key: "ItemName_738"
kind: 11
kind_name: "Normal"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 15}
cost_pair:
  - {"currency": 2, "amount": 15}
flags: 1
no_sell: false
period: 1500
use_buff: 2111
cooldown_s: 2
cooldown_group: 27
stats: []
options:
  - {"code": 301, "value": 2111}
  - {"code": 261, "value": 2}
  - {"code": 262, "value": 27}
icon: {"file": "Items_03.png", "index": 30}
obtained_from:
  - {"how": "craft", "recipe": 526}
---
<!-- generated:start -->
<!-- generated-keys: title=5ac65f type=d36ca9 id=641e2c sources=79e958 name_key=c089a3 kind=17ba07 kind_name=6f63d6 classes=92d079 bind=2be88c price=2ae737 cost_pair=be4ef7 flags=356a19 no_sell=7cb6ef period=7841fb use_buff=40a251 cooldown_s=da4b92 cooldown_group=bc33ea stats=97d170 options=515097 icon=09212a obtained_from=500b87 -->
|  |  |
|---|---|
|  | ![Elixir of Health (A)](wiki/assets/items/738.png) |
| **Item id** | `738` |
| **Kind** | Normal (11) |
| **Category** | [[wiki/items/consumables\|Consumables]] |
| **Classes** | all |
| **Buy price** | 15 Gold |
| **Period** | 1500 (unit unknown) |
| **Cooldown** | 2 s (group 27) |
| **On use: buff** | [[wiki/buffs/2111-elixir-of-health-a-health-regeneration-6-maximum-health-300\|Elixir of Health (A) : Health Regeneration +6, Maximum Health +300]] |
| **Icon** | `ui/icons/Items_03.png` cell 30 |

### Tooltip

> Gain 6 Health Regeneration and 300 Max Health for 5 minutes.

### Other options

| code | value | meaning |
|---|---|---|
| 301 | 2111 | buff applied on use |
| 261 | 2 | cooldown (s) |
| 262 | 27 | cooldown group |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 526 | [[wiki/items/819-lavender-powder\|Lavender powder]] × 30, [[wiki/items/836-empty-flask-a\|Empty Flask (A)]] × 1, [[wiki/items/844-dried-flower\|Dried flower]] × 2 | 0 | 100 |

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
