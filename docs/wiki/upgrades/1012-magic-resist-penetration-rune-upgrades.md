---
title: "Magic resist Penetration(%) Rune upgrades"
type: "upgrade"
id: 1012
status: "partial"
missing: ["success_rates"]
sources: ["client: JewelSocketMake.cdb group 12 (rows 111–120)", "docs: [[gameplay/reinforce-and-runes]] §1 (WM 0920 rune cost table matches JewelSocketMake +0→+9)", "contract: items.yaml rune_upgrade 0x4a8, server_rules craft_reinforce_rune_odds", "video: [[gameplay/video-rune-upgrades]] §1 (83 attempts, all 41 failures dropped exactly one level, materials and gold spent on every try; Jul 2018) + guide: [[gameplay/reinforce-and-runes]] §3 (blog runas)", "notes: [[gameplay/reinforce-and-runes]] §3 (cap +5 at launch WM 0613, +9 from WM 0726)"]
group: 12
rune: 7112
levels:
  - {"row": 111, "level": 0, "item": 7112, "next": 7113, "materials": [{"item": 702, "count": 10}, {"item": 615, "count": 15}, {"item": 856, "count": 1}]}
  - {"row": 112, "level": 1, "item": 7113, "next": 7114, "materials": [{"item": 702, "count": 20}, {"item": 615, "count": 20}, {"item": 856, "count": 1}]}
  - {"row": 113, "level": 2, "item": 7114, "next": 7115, "materials": [{"item": 702, "count": 40}, {"item": 615, "count": 30}, {"item": 856, "count": 1}]}
  - {"row": 114, "level": 3, "item": 7115, "next": 7116, "materials": [{"item": 702, "count": 60}, {"item": 615, "count": 40}, {"item": 856, "count": 1}]}
  - {"row": 115, "level": 4, "item": 7116, "next": 7117, "materials": [{"item": 703, "count": 10}, {"item": 616, "count": 10}, {"item": 857, "count": 1}]}
  - {"row": 116, "level": 5, "item": 7117, "next": 7118, "materials": [{"item": 703, "count": 20}, {"item": 616, "count": 15}, {"item": 857, "count": 1}]}
  - {"row": 117, "level": 6, "item": 7118, "next": 7119, "materials": [{"item": 703, "count": 40}, {"item": 616, "count": 20}, {"item": 857, "count": 1}]}
  - {"row": 118, "level": 7, "item": 7119, "next": 7120, "materials": [{"item": 703, "count": 60}, {"item": 616, "count": 30}, {"item": 857, "count": 1}]}
  - {"row": 119, "level": 8, "item": 7120, "next": 7121, "materials": [{"item": 703, "count": 80}, {"item": 616, "count": 40}, {"item": 857, "count": 1}]}
  - {"row": 120, "level": 9, "item": 7121, "next": 0, "materials": [{"item": 703, "count": 120}, {"item": 616, "count": 60}, {"item": 857, "count": 1}]}
kind: "rune_upgrade"
on_failure: "drop_one_level"
max_level: 9
---
<!-- generated:start -->
<!-- generated-keys: title=7a660c type=4389c5 id=899a19 sources=c2169b group=7b5200 rune=c7b6db levels=8fb12a kind=6a6d0e -->
|  |  |
|---|---|
|  | ![](../assets/items/7112.png) |
| **Rune line** | `JewelSocketMake` group 12 |
| **Starts at** | [[wiki/items/7112-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] |
| **Success rates** | unknown (server side; patch notes give only trends) |

### Levels

Each row upgrades the rune to the next item (C->S `0x4a8`). The +9 row has no next item, so its cost is never used. The costs match the 20 Sep 2018 patch table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1).

| level |  | rune | becomes | materials | row |
|---|---|---|---|---|---|
| +0 | ![](../assets/items/7112.png) | [[wiki/items/7112-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/7113-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 10, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 15, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 111 |
| +1 | ![](../assets/items/7113.png) | [[wiki/items/7113-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/7114-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 20, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 20, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 112 |
| +2 | ![](../assets/items/7114.png) | [[wiki/items/7114-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/7115-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 40, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 30, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 113 |
| +3 | ![](../assets/items/7115.png) | [[wiki/items/7115-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/7116-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 60, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 40, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 114 |
| +4 | ![](../assets/items/7116.png) | [[wiki/items/7116-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/7117-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 10, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 10, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 115 |
| +5 | ![](../assets/items/7117.png) | [[wiki/items/7117-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/7118-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 20, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 15, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 116 |
| +6 | ![](../assets/items/7118.png) | [[wiki/items/7118-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/7119-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 40, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 20, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 117 |
| +7 | ![](../assets/items/7119.png) | [[wiki/items/7119-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/7120-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 60, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 30, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 118 |
| +8 | ![](../assets/items/7120.png) | [[wiki/items/7120-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/7121-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 80, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 40, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 119 |
| +9 | ![](../assets/items/7121.png) | [[wiki/items/7121-magic-resist-penetration-rune\|Magic resist Penetration(%) Rune]] | – (max) | [[wiki/items/703-crystal-black\|Crystal : Black]] × 120, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 60, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 120 |

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
