---
title: "Drop Chance Potion"
type: "item"
id: 764
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 764", "notes: [[gameplay/reinforce-and-runes]] §7 (WM 0726, CO 1222)"]
name_key: "ItemName_764"
kind: 11
kind_name: "Normal"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
use_buff: 2134
cooldown_s: 2
stats: []
options:
  - {"code": 301, "value": 2134}
  - {"code": 261, "value": 2}
icon: {"file": "Items_07.png", "index": 59}
obtained_from:
  - {"how": "shop", "shop": 401}
  - {"how": "premium_shop", "entry": 30}
---
<!-- generated:start -->
<!-- generated-keys: title=22eb9d type=d36ca9 id=b55860 sources=35b1b7 name_key=d10ff4 kind=17ba07 kind_name=6f63d6 classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a use_buff=9e1f50 cooldown_s=da4b92 stats=97d170 options=e93995 icon=37da9a obtained_from=47e0d7 -->
|  |  |
|---|---|
|  | ![Drop Chance Potion](wiki/assets/items/764.png) |
| **Item id** | `764` |
| **Kind** | Normal (11) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Cooldown** | 2 s (group -) |
| **On use: buff** | [[wiki/buffs/2134-drop-chance-potion-increase-item-drop-chance-by-40\|Drop Chance Potion: Increase Item Drop Chance by 40%.]] |
| **Icon** | `ui/icons/Items_07.png` cell 59 |

### Tooltip

> This potion will increase the item drop chance by 40%.
> Effect duration : 1hour

### Other options

| code | value | meaning |
|---|---|---|
| 301 | 2134 | buff applied on use |
| 261 | 2 | cooldown (s) |

### Where to get it

- Sold in [[wiki/shops/401-shop-401-no-npc|Shop 401 (no NPC)]] (no NPC found)
- Premium shop entry 30: 1,000 (currency code 3, discount 0%)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]]
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]]
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]]
- [[gameplay/patch-history|Patch notes and other sources]]
- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]]
- [[gameplay/server-rules|Server rules checklist]]
<!-- generated:end -->

## Notes

Drop chance **+40 % for 1 hour** in Warmonger (WM 0726; client buff 2134 = 40 %). In Crush Online it was +20 % for 1 h at 500 jewels, or 10 for 4,500 ([[gameplay/reinforce-and-runes|Reinforce and runes]] §7, [[gameplay/crush-patch-notes|Crush patch notes]] 2016-12-22, *notes*).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- notes: [[gameplay/reinforce-and-runes]] §7 (WM 0726, CO 1222)

## Open questions

Crush Online's +20 % differs from the client's +40 %; the client value is used.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
