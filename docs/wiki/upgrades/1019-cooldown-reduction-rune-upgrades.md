---
title: "Cooldown Reduction Rune upgrades"
type: "upgrade"
id: 1019
status: "partial"
missing: ["success_rates"]
sources: ["client: JewelSocketMake.cdb group 19 (rows 181–190)", "docs: [[gameplay/reinforce-and-runes]] §1 (WM 0920 rune cost table matches JewelSocketMake +0→+9)", "contract: items.yaml rune_upgrade 0x4a8, server_rules craft_reinforce_rune_odds", "video: [[gameplay/video-rune-upgrades]] §1 (83 attempts, all 41 failures dropped exactly one level, materials and gold spent on every try; Jul 2018) + guide: [[gameplay/reinforce-and-runes]] §3 (blog runas)", "notes: [[gameplay/reinforce-and-runes]] §3 (cap +5 at launch WM 0613, +9 from WM 0726)"]
group: 19
rune: 7182
levels:
  - {"row": 181, "level": 0, "item": 7182, "next": 7183, "materials": [{"item": 701, "count": 10}, {"item": 613, "count": 10}, {"item": 855, "count": 1}]}
  - {"row": 182, "level": 1, "item": 7183, "next": 7184, "materials": [{"item": 701, "count": 20}, {"item": 613, "count": 15}, {"item": 855, "count": 1}]}
  - {"row": 183, "level": 2, "item": 7184, "next": 7185, "materials": [{"item": 701, "count": 40}, {"item": 613, "count": 20}, {"item": 855, "count": 1}]}
  - {"row": 184, "level": 3, "item": 7185, "next": 7186, "materials": [{"item": 701, "count": 60}, {"item": 613, "count": 30}, {"item": 855, "count": 1}]}
  - {"row": 185, "level": 4, "item": 7186, "next": 7187, "materials": [{"item": 701, "count": 80}, {"item": 613, "count": 40}, {"item": 855, "count": 1}]}
  - {"row": 186, "level": 5, "item": 7187, "next": 7188, "materials": [{"item": 702, "count": 10}, {"item": 614, "count": 10}, {"item": 856, "count": 1}]}
  - {"row": 187, "level": 6, "item": 7188, "next": 7189, "materials": [{"item": 702, "count": 20}, {"item": 614, "count": 15}, {"item": 856, "count": 1}]}
  - {"row": 188, "level": 7, "item": 7189, "next": 7190, "materials": [{"item": 702, "count": 40}, {"item": 614, "count": 20}, {"item": 856, "count": 1}]}
  - {"row": 189, "level": 8, "item": 7190, "next": 7191, "materials": [{"item": 702, "count": 60}, {"item": 614, "count": 30}, {"item": 856, "count": 1}]}
  - {"row": 190, "level": 9, "item": 7191, "next": 0, "materials": [{"item": 702, "count": 80}, {"item": 614, "count": 40}, {"item": 856, "count": 1}]}
kind: "rune_upgrade"
on_failure: "drop_one_level"
max_level: 9
---
<!-- generated:start -->
<!-- generated-keys: title=449f3d type=4389c5 id=8b05af sources=a593bf group=b3f0c7 rune=b7c1d0 levels=7dae80 kind=6a6d0e -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/7182.png) |
| **Rune line** | `JewelSocketMake` group 19 |
| **Starts at** | [[wiki/items/7182-cooldown-reduction-rune\|Cooldown Reduction Rune]] |
| **Success rates** | unknown (server side; patch notes give only trends) |

### Levels

Each row upgrades the rune to the next item (C->S `0x4a8`). The +9 row has no next item, so its cost is never used. The costs match the 20 Sep 2018 patch table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1).

| level |  | rune | becomes | materials | row |
|---|---|---|---|---|---|
| +0 | ![](wiki/assets/items/7182.png) | [[wiki/items/7182-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/7183-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 10, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 181 |
| +1 | ![](wiki/assets/items/7183.png) | [[wiki/items/7183-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/7184-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 20, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 15, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 182 |
| +2 | ![](wiki/assets/items/7184.png) | [[wiki/items/7184-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/7185-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 40, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 20, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 183 |
| +3 | ![](wiki/assets/items/7185.png) | [[wiki/items/7185-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/7186-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 60, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 30, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 184 |
| +4 | ![](wiki/assets/items/7186.png) | [[wiki/items/7186-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/7187-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 80, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 40, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 185 |
| +5 | ![](wiki/assets/items/7187.png) | [[wiki/items/7187-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/7188-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 10, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 10, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 186 |
| +6 | ![](wiki/assets/items/7188.png) | [[wiki/items/7188-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/7189-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 20, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 15, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 187 |
| +7 | ![](wiki/assets/items/7189.png) | [[wiki/items/7189-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/7190-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 40, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 20, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 188 |
| +8 | ![](wiki/assets/items/7190.png) | [[wiki/items/7190-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/7191-cooldown-reduction-rune\|Cooldown Reduction Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 60, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 30, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 189 |
| +9 | ![](wiki/assets/items/7191.png) | [[wiki/items/7191-cooldown-reduction-rune\|Cooldown Reduction Rune]] | – (max) | [[wiki/items/702-crystal-red\|Crystal : Red]] × 80, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 40, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 190 |

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
