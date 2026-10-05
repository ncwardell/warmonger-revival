---
title: "Potion of Mana [D]"
type: "item"
id: 884
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 884", "image: [[gameplay/progression-and-economy]] §4 (Wren prices)"]
name_key: "ItemName_884"
kind: 11
kind_name: "Normal"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
flags: 1
no_sell: false
use_buff: 2051
cooldown_s: 15
cooldown_group: 2
stats: []
options:
  - {"code": 301, "value": 2051}
  - {"code": 261, "value": 15}
  - {"code": 262, "value": 2}
icon: {"file": "Items_01.png", "index": 5}
obtained_from:
  - {"how": "shop", "shop": 281}
  - {"how": "shop", "shop": 287}
  - {"how": "shop", "shop": 291}
  - {"how": "quest_reward", "quest": 722, "count": 10}
---
<!-- generated:start -->
<!-- generated-keys: title=b017fe type=d36ca9 id=8cc981 sources=b185fd name_key=76a038 kind=17ba07 kind_name=6f63d6 classes=92d079 bind=2be88c price=8c6ae2 cost_pair=982f5a flags=356a19 no_sell=7cb6ef use_buff=33b82c cooldown_s=f1abd6 cooldown_group=da4b92 stats=97d170 options=226851 icon=7bc914 obtained_from=70272f -->
|  |  |
|---|---|
|  | ![Potion of Mana (D)](wiki/assets/items/884.png) |
| **Item id** | `884` |
| **Kind** | Normal (11) |
| **Classes** | all |
| **Buy price** | 10 Gold |
| **Cooldown** | 15 s (group 2) |
| **On use: buff** | [[wiki/buffs/2051-mana-potion-d-weak-mana-regeneration\|Mana Potion (D) : Weak Mana Regeneration]] |
| **Icon** | `ui/icons/Items_01.png` cell 5 |

### Tooltip

> Regenerates Mana for 16 seconds. 
> Restores up to 100 Mana.

### Other options

| code | value | meaning |
|---|---|---|
| 301 | 2051 | buff applied on use |
| 261 | 15 | cooldown (s) |
| 262 | 2 | cooldown group |

### Where to get it

- Sold in [[wiki/shops/281-wren-s-shop-merchant-281|Wren's shop (Merchant) 281]] ([[wiki/npcs/203|NPC 203]], [[wiki/npcs/204-wren|Wren]], [[wiki/npcs/330-tora|Tora]])
- Sold in [[wiki/shops/287-wren-s-shop-merchant-287|Wren's shop (Merchant) 287]] ([[wiki/npcs/238-wren|Wren]])
- Sold in [[wiki/shops/291-wren-s-shop-merchant-291|Wren's shop (Merchant) 291]] ([[wiki/npcs/319-wren|Wren]])
- Reward of quest [[wiki/quests/722-juicy-potions|Juicy Potions]] × 10

### Mentioned in

- [[gameplay/potion-regen|Potion regeneration ticks]]
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]
<!-- generated:end -->

## Notes

Wren sold the D potions for **79 gold** in spring 2018 against a base of 10, the 7.92 × shop rate of that fort ([[gameplay/progression-and-economy|Progression and economy]] §4, *image*). Potions restore their buff value per second for 16 s ([[gameplay/potion-regen|Potion regeneration]], *guess* from the tooltips).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- image: [[gameplay/progression-and-economy]] §4 (Wren prices)

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
