---
title: "Critical Strike Deal Rune upgrades"
type: "upgrade"
id: 1020
status: "partial"
missing: ["success_rates"]
sources: ["client: JewelSocketMake.cdb group 20 (rows 191–200)", "docs: [[gameplay/reinforce-and-runes]] §1 (WM 0920 rune cost table matches JewelSocketMake +0→+9)", "contract: items.yaml rune_upgrade 0x4a8, server_rules craft_reinforce_rune_odds", "video: [[gameplay/video-rune-upgrades]] §1 (83 attempts, all 41 failures dropped exactly one level, materials and gold spent on every try; Jul 2018) + guide: [[gameplay/reinforce-and-runes]] §3 (blog runas)", "notes: [[gameplay/reinforce-and-runes]] §3 (cap +5 at launch WM 0613, +9 from WM 0726)"]
group: 20
rune: 7192
levels:
  - {"row": 191, "level": 0, "item": 7192, "next": 7193, "materials": [{"item": 702, "count": 10}, {"item": 615, "count": 15}, {"item": 856, "count": 1}]}
  - {"row": 192, "level": 1, "item": 7193, "next": 7194, "materials": [{"item": 702, "count": 20}, {"item": 615, "count": 20}, {"item": 856, "count": 1}]}
  - {"row": 193, "level": 2, "item": 7194, "next": 7195, "materials": [{"item": 702, "count": 40}, {"item": 615, "count": 30}, {"item": 856, "count": 1}]}
  - {"row": 194, "level": 3, "item": 7195, "next": 7196, "materials": [{"item": 702, "count": 60}, {"item": 615, "count": 40}, {"item": 856, "count": 1}]}
  - {"row": 195, "level": 4, "item": 7196, "next": 7197, "materials": [{"item": 703, "count": 10}, {"item": 616, "count": 10}, {"item": 857, "count": 1}]}
  - {"row": 196, "level": 5, "item": 7197, "next": 7198, "materials": [{"item": 703, "count": 20}, {"item": 616, "count": 15}, {"item": 857, "count": 1}]}
  - {"row": 197, "level": 6, "item": 7198, "next": 7199, "materials": [{"item": 703, "count": 40}, {"item": 616, "count": 20}, {"item": 857, "count": 1}]}
  - {"row": 198, "level": 7, "item": 7199, "next": 7200, "materials": [{"item": 703, "count": 60}, {"item": 616, "count": 30}, {"item": 857, "count": 1}]}
  - {"row": 199, "level": 8, "item": 7200, "next": 7201, "materials": [{"item": 703, "count": 80}, {"item": 616, "count": 40}, {"item": 857, "count": 1}]}
  - {"row": 200, "level": 9, "item": 7201, "next": 0, "materials": [{"item": 703, "count": 120}, {"item": 616, "count": 60}, {"item": 857, "count": 1}]}
kind: "rune_upgrade"
on_failure: "drop_one_level"
max_level: 9
---
<!-- generated:start -->
<!-- generated-keys: title=85cdbe type=4389c5 id=6d1270 sources=a5ead2 group=91032a rune=8e5b51 levels=a02b92 kind=6a6d0e -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/7192.png) |
| **Rune line** | `JewelSocketMake` group 20 |
| **Starts at** | [[wiki/items/7192-critical-strike-deal-rune\|Critical Strike Deal Rune]] |
| **Success rates** | unknown (server side; patch notes give only trends) |

### Levels

Each row upgrades the rune to the next item (C->S `0x4a8`). The +9 row has no next item, so its cost is never used. The costs match the 20 Sep 2018 patch table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1).

| level |  | rune | becomes | materials | row |
|---|---|---|---|---|---|
| +0 | ![](wiki/assets/items/7192.png) | [[wiki/items/7192-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/7193-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 10, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 15, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 191 |
| +1 | ![](wiki/assets/items/7193.png) | [[wiki/items/7193-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/7194-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 20, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 20, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 192 |
| +2 | ![](wiki/assets/items/7194.png) | [[wiki/items/7194-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/7195-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 40, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 30, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 193 |
| +3 | ![](wiki/assets/items/7195.png) | [[wiki/items/7195-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/7196-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 60, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 40, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 194 |
| +4 | ![](wiki/assets/items/7196.png) | [[wiki/items/7196-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/7197-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 10, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 10, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 195 |
| +5 | ![](wiki/assets/items/7197.png) | [[wiki/items/7197-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/7198-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 20, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 15, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 196 |
| +6 | ![](wiki/assets/items/7198.png) | [[wiki/items/7198-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/7199-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 40, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 20, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 197 |
| +7 | ![](wiki/assets/items/7199.png) | [[wiki/items/7199-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/7200-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 60, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 30, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 198 |
| +8 | ![](wiki/assets/items/7200.png) | [[wiki/items/7200-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/7201-critical-strike-deal-rune\|Critical Strike Deal Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 80, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 40, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 199 |
| +9 | ![](wiki/assets/items/7201.png) | [[wiki/items/7201-critical-strike-deal-rune\|Critical Strike Deal Rune]] | – (max) | [[wiki/items/703-crystal-black\|Crystal : Black]] × 120, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 60, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 200 |

### Rules from the patch notes

- Cap +5 at launch, +9 from WM 0726; success falls with level, earlier for rarer runes (WM 0406); raised overall in WM 0920. A failure usually loses one level.
- Source: [[gameplay/reinforce-and-runes|Reinforce and runes]] §3.
<!-- generated:end -->

## Notes

Tier 3 rune line (level-0 cost in Red) ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1, *client*). The 20 Sep 2018 cost table matches this line's materials; before that, upgrades cost crystals only ([[gameplay/reinforce-and-runes|Reinforce and runes]] §2, WM 0420 images).

## Behaviour

On a failed upgrade the rune drops **one level**; gold and materials are spent on every try ([[gameplay/video-rune-upgrades|Rune upgrade video]] §1, 41 of 41 failures, *video*; the blog says the same, [[gameplay/reinforce-and-runes|Reinforce and runes]] §3). The window still shows a "destruction of rune in case of failure" warning beside an optional sub-material slot.

Cap: +5 at launch (WM 0613), about +7 on 12 Jul 2018 (*video*), **+9** from WM 0726 ([[gameplay/reinforce-and-runes|Reinforce and runes]] §3, [[gameplay/video-rune-upgrades|Rune upgrade video]] §1).

Success rates were never published. Patch notes give only trends: until WM 0404 tier-1 runes could not fail at all (bug), then got a "really small" fail chance at +8 and +9; WM 0406 made success fall slowly with level, starting earlier for rarer runes (rarity 3, from level 4–5; rarity = tier is a *guess*); WM 0920 raised rune success overall ([[gameplay/reinforce-and-runes|Reinforce and runes]] §3, *notes*).

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
