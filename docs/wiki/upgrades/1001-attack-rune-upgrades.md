---
title: "Attack Rune upgrades"
type: "upgrade"
id: 1001
status: "partial"
missing: ["success_rates"]
sources: ["client: JewelSocketMake.cdb group 1 (rows 1–10)", "docs: [[gameplay/reinforce-and-runes]] §1 (WM 0920 rune cost table matches JewelSocketMake +0→+9)", "contract: items.yaml rune_upgrade 0x4a8, server_rules craft_reinforce_rune_odds", "video: [[gameplay/video-rune-upgrades]] §1 (83 attempts, all 41 failures dropped exactly one level, materials and gold spent on every try; Jul 2018) + guide: [[gameplay/reinforce-and-runes]] §3 (blog runas)", "notes: [[gameplay/reinforce-and-runes]] §3 (cap +5 at launch WM 0613, +9 from WM 0726)", "video: [[gameplay/video-rune-upgrades]] §2 (gold per attempt = 1,000 × level after the upgrade, tier-1 Attack rune, steps +2→+3 … +6→+7)", "video: [[gameplay/video-rune-upgrades]] §1 (observed success per step, Attack rune, 12 Jul 2018, before the WM 0920 rate rise; small sample)"]
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
on_failure: "drop_one_level"
max_level: 9
gold_rule: {"per_level_after_upgrade": 1000}
success_rates_observed:
  - {"from": 2, "to": 3, "tries": 1, "success": 1}
  - {"from": 3, "to": 4, "tries": 9, "success": 8, "rate": 89}
  - {"from": 4, "to": 5, "tries": 28, "success": 20, "rate": 71}
  - {"from": 5, "to": 6, "tries": 32, "success": 12, "rate": 38}
  - {"from": 6, "to": 7, "tries": 13, "success": 1, "rate": 8}
---
<!-- generated:start -->
<!-- generated-keys: title=b578d0 type=4389c5 id=dd0190 sources=841fe7 group=356a19 rune=76096e levels=72849f kind=6a6d0e -->
|  |  |
|---|---|
|  | ![](../assets/items/7002.png) |
| **Rune line** | `JewelSocketMake` group 1 |
| **Starts at** | [[wiki/items/7002-attack-rune\|Attack Rune]] |
| **Success rates** | unknown (server side; patch notes give only trends) |

### Levels

Each row upgrades the rune to the next item (C->S `0x4a8`). The +9 row has no next item, so its cost is never used. The costs match the 20 Sep 2018 patch table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1).

| level |  | rune | becomes | materials | row |
|---|---|---|---|---|---|
| +0 | ![](../assets/items/7002.png) | [[wiki/items/7002-attack-rune\|Attack Rune]] | [[wiki/items/7003-attack-rune\|Attack Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 10 | 1 |
| +1 | ![](../assets/items/7003.png) | [[wiki/items/7003-attack-rune\|Attack Rune]] | [[wiki/items/7004-attack-rune\|Attack Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 15, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 15 | 2 |
| +2 | ![](../assets/items/7004.png) | [[wiki/items/7004-attack-rune\|Attack Rune]] | [[wiki/items/7005-attack-rune\|Attack Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 20, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 20 | 3 |
| +3 | ![](../assets/items/7005.png) | [[wiki/items/7005-attack-rune\|Attack Rune]] | [[wiki/items/7006-attack-rune\|Attack Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 30, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 30 | 4 |
| +4 | ![](../assets/items/7006.png) | [[wiki/items/7006-attack-rune\|Attack Rune]] | [[wiki/items/7007-attack-rune\|Attack Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 60, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 40, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 5 |
| +5 | ![](../assets/items/7007.png) | [[wiki/items/7007-attack-rune\|Attack Rune]] | [[wiki/items/7008-attack-rune\|Attack Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 80, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 50, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 6 |
| +6 | ![](../assets/items/7008.png) | [[wiki/items/7008-attack-rune\|Attack Rune]] | [[wiki/items/7009-attack-rune\|Attack Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 100, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 60, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 7 |
| +7 | ![](../assets/items/7009.png) | [[wiki/items/7009-attack-rune\|Attack Rune]] | [[wiki/items/7010-attack-rune\|Attack Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 10, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 8 |
| +8 | ![](../assets/items/7010.png) | [[wiki/items/7010-attack-rune\|Attack Rune]] | [[wiki/items/7011-attack-rune\|Attack Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 20, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 15, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 9 |
| +9 | ![](../assets/items/7011.png) | [[wiki/items/7011-attack-rune\|Attack Rune]] | – (max) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 30, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 20, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 10 |

### Rules from the patch notes

- Cap +5 at launch, +9 from WM 0726; success falls with level, earlier for rarer runes (WM 0406); raised overall in WM 0920. A failure usually loses one level.
- Source: [[gameplay/reinforce-and-runes|Reinforce and runes]] §3.
<!-- generated:end -->

## Notes

Tier 1 rune line (level-0 cost in Blue) ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1, *client*). The 20 Sep 2018 cost table matches this line's materials; before that, upgrades cost crystals only ([[gameplay/reinforce-and-runes|Reinforce and runes]] §2, WM 0420 images).

Patch-note stat values: Attack **45** at +9 (WM 0412); the client's `Item_Jewel` has 120. Use the client table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §3).

ZonderCoRe's July 2018 video counts 83 attempts on one Attack rune: +3→+4 8/9 (89 %), +4→+5 20/28 (71 %), +5→+6 12/32 (38 %), +6→+7 1/13 (8 %), sub-material slot empty ([[gameplay/video-rune-upgrades|Rune upgrade video]] §1, *video*). Kept in `success_rates_observed`, not `success_rates`: it covers only five steps, predates the WM 0920 rate rise and the sample is small.

July 2018 cost per attempt in that video (+2→+3 … +6→+7): 3,000–7,000 gold, Blue Crystal 40/60/80/100/120 (the WM 0420 "after" column, not the client) and Red Passion 20–60 (= client), with no Shining Passion yet ([[gameplay/video-rune-upgrades|Rune upgrade video]] §2, *video*). Attack per level in the video: +2 9, +3 13, +4 17, +5 22, +6 27, +7 33; `Item_Jewel` is steeper (+9 = 120) ([[gameplay/video-rune-upgrades|Rune upgrade video]] §3).

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
- video: [[gameplay/video-rune-upgrades]] §1 (observed success per step, Attack rune, 12 Jul 2018, before the WM 0920 rate rise; small sample)

## Open questions

Fill `success_rates` for every step; the video gives only +2→+7 for one tier-1 rune before WM 0920 ([[gameplay/video-rune-upgrades|Rune upgrade video]] §4 suggests starting from these and raising them, *guess*).

Destruction or one-level drop? The UI warns of destruction without a sub-material, but every recorded failure only dropped one level ([[gameplay/video-rune-upgrades|Rune upgrade video]] §1, [[gameplay/reinforce-and-runes|Reinforce and runes]] §3).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
