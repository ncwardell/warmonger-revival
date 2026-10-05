---
title: "Armor Rune upgrades"
type: "upgrade"
id: 1003
status: "stub"
missing: ["success_rates"]
sources: ["client: JewelSocketMake.cdb group 3 (rows 21–30)", "docs: [[gameplay/reinforce-and-runes]] §1 (WM 0920 rune cost table matches JewelSocketMake +0→+9)", "contract: items.yaml rune_upgrade 0x4a8, server_rules craft_reinforce_rune_odds"]
group: 3
rune: 7022
levels:
  - {"row": 21, "level": 0, "item": 7022, "next": 7023, "materials": [{"item": 700, "count": 10}, {"item": 611, "count": 10}]}
  - {"row": 22, "level": 1, "item": 7023, "next": 7024, "materials": [{"item": 700, "count": 15}, {"item": 611, "count": 15}]}
  - {"row": 23, "level": 2, "item": 7024, "next": 7025, "materials": [{"item": 700, "count": 20}, {"item": 611, "count": 20}]}
  - {"row": 24, "level": 3, "item": 7025, "next": 7026, "materials": [{"item": 700, "count": 30}, {"item": 611, "count": 30}]}
  - {"row": 25, "level": 4, "item": 7026, "next": 7027, "materials": [{"item": 700, "count": 60}, {"item": 611, "count": 40}, {"item": 854, "count": 1}]}
  - {"row": 26, "level": 5, "item": 7027, "next": 7028, "materials": [{"item": 700, "count": 80}, {"item": 611, "count": 50}, {"item": 854, "count": 1}]}
  - {"row": 27, "level": 6, "item": 7028, "next": 7029, "materials": [{"item": 700, "count": 100}, {"item": 611, "count": 60}, {"item": 854, "count": 1}]}
  - {"row": 28, "level": 7, "item": 7029, "next": 7030, "materials": [{"item": 701, "count": 10}, {"item": 612, "count": 10}, {"item": 854, "count": 1}]}
  - {"row": 29, "level": 8, "item": 7030, "next": 7031, "materials": [{"item": 701, "count": 20}, {"item": 612, "count": 15}, {"item": 854, "count": 1}]}
  - {"row": 30, "level": 9, "item": 7031, "next": 0, "materials": [{"item": 701, "count": 30}, {"item": 612, "count": 20}, {"item": 854, "count": 1}]}
kind: "rune_upgrade"
---
<!-- generated:start -->
<!-- generated-keys: title=4a7d97 type=4389c5 id=9f6bf8 sources=8e67f6 group=77de68 rune=fca763 levels=41bae9 kind=6a6d0e -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/7022.png) |
| **Rune line** | `JewelSocketMake` group 3 |
| **Starts at** | [[wiki/items/7022-armor-rune\|Armor Rune]] |
| **Success rates** | unknown (server side; patch notes give only trends) |

### Levels

Each row upgrades the rune to the next item (C->S `0x4a8`). The +9 row has no next item, so its cost is never used. The costs match the 20 Sep 2018 patch table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1).

| level |  | rune | becomes | materials | row |
|---|---|---|---|---|---|
| +0 | ![](wiki/assets/items/7022.png) | [[wiki/items/7022-armor-rune\|Armor Rune]] | [[wiki/items/7023-armor-rune\|Armor Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 10 | 21 |
| +1 | ![](wiki/assets/items/7023.png) | [[wiki/items/7023-armor-rune\|Armor Rune]] | [[wiki/items/7024-armor-rune\|Armor Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 15, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 15 | 22 |
| +2 | ![](wiki/assets/items/7024.png) | [[wiki/items/7024-armor-rune\|Armor Rune]] | [[wiki/items/7025-armor-rune\|Armor Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 20, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 20 | 23 |
| +3 | ![](wiki/assets/items/7025.png) | [[wiki/items/7025-armor-rune\|Armor Rune]] | [[wiki/items/7026-armor-rune\|Armor Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 30, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 30 | 24 |
| +4 | ![](wiki/assets/items/7026.png) | [[wiki/items/7026-armor-rune\|Armor Rune]] | [[wiki/items/7027-armor-rune\|Armor Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 60, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 40, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 25 |
| +5 | ![](wiki/assets/items/7027.png) | [[wiki/items/7027-armor-rune\|Armor Rune]] | [[wiki/items/7028-armor-rune\|Armor Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 80, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 50, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 26 |
| +6 | ![](wiki/assets/items/7028.png) | [[wiki/items/7028-armor-rune\|Armor Rune]] | [[wiki/items/7029-armor-rune\|Armor Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 100, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 60, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 27 |
| +7 | ![](wiki/assets/items/7029.png) | [[wiki/items/7029-armor-rune\|Armor Rune]] | [[wiki/items/7030-armor-rune\|Armor Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 10, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 28 |
| +8 | ![](wiki/assets/items/7030.png) | [[wiki/items/7030-armor-rune\|Armor Rune]] | [[wiki/items/7031-armor-rune\|Armor Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 20, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 15, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 29 |
| +9 | ![](wiki/assets/items/7031.png) | [[wiki/items/7031-armor-rune\|Armor Rune]] | – (max) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 30, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 20, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 30 |

### Rules from the patch notes

- Cap +5 at launch, +9 from WM 0726; success falls with level, earlier for rarer runes (WM 0406); raised overall in WM 0920. A failure usually loses one level.
- Source: [[gameplay/reinforce-and-runes|Reinforce and runes]] §3.
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
