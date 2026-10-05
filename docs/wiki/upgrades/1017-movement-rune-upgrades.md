---
title: "Movement(%) Rune upgrades"
type: "upgrade"
id: 1017
status: "partial"
missing: ["success_rates"]
sources: ["client: JewelSocketMake.cdb group 17 (rows 161–170)", "docs: [[gameplay/reinforce-and-runes]] §1 (WM 0920 rune cost table matches JewelSocketMake +0→+9)", "contract: items.yaml rune_upgrade 0x4a8, server_rules craft_reinforce_rune_odds", "video: [[gameplay/video-rune-upgrades]] §1 (83 attempts, all 41 failures dropped exactly one level, materials and gold spent on every try; Jul 2018) + guide: [[gameplay/reinforce-and-runes]] §3 (blog runas)", "notes: [[gameplay/reinforce-and-runes]] §3 (cap +5 at launch WM 0613, +9 from WM 0726)"]
group: 17
rune: 7162
levels:
  - {"row": 161, "level": 0, "item": 7162, "next": 7163, "materials": [{"item": 701, "count": 10}, {"item": 613, "count": 10}, {"item": 855, "count": 1}]}
  - {"row": 162, "level": 1, "item": 7163, "next": 7164, "materials": [{"item": 701, "count": 20}, {"item": 613, "count": 15}, {"item": 855, "count": 1}]}
  - {"row": 163, "level": 2, "item": 7164, "next": 7165, "materials": [{"item": 701, "count": 40}, {"item": 613, "count": 20}, {"item": 855, "count": 1}]}
  - {"row": 164, "level": 3, "item": 7165, "next": 7166, "materials": [{"item": 701, "count": 60}, {"item": 613, "count": 30}, {"item": 855, "count": 1}]}
  - {"row": 165, "level": 4, "item": 7166, "next": 7167, "materials": [{"item": 701, "count": 80}, {"item": 613, "count": 40}, {"item": 855, "count": 1}]}
  - {"row": 166, "level": 5, "item": 7167, "next": 7168, "materials": [{"item": 702, "count": 10}, {"item": 614, "count": 10}, {"item": 856, "count": 1}]}
  - {"row": 167, "level": 6, "item": 7168, "next": 7169, "materials": [{"item": 702, "count": 20}, {"item": 614, "count": 15}, {"item": 856, "count": 1}]}
  - {"row": 168, "level": 7, "item": 7169, "next": 7170, "materials": [{"item": 702, "count": 40}, {"item": 614, "count": 20}, {"item": 856, "count": 1}]}
  - {"row": 169, "level": 8, "item": 7170, "next": 7171, "materials": [{"item": 702, "count": 60}, {"item": 614, "count": 30}, {"item": 856, "count": 1}]}
  - {"row": 170, "level": 9, "item": 7171, "next": 0, "materials": [{"item": 702, "count": 80}, {"item": 614, "count": 40}, {"item": 856, "count": 1}]}
kind: "rune_upgrade"
on_failure: "drop_one_level"
max_level: 9
---
<!-- generated:start -->
<!-- generated-keys: title=4621b4 type=4389c5 id=4dd260 sources=7fc1bc group=0716d9 rune=dff52c levels=384602 kind=6a6d0e -->
|  |  |
|---|---|
|  | ![](../assets/items/7162.png) |
| **Rune line** | `JewelSocketMake` group 17 |
| **Starts at** | [[wiki/items/7162-movement-rune\|Movement(%) Rune]] |
| **Success rates** | unknown (server side; patch notes give only trends) |

### Levels

Each row upgrades the rune to the next item (C->S `0x4a8`). The +9 row has no next item, so its cost is never used. The costs match the 20 Sep 2018 patch table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1).

| level |  | rune | becomes | materials | row |
|---|---|---|---|---|---|
| +0 | ![](../assets/items/7162.png) | [[wiki/items/7162-movement-rune\|Movement(%) Rune]] | [[wiki/items/7163-movement-rune\|Movement(%) Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 10, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 161 |
| +1 | ![](../assets/items/7163.png) | [[wiki/items/7163-movement-rune\|Movement(%) Rune]] | [[wiki/items/7164-movement-rune\|Movement(%) Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 20, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 15, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 162 |
| +2 | ![](../assets/items/7164.png) | [[wiki/items/7164-movement-rune\|Movement(%) Rune]] | [[wiki/items/7165-movement-rune\|Movement(%) Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 40, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 20, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 163 |
| +3 | ![](../assets/items/7165.png) | [[wiki/items/7165-movement-rune\|Movement(%) Rune]] | [[wiki/items/7166-movement-rune\|Movement(%) Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 60, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 30, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 164 |
| +4 | ![](../assets/items/7166.png) | [[wiki/items/7166-movement-rune\|Movement(%) Rune]] | [[wiki/items/7167-movement-rune\|Movement(%) Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 80, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 40, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 165 |
| +5 | ![](../assets/items/7167.png) | [[wiki/items/7167-movement-rune\|Movement(%) Rune]] | [[wiki/items/7168-movement-rune\|Movement(%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 10, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 10, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 166 |
| +6 | ![](../assets/items/7168.png) | [[wiki/items/7168-movement-rune\|Movement(%) Rune]] | [[wiki/items/7169-movement-rune\|Movement(%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 20, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 15, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 167 |
| +7 | ![](../assets/items/7169.png) | [[wiki/items/7169-movement-rune\|Movement(%) Rune]] | [[wiki/items/7170-movement-rune\|Movement(%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 40, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 20, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 168 |
| +8 | ![](../assets/items/7170.png) | [[wiki/items/7170-movement-rune\|Movement(%) Rune]] | [[wiki/items/7171-movement-rune\|Movement(%) Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 60, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 30, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 169 |
| +9 | ![](../assets/items/7171.png) | [[wiki/items/7171-movement-rune\|Movement(%) Rune]] | – (max) | [[wiki/items/702-crystal-red\|Crystal : Red]] × 80, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 40, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 170 |

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
