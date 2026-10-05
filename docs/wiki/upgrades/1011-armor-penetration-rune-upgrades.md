---
title: "Armor Penetration(%) Rune upgrades"
type: "upgrade"
id: 1011
status: "partial"
missing: ["success_rates"]
sources: ["client: JewelSocketMake.cdb group 11 (rows 101–110)", "docs: [[gameplay/reinforce-and-runes]] §1 (WM 0920 rune cost table matches JewelSocketMake +0→+9)", "contract: items.yaml rune_upgrade 0x4a8, server_rules craft_reinforce_rune_odds", "video: [[gameplay/video-rune-upgrades]] §1 (83 attempts, all 41 failures dropped exactly one level, materials and gold spent on every try; Jul 2018) + guide: [[gameplay/reinforce-and-runes]] §3 (blog runas)", "notes: [[gameplay/reinforce-and-runes]] §3 (cap +5 at launch WM 0613, +9 from WM 0726)"]
group: 11
rune: 7102
levels:
  - {"row": 101, "level": 0, "item": 7102, "next": 7103, "materials": [{"item": 702, "count": 10}, {"item": 615, "count": 15}, {"item": 856, "count": 1}]}
  - {"row": 102, "level": 1, "item": 7103, "next": 7104, "materials": [{"item": 702, "count": 20}, {"item": 615, "count": 20}, {"item": 856, "count": 1}]}
  - {"row": 103, "level": 2, "item": 7104, "next": 7105, "materials": [{"item": 702, "count": 40}, {"item": 615, "count": 30}, {"item": 856, "count": 1}]}
  - {"row": 104, "level": 3, "item": 7105, "next": 7106, "materials": [{"item": 702, "count": 60}, {"item": 615, "count": 40}, {"item": 856, "count": 1}]}
  - {"row": 105, "level": 4, "item": 7106, "next": 7107, "materials": [{"item": 703, "count": 10}, {"item": 616, "count": 10}, {"item": 857, "count": 1}]}
  - {"row": 106, "level": 5, "item": 7107, "next": 7108, "materials": [{"item": 703, "count": 20}, {"item": 616, "count": 15}, {"item": 857, "count": 1}]}
  - {"row": 107, "level": 6, "item": 7108, "next": 7109, "materials": [{"item": 703, "count": 40}, {"item": 616, "count": 20}, {"item": 857, "count": 1}]}
  - {"row": 108, "level": 7, "item": 7109, "next": 7110, "materials": [{"item": 703, "count": 60}, {"item": 616, "count": 30}, {"item": 857, "count": 1}]}
  - {"row": 109, "level": 8, "item": 7110, "next": 7111, "materials": [{"item": 703, "count": 80}, {"item": 616, "count": 40}, {"item": 857, "count": 1}]}
  - {"row": 110, "level": 9, "item": 7111, "next": 0, "materials": [{"item": 703, "count": 120}, {"item": 616, "count": 60}, {"item": 857, "count": 1}]}
kind: "rune_upgrade"
on_failure: "drop_one_level"
max_level: 9
---
<!-- generated:start -->
<!-- generated-keys: title=3f8637 type=4389c5 id=dd2dfa sources=d1e0ef group=17ba07 rune=67c39b levels=355074 kind=6a6d0e -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/7102.png) |
| **Rune line** | `JewelSocketMake` group 11 |
| **Starts at** | [[wiki/items/7102-armor-penetration-rune\|Armor Penetration(%) Rune]] |
| **Success rates** | unknown (server side; patch notes give only trends) |

### Levels

Each row upgrades the rune to the next item (C->S `0x4a8`). The +9 row has no next item, so its cost is never used. The costs match the 20 Sep 2018 patch table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1).

| level |  | rune | becomes | materials | row |
|---|---|---|---|---|---|
| +0 | ![](wiki/assets/items/7102.png) | [[wiki/items/7102-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/7103-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 10, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 15, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 101 |
| +1 | ![](wiki/assets/items/7103.png) | [[wiki/items/7103-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/7104-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 20, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 20, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 102 |
| +2 | ![](wiki/assets/items/7104.png) | [[wiki/items/7104-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/7105-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 40, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 30, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 103 |
| +3 | ![](wiki/assets/items/7105.png) | [[wiki/items/7105-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/7106-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 60, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 40, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 104 |
| +4 | ![](wiki/assets/items/7106.png) | [[wiki/items/7106-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/7107-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 10, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 10, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 105 |
| +5 | ![](wiki/assets/items/7107.png) | [[wiki/items/7107-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/7108-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 20, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 15, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 106 |
| +6 | ![](wiki/assets/items/7108.png) | [[wiki/items/7108-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/7109-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 40, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 20, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 107 |
| +7 | ![](wiki/assets/items/7109.png) | [[wiki/items/7109-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/7110-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 60, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 30, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 108 |
| +8 | ![](wiki/assets/items/7110.png) | [[wiki/items/7110-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/7111-armor-penetration-rune\|Armor Penetration(%) Rune]] | [[wiki/items/703-crystal-black\|Crystal : Black]] × 80, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 40, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 109 |
| +9 | ![](wiki/assets/items/7111.png) | [[wiki/items/7111-armor-penetration-rune\|Armor Penetration(%) Rune]] | – (max) | [[wiki/items/703-crystal-black\|Crystal : Black]] × 120, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 60, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 1 | 110 |

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
