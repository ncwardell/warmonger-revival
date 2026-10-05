---
title: "Pirate Set"
type: "costume"
id: 2076
status: "complete"
missing: []
sources: ["client: Item_Base.cdb kind 32 ids 2076, 2077, 2078", "docs: [[gameplay/events-and-schedules]] §9 (WM 0406: costume duration 1,440 → 2,610 min, counts only while worn); Item_Base period@3a read as minutes (inferred)"]
items:
  - {"item": 2076, "class": "Saint", "period": 2160, "look": 27, "colors": [75, 75, 16]}
  - {"item": 2077, "class": "Punisher", "period": 2160, "look": 28, "colors": [71, 16, 75]}
  - {"item": 2078, "class": "Guardian", "period": 2160, "look": 27, "colors": [85, 42, 16]}
classes: ["Saint", "Punisher", "Guardian"]
stats:
  - {"code": 269, "stat": "Toughness(%)", "value": 10}
  - {"code": 273, "stat": "Drop Chance(%)", "value": 5}
duration: {"minutes": 2160, "counts": "while worn"}
obtained_from:
  - {"how": "premium_shop", "entry": 23, "item": 2076}
  - {"how": "premium_shop", "entry": 24, "item": 2077}
  - {"how": "premium_shop", "entry": 25, "item": 2078}
---
<!-- generated:start -->
<!-- generated-keys: title=33859c type=0d87ef id=bae6cc sources=b75c79 items=4587e6 classes=292ac5 stats=10864e duration=1c0d99 obtained_from=171a1e -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/2076.png) ![](wiki/assets/items/2077.png) ![](wiki/assets/items/2078.png) |
| **Pieces** | 3, for [[wiki/classes/1-saint\|Saint]], [[wiki/classes/4-punisher\|Punisher]], [[wiki/classes/5-guardian\|Guardian]] |
| **Duration** | 2,160 min (36.0 h) of wearing time |
| **Stat bonus** | Toughness(%) +10, Drop Chance(%) +5 |

### Pieces

`look` is option 209 (the costume model, *inferred*); the colours are the three option-208 values, read as `ColorDB` ids for costume parts 1–3 (*inferred*).

|  | item | class | period | look | part colours |
|---|---|---|---|---|---|
| ![](wiki/assets/items/2076.png) | [[wiki/items/2076-pirate-set\|Pirate Set]] | [[wiki/classes/1-saint\|Saint]] | 2,160 min | 27 | `#131927` (75), `#131927` (75), `#820000` (16) |
| ![](wiki/assets/items/2077.png) | [[wiki/items/2077-pirate-set\|Pirate Set]] | [[wiki/classes/4-punisher\|Punisher]] | 2,160 min | 28 | `#4a2324` (71), `#820000` (16), `#131927` (75) |
| ![](wiki/assets/items/2078.png) | [[wiki/items/2078-pirate-set\|Pirate Set]] | [[wiki/classes/5-guardian\|Guardian]] | 2,160 min | 27 | `#b88357` (85), `#0f2511` (42), `#820000` (16) |

### Duration

Timed costumes run for their item period in minutes of **wearing** time: the timer only counts while the costume is worn (WM 0406 raised it from 1,440 to 2,610 minutes; [[gameplay/events-and-schedules|Events and schedules]] §9). The client rows hold 2,610 or 2,160; period 0 is a permanent costume. In Crush Online a timed costume could be *carved* (made permanent, losing its bonus) at the Merits Costume Merchant, and a Costume Remover hides it while keeping the stats ([[gameplay/crush-patch-notes|Crush patch notes]]).

### Where to get it

- [[wiki/items/2076-pirate-set|Pirate Set]]: how premium_shop, entry 23
- [[wiki/items/2077-pirate-set|Pirate Set]]: how premium_shop, entry 24
- [[wiki/items/2078-pirate-set|Pirate Set]]: how premium_shop, entry 25

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
