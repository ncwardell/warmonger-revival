---
title: "Military Set"
type: "costume"
id: 2030
status: "complete"
missing: []
sources: ["client: Item_Base.cdb kind 32 ids 2030, 2031, 2032, 2039", "docs: [[gameplay/events-and-schedules]] §9 (WM 0406: costume duration 1,440 → 2,610 min, counts only while worn); Item_Base period@3a read as minutes (inferred)"]
items:
  - {"item": 2030, "class": "Guardian", "period": 2160, "look": 20, "colors": [63, 62, 44]}
  - {"item": 2031, "class": "Saint", "period": 2160, "look": 20, "colors": [91, 15, 91]}
  - {"item": 2032, "class": "Punisher", "period": 2610, "look": 20, "colors": [18, 59, 63]}
  - {"item": 2039, "class": "Punisher", "period": 2160, "look": 23, "colors": [18, 59, 63]}
classes: ["Saint", "Punisher", "Guardian"]
stats:
  - {"code": 7, "stat": "Magic Resist", "value": 20}
  - {"code": 6, "stat": "Armor", "value": 30}
  - {"code": 273, "stat": "Drop Chance(%)", "value": 5}
duration: {"minutes_by_item": {"2030": 2160, "2031": 2160, "2032": 2610, "2039": 2160}, "counts": "while worn", "note": "0 = permanent"}
obtained_from:
  - {"how": "premium_shop", "entry": 8, "item": 2030}
  - {"how": "premium_shop", "entry": 9, "item": 2031}
  - {"how": "costume_shop_crush", "price": 2000, "currency": "jewels", "days": 14, "item": 2032}
  - {"how": "premium_shop", "entry": 16, "item": 2039}
---
<!-- generated:start -->
<!-- generated-keys: title=c221b5 type=0d87ef id=f0ee73 sources=ec1875 items=5e4957 classes=292ac5 stats=f2fac1 duration=9bc973 obtained_from=2b5810 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/2030.png) ![](wiki/assets/items/2031.png) ![](wiki/assets/items/2032.png) ![](wiki/assets/items/2039.png) |
| **Pieces** | 4, for [[wiki/classes/1-saint\|Saint]], [[wiki/classes/4-punisher\|Punisher]], [[wiki/classes/5-guardian\|Guardian]] |
| **Duration** | differs per piece (see below) |
| **Stat bonus** | Magic Resist +20, Armor +30, Drop Chance(%) +5 |

### Pieces

`look` is option 209 (the costume model, *inferred*); the colours are the three option-208 values, read as `ColorDB` ids for costume parts 1–3 (*inferred*).

|  | item | class | period | look | part colours |
|---|---|---|---|---|---|
| ![](wiki/assets/items/2030.png) | [[wiki/items/2030-military-set\|Military Set]] | [[wiki/classes/5-guardian\|Guardian]] | 2,160 min | 20 | `#263145` (63), `#2d525b` (62), `#b98412` (44) |
| ![](wiki/assets/items/2031.png) | [[wiki/items/2031-military-set\|Military Set]] | [[wiki/classes/1-saint\|Saint]] | 2,160 min | 20 | `#ff0000` (91), `#46322b` (15), `#ff0000` (91) |
| ![](wiki/assets/items/2032.png) | [[wiki/items/2032-military-set\|Military Set]] | [[wiki/classes/4-punisher\|Punisher]] | 2,610 min | 20 | `#c2ab8b` (18), `#423731` (59), `#263145` (63) |
| ![](wiki/assets/items/2039.png) | [[wiki/items/2039-military-set\|Military Set]] | [[wiki/classes/4-punisher\|Punisher]] | 2,160 min | 23 | `#c2ab8b` (18), `#423731` (59), `#263145` (63) |

### Duration

Timed costumes run for their item period in minutes of **wearing** time: the timer only counts while the costume is worn (WM 0406 raised it from 1,440 to 2,610 minutes; [[gameplay/events-and-schedules|Events and schedules]] §9). The client rows hold 2,610 or 2,160; period 0 is a permanent costume. In Crush Online a timed costume could be *carved* (made permanent, losing its bonus) at the Merits Costume Merchant, and a Costume Remover hides it while keeping the stats ([[gameplay/crush-patch-notes|Crush patch notes]]).

### Where to get it

- [[wiki/items/2030-military-set|Military Set]]: how premium_shop, entry 8
- [[wiki/items/2031-military-set|Military Set]]: how premium_shop, entry 9
- [[wiki/items/2032-military-set|Military Set]]: how costume_shop_crush, price 2000, currency jewels, days 14
- [[wiki/items/2039-military-set|Military Set]]: how premium_shop, entry 16

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
