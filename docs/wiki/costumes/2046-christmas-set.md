---
title: "Christmas Set"
type: "costume"
id: 2046
status: "complete"
missing: []
sources: ["client: Item_Base.cdb kind 32 ids 2046, 2047, 2048, 2085, 2086, 2087", "docs: [[gameplay/events-and-schedules]] §9 (WM 0406: costume duration 1,440 → 2,610 min, counts only while worn); Item_Base period@3a read as minutes (inferred)"]
items:
  - {"item": 2046, "class": "Saint", "period": 2610, "look": 25, "colors": [16, 42, 16]}
  - {"item": 2047, "class": "Punisher", "period": 2610, "look": 26, "colors": [16, 42, 66]}
  - {"item": 2048, "class": "Guardian", "period": 2610, "look": 25, "colors": [71, 16, 36]}
  - {"item": 2085, "class": "Saint", "period": 0, "look": 25, "colors": [16, 42, 16]}
  - {"item": 2086, "class": "Punisher", "period": 0, "look": 26, "colors": [16, 42, 66]}
  - {"item": 2087, "class": "Guardian", "period": 0, "look": 25, "colors": [71, 16, 36]}
classes: ["Saint", "Punisher", "Guardian"]
stats:
  - {"code": 273, "stat": "Drop Chance(%)", "value": 10}
duration: {"minutes_by_item": {"2046": 2610, "2047": 2610, "2048": 2610, "2085": 0, "2086": 0, "2087": 0}, "counts": "while worn", "note": "0 = permanent"}
obtained_from:
  - {"how": "costume_shop_crush", "price": 3800, "currency": "jewels", "days": 14, "item": 2046}
  - {"how": "costume_shop_crush", "price": 3800, "currency": "jewels", "days": 14, "item": 2047}
  - {"how": "costume_shop_crush", "price": 3800, "currency": "jewels", "days": 14, "item": 2048}
  - {"how": "premium_shop", "entry": 54, "item": 2085}
  - {"how": "costume_shop_crush", "price": 5000, "currency": "jewels", "item": 2085}
  - {"how": "premium_shop", "entry": 55, "item": 2086}
  - {"how": "costume_shop_crush", "price": 5000, "currency": "jewels", "item": 2086}
  - {"how": "premium_shop", "entry": 56, "item": 2087}
  - {"how": "costume_shop_crush", "price": 5000, "currency": "jewels", "item": 2087}
---
<!-- generated:start -->
<!-- generated-keys: title=a5f2eb type=0d87ef id=d656e6 sources=a7ae7b items=25eae4 classes=292ac5 stats=582601 duration=ed981a obtained_from=b1ca07 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/2046.png) ![](wiki/assets/items/2047.png) ![](wiki/assets/items/2048.png) ![](wiki/assets/items/2085.png) ![](wiki/assets/items/2086.png) ![](wiki/assets/items/2087.png) |
| **Pieces** | 6, for [[wiki/classes/1-saint\|Saint]], [[wiki/classes/4-punisher\|Punisher]], [[wiki/classes/5-guardian\|Guardian]] |
| **Duration** | differs per piece (see below) |
| **Stat bonus** | Drop Chance(%) +10 |

### Pieces

`look` is option 209 (the costume model, *inferred*); the colours are the three option-208 values, read as `ColorDB` ids for costume parts 1–3 (*inferred*).

|  | item | class | period | look | part colours |
|---|---|---|---|---|---|
| ![](wiki/assets/items/2046.png) | [[wiki/items/2046-christmas-set\|Christmas Set]] | [[wiki/classes/1-saint\|Saint]] | 2,610 min | 25 | `#820000` (16), `#0f2511` (42), `#820000` (16) |
| ![](wiki/assets/items/2047.png) | [[wiki/items/2047-christmas-set\|Christmas Set]] | [[wiki/classes/4-punisher\|Punisher]] | 2,610 min | 26 | `#820000` (16), `#0f2511` (42), `#2d4b31` (66) |
| ![](wiki/assets/items/2048.png) | [[wiki/items/2048-christmas-set\|Christmas Set]] | [[wiki/classes/5-guardian\|Guardian]] | 2,610 min | 25 | `#4a2324` (71), `#820000` (16), `#471b00` (36) |
| ![](wiki/assets/items/2085.png) | [[wiki/items/2085-christmas-set\|Christmas Set]] | [[wiki/classes/1-saint\|Saint]] | permanent | 25 | `#820000` (16), `#0f2511` (42), `#820000` (16) |
| ![](wiki/assets/items/2086.png) | [[wiki/items/2086-christmas-set\|Christmas Set]] | [[wiki/classes/4-punisher\|Punisher]] | permanent | 26 | `#820000` (16), `#0f2511` (42), `#2d4b31` (66) |
| ![](wiki/assets/items/2087.png) | [[wiki/items/2087-christmas-set\|Christmas Set]] | [[wiki/classes/5-guardian\|Guardian]] | permanent | 25 | `#4a2324` (71), `#820000` (16), `#471b00` (36) |

### Duration

Timed costumes run for their item period in minutes of **wearing** time: the timer only counts while the costume is worn (WM 0406 raised it from 1,440 to 2,610 minutes; [[gameplay/events-and-schedules|Events and schedules]] §9). The client rows hold 2,610 or 2,160; period 0 is a permanent costume. In Crush Online a timed costume could be *carved* (made permanent, losing its bonus) at the Merits Costume Merchant, and a Costume Remover hides it while keeping the stats ([[gameplay/crush-patch-notes|Crush patch notes]]).

### Where to get it

- [[wiki/items/2046-christmas-set|Christmas Set]]: how costume_shop_crush, price 3800, currency jewels, days 14
- [[wiki/items/2047-christmas-set|Christmas Set]]: how costume_shop_crush, price 3800, currency jewels, days 14
- [[wiki/items/2048-christmas-set|Christmas Set]]: how costume_shop_crush, price 3800, currency jewels, days 14
- [[wiki/items/2085-christmas-set|Christmas Set]]: how premium_shop, entry 54
- [[wiki/items/2085-christmas-set|Christmas Set]]: how costume_shop_crush, price 5000, currency jewels
- [[wiki/items/2086-christmas-set|Christmas Set]]: how premium_shop, entry 55
- [[wiki/items/2086-christmas-set|Christmas Set]]: how costume_shop_crush, price 5000, currency jewels
- [[wiki/items/2087-christmas-set|Christmas Set]]: how premium_shop, entry 56
- [[wiki/items/2087-christmas-set|Christmas Set]]: how costume_shop_crush, price 5000, currency jewels

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
