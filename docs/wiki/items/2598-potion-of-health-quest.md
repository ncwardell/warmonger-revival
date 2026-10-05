---
title: "Potion of Health [Quest]"
type: "item"
id: 2598
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 2598", "client: [[gameplay/consumables]] §3, §6"]
name_key: "ItemName_2598"
kind: 11
kind_name: "Normal"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 135}
cost_pair:
  - {"currency": 2, "amount": 135}
flags: 1
no_sell: false
use_buff: 2062
cooldown_s: 15
cooldown_group: 1
stats: []
options:
  - {"code": 301, "value": 2062}
  - {"code": 261, "value": 15}
  - {"code": 262, "value": 1}
icon: {"file": "Items_01.png", "index": 3}
obtained_from:
  - {"how": "craft", "recipe": 749}
---
<!-- generated:start -->
<!-- generated-keys: title=f97a50 type=d36ca9 id=e5b088 sources=ae5c73 name_key=e4a191 kind=17ba07 kind_name=6f63d6 classes=92d079 bind=2be88c price=15ffcd cost_pair=0a5b72 flags=356a19 no_sell=7cb6ef use_buff=329bcc cooldown_s=f1abd6 cooldown_group=356a19 stats=97d170 options=cc2b4d icon=966ff7 obtained_from=a9816a -->
|  |  |
|---|---|
|  | ![Potion of Health (Quest)](../assets/items/2598.png) |
| **Item id** | `2598` |
| **Kind** | Normal (11) |
| **Classes** | all |
| **Buy price** | 135 Gold |
| **Cooldown** | 15 s (group 1) |
| **On use: buff** | [[wiki/buffs/2062-hp-potion-a-major-hp-regeneration\|HP Potion (A): Major HP Regeneration]] |
| **Icon** | `ui/icons/Items_01.png` cell 3 |

### Tooltip

> Regenerates Health for 16 seconds. 
> Restores a total of 1000 Health.

### Other options

| code | value | meaning |
|---|---|---|
| 301 | 2062 | buff applied on use |
| 261 | 15 | cooldown (s) |
| 262 | 1 | cooldown group |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 749 | [[wiki/items/2593-empty-flask-a\|Empty Flask (A)]] × 100, [[wiki/items/2594-crystal-red\|Crystal : Red]] × 2 | 0 | 100 |

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]]
- [[gameplay/potion-regen|Potion regeneration ticks]]
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
