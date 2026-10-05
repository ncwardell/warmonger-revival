---
title: "Critical Strike (%) Rune upgrades"
type: "upgrade"
id: 1021
status: "partial"
missing: ["success_rates"]
sources: ["client: JewelSocketMake.cdb group 21 (rows 201–210)", "docs: [[gameplay/reinforce-and-runes]] §1 (WM 0920 rune cost table matches JewelSocketMake +0→+9)", "contract: items.yaml rune_upgrade 0x4a8, server_rules craft_reinforce_rune_odds", "video: [[gameplay/video-rune-upgrades]] §1 (83 attempts, all 41 failures dropped exactly one level, materials and gold spent on every try; Jul 2018) + guide: [[gameplay/reinforce-and-runes]] §3 (blog runas)", "notes: [[gameplay/reinforce-and-runes]] §3 (cap +5 at launch WM 0613, +9 from WM 0726)"]
group: 21
rune: 7202
levels:
  - {"row": 201, "level": 0, "item": 7202, "next": 7203, "materials": [{"item": 701, "count": 10}, {"item": 613, "count": 10}, {"item": 855, "count": 1}]}
  - {"row": 202, "level": 1, "item": 7203, "next": 7204, "materials": [{"item": 701, "count": 20}, {"item": 613, "count": 15}, {"item": 855, "count": 1}]}
  - {"row": 203, "level": 2, "item": 7204, "next": 7205, "materials": [{"item": 701, "count": 40}, {"item": 613, "count": 20}, {"item": 855, "count": 1}]}
  - {"row": 204, "level": 3, "item": 7205, "next": 7206, "materials": [{"item": 701, "count": 60}, {"item": 613, "count": 30}, {"item": 855, "count": 1}]}
  - {"row": 205, "level": 4, "item": 7206, "next": 7207, "materials": [{"item": 701, "count": 80}, {"item": 613, "count": 40}, {"item": 855, "count": 1}]}
  - {"row": 206, "level": 5, "item": 7207, "next": 7208, "materials": [{"item": 702, "count": 10}, {"item": 614, "count": 10}, {"item": 856, "count": 1}]}
  - {"row": 207, "level": 6, "item": 7208, "next": 7209, "materials": [{"item": 702, "count": 20}, {"item": 614, "count": 15}, {"item": 856, "count": 1}]}
  - {"row": 208, "level": 7, "item": 7209, "next": 7210, "materials": [{"item": 702, "count": 40}, {"item": 614, "count": 20}, {"item": 856, "count": 1}]}
  - {"row": 209, "level": 8, "item": 7210, "next": 7211, "materials": [{"item": 702, "count": 60}, {"item": 614, "count": 30}, {"item": 856, "count": 1}]}
  - {"row": 210, "level": 9, "item": 7211, "next": 0, "materials": [{"item": 702, "count": 80}, {"item": 614, "count": 40}, {"item": 856, "count": 1}]}
kind: "rune_upgrade"
on_failure: "drop_one_level"
max_level: 9
---
<!-- generated:start -->
<!-- generated-keys: title=d44b68 type=4389c5 id=00e263 sources=845390 group=472b07 rune=ecb216 levels=7c3f02 kind=6a6d0e -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/7202.png) |
| **Rune line** | `JewelSocketMake` group 21 |
| **Starts at** | [[wiki/items/7202-critical-strike-rune\|Critical Strike (%) Rune]] |
| **Success rates** | unknown (server side; patch notes give only trends) |

### Levels

Each row upgrades the rune to the next item (C->S `0x4a8`). The +9 row has no next item, so its cost is never used. The costs match the 20 Sep 2018 patch table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1).

| level |  | rune | becomes | materials | row |
|---|---|---|---|---|---|
| +0 | ![](wiki/assets/items/7202.png) | [[wiki/items/7202-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/7203-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 10, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 201 |
| +1 | ![](wiki/assets/items/7203.png) | [[wiki/items/7203-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/7204-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 20, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 15, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 202 |
| +2 | ![](wiki/assets/items/7204.png) | [[wiki/items/7204-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/7205-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 40, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 20, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 203 |
| +3 | ![](wiki/assets/items/7205.png) | [[wiki/items/7205-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/7206-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 60, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 30, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 204 |
| +4 | ![](wiki/assets/items/7206.png) | [[wiki/items/7206-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/7207-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 80, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 40, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 205 |
| +5 | ![](wiki/assets/items/7207.png) | [[wiki/items/7207-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/7208-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 10, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 10, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 206 |
| +6 | ![](wiki/assets/items/7208.png) | [[wiki/items/7208-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/7209-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 20, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 15, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 207 |
| +7 | ![](wiki/assets/items/7209.png) | [[wiki/items/7209-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/7210-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 40, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 20, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 208 |
| +8 | ![](wiki/assets/items/7210.png) | [[wiki/items/7210-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/7211-critical-strike-rune\|Critical Strike (%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 60, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 30, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 209 |
| +9 | ![](wiki/assets/items/7211.png) | [[wiki/items/7211-critical-strike-rune\|Critical Strike (%) Rune]] | – (max) | [[wiki/items/702-crystal-red\|Crystal : Red]] × 80, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 40, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 210 |

### Rules from the patch notes

- Cap +5 at launch, +9 from WM 0726; success falls with level, earlier for rarer runes (WM 0406); raised overall in WM 0920. A failure usually loses one level.
- Source: [[gameplay/reinforce-and-runes|Reinforce and runes]] §3.
<!-- generated:end -->

## Notes

Tier 2 rune line (level-0 cost in Yellow) ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1, *client*). The 20 Sep 2018 cost table matches this line's materials; before that, upgrades cost crystals only ([[gameplay/reinforce-and-runes|Reinforce and runes]] §2, WM 0420 images).

## Behaviour

On a failed upgrade the rune drops **one level**; gold and materials are spent on every try ([[gameplay/video-rune-upgrades|Rune upgrade video]] §1, 41 of 41 failures, *video*; the blog says the same, [[gameplay/reinforce-and-runes|Reinforce and runes]] §3). The window still shows a "destruction of rune in case of failure" warning beside an optional sub-material slot.

Cap: +5 at launch (WM 0613), about +7 on 12 Jul 2018 (*video*), **+9** from WM 0726 ([[gameplay/reinforce-and-runes|Reinforce and runes]] §3, [[gameplay/video-rune-upgrades|Rune upgrade video]] §1).

Success rates were never published. Patch notes give only trends: until WM 0404 tier-1 runes could not fail at all (bug), then got a "really small" fail chance at +8 and +9; WM 0406 made success fall slowly with level, starting earlier for rarer runes (rarity 2, from level 5–6; rarity = tier is a *guess*); WM 0920 raised rune success overall ([[gameplay/reinforce-and-runes|Reinforce and runes]] §3, *notes*).

From WM 1107 runes are affected by the PvP stat correction ([[gameplay/reinforce-and-runes|Reinforce and runes]] §3, *notes*).

## Sources

- video: [[gameplay/video-rune-upgrades]] §1 (83 attempts, all 41 failures dropped exactly one level, materials and gold spent on every try; Jul 2018) + guide: [[gameplay/reinforce-and-runes]] §3 (blog runas)
- notes: [[gameplay/reinforce-and-runes]] §3 (cap +5 at launch WM 0613, +9 from WM 0726)

## Open questions

Destruction or one-level drop? The UI warns of destruction without a sub-material, but every recorded failure only dropped one level ([[gameplay/video-rune-upgrades|Rune upgrade video]] §1, [[gameplay/reinforce-and-runes|Reinforce and runes]] §3).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
