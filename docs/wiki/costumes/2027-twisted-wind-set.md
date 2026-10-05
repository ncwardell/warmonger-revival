---
title: "Twisted Wind Set"
type: "costume"
id: 2027
status: "complete"
missing: []
sources: ["client: Item_Base.cdb kind 32 ids 2027, 2028, 2029", "docs: [[gameplay/events-and-schedules]] §9 (WM 0406: costume duration 1,440 → 2,610 min, counts only while worn); Item_Base period@3a read as minutes (inferred)"]
items:
  - {"item": 2027, "class": "Saint", "period": 2610, "look": 19, "colors": [80, 36, 80]}
  - {"item": 2028, "class": "Punisher", "period": 2610, "look": 19, "colors": [41, 14, 5]}
  - {"item": 2029, "class": "Guardian", "period": 2610, "look": 19, "colors": [41, 14, 5]}
classes: ["Saint", "Punisher", "Guardian"]
stats:
  - {"code": 105, "stat": "Movement(%)", "value": 10}
duration: {"minutes": 2610, "counts": "while worn"}
obtained_from:
  - {"how": "shop", "shop": 284, "item": 2027}
  - {"how": "shop", "shop": 284, "item": 2028}
  - {"how": "shop", "shop": 284, "item": 2029}
---
<!-- generated:start -->
<!-- generated-keys: title=ef66ec type=0d87ef id=64e0cf sources=cc0c89 items=a92547 classes=292ac5 stats=bed1fe duration=88544d obtained_from=fc2f34 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/2027.png) ![](wiki/assets/items/2028.png) ![](wiki/assets/items/2029.png) |
| **Pieces** | 3, for [[wiki/classes/1-saint\|Saint]], [[wiki/classes/4-punisher\|Punisher]], [[wiki/classes/5-guardian\|Guardian]] |
| **Duration** | 2,610 min (43.5 h) of wearing time |
| **Stat bonus** | Movement(%) +10 |

### Pieces

`look` is option 209 (the costume model, *inferred*); the colours are the three option-208 values, read as `ColorDB` ids for costume parts 1–3 (*inferred*).

|  | item | class | period | look | part colours |
|---|---|---|---|---|---|
| ![](wiki/assets/items/2027.png) | [[wiki/items/2027-twisted-wind-set\|Twisted Wind Set]] | [[wiki/classes/1-saint\|Saint]] | 2,610 min | 19 | `#3a1d1f` (80), `#471b00` (36), `#3a1d1f` (80) |
| ![](wiki/assets/items/2028.png) | [[wiki/items/2028-twisted-wind-set\|Twisted Wind Set]] | [[wiki/classes/4-punisher\|Punisher]] | 2,610 min | 19 | `#1a2946` (41), `#5e4c28` (14), `#4467c5` (5) |
| ![](wiki/assets/items/2029.png) | [[wiki/items/2029-twisted-wind-set\|Twisted Wind Set]] | [[wiki/classes/5-guardian\|Guardian]] | 2,610 min | 19 | `#1a2946` (41), `#5e4c28` (14), `#4467c5` (5) |

### Duration

Timed costumes run for their item period in minutes of **wearing** time: the timer only counts while the costume is worn (WM 0406 raised it from 1,440 to 2,610 minutes; [[gameplay/events-and-schedules|Events and schedules]] §9). The client rows hold 2,610 or 2,160; period 0 is a permanent costume. In Crush Online a timed costume could be *carved* (made permanent, losing its bonus) at the Merits Costume Merchant, and a Costume Remover hides it while keeping the stats ([[gameplay/crush-patch-notes|Crush patch notes]]).

### Where to get it

- [[wiki/items/2027-twisted-wind-set|Twisted Wind Set]]: sold in [[wiki/shops/284-ashley-s-shop-merits-costume-merchant|Ashley's shop (Merits Costume Merchant)]]
- [[wiki/items/2028-twisted-wind-set|Twisted Wind Set]]: sold in [[wiki/shops/284-ashley-s-shop-merits-costume-merchant|Ashley's shop (Merits Costume Merchant)]]
- [[wiki/items/2029-twisted-wind-set|Twisted Wind Set]]: sold in [[wiki/shops/284-ashley-s-shop-merits-costume-merchant|Ashley's shop (Merits Costume Merchant)]]

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
