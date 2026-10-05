---
title: "Ninja Set"
type: "costume"
id: 2049
status: "complete"
missing: []
sources: ["client: Item_Base.cdb kind 32 ids 2049, 2050, 2051", "docs: [[gameplay/events-and-schedules]] §9 (WM 0406: costume duration 1,440 → 2,610 min, counts only while worn); Item_Base period@3a read as minutes (inferred)"]
items:
  - {"item": 2049, "class": "Saint", "period": 2160, "look": 28, "colors": [16, 30, 6]}
  - {"item": 2050, "class": "Punisher", "period": 2160, "look": 29, "colors": [16, 42, 87]}
  - {"item": 2051, "class": "Guardian", "period": 2160, "look": 28, "colors": [66, 16, 42]}
classes: ["Saint", "Punisher", "Guardian"]
stats:
  - {"code": 105, "stat": "Movement(%)", "value": 5}
  - {"code": 8, "stat": "Dodge(%)", "value": 5}
duration: {"minutes": 2160, "counts": "while worn"}
obtained_from:
  - {"how": "premium_shop", "entry": 27, "item": 2049}
  - {"how": "premium_shop", "entry": 28, "item": 2050}
  - {"how": "premium_shop", "entry": 29, "item": 2051}
---
<!-- generated:start -->
<!-- generated-keys: title=84f93b type=0d87ef id=d1c382 sources=ebd13c items=9d37e6 classes=292ac5 stats=328cdd duration=1c0d99 obtained_from=20ca63 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/2049.png) ![](wiki/assets/items/2050.png) ![](wiki/assets/items/2051.png) |
| **Pieces** | 3, for [[wiki/classes/1-saint\|Saint]], [[wiki/classes/4-punisher\|Punisher]], [[wiki/classes/5-guardian\|Guardian]] |
| **Duration** | 2,160 min (36.0 h) of wearing time |
| **Stat bonus** | Movement(%) +5, Dodge(%) +5 |

### Pieces

`look` is option 209 (the costume model, *inferred*); the colours are the three option-208 values, read as `ColorDB` ids for costume parts 1–3 (*inferred*).

|  | item | class | period | look | part colours |
|---|---|---|---|---|---|
| ![](wiki/assets/items/2049.png) | [[wiki/items/2049-ninja-set\|Ninja Set]] | [[wiki/classes/1-saint\|Saint]] | 2,160 min | 28 | `#820000` (16), `#b1403c` (30), `#eaebf0` (6) |
| ![](wiki/assets/items/2050.png) | [[wiki/items/2050-ninja-set\|Ninja Set]] | [[wiki/classes/4-punisher\|Punisher]] | 2,160 min | 29 | `#820000` (16), `#0f2511` (42), `#4e6c30` (87) |
| ![](wiki/assets/items/2051.png) | [[wiki/items/2051-ninja-set\|Ninja Set]] | [[wiki/classes/5-guardian\|Guardian]] | 2,160 min | 28 | `#2d4b31` (66), `#820000` (16), `#0f2511` (42) |

### Duration

Timed costumes run for their item period in minutes of **wearing** time: the timer only counts while the costume is worn (WM 0406 raised it from 1,440 to 2,610 minutes; [[gameplay/events-and-schedules|Events and schedules]] §9). The client rows hold 2,610 or 2,160; period 0 is a permanent costume. In Crush Online a timed costume could be *carved* (made permanent, losing its bonus) at the Merits Costume Merchant, and a Costume Remover hides it while keeping the stats ([[gameplay/crush-patch-notes|Crush patch notes]]).

### Where to get it

- [[wiki/items/2049-ninja-set|Ninja Set]]: how premium_shop, entry 27
- [[wiki/items/2050-ninja-set|Ninja Set]]: how premium_shop, entry 28
- [[wiki/items/2051-ninja-set|Ninja Set]]: how premium_shop, entry 29

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
