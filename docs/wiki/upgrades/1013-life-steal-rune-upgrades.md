---
title: "Life Steal Rune upgrades"
type: "upgrade"
id: 1013
status: "partial"
missing: ["success_rates"]
sources: ["client: JewelSocketMake.cdb group 13 (rows 121–130)", "docs: [[gameplay/reinforce-and-runes]] §1 (WM 0920 rune cost table matches JewelSocketMake +0→+9)", "contract: items.yaml rune_upgrade 0x4a8, server_rules craft_reinforce_rune_odds", "video: [[gameplay/video-rune-upgrades]] §1 (83 attempts, all 41 failures dropped exactly one level, materials and gold spent on every try; Jul 2018) + guide: [[gameplay/reinforce-and-runes]] §3 (blog runas)", "notes: [[gameplay/reinforce-and-runes]] §3 (cap +5 at launch WM 0613, +9 from WM 0726)"]
group: 13
rune: 7122
levels:
  - {"row": 121, "level": 0, "item": 7122, "next": 7123, "materials": [{"item": 701, "count": 10}, {"item": 613, "count": 10}, {"item": 855, "count": 1}]}
  - {"row": 122, "level": 1, "item": 7123, "next": 7124, "materials": [{"item": 701, "count": 20}, {"item": 613, "count": 15}, {"item": 855, "count": 1}]}
  - {"row": 123, "level": 2, "item": 7124, "next": 7125, "materials": [{"item": 701, "count": 40}, {"item": 613, "count": 20}, {"item": 855, "count": 1}]}
  - {"row": 124, "level": 3, "item": 7125, "next": 7126, "materials": [{"item": 701, "count": 60}, {"item": 613, "count": 30}, {"item": 855, "count": 1}]}
  - {"row": 125, "level": 4, "item": 7126, "next": 7127, "materials": [{"item": 701, "count": 80}, {"item": 613, "count": 40}, {"item": 855, "count": 1}]}
  - {"row": 126, "level": 5, "item": 7127, "next": 7128, "materials": [{"item": 702, "count": 10}, {"item": 614, "count": 10}, {"item": 856, "count": 1}]}
  - {"row": 127, "level": 6, "item": 7128, "next": 7129, "materials": [{"item": 702, "count": 20}, {"item": 614, "count": 15}, {"item": 856, "count": 1}]}
  - {"row": 128, "level": 7, "item": 7129, "next": 7130, "materials": [{"item": 702, "count": 40}, {"item": 614, "count": 20}, {"item": 856, "count": 1}]}
  - {"row": 129, "level": 8, "item": 7130, "next": 7131, "materials": [{"item": 702, "count": 60}, {"item": 614, "count": 30}, {"item": 856, "count": 1}]}
  - {"row": 130, "level": 9, "item": 7131, "next": 0, "materials": [{"item": 702, "count": 80}, {"item": 614, "count": 40}, {"item": 856, "count": 1}]}
kind: "rune_upgrade"
on_failure: "drop_one_level"
max_level: 9
---
<!-- generated:start -->
<!-- generated-keys: title=4c0e51 type=4389c5 id=ba5bfc sources=ca85fb group=bd307a rune=4f4913 levels=d7e716 kind=6a6d0e -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/7122.png) |
| **Rune line** | `JewelSocketMake` group 13 |
| **Starts at** | [[wiki/items/7122-life-steal-rune\|Life Steal Rune]] |
| **Success rates** | unknown (server side; patch notes give only trends) |

### Levels

Each row upgrades the rune to the next item (C->S `0x4a8`). The +9 row has no next item, so its cost is never used. The costs match the 20 Sep 2018 patch table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1).

| level |  | rune | becomes | materials | row |
|---|---|---|---|---|---|
| +0 | ![](wiki/assets/items/7122.png) | [[wiki/items/7122-life-steal-rune\|Life Steal Rune]] | [[wiki/items/7123-life-steal-rune\|Life Steal Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 10, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 121 |
| +1 | ![](wiki/assets/items/7123.png) | [[wiki/items/7123-life-steal-rune\|Life Steal Rune]] | [[wiki/items/7124-life-steal-rune\|Life Steal Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 20, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 15, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 122 |
| +2 | ![](wiki/assets/items/7124.png) | [[wiki/items/7124-life-steal-rune\|Life Steal Rune]] | [[wiki/items/7125-life-steal-rune\|Life Steal Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 40, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 20, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 123 |
| +3 | ![](wiki/assets/items/7125.png) | [[wiki/items/7125-life-steal-rune\|Life Steal Rune]] | [[wiki/items/7126-life-steal-rune\|Life Steal Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 60, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 30, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 124 |
| +4 | ![](wiki/assets/items/7126.png) | [[wiki/items/7126-life-steal-rune\|Life Steal Rune]] | [[wiki/items/7127-life-steal-rune\|Life Steal Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 80, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 40, [[wiki/items/855-mysterious-passion\|Mysterious Passion]] × 1 | 125 |
| +5 | ![](wiki/assets/items/7127.png) | [[wiki/items/7127-life-steal-rune\|Life Steal Rune]] | [[wiki/items/7128-life-steal-rune\|Life Steal Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 10, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 10, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 126 |
| +6 | ![](wiki/assets/items/7128.png) | [[wiki/items/7128-life-steal-rune\|Life Steal Rune]] | [[wiki/items/7129-life-steal-rune\|Life Steal Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 20, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 15, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 127 |
| +7 | ![](wiki/assets/items/7129.png) | [[wiki/items/7129-life-steal-rune\|Life Steal Rune]] | [[wiki/items/7130-life-steal-rune\|Life Steal Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 40, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 20, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 128 |
| +8 | ![](wiki/assets/items/7130.png) | [[wiki/items/7130-life-steal-rune\|Life Steal Rune]] | [[wiki/items/7131-life-steal-rune\|Life Steal Rune]] | [[wiki/items/702-crystal-red\|Crystal : Red]] × 60, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 30, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 129 |
| +9 | ![](wiki/assets/items/7131.png) | [[wiki/items/7131-life-steal-rune\|Life Steal Rune]] | – (max) | [[wiki/items/702-crystal-red\|Crystal : Red]] × 80, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 40, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 1 | 130 |

### Rules from the patch notes

- Cap +5 at launch, +9 from WM 0726; success falls with level, earlier for rarer runes (WM 0406); raised overall in WM 0920. A failure usually loses one level.
- Source: [[gameplay/reinforce-and-runes|Reinforce and runes]] §3.
<!-- generated:end -->

## Notes

Tier 2 rune line (level-0 cost in Yellow) ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1, *client*). The 20 Sep 2018 cost table matches this line's materials; before that, upgrades cost crystals only ([[gameplay/reinforce-and-runes|Reinforce and runes]] §2, WM 0420 images).

A 2018 screenshot shows +4→+5 Life Steal at **5,000 gold + 20 + 10 materials**, with the destruction warning; +4 Life Steal = 5 % life steal ([[gameplay/items-and-crafting|Items and crafting]] §2, *image*). The gold fits the 1,000 × target-level rule seen on tier-1 runes.

## Behaviour

On a failed upgrade the rune drops **one level**; gold and materials are spent on every try ([[gameplay/video-rune-upgrades|Rune upgrade video]] §1, 41 of 41 failures, *video*; the blog says the same, [[gameplay/reinforce-and-runes|Reinforce and runes]] §3). The window still shows a "destruction of rune in case of failure" warning beside an optional sub-material slot.

Cap: +5 at launch (WM 0613), about +7 on 12 Jul 2018 (*video*), **+9** from WM 0726 ([[gameplay/reinforce-and-runes|Reinforce and runes]] §3, [[gameplay/video-rune-upgrades|Rune upgrade video]] §1).

Success rates were never published. Patch notes give only trends: until WM 0404 tier-1 runes could not fail at all (bug), then got a "really small" fail chance at +8 and +9; WM 0406 made success fall slowly with level, starting earlier for rarer runes (rarity 2, from level 5–6; rarity = tier is a *guess*); WM 0920 raised rune success overall ([[gameplay/reinforce-and-runes|Reinforce and runes]] §3, *notes*).

From WM 1107 runes are affected by the PvP stat correction ([[gameplay/reinforce-and-runes|Reinforce and runes]] §3, *notes*).

## Sources

- video: [[gameplay/video-rune-upgrades]] §1 (83 attempts, all 41 failures dropped exactly one level, materials and gold spent on every try; Jul 2018) + guide: [[gameplay/reinforce-and-runes]] §3 (blog runas)
- notes: [[gameplay/reinforce-and-runes]] §3 (cap +5 at launch WM 0613, +9 from WM 0726)

## Open questions

Is the 1,000 × level gold rule the same for tier 2 and 3 runes? Only this +5 screenshot supports it for tier 2.

Destruction or one-level drop? The UI warns of destruction without a sub-material, but every recorded failure only dropped one level ([[gameplay/video-rune-upgrades|Rune upgrade video]] §1, [[gameplay/reinforce-and-runes|Reinforce and runes]] §3).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
