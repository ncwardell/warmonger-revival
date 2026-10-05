---
title: "Random box 46 ([Bronze] Medal Reward Box?)"
type: "box"
id: 46
status: "partial"
missing: ["odds", "opened_by"]
sources: ["client: RandomBox.cdb id 46", "contract: items.yaml use_item 0x42d (random box -> 0x427 reason 0x46 per item)", "image: [[gameplay/progression-and-economy]] §3–4 (Athan sells the medal boxes for 4 bronze / 3 silver / 2 gold / 1 mithril; Mithril medals only from Gold/Mithril boxes) + staff: [[gameplay/crush-patch-notes]] (Dec 2016: Magic Crafting Stone only from the Diamond box; Feb 2017: medal boxes drop more medals)"]
contents:
  - {"slot": 0, "item": 1021, "count": 10000, "p": 0}
  - {"slot": 1, "item": 1021, "count": 10000, "p": 0}
  - {"slot": 2, "item": 1021, "count": 30000, "p": 0}
  - {"slot": 3, "item": 1001, "count": 1, "p": 0}
  - {"slot": 4, "item": 1052, "count": 1, "p": 0}
  - {"slot": 5, "item": 1052, "count": 1, "p": 0}
  - {"slot": 6, "item": 7042, "count": 1, "p": 0}
  - {"slot": 7, "item": 7052, "count": 1, "p": 0}
  - {"slot": 8, "item": 7062, "count": 1, "p": 0}
  - {"slot": 9, "item": 7072, "count": 1, "p": 0}
value_4c: 10000
opened_by_guess: 1051
kind: "random_box"
---
<!-- generated:start -->
<!-- generated-keys: title=9ca46a type=24f03d id=fe2ef4 sources=d211ae contents=d23380 value_4c=8a12a3 opened_by_guess=929f96 kind=364c90 -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/1051.png) |
| **RandomBox id** | `46` |
| **Opened by** | [[wiki/items/1051-bronze-medal-reward-box\|(Bronze) Medal Reward Box]] (*guess*, not confirmed) |
| **Value @4c** | 10,000 (unknown; decoder guesses gold. The Lord of the Land reward box cost 300,000 gold to open, later 200,000 — [[gameplay/server-rules\|server rules]], WM 0426 / 0920 — so this may be the gold cost of opening: *guess*) |
| **Odds** | unknown (server side) |

### Contents

One of these is given when the box is used (contract `use_item`; *guess*: one roll per use). `p` is an unknown per-entry value (0–5; in rows 40–45 it rises with the box tier).

| slot |  | item | count | p |
|---|---|---|---|---|
| 0 | ![](wiki/assets/items/1021.png) | [[wiki/items/1021-gold\|Gold]] | 10,000 |  |
| 1 | ![](wiki/assets/items/1021.png) | [[wiki/items/1021-gold\|Gold]] | 10,000 |  |
| 2 | ![](wiki/assets/items/1021.png) | [[wiki/items/1021-gold\|Gold]] | 30,000 |  |
| 3 | ![](wiki/assets/items/1001.png) | [[wiki/items/1001-medal-silver\|Medal : Silver]] | 1 |  |
| 4 | ![](wiki/assets/items/1052.png) | [[wiki/items/1052-silver-medal-reward-box\|(Silver) Medal Reward Box]] | 1 |  |
| 5 | ![](wiki/assets/items/1052.png) | [[wiki/items/1052-silver-medal-reward-box\|(Silver) Medal Reward Box]] | 1 |  |
| 6 | ![](wiki/assets/items/7042.png) | [[wiki/items/7042-health-rune\|Health Rune]] | 1 |  |
| 7 | ![](wiki/assets/items/7052.png) | [[wiki/items/7052-mana-rune\|Mana Rune]] | 1 |  |
| 8 | ![](wiki/assets/items/7062.png) | [[wiki/items/7062-health-regeneration-rune\|Health Regeneration Rune]] | 1 |  |
| 9 | ![](wiki/assets/items/7072.png) | [[wiki/items/7072-mana-regeneration-rune\|Mana Regeneration Rune]] | 1 |  |

### Why this box item

No client column links a box item to a RandomBox row. The guess pairs rows and box items by number and contents: rows 20–25 ↔ Gaia boxes 1023–1028, 30–35 ↔ Box of the Victorious, 40–45 ↔ Box of the Participant, 46–50 ↔ the medal reward boxes, 51 ↔ the Halloween box (it holds the Jack transform scroll), 81–83 ↔ the dye boxes. Set `opened_by:` once a source confirms it.

### Seen in

- Seen in [[gameplay/crush-mechanics|Crush Online mechanics from the forum]], section *7. Medals, contribution, arena*
- Seen in [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]], section *2016-12-15: Civil War ((t816); Steam 15 Dec)*
<!-- generated:end -->

## Notes

The [Bronze] Medal Reward Box is sold by Athan for **4 bronze medals** ([[gameplay/progression-and-economy|Progression and economy]] §4, *image*; [[gameplay/crush-patch-notes|Crush patch notes]], *client*). Mithril medals came only from the Gold and Mithril boxes ([[gameplay/progression-and-economy|Progression and economy]] §3, *guide*).

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
