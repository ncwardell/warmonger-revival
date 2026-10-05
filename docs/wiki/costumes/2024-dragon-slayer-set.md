---
title: "Dragon Slayer Set"
type: "costume"
id: 2024
status: "complete"
missing: []
sources: ["client: Item_Base.cdb kind 32 ids 2024, 2025, 2026", "docs: [[gameplay/events-and-schedules]] §9 (WM 0406: costume duration 1,440 → 2,610 min, counts only while worn); Item_Base period@3a read as minutes (inferred)"]
items:
  - {"item": 2024, "class": "Saint", "period": 2160, "look": 18, "colors": [6, 15, 6]}
  - {"item": 2025, "class": "Punisher", "period": 2160, "look": 18, "colors": [33, 34, 44]}
  - {"item": 2026, "class": "Guardian", "period": 2160, "look": 18, "colors": [75, 6, 76]}
classes: ["Saint", "Punisher", "Guardian"]
stats:
  - {"code": 1, "stat": "Attack", "value": 30}
  - {"code": 6, "stat": "Armor", "value": 25}
  - {"code": 273, "stat": "Drop Chance(%)", "value": 5}
duration: {"minutes": 2160, "counts": "while worn"}
obtained_from:
  - {"how": "premium_shop", "entry": 5, "item": 2024}
  - {"how": "premium_shop", "entry": 6, "item": 2025}
  - {"how": "premium_shop", "entry": 7, "item": 2026}
---
<!-- generated:start -->
<!-- generated-keys: title=b1c73b type=0d87ef id=7e79a3 sources=edf2d5 items=62d508 classes=292ac5 stats=2ff5a5 duration=1c0d99 obtained_from=b94567 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/2024.png) ![](wiki/assets/items/2025.png) ![](wiki/assets/items/2026.png) |
| **Pieces** | 3, for [[wiki/classes/1-saint\|Saint]], [[wiki/classes/4-punisher\|Punisher]], [[wiki/classes/5-guardian\|Guardian]] |
| **Duration** | 2,160 min (36.0 h) of wearing time |
| **Stat bonus** | Attack +30, Armor +25, Drop Chance(%) +5 |

### Pieces

`look` is option 209 (the costume model, *inferred*); the colours are the three option-208 values, read as `ColorDB` ids for costume parts 1–3 (*inferred*).

|  | item | class | period | look | part colours |
|---|---|---|---|---|---|
| ![](wiki/assets/items/2024.png) | [[wiki/items/2024-dragon-slayer-set\|Dragon Slayer Set]] | [[wiki/classes/1-saint\|Saint]] | 2,160 min | 18 | `#eaebf0` (6), `#46322b` (15), `#eaebf0` (6) |
| ![](wiki/assets/items/2025.png) | [[wiki/items/2025-dragon-slayer-set\|Dragon Slayer Set]] | [[wiki/classes/4-punisher\|Punisher]] | 2,160 min | 18 | `#6c451e` (33), `#4a3137` (34), `#b98412` (44) |
| ![](wiki/assets/items/2026.png) | [[wiki/items/2026-dragon-slayer-set\|Dragon Slayer Set]] | [[wiki/classes/5-guardian\|Guardian]] | 2,160 min | 18 | `#131927` (75), `#eaebf0` (6), `#172741` (76) |

### Duration

Timed costumes run for their item period in minutes of **wearing** time: the timer only counts while the costume is worn (WM 0406 raised it from 1,440 to 2,610 minutes; [[gameplay/events-and-schedules|Events and schedules]] §9). The client rows hold 2,610 or 2,160; period 0 is a permanent costume. In Crush Online a timed costume could be *carved* (made permanent, losing its bonus) at the Merits Costume Merchant, and a Costume Remover hides it while keeping the stats ([[gameplay/crush-patch-notes|Crush patch notes]]).

### Where to get it

- [[wiki/items/2024-dragon-slayer-set|Dragon Slayer Set]]: how premium_shop, entry 5
- [[wiki/items/2025-dragon-slayer-set|Dragon Slayer Set]]: how premium_shop, entry 6
- [[wiki/items/2026-dragon-slayer-set|Dragon Slayer Set]]: how premium_shop, entry 7

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
