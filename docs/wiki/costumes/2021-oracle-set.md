---
title: "Oracle Set"
type: "costume"
id: 2021
status: "complete"
missing: []
sources: ["client: Item_Base.cdb kind 32 ids 2021, 2022, 2023, 2082, 2083, 2084", "docs: [[gameplay/events-and-schedules]] §9 (WM 0406: costume duration 1,440 → 2,610 min, counts only while worn); Item_Base period@3a read as minutes (inferred)"]
items:
  - {"item": 2021, "class": "Saint", "period": 2610, "look": 17, "colors": [5, 48, 6]}
  - {"item": 2022, "class": "Punisher", "period": 2610, "look": 17, "colors": [6, 5, 6]}
  - {"item": 2023, "class": "Guardian", "period": 2610, "look": 17, "colors": [5, 48, 6]}
  - {"item": 2082, "class": "Saint", "period": 2610, "look": 17, "colors": [5, 48, 6]}
  - {"item": 2083, "class": "Punisher", "period": 2610, "look": 17, "colors": [6, 5, 6]}
  - {"item": 2084, "class": "Guardian", "period": 2610, "look": 17, "colors": [5, 48, 6]}
classes: ["Saint", "Punisher", "Guardian"]
stats:
  - {"code": 34, "stat": "Mana Regeneration", "value": 4}
duration: {"minutes": 2610, "counts": "while worn"}
obtained_from:
  - {"how": "quest_reward", "quest": 10, "count": 1, "item": 2021}
  - {"how": "quest_reward", "quest": 10, "count": 1, "item": 2022}
  - {"how": "quest_reward", "quest": 10, "count": 1, "item": 2023}
  - {"how": "shop", "shop": 284, "item": 2082}
  - {"how": "shop", "shop": 284, "item": 2083}
  - {"how": "shop", "shop": 284, "item": 2084}
---
<!-- generated:start -->
<!-- generated-keys: title=915252 type=0d87ef id=fd93ac sources=dd64f1 items=e8709c classes=292ac5 stats=fe52a3 duration=88544d obtained_from=6ec984 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/2021.png) ![](wiki/assets/items/2022.png) ![](wiki/assets/items/2023.png) ![](wiki/assets/items/2082.png) ![](wiki/assets/items/2083.png) ![](wiki/assets/items/2084.png) |
| **Pieces** | 6, for [[wiki/classes/1-saint\|Saint]], [[wiki/classes/4-punisher\|Punisher]], [[wiki/classes/5-guardian\|Guardian]] |
| **Duration** | 2,610 min (43.5 h) of wearing time |
| **Stat bonus** | Mana Regeneration +4 |

### Pieces

`look` is option 209 (the costume model, *inferred*); the colours are the three option-208 values, read as `ColorDB` ids for costume parts 1–3 (*inferred*).

|  | item | class | period | look | part colours |
|---|---|---|---|---|---|
| ![](wiki/assets/items/2021.png) | [[wiki/items/2021-oracle-set\|Oracle Set]] | [[wiki/classes/1-saint\|Saint]] | 2,610 min | 17 | `#4467c5` (5), `#6c71c5` (48), `#eaebf0` (6) |
| ![](wiki/assets/items/2022.png) | [[wiki/items/2022-oracle-set\|Oracle Set]] | [[wiki/classes/4-punisher\|Punisher]] | 2,610 min | 17 | `#eaebf0` (6), `#4467c5` (5), `#eaebf0` (6) |
| ![](wiki/assets/items/2023.png) | [[wiki/items/2023-oracle-set\|Oracle Set]] | [[wiki/classes/5-guardian\|Guardian]] | 2,610 min | 17 | `#4467c5` (5), `#6c71c5` (48), `#eaebf0` (6) |
| ![](wiki/assets/items/2082.png) | [[wiki/items/2082-oracle-set\|Oracle Set]] | [[wiki/classes/1-saint\|Saint]] | 2,610 min | 17 | `#4467c5` (5), `#6c71c5` (48), `#eaebf0` (6) |
| ![](wiki/assets/items/2083.png) | [[wiki/items/2083-oracle-set\|Oracle Set]] | [[wiki/classes/4-punisher\|Punisher]] | 2,610 min | 17 | `#eaebf0` (6), `#4467c5` (5), `#eaebf0` (6) |
| ![](wiki/assets/items/2084.png) | [[wiki/items/2084-oracle-set\|Oracle Set]] | [[wiki/classes/5-guardian\|Guardian]] | 2,610 min | 17 | `#4467c5` (5), `#6c71c5` (48), `#eaebf0` (6) |

### Duration

Timed costumes run for their item period in minutes of **wearing** time: the timer only counts while the costume is worn (WM 0406 raised it from 1,440 to 2,610 minutes; [[gameplay/events-and-schedules|Events and schedules]] §9). The client rows hold 2,610 or 2,160; period 0 is a permanent costume. In Crush Online a timed costume could be *carved* (made permanent, losing its bonus) at the Merits Costume Merchant, and a Costume Remover hides it while keeping the stats ([[gameplay/crush-patch-notes|Crush patch notes]]).

### Where to get it

- [[wiki/items/2021-oracle-set|Oracle Set]]: reward of quest [[wiki/quests/10-find-the-secret-document|Find the Secret Document]]
- [[wiki/items/2022-oracle-set|Oracle Set]]: reward of quest [[wiki/quests/10-find-the-secret-document|Find the Secret Document]]
- [[wiki/items/2023-oracle-set|Oracle Set]]: reward of quest [[wiki/quests/10-find-the-secret-document|Find the Secret Document]]
- [[wiki/items/2082-oracle-set|Oracle Set]]: sold in [[wiki/shops/284-ashley-s-shop-merits-costume-merchant|Ashley's shop (Merits Costume Merchant)]]
- [[wiki/items/2083-oracle-set|Oracle Set]]: sold in [[wiki/shops/284-ashley-s-shop-merits-costume-merchant|Ashley's shop (Merits Costume Merchant)]]
- [[wiki/items/2084-oracle-set|Oracle Set]]: sold in [[wiki/shops/284-ashley-s-shop-merits-costume-merchant|Ashley's shop (Merits Costume Merchant)]]

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
