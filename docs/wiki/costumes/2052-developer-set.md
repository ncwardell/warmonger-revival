---
title: "Developer Set"
type: "costume"
id: 2052
status: "stub"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb kind 32 ids 2052, 2053, 2054"]
items:
  - {"item": 2052, "class": "Saint", "period": 0, "look": 29, "colors": [8, 5, 6]}
  - {"item": 2053, "class": "Guardian", "period": 0, "look": 29, "colors": [81, 56, 6]}
  - {"item": 2054, "class": "Punisher", "period": 0, "look": 30, "colors": [16, 66, 42]}
classes: ["Saint", "Punisher", "Guardian"]
stats: []
duration: {"permanent": true}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=e1223d type=0d87ef id=a2cf0c sources=44e835 items=c141ee classes=292ac5 stats=97d170 duration=bca91d obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/2052.png) ![](wiki/assets/items/2053.png) ![](wiki/assets/items/2054.png) |
| **Pieces** | 3, for [[wiki/classes/1-saint\|Saint]], [[wiki/classes/4-punisher\|Punisher]], [[wiki/classes/5-guardian\|Guardian]] |
| **Duration** | permanent (period 0) |
| **Stat bonus** | none |

### Tooltip

> Bugs +20%
> Damage -9999

### Pieces

`look` is option 209 (the costume model, *inferred*); the colours are the three option-208 values, read as `ColorDB` ids for costume parts 1–3 (*inferred*).

|  | item | class | period | look | part colours |
|---|---|---|---|---|---|
| ![](wiki/assets/items/2052.png) | [[wiki/items/2052-developer-set\|Developer Set]] | [[wiki/classes/1-saint\|Saint]] | permanent | 29 | `#ba2924` (8), `#4467c5` (5), `#eaebf0` (6) |
| ![](wiki/assets/items/2053.png) | [[wiki/items/2053-developer-set\|Developer Set]] | [[wiki/classes/5-guardian\|Guardian]] | permanent | 29 | `#2a3547` (81), `#992437` (56), `#eaebf0` (6) |
| ![](wiki/assets/items/2054.png) | [[wiki/items/2054-developer-set\|Developer Set]] | [[wiki/classes/4-punisher\|Punisher]] | permanent | 30 | `#820000` (16), `#2d4b31` (66), `#0f2511` (42) |

### Duration

Timed costumes run for their item period in minutes of **wearing** time: the timer only counts while the costume is worn (WM 0406 raised it from 1,440 to 2,610 minutes; [[gameplay/events-and-schedules|Events and schedules]] §9). The client rows hold 2,610 or 2,160; period 0 is a permanent costume. In Crush Online a timed costume could be *carved* (made permanent, losing its bonus) at the Merits Costume Merchant, and a Costume Remover hides it while keeping the stats ([[gameplay/crush-patch-notes|Crush patch notes]]).

### Where to get it

Nothing in the client data (no shop, box, quest or gacha row). Costumes were sold in the cash shop and by the Merits costume merchant for medals ([[gameplay/reinforce-and-runes|Reinforce and runes]]: costume medal prices); add the source to `obtained_from:`.

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
