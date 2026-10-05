---
title: "Helios Set"
type: "costume"
id: 2018
status: "complete"
missing: []
sources: ["client: Item_Base.cdb kind 32 ids 2018, 2019, 2020", "docs: [[gameplay/events-and-schedules]] §9 (WM 0406: costume duration 1,440 → 2,610 min, counts only while worn); Item_Base period@3a read as minutes (inferred)"]
items:
  - {"item": 2018, "class": "Guardian", "period": 2610, "look": 16, "colors": [39, 41, 75]}
  - {"item": 2019, "class": "Saint", "period": 2610, "look": 16, "colors": [75, 16, 16]}
  - {"item": 2020, "class": "Punisher", "period": 2610, "look": 16, "colors": [35, 35, 54]}
classes: ["Saint", "Punisher", "Guardian"]
stats:
  - {"code": 6, "stat": "Armor", "value": 80}
duration: {"minutes": 2610, "counts": "while worn"}
obtained_from:
  - {"how": "shop", "shop": 284, "item": 2018}
  - {"how": "shop", "shop": 284, "item": 2019}
  - {"how": "shop", "shop": 284, "item": 2020}
---
<!-- generated:start -->
<!-- generated-keys: title=cfad52 type=0d87ef id=66efd9 sources=5a4fa7 items=39d527 classes=292ac5 stats=99f4db duration=88544d obtained_from=42f4a6 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/2018.png) ![](wiki/assets/items/2019.png) ![](wiki/assets/items/2020.png) |
| **Pieces** | 3, for [[wiki/classes/1-saint\|Saint]], [[wiki/classes/4-punisher\|Punisher]], [[wiki/classes/5-guardian\|Guardian]] |
| **Duration** | 2,610 min (43.5 h) of wearing time |
| **Stat bonus** | Armor +80 |

### Pieces

`look` is option 209 (the costume model, *inferred*); the colours are the three option-208 values, read as `ColorDB` ids for costume parts 1–3 (*inferred*).

|  | item | class | period | look | part colours |
|---|---|---|---|---|---|
| ![](wiki/assets/items/2018.png) | [[wiki/items/2018-helios-set\|Helios Set]] | [[wiki/classes/5-guardian\|Guardian]] | 2,610 min | 16 | `#3c4e62` (39), `#1a2946` (41), `#131927` (75) |
| ![](wiki/assets/items/2019.png) | [[wiki/items/2019-helios-set\|Helios Set]] | [[wiki/classes/1-saint\|Saint]] | 2,610 min | 16 | `#131927` (75), `#820000` (16), `#820000` (16) |
| ![](wiki/assets/items/2020.png) | [[wiki/items/2020-helios-set\|Helios Set]] | [[wiki/classes/4-punisher\|Punisher]] | 2,610 min | 16 | `#4a133a` (35), `#4a133a` (35), `#5a3662` (54) |

### Duration

Timed costumes run for their item period in minutes of **wearing** time: the timer only counts while the costume is worn (WM 0406 raised it from 1,440 to 2,610 minutes; [[gameplay/events-and-schedules|Events and schedules]] §9). The client rows hold 2,610 or 2,160; period 0 is a permanent costume. In Crush Online a timed costume could be *carved* (made permanent, losing its bonus) at the Merits Costume Merchant, and a Costume Remover hides it while keeping the stats ([[gameplay/crush-patch-notes|Crush patch notes]]).

### Where to get it

- [[wiki/items/2018-helios-set|Helios Set]]: sold in [[wiki/shops/284-ashley-s-shop-merits-costume-merchant|Ashley's shop (Merits Costume Merchant)]]
- [[wiki/items/2019-helios-set|Helios Set]]: sold in [[wiki/shops/284-ashley-s-shop-merits-costume-merchant|Ashley's shop (Merits Costume Merchant)]]
- [[wiki/items/2020-helios-set|Helios Set]]: sold in [[wiki/shops/284-ashley-s-shop-merits-costume-merchant|Ashley's shop (Merits Costume Merchant)]]

See also: [[wiki/items/costume-items|all costume items]].
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
