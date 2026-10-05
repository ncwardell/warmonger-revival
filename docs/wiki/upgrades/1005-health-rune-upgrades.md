---
title: "Health Rune upgrades"
type: "upgrade"
id: 1005
status: "partial"
missing: ["success_rates"]
sources: ["client: JewelSocketMake.cdb group 5 (rows 41–50)", "docs: [[gameplay/reinforce-and-runes]] §1 (WM 0920 rune cost table matches JewelSocketMake +0→+9)", "contract: items.yaml rune_upgrade 0x4a8, server_rules craft_reinforce_rune_odds", "video: [[gameplay/video-rune-upgrades]] §1 (83 attempts, all 41 failures dropped exactly one level, materials and gold spent on every try; Jul 2018) + guide: [[gameplay/reinforce-and-runes]] §3 (blog runas)", "notes: [[gameplay/reinforce-and-runes]] §3 (cap +5 at launch WM 0613, +9 from WM 0726)", "video: [[gameplay/video-rune-upgrades]] §2 (gold per attempt = 1,000 × level after the upgrade, tier-1 Attack rune, steps +2→+3 … +6→+7)"]
group: 5
rune: 7042
levels:
  - {"row": 41, "level": 0, "item": 7042, "next": 7043, "materials": [{"item": 700, "count": 10}, {"item": 611, "count": 10}]}
  - {"row": 42, "level": 1, "item": 7043, "next": 7044, "materials": [{"item": 700, "count": 15}, {"item": 611, "count": 15}]}
  - {"row": 43, "level": 2, "item": 7044, "next": 7045, "materials": [{"item": 700, "count": 20}, {"item": 611, "count": 20}]}
  - {"row": 44, "level": 3, "item": 7045, "next": 7046, "materials": [{"item": 700, "count": 30}, {"item": 611, "count": 30}]}
  - {"row": 45, "level": 4, "item": 7046, "next": 7047, "materials": [{"item": 700, "count": 60}, {"item": 611, "count": 40}, {"item": 854, "count": 1}]}
  - {"row": 46, "level": 5, "item": 7047, "next": 7048, "materials": [{"item": 700, "count": 80}, {"item": 611, "count": 50}, {"item": 854, "count": 1}]}
  - {"row": 47, "level": 6, "item": 7048, "next": 7049, "materials": [{"item": 700, "count": 100}, {"item": 611, "count": 60}, {"item": 854, "count": 1}]}
  - {"row": 48, "level": 7, "item": 7049, "next": 7050, "materials": [{"item": 701, "count": 10}, {"item": 612, "count": 10}, {"item": 854, "count": 1}]}
  - {"row": 49, "level": 8, "item": 7050, "next": 7051, "materials": [{"item": 701, "count": 20}, {"item": 612, "count": 15}, {"item": 854, "count": 1}]}
  - {"row": 50, "level": 9, "item": 7051, "next": 0, "materials": [{"item": 701, "count": 30}, {"item": 612, "count": 20}, {"item": 854, "count": 1}]}
kind: "rune_upgrade"
on_failure: "drop_one_level"
max_level: 9
gold_rule: {"per_level_after_upgrade": 1000}
---
<!-- generated:start -->
<!-- generated-keys: title=b3f0df type=4389c5 id=0477d7 sources=e390fa group=ac3478 rune=b1e381 levels=60f824 kind=6a6d0e -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/7042.png) |
| **Rune line** | `JewelSocketMake` group 5 |
| **Starts at** | [[wiki/items/7042-health-rune\|Health Rune]] |
| **Success rates** | unknown (server side; patch notes give only trends) |

### Levels

Each row upgrades the rune to the next item (C->S `0x4a8`). The +9 row has no next item, so its cost is never used. The costs match the 20 Sep 2018 patch table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1).

| level |  | rune | becomes | materials | row |
|---|---|---|---|---|---|
| +0 | ![](wiki/assets/items/7042.png) | [[wiki/items/7042-health-rune\|Health Rune]] | [[wiki/items/7043-health-rune\|Health Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 10 | 41 |
| +1 | ![](wiki/assets/items/7043.png) | [[wiki/items/7043-health-rune\|Health Rune]] | [[wiki/items/7044-health-rune\|Health Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 15, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 15 | 42 |
| +2 | ![](wiki/assets/items/7044.png) | [[wiki/items/7044-health-rune\|Health Rune]] | [[wiki/items/7045-health-rune\|Health Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 20, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 20 | 43 |
| +3 | ![](wiki/assets/items/7045.png) | [[wiki/items/7045-health-rune\|Health Rune]] | [[wiki/items/7046-health-rune\|Health Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 30, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 30 | 44 |
| +4 | ![](wiki/assets/items/7046.png) | [[wiki/items/7046-health-rune\|Health Rune]] | [[wiki/items/7047-health-rune\|Health Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 60, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 40, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 45 |
| +5 | ![](wiki/assets/items/7047.png) | [[wiki/items/7047-health-rune\|Health Rune]] | [[wiki/items/7048-health-rune\|Health Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 80, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 50, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 46 |
| +6 | ![](wiki/assets/items/7048.png) | [[wiki/items/7048-health-rune\|Health Rune]] | [[wiki/items/7049-health-rune\|Health Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 100, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 60, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 47 |
| +7 | ![](wiki/assets/items/7049.png) | [[wiki/items/7049-health-rune\|Health Rune]] | [[wiki/items/7050-health-rune\|Health Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 10, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 48 |
| +8 | ![](wiki/assets/items/7050.png) | [[wiki/items/7050-health-rune\|Health Rune]] | [[wiki/items/7051-health-rune\|Health Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 20, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 15, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 49 |
| +9 | ![](wiki/assets/items/7051.png) | [[wiki/items/7051-health-rune\|Health Rune]] | – (max) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 30, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 20, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 50 |

### Rules from the patch notes

- Cap +5 at launch, +9 from WM 0726; success falls with level, earlier for rarer runes (WM 0406); raised overall in WM 0920. A failure usually loses one level.
- Source: [[gameplay/reinforce-and-runes|Reinforce and runes]] §3.
<!-- generated:end -->

## Notes

Tier 1 rune line (level-0 cost in Blue) ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1, *client*). The 20 Sep 2018 cost table matches this line's materials; before that, upgrades cost crystals only ([[gameplay/reinforce-and-runes|Reinforce and runes]] §2, WM 0420 images).

## Behaviour

On a failed upgrade the rune drops **one level**; gold and materials are spent on every try ([[gameplay/video-rune-upgrades|Rune upgrade video]] §1, 41 of 41 failures, *video*; the blog says the same, [[gameplay/reinforce-and-runes|Reinforce and runes]] §3). The window still shows a "destruction of rune in case of failure" warning beside an optional sub-material slot.

Gold per attempt = **1,000 × the level after the upgrade** (+4→+5 costs 5,000). `JewelSocketMake` has no gold column, so this rule comes only from the video ([[gameplay/video-rune-upgrades|Rune upgrade video]] §2, *video*).

Cap: +5 at launch (WM 0613), about +7 on 12 Jul 2018 (*video*), **+9** from WM 0726 ([[gameplay/reinforce-and-runes|Reinforce and runes]] §3, [[gameplay/video-rune-upgrades|Rune upgrade video]] §1).

Success rates were never published. Patch notes give only trends: until WM 0404 tier-1 runes could not fail at all (bug), then got a "really small" fail chance at +8 and +9; WM 0406 made success fall slowly with level, starting earlier for rarer runes (rarity 1, from level 6–7; rarity = tier is a *guess*); WM 0920 raised rune success overall ([[gameplay/reinforce-and-runes|Reinforce and runes]] §3, *notes*).

From WM 1107 runes are affected by the PvP stat correction ([[gameplay/reinforce-and-runes|Reinforce and runes]] §3, *notes*).

## Sources

- video: [[gameplay/video-rune-upgrades]] §1 (83 attempts, all 41 failures dropped exactly one level, materials and gold spent on every try; Jul 2018) + guide: [[gameplay/reinforce-and-runes]] §3 (blog runas)
- notes: [[gameplay/reinforce-and-runes]] §3 (cap +5 at launch WM 0613, +9 from WM 0726)
- video: [[gameplay/video-rune-upgrades]] §2 (gold per attempt = 1,000 × level after the upgrade, tier-1 Attack rune, steps +2→+3 … +6→+7)

## Open questions

Destruction or one-level drop? The UI warns of destruction without a sub-material, but every recorded failure only dropped one level ([[gameplay/video-rune-upgrades|Rune upgrade video]] §1, [[gameplay/reinforce-and-runes|Reinforce and runes]] §3).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
