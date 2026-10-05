---
title: "Magic resist Penetration Rune upgrades"
type: "upgrade"
id: 1010
status: "partial"
missing: ["success_rates"]
sources: ["client: JewelSocketMake.cdb group 10 (rows 91–100)", "docs: [[gameplay/reinforce-and-runes]] §1 (WM 0920 rune cost table matches JewelSocketMake +0→+9)", "contract: items.yaml rune_upgrade 0x4a8, server_rules craft_reinforce_rune_odds", "video: [[gameplay/video-rune-upgrades]] §1 (83 attempts, all 41 failures dropped exactly one level, materials and gold spent on every try; Jul 2018) + guide: [[gameplay/reinforce-and-runes]] §3 (blog runas)", "notes: [[gameplay/reinforce-and-runes]] §3 (cap +5 at launch WM 0613, +9 from WM 0726)"]
group: 10
rune: 7092
levels:
  - {"row": 91, "level": 0, "item": 7092, "next": 7093, "materials": [{"item": 701, "count": 10}, {"item": 613, "count": 10}, {"item": 855, "count": 1}]}
  - {"row": 92, "level": 1, "item": 7093, "next": 7094, "materials": [{"item": 701, "count": 20}, {"item": 613, "count": 15}, {"item": 855, "count": 1}]}
  - {"row": 93, "level": 2, "item": 7094, "next": 7095, "materials": [{"item": 701, "count": 40}, {"item": 613, "count": 20}, {"item": 855, "count": 1}]}
  - {"row": 94, "level": 3, "item": 7095, "next": 7096, "materials": [{"item": 701, "count": 60}, {"item": 613, "count": 30}, {"item": 855, "count": 1}]}
  - {"row": 95, "level": 4, "item": 7096, "next": 7097, "materials": [{"item": 701, "count": 80}, {"item": 613, "count": 40}, {"item": 855, "count": 1}]}
  - {"row": 96, "level": 5, "item": 7097, "next": 7098, "materials": [{"item": 702, "count": 10}, {"item": 614, "count": 10}, {"item": 856, "count": 1}]}
  - {"row": 97, "level": 6, "item": 7098, "next": 7099, "materials": [{"item": 702, "count": 20}, {"item": 614, "count": 15}, {"item": 856, "count": 1}]}
  - {"row": 98, "level": 7, "item": 7099, "next": 7100, "materials": [{"item": 702, "count": 40}, {"item": 614, "count": 20}, {"item": 856, "count": 1}]}
  - {"row": 99, "level": 8, "item": 7100, "next": 7101, "materials": [{"item": 702, "count": 60}, {"item": 614, "count": 30}, {"item": 856, "count": 1}]}
  - {"row": 100, "level": 9, "item": 7101, "next": 0, "materials": [{"item": 702, "count": 80}, {"item": 614, "count": 40}, {"item": 856, "count": 1}]}
kind: "rune_upgrade"
on_failure: "drop_one_level"
max_level: 9
---
<!-- generated:start -->
<!-- generated-keys: title=e87bd2 type=4389c5 id=1966e6 sources=d379b0 group=b1d578 rune=b3db2f levels=1a211a kind=6a6d0e -->
|  |  |
|---|---|
|  | ![](../assets/items/7092.png) |
| **Rune line** | `JewelSocketMake` group 10 |
| **Starts at** | [[wiki/items/7092-magic-resist-penetration-rune\|Magic resist Penetration Rune]] |
| **Success rates** | unknown (server side; patch notes give only trends) |

### Levels

Each row upgrades the rune to the next item (C->S `0x4a8`). The +9 row has no next item, so its cost is never used. The costs match the 20 Sep 2018 patch table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1).

| level |  | rune | becomes | materials | row |
|---|---|---|---|---|---|
| +0 | ![](../assets/items/7092.png) | [[wiki/items/7092-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/7093-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 10, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 91 |
| +1 | ![](../assets/items/7093.png) | [[wiki/items/7093-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/7094-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 20, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 15, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 92 |
| +2 | ![](../assets/items/7094.png) | [[wiki/items/7094-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/7095-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 40, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 20, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 93 |
| +3 | ![](../assets/items/7095.png) | [[wiki/items/7095-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/7096-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 60, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 30, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 94 |
| +4 | ![](../assets/items/7096.png) | [[wiki/items/7096-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/7097-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 80, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 40, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 95 |
| +5 | ![](../assets/items/7097.png) | [[wiki/items/7097-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/7098-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 10, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 10, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 96 |
| +6 | ![](../assets/items/7098.png) | [[wiki/items/7098-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/7099-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 20, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 15, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 97 |
| +7 | ![](../assets/items/7099.png) | [[wiki/items/7099-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/7100-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 40, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 20, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 98 |
| +8 | ![](../assets/items/7100.png) | [[wiki/items/7100-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/7101-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 60, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 30, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 99 |
| +9 | ![](../assets/items/7101.png) | [[wiki/items/7101-magic-resist-penetration-rune\|Magic resist Penetration Rune]] | – (max) | [[wiki/items/702-crystal-red\|Crystal : Red]] × 80, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 40, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 100 |

### Rules from the patch notes

- Cap +5 at launch, +9 from WM 0726; success falls with level, earlier for rarer runes (WM 0406); raised overall in WM 0920. A failure usually loses one level.
- Source: [[gameplay/reinforce-and-runes|Reinforce and runes]] §3.
<!-- generated:end -->

## Notes

Tier 2 rune line (level-0 cost in Yellow) ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1, *client*). The 20 Sep 2018 cost table matches this line's materials; before that, upgrades cost crystals only ([[gameplay/reinforce-and-runes|Reinforce and runes]] §2, WM 0420 images).

Patch-note stat values: Magic Resist Penetration at +7/+8/+9 went 13/16/19 → 12/13/15 (WM 0412) → **11/12/13** (WM 0420). Use the client table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §3).

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
