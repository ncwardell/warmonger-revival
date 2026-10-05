---
title: "Random box 48 ([Gold] Medal Reward Box?)"
type: "box"
id: 48
status: "partial"
missing: ["odds", "opened_by"]
sources: ["client: RandomBox.cdb id 48", "contract: items.yaml use_item 0x42d (random box -> 0x427 reason 0x46 per item)", "image: [[gameplay/progression-and-economy]] §3–4 (Athan sells the medal boxes for 4 bronze / 3 silver / 2 gold / 1 mithril; Mithril medals only from Gold/Mithril boxes) + staff: [[gameplay/crush-patch-notes]] (Dec 2016: Magic Crafting Stone only from the Diamond box; Feb 2017: medal boxes drop more medals)"]
contents:
  - {"slot": 0, "item": 1021, "count": 60000, "p": 0}
  - {"slot": 1, "item": 1021, "count": 60000, "p": 0}
  - {"slot": 2, "item": 1021, "count": 140000, "p": 0}
  - {"slot": 3, "item": 999, "count": 1, "p": 0}
  - {"slot": 4, "item": 1054, "count": 1, "p": 0}
  - {"slot": 5, "item": 1054, "count": 1, "p": 0}
  - {"slot": 6, "item": 7082, "count": 1, "p": 0}
  - {"slot": 7, "item": 7092, "count": 1, "p": 0}
  - {"slot": 8, "item": 7122, "count": 1, "p": 0}
  - {"slot": 9, "item": 7132, "count": 1, "p": 0}
value_4c: 100000
opened_by_guess: 1053
kind: "random_box"
---
<!-- generated:start -->
<!-- generated-keys: title=ff83c4 type=24f03d id=64e095 sources=ef1090 contents=a69216 value_4c=409e95 opened_by_guess=17cc4e kind=364c90 -->
|  |  |
|---|---|
|  | ![](../assets/items/1053.png) |
| **RandomBox id** | `48` |
| **Opened by** | [[wiki/items/1053-gold-medal-reward-box\|(Gold) Medal Reward Box]] (*guess*, not confirmed) |
| **Value @4c** | 100,000 (unknown; decoder guesses gold. The Lord of the Land reward box cost 300,000 gold to open, later 200,000 — [[gameplay/server-rules\|server rules]], WM 0426 / 0920 — so this may be the gold cost of opening: *guess*) |
| **Odds** | unknown (server side) |

### Contents

One of these is given when the box is used (contract `use_item`; *guess*: one roll per use). `p` is an unknown per-entry value (0–5; in rows 40–45 it rises with the box tier).

| slot |  | item | count | p |
|---|---|---|---|---|
| 0 | ![](../assets/items/1021.png) | [[wiki/items/1021-gold\|Gold]] | 60,000 |  |
| 1 | ![](../assets/items/1021.png) | [[wiki/items/1021-gold\|Gold]] | 60,000 |  |
| 2 | ![](../assets/items/1021.png) | [[wiki/items/1021-gold\|Gold]] | 140,000 |  |
| 3 | ![](../assets/items/999.png) | [[wiki/items/999-medal-mithril\|Medal : Mithril]] | 1 |  |
| 4 | ![](../assets/items/1054.png) | [[wiki/items/1054-mithril-medal-reward-box\|(Mithril) Medal Reward Box]] | 1 |  |
| 5 | ![](../assets/items/1054.png) | [[wiki/items/1054-mithril-medal-reward-box\|(Mithril) Medal Reward Box]] | 1 |  |
| 6 | ![](../assets/items/7082.png) | [[wiki/items/7082-armor-penetration-rune\|Armor Penetration Rune]] | 1 |  |
| 7 | ![](../assets/items/7092.png) | [[wiki/items/7092-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | 1 |  |
| 8 | ![](../assets/items/7122.png) | [[wiki/items/7122-life-steal-rune\|Life Steal Rune]] | 1 |  |
| 9 | ![](../assets/items/7132.png) | [[wiki/items/7132-spell-vamp-rune\|Spell Vamp Rune]] | 1 |  |

### Why this box item

No client column links a box item to a RandomBox row. The guess pairs rows and box items by number and contents: rows 20–25 ↔ Gaia boxes 1023–1028, 30–35 ↔ Box of the Victorious, 40–45 ↔ Box of the Participant, 46–50 ↔ the medal reward boxes, 51 ↔ the Halloween box (it holds the Jack transform scroll), 81–83 ↔ the dye boxes. Set `opened_by:` once a source confirms it.
<!-- generated:end -->

## Notes

The [Gold] Medal Reward Box is sold by Athan for **2 gold medals** ([[gameplay/progression-and-economy|Progression and economy]] §4, *image*; [[gameplay/crush-patch-notes|Crush patch notes]], *client*). Mithril medals came only from the Gold and Mithril boxes ([[gameplay/progression-and-economy|Progression and economy]] §3, *guide*).

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
