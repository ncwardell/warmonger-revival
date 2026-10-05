---
title: "Attack Rune upgrades"
type: "upgrade"
id: 1001
status: "stub"
missing: ["success_rates"]
sources: ["client: JewelSocketMake.cdb group 1 (rows 1–10)", "docs: [[gameplay/reinforce-and-runes]] §1 (WM 0920 rune cost table matches JewelSocketMake +0→+9)", "contract: items.yaml rune_upgrade 0x4a8, server_rules craft_reinforce_rune_odds"]
group: 1
rune: 7002
levels:
  - {"row": 1, "level": 0, "item": 7002, "next": 7003, "materials": [{"item": 700, "count": 10}, {"item": 611, "count": 10}]}
  - {"row": 2, "level": 1, "item": 7003, "next": 7004, "materials": [{"item": 700, "count": 15}, {"item": 611, "count": 15}]}
  - {"row": 3, "level": 2, "item": 7004, "next": 7005, "materials": [{"item": 700, "count": 20}, {"item": 611, "count": 20}]}
  - {"row": 4, "level": 3, "item": 7005, "next": 7006, "materials": [{"item": 700, "count": 30}, {"item": 611, "count": 30}]}
  - {"row": 5, "level": 4, "item": 7006, "next": 7007, "materials": [{"item": 700, "count": 60}, {"item": 611, "count": 40}, {"item": 854, "count": 1}]}
  - {"row": 6, "level": 5, "item": 7007, "next": 7008, "materials": [{"item": 700, "count": 80}, {"item": 611, "count": 50}, {"item": 854, "count": 1}]}
  - {"row": 7, "level": 6, "item": 7008, "next": 7009, "materials": [{"item": 700, "count": 100}, {"item": 611, "count": 60}, {"item": 854, "count": 1}]}
  - {"row": 8, "level": 7, "item": 7009, "next": 7010, "materials": [{"item": 701, "count": 10}, {"item": 612, "count": 10}, {"item": 854, "count": 1}]}
  - {"row": 9, "level": 8, "item": 7010, "next": 7011, "materials": [{"item": 701, "count": 20}, {"item": 612, "count": 15}, {"item": 854, "count": 1}]}
  - {"row": 10, "level": 9, "item": 7011, "next": 0, "materials": [{"item": 701, "count": 30}, {"item": 612, "count": 20}, {"item": 854, "count": 1}]}
kind: "rune_upgrade"
---
<!-- generated:start -->
<!-- generated-keys: title=b578d0 type=4389c5 id=dd0190 sources=841fe7 group=356a19 rune=76096e levels=72849f kind=6a6d0e -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/7002.png) |
| **Rune line** | `JewelSocketMake` group 1 |
| **Starts at** | [[wiki/items/7002-attack-rune\|Attack Rune]] |
| **Success rates** | unknown (server side; patch notes give only trends) |

### Levels

Each row upgrades the rune to the next item (C->S `0x4a8`). The +9 row has no next item, so its cost is never used. The costs match the 20 Sep 2018 patch table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1).

| level |  | rune | becomes | materials | row |
|---|---|---|---|---|---|
| +0 | ![](wiki/assets/items/7002.png) | [[wiki/items/7002-attack-rune\|Attack Rune]] | [[wiki/items/7003-attack-rune\|Attack Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 10 | 1 |
| +1 | ![](wiki/assets/items/7003.png) | [[wiki/items/7003-attack-rune\|Attack Rune]] | [[wiki/items/7004-attack-rune\|Attack Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 15, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 15 | 2 |
| +2 | ![](wiki/assets/items/7004.png) | [[wiki/items/7004-attack-rune\|Attack Rune]] | [[wiki/items/7005-attack-rune\|Attack Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 20, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 20 | 3 |
| +3 | ![](wiki/assets/items/7005.png) | [[wiki/items/7005-attack-rune\|Attack Rune]] | [[wiki/items/7006-attack-rune\|Attack Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 30, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 30 | 4 |
| +4 | ![](wiki/assets/items/7006.png) | [[wiki/items/7006-attack-rune\|Attack Rune]] | [[wiki/items/7007-attack-rune\|Attack Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 60, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 40, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 5 |
| +5 | ![](wiki/assets/items/7007.png) | [[wiki/items/7007-attack-rune\|Attack Rune]] | [[wiki/items/7008-attack-rune\|Attack Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 80, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 50, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 6 |
| +6 | ![](wiki/assets/items/7008.png) | [[wiki/items/7008-attack-rune\|Attack Rune]] | [[wiki/items/7009-attack-rune\|Attack Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 100, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 60, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 7 |
| +7 | ![](wiki/assets/items/7009.png) | [[wiki/items/7009-attack-rune\|Attack Rune]] | [[wiki/items/7010-attack-rune\|Attack Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 10, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 8 |
| +8 | ![](wiki/assets/items/7010.png) | [[wiki/items/7010-attack-rune\|Attack Rune]] | [[wiki/items/7011-attack-rune\|Attack Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 20, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 15, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 9 |
| +9 | ![](wiki/assets/items/7011.png) | [[wiki/items/7011-attack-rune\|Attack Rune]] | – (max) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 30, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 20, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 10 |

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
