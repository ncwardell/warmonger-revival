---
title: "Working on that!"
type: "costume"
id: 2003
status: "stub"
missing: ["obtained_from"]
sources: ["client: Item_Base.cdb kind 32 ids 2003, 2009, 2011", "docs: [[gameplay/events-and-schedules]] §9 (WM 0406: costume duration 1,440 → 2,610 min, counts only while worn); Item_Base period@3a read as minutes (inferred)"]
items:
  - {"item": 2003, "class": "Punisher", "period": 2610, "look": 11, "colors": [1, 1, 1]}
  - {"item": 2009, "class": "Guardian", "period": 2610, "look": 13, "colors": [1, 1, 1]}
  - {"item": 2011, "class": "Punisher", "period": 2610, "look": 13, "colors": [1, 1, 1]}
classes: ["Punisher", "Guardian"]
stats: []
duration: {"minutes": 2610, "counts": "while worn"}
obtained_from: []
---
<!-- generated:start -->
<!-- generated-keys: title=e42e4f type=0d87ef id=ab165c sources=27882b items=d022b8 classes=970b90 stats=97d170 duration=88544d obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/2003.png) ![](wiki/assets/items/2009.png) ![](wiki/assets/items/2011.png) |
| **Pieces** | 3, for [[wiki/classes/4-punisher\|Punisher]], [[wiki/classes/5-guardian\|Guardian]] |
| **Duration** | 2,610 min (43.5 h) of wearing time |
| **Stat bonus** | none |

### Pieces

`look` is option 209 (the costume model, *inferred*); the colours are the three option-208 values, read as `ColorDB` ids for costume parts 1–3 (*inferred*).

|  | item | class | period | look | part colours |
|---|---|---|---|---|---|
| ![](wiki/assets/items/2003.png) | [[wiki/items/2003-working-on-that\|Working on that!]] | [[wiki/classes/4-punisher\|Punisher]] | 2,610 min | 11 | `#2a2829` (1), `#2a2829` (1), `#2a2829` (1) |
| ![](wiki/assets/items/2009.png) | [[wiki/items/2009-working-on-that\|Working on that!]] | [[wiki/classes/5-guardian\|Guardian]] | 2,610 min | 13 | `#2a2829` (1), `#2a2829` (1), `#2a2829` (1) |
| ![](wiki/assets/items/2011.png) | [[wiki/items/2011-working-on-that\|Working on that!]] | [[wiki/classes/4-punisher\|Punisher]] | 2,610 min | 13 | `#2a2829` (1), `#2a2829` (1), `#2a2829` (1) |

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
