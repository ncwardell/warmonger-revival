---
title: "Maid Set"
type: "costume"
id: 2036
status: "complete"
missing: []
sources: ["client: Item_Base.cdb kind 32 ids 2036, 2037, 2038", "docs: [[gameplay/events-and-schedules]] §9 (WM 0406: costume duration 1,440 → 2,610 min, counts only while worn); Item_Base period@3a read as minutes (inferred)"]
items:
  - {"item": 2036, "class": "Guardian", "period": 2160, "look": 22, "colors": [5, 41, 1]}
  - {"item": 2037, "class": "Saint", "period": 2160, "look": 22, "colors": [6, 63, 63]}
  - {"item": 2038, "class": "Punisher", "period": 2160, "look": 22, "colors": [59, 22, 75]}
classes: ["Saint", "Punisher", "Guardian"]
stats:
  - {"code": 105, "stat": "Movement(%)", "value": 10}
  - {"code": 32, "stat": "Health Regeneration", "value": 6}
duration: {"minutes": 2160, "counts": "while worn"}
obtained_from:
  - {"how": "premium_shop", "entry": 13, "item": 2036}
  - {"how": "premium_shop", "entry": 14, "item": 2037}
  - {"how": "premium_shop", "entry": 15, "item": 2038}
---
<!-- generated:start -->
<!-- generated-keys: title=a0a238 type=0d87ef id=ad707e sources=80b766 items=a8c877 classes=292ac5 stats=1d6d04 duration=1c0d99 obtained_from=f9c4da -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/2036.png) ![](wiki/assets/items/2037.png) ![](wiki/assets/items/2038.png) |
| **Pieces** | 3, for [[wiki/classes/1-saint\|Saint]], [[wiki/classes/4-punisher\|Punisher]], [[wiki/classes/5-guardian\|Guardian]] |
| **Duration** | 2,160 min (36.0 h) of wearing time |
| **Stat bonus** | Movement(%) +10, Health Regeneration +6 |

### Pieces

`look` is option 209 (the costume model, *inferred*); the colours are the three option-208 values, read as `ColorDB` ids for costume parts 1–3 (*inferred*).

|  | item | class | period | look | part colours |
|---|---|---|---|---|---|
| ![](wiki/assets/items/2036.png) | [[wiki/items/2036-maid-set\|Maid Set]] | [[wiki/classes/5-guardian\|Guardian]] | 2,160 min | 22 | `#4467c5` (5), `#1a2946` (41), `#2a2829` (1) |
| ![](wiki/assets/items/2037.png) | [[wiki/items/2037-maid-set\|Maid Set]] | [[wiki/classes/1-saint\|Saint]] | 2,160 min | 22 | `#eaebf0` (6), `#263145` (63), `#263145` (63) |
| ![](wiki/assets/items/2038.png) | [[wiki/items/2038-maid-set\|Maid Set]] | [[wiki/classes/4-punisher\|Punisher]] | 2,160 min | 22 | `#423731` (59), `#b3717f` (22), `#131927` (75) |

### Duration

Timed costumes run for their item period in minutes of **wearing** time: the timer only counts while the costume is worn (WM 0406 raised it from 1,440 to 2,610 minutes; [[gameplay/events-and-schedules|Events and schedules]] §9). The client rows hold 2,610 or 2,160; period 0 is a permanent costume. In Crush Online a timed costume could be *carved* (made permanent, losing its bonus) at the Merits Costume Merchant, and a Costume Remover hides it while keeping the stats ([[gameplay/crush-patch-notes|Crush patch notes]]).

### Where to get it

- [[wiki/items/2036-maid-set|Maid Set]]: how premium_shop, entry 13
- [[wiki/items/2037-maid-set|Maid Set]]: how premium_shop, entry 14
- [[wiki/items/2038-maid-set|Maid Set]]: how premium_shop, entry 15

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
