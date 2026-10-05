---
title: "Athletics Set"
type: "costume"
id: 2033
status: "complete"
missing: []
sources: ["client: Item_Base.cdb kind 32 ids 2033, 2034, 2035", "docs: [[gameplay/events-and-schedules]] §9 (WM 0406: costume duration 1,440 → 2,610 min, counts only while worn); Item_Base period@3a read as minutes (inferred)"]
items:
  - {"item": 2033, "class": "Guardian", "period": 2160, "look": 21, "colors": [6, 4, 12]}
  - {"item": 2034, "class": "Saint", "period": 2160, "look": 21, "colors": [75, 48, 48]}
  - {"item": 2035, "class": "Punisher", "period": 2160, "look": 21, "colors": [50, 80, 41]}
classes: ["Saint", "Punisher", "Guardian"]
stats:
  - {"code": 105, "stat": "Movement(%)", "value": 5}
  - {"code": 273, "stat": "Drop Chance(%)", "value": 5}
duration: {"minutes": 2160, "counts": "while worn"}
obtained_from:
  - {"how": "premium_shop", "entry": 10, "item": 2033}
  - {"how": "premium_shop", "entry": 11, "item": 2034}
  - {"how": "premium_shop", "entry": 12, "item": 2035}
---
<!-- generated:start -->
<!-- generated-keys: title=5d5476 type=0d87ef id=ffba58 sources=996380 items=320399 classes=292ac5 stats=a3dec1 duration=1c0d99 obtained_from=5005e1 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/2033.png) ![](wiki/assets/items/2034.png) ![](wiki/assets/items/2035.png) |
| **Pieces** | 3, for [[wiki/classes/1-saint\|Saint]], [[wiki/classes/4-punisher\|Punisher]], [[wiki/classes/5-guardian\|Guardian]] |
| **Duration** | 2,160 min (36.0 h) of wearing time |
| **Stat bonus** | Movement(%) +5, Drop Chance(%) +5 |

### Pieces

`look` is option 209 (the costume model, *inferred*); the colours are the three option-208 values, read as `ColorDB` ids for costume parts 1–3 (*inferred*).

|  | item | class | period | look | part colours |
|---|---|---|---|---|---|
| ![](wiki/assets/items/2033.png) | [[wiki/items/2033-athletics-set\|Athletics Set]] | [[wiki/classes/5-guardian\|Guardian]] | 2,160 min | 21 | `#eaebf0` (6), `#ffd728` (4), `#198839` (12) |
| ![](wiki/assets/items/2034.png) | [[wiki/items/2034-athletics-set\|Athletics Set]] | [[wiki/classes/1-saint\|Saint]] | 2,160 min | 21 | `#131927` (75), `#6c71c5` (48), `#6c71c5` (48) |
| ![](wiki/assets/items/2035.png) | [[wiki/items/2035-athletics-set\|Athletics Set]] | [[wiki/classes/4-punisher\|Punisher]] | 2,160 min | 21 | `#2d9e9c` (50), `#3a1d1f` (80), `#1a2946` (41) |

### Duration

Timed costumes run for their item period in minutes of **wearing** time: the timer only counts while the costume is worn (WM 0406 raised it from 1,440 to 2,610 minutes; [[gameplay/events-and-schedules|Events and schedules]] §9). The client rows hold 2,610 or 2,160; period 0 is a permanent costume. In Crush Online a timed costume could be *carved* (made permanent, losing its bonus) at the Merits Costume Merchant, and a Costume Remover hides it while keeping the stats ([[gameplay/crush-patch-notes|Crush patch notes]]).

### Where to get it

- [[wiki/items/2033-athletics-set|Athletics Set]]: how premium_shop, entry 10
- [[wiki/items/2034-athletics-set|Athletics Set]]: how premium_shop, entry 11
- [[wiki/items/2035-athletics-set|Athletics Set]]: how premium_shop, entry 12

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
