---
title: "Random box 50 ([Diamond] Medal Rewar Box?)"
type: "box"
id: 50
status: "partial"
missing: ["odds", "opened_by"]
sources: ["client: RandomBox.cdb id 50", "contract: items.yaml use_item 0x42d (random box -> 0x427 reason 0x46 per item)", "image: [[gameplay/progression-and-economy]] §3–4 (Athan sells the medal boxes for 4 bronze / 3 silver / 2 gold / 1 mithril; Mithril medals only from Gold/Mithril boxes) + staff: [[gameplay/crush-patch-notes]] (Dec 2016: Magic Crafting Stone only from the Diamond box; Feb 2017: medal boxes drop more medals)"]
contents:
  - {"slot": 0, "item": 1021, "count": 300000, "p": 0}
  - {"slot": 1, "item": 1021, "count": 300000, "p": 0}
  - {"slot": 2, "item": 1021, "count": 560000, "p": 0}
  - {"slot": 3, "item": 1021, "count": 1000000, "p": 0}
  - {"slot": 4, "item": 1021, "count": 1000000, "p": 0}
  - {"slot": 5, "item": 1021, "count": 1000000, "p": 0}
  - {"slot": 6, "item": 7164, "count": 1, "p": 0}
  - {"slot": 7, "item": 7164, "count": 1, "p": 0}
  - {"slot": 8, "item": 7144, "count": 1, "p": 0}
  - {"slot": 9, "item": 7154, "count": 1, "p": 0}
value_4c: 500000
opened_by_guess: 1055
kind: "random_box"
---
<!-- generated:start -->
<!-- generated-keys: title=8d143c type=24f03d id=e1822d sources=0b0cfd contents=719856 value_4c=15f8d1 opened_by_guess=54c179 kind=364c90 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/1055.png) |
| **RandomBox id** | `50` |
| **Opened by** | [[wiki/items/1055-diamond-medal-rewar-box\|(Diamond) Medal Rewar Box]] (*guess*, not confirmed) |
| **Value @4c** | 500,000 (unknown; decoder guesses gold. The Lord of the Land reward box cost 300,000 gold to open, later 200,000 — [[gameplay/server-rules\|server rules]], WM 0426 / 0920 — so this may be the gold cost of opening: *guess*) |
| **Odds** | unknown (server side) |

### Contents

One of these is given when the box is used (contract `use_item`; *guess*: one roll per use). `p` is an unknown per-entry value (0–5; in rows 40–45 it rises with the box tier).

| slot |  | item | count | p |
|---|---|---|---|---|
| 0 | ![](wiki/assets/items/1021.png) | [[wiki/items/1021-gold\|Gold]] | 300,000 |  |
| 1 | ![](wiki/assets/items/1021.png) | [[wiki/items/1021-gold\|Gold]] | 300,000 |  |
| 2 | ![](wiki/assets/items/1021.png) | [[wiki/items/1021-gold\|Gold]] | 560,000 |  |
| 3 | ![](wiki/assets/items/1021.png) | [[wiki/items/1021-gold\|Gold]] | 1,000,000 |  |
| 4 | ![](wiki/assets/items/1021.png) | [[wiki/items/1021-gold\|Gold]] | 1,000,000 |  |
| 5 | ![](wiki/assets/items/1021.png) | [[wiki/items/1021-gold\|Gold]] | 1,000,000 |  |
| 6 | ![](wiki/assets/items/7164.png) | [[wiki/items/7164-movement-rune\|Movement(%) Rune]] | 1 |  |
| 7 | ![](wiki/assets/items/7164.png) | [[wiki/items/7164-movement-rune\|Movement(%) Rune]] | 1 |  |
| 8 | ![](wiki/assets/items/7144.png) | [[wiki/items/7144-pvp-attack-rune\|PvP Attack Rune]] | 1 |  |
| 9 | ![](wiki/assets/items/7154.png) | [[wiki/items/7154-pvp-armor-rune\|PvP Armor Rune]] | 1 |  |

### Why this box item

No client column links a box item to a RandomBox row. The guess pairs rows and box items by number and contents: rows 20–25 ↔ Gaia boxes 1023–1028, 30–35 ↔ Box of the Victorious, 40–45 ↔ Box of the Participant, 46–50 ↔ the medal reward boxes, 51 ↔ the Halloween box (it holds the Jack transform scroll), 81–83 ↔ the dye boxes. Set `opened_by:` once a source confirms it.

### Seen in

- Seen in [[gameplay/crush-mechanics|Crush Online mechanics from the forum]], section *7. Medals, contribution, arena*
- Seen in [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]], section *2016-12-15: Civil War ((t816); Steam 15 Dec)*
<!-- generated:end -->

## Notes

The [Diamond] Medal Reward Box is not on Athan's price list; it comes out of the Mithril box ([[gameplay/progression-and-economy|Progression and economy]] §4, *image*; [[gameplay/crush-patch-notes|Crush patch notes]], *client*). Mithril medals came only from the Gold and Mithril boxes ([[gameplay/progression-and-economy|Progression and economy]] §3, *guide*). In Crush Online the Magic Crafting Stone was sold only through this box from Dec 2016 ([[gameplay/crush-patch-notes|Crush patch notes]], [[gameplay/crush-mechanics|Crush mechanics]], *staff*).

## Behaviour

Crush Online changed all box loot in Dec 2016 (image lost) and made the medal boxes drop more medals in Feb 2017 ([[gameplay/crush-patch-notes|Crush patch notes]], *staff*).

## Sources

- image: [[gameplay/progression-and-economy]] §3–4 (Athan sells the medal boxes for 4 bronze / 3 silver / 2 gold / 1 mithril; Mithril medals only from Gold/Mithril boxes) + staff: [[gameplay/crush-patch-notes]] (Dec 2016: Magic Crafting Stone only from the Diamond box; Feb 2017: medal boxes drop more medals)

## Open questions

No odds survive; [[gameplay/sources|Sources]] (open item 10) lists box odds as unknown.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
