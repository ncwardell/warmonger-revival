---
title: "Tome of Cooldown [Quest]"
type: "item"
id: 2599
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 2599", "client: [[gameplay/consumables]] §3, §6"]
name_key: "ItemName_2599"
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
use_buff: 2091
cooldown_s: 2
cooldown_group: 26
stats: []
options:
  - {"code": 301, "value": 2091}
  - {"code": 261, "value": 2}
  - {"code": 262, "value": 26}
icon: {"file": "Items_30.png", "index": 17}
obtained_from:
  - {"how": "craft", "recipe": 599}
---
<!-- generated:start -->
<!-- generated-keys: title=9aaabe type=d36ca9 id=ca060c sources=ab8aec name_key=7a8835 kind=17ba07 kind_name=6f63d6 classes=92d079 bind=2be88c price=2ae737 cost_pair=be4ef7 flags=356a19 no_sell=7cb6ef period=7841fb use_buff=2d7cf6 cooldown_s=da4b92 cooldown_group=887309 stats=97d170 options=e62895 icon=7809ef obtained_from=b4f2b3 -->
|  |  |
|---|---|
|  | ![Tome of Cooldown (Quest)](wiki/assets/items/2599.png) |
| **Item id** | `2599` |
| **Kind** | Normal (11) |
| **Classes** | all |
| **Buy price** | 15 Gold |
| **Period** | 1500 (unit unknown; costume duration) |
| **Cooldown** | 2 s (group 26) |
| **On use: buff** | [[wiki/buffs/2091-scroll-of-cooldown-reduction-a-9-cooldown-reduction\|Scroll of Cooldown Reduction (A) : 9% Cooldown Reduction]] |
| **Icon** | `ui/icons/Items_30.png` cell 17 |

### Tooltip

> Gain 9% Cooldown Reduction for 5 minutes.

### Other options

| code | value | meaning |
|---|---|---|
| 301 | 2091 | buff applied on use |
| 261 | 2 | cooldown (s) |
| 262 | 26 | cooldown group |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 599 | [[wiki/items/2595-peppermint-powder\|Peppermint powder]] × 30, [[wiki/items/2596-empty-scroll-a\|Empty Scroll (A)]] × 1, [[wiki/items/2597-burning-water\|Burning water]] × 2 | 0 | 100 |

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]]
<!-- generated:end -->

## Notes

Quest-only copy made in Owen's alchemy tutorial quests (47 "Create Potion", 48 "Doping Create") from bind-on-pickup quest inputs 2593–2597 ([[gameplay/consumables|Consumables]] §6, *client*).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- client: [[gameplay/consumables]] §3, §6

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
