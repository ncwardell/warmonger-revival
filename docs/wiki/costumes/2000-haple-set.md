---
title: "Haple Set"
type: "costume"
id: 2000
status: "complete"
missing: []
sources: ["client: Item_Base.cdb kind 32 ids 2000, 2001, 2002, 2079, 2080, 2081", "docs: [[gameplay/events-and-schedules]] §9 (WM 0406: costume duration 1,440 → 2,610 min, counts only while worn); Item_Base period@3a read as minutes (inferred)"]
items:
  - {"item": 2000, "class": "Punisher", "period": 2610, "look": 10, "colors": [75, 41, 11]}
  - {"item": 2001, "class": "Saint", "period": 2610, "look": 10, "colors": [16, 16, 15]}
  - {"item": 2002, "class": "Guardian", "period": 2610, "look": 10, "colors": [6, 75, 36]}
  - {"item": 2079, "class": "Punisher", "period": 2610, "look": 10, "colors": [75, 41, 11]}
  - {"item": 2080, "class": "Saint", "period": 2610, "look": 10, "colors": [16, 16, 15]}
  - {"item": 2081, "class": "Guardian", "period": 2610, "look": 10, "colors": [6, 75, 36]}
classes: ["Saint", "Punisher", "Guardian"]
stats:
  - {"code": 105, "stat": "Movement(%)", "value": 10}
duration: {"minutes": 2610, "counts": "while worn"}
obtained_from:
  - {"how": "quest_reward", "quest": 24, "count": 1, "item": 2000}
  - {"how": "quest_reward", "quest": 23, "count": 1, "item": 2001}
  - {"how": "quest_reward", "quest": 25, "count": 1, "item": 2002}
  - {"how": "shop", "shop": 284, "item": 2079}
  - {"how": "shop", "shop": 284, "item": 2080}
  - {"how": "shop", "shop": 284, "item": 2081}
---
<!-- generated:start -->
<!-- generated-keys: title=e1c17c type=0d87ef id=a4ac91 sources=4a3339 items=3dbb2f classes=292ac5 stats=bed1fe duration=88544d obtained_from=ab0cf7 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/2000.png) ![](wiki/assets/items/2001.png) ![](wiki/assets/items/2002.png) ![](wiki/assets/items/2079.png) ![](wiki/assets/items/2080.png) ![](wiki/assets/items/2081.png) |
| **Pieces** | 6, for [[wiki/classes/1-saint\|Saint]], [[wiki/classes/4-punisher\|Punisher]], [[wiki/classes/5-guardian\|Guardian]] |
| **Duration** | 2,610 min (43.5 h) of wearing time |
| **Stat bonus** | Movement(%) +10 |

### Pieces

`look` is option 209 (the costume model, *inferred*); the colours are the three option-208 values, read as `ColorDB` ids for costume parts 1–3 (*inferred*).

|  | item | class | period | look | part colours |
|---|---|---|---|---|---|
| ![](wiki/assets/items/2000.png) | [[wiki/items/2000-haple-set\|Haple Set]] | [[wiki/classes/4-punisher\|Punisher]] | 2,610 min | 10 | `#131927` (75), `#1a2946` (41), `#2f8ad9` (11) |
| ![](wiki/assets/items/2001.png) | [[wiki/items/2001-haple-set\|Haple Set]] | [[wiki/classes/1-saint\|Saint]] | 2,610 min | 10 | `#820000` (16), `#820000` (16), `#46322b` (15) |
| ![](wiki/assets/items/2002.png) | [[wiki/items/2002-haple-set\|Haple Set]] | [[wiki/classes/5-guardian\|Guardian]] | 2,610 min | 10 | `#eaebf0` (6), `#131927` (75), `#471b00` (36) |
| ![](wiki/assets/items/2079.png) | [[wiki/items/2079-haple-set\|Haple Set]] | [[wiki/classes/4-punisher\|Punisher]] | 2,610 min | 10 | `#131927` (75), `#1a2946` (41), `#2f8ad9` (11) |
| ![](wiki/assets/items/2080.png) | [[wiki/items/2080-haple-set\|Haple Set]] | [[wiki/classes/1-saint\|Saint]] | 2,610 min | 10 | `#820000` (16), `#820000` (16), `#46322b` (15) |
| ![](wiki/assets/items/2081.png) | [[wiki/items/2081-haple-set\|Haple Set]] | [[wiki/classes/5-guardian\|Guardian]] | 2,610 min | 10 | `#eaebf0` (6), `#131927` (75), `#471b00` (36) |

### Duration

Timed costumes run for their item period in minutes of **wearing** time: the timer only counts while the costume is worn (WM 0406 raised it from 1,440 to 2,610 minutes; [[gameplay/events-and-schedules|Events and schedules]] §9). The client rows hold 2,610 or 2,160; period 0 is a permanent costume. In Crush Online a timed costume could be *carved* (made permanent, losing its bonus) at the Merits Costume Merchant, and a Costume Remover hides it while keeping the stats ([[gameplay/crush-patch-notes|Crush patch notes]]).

### Where to get it

- [[wiki/items/2000-haple-set|Haple Set]]: reward of quest [[wiki/quests/24-stepping-up-your-game|Stepping up your game]]
- [[wiki/items/2001-haple-set|Haple Set]]: reward of quest [[wiki/quests/23-stepping-up-your-game|Stepping up your game]]
- [[wiki/items/2002-haple-set|Haple Set]]: reward of quest [[wiki/quests/25-stepping-up-your-game|Stepping up your game]]
- [[wiki/items/2079-haple-set|Haple Set]]: sold in [[wiki/shops/284-ashley-s-shop-merits-costume-merchant|Ashley's shop (Merits Costume Merchant)]]
- [[wiki/items/2080-haple-set|Haple Set]]: sold in [[wiki/shops/284-ashley-s-shop-merits-costume-merchant|Ashley's shop (Merits Costume Merchant)]]
- [[wiki/items/2081-haple-set|Haple Set]]: sold in [[wiki/shops/284-ashley-s-shop-merits-costume-merchant|Ashley's shop (Merits Costume Merchant)]]

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
