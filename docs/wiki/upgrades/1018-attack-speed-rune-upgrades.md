---
title: "Attack Speed(%) Rune upgrades"
type: "upgrade"
id: 1018
status: "partial"
missing: ["success_rates"]
sources: ["client: JewelSocketMake.cdb group 18 (rows 171–180)", "docs: [[gameplay/reinforce-and-runes]] §1 (WM 0920 rune cost table matches JewelSocketMake +0→+9)", "contract: items.yaml rune_upgrade 0x4a8, server_rules craft_reinforce_rune_odds", "video: [[gameplay/video-rune-upgrades]] §1 (83 attempts, all 41 failures dropped exactly one level, materials and gold spent on every try; Jul 2018) + guide: [[gameplay/reinforce-and-runes]] §3 (blog runas)", "notes: [[gameplay/reinforce-and-runes]] §3 (cap +5 at launch WM 0613, +9 from WM 0726)", "video: [[gameplay/video-rune-upgrades]] §2 (gold per attempt = 1,000 × level after the upgrade, tier-1 Attack rune, steps +2→+3 … +6→+7)"]
group: 18
rune: 7172
levels:
  - {"row": 171, "level": 0, "item": 7172, "next": 7173, "materials": [{"item": 700, "count": 10}, {"item": 611, "count": 10}]}
  - {"row": 172, "level": 1, "item": 7173, "next": 7174, "materials": [{"item": 700, "count": 15}, {"item": 611, "count": 15}]}
  - {"row": 173, "level": 2, "item": 7174, "next": 7175, "materials": [{"item": 700, "count": 20}, {"item": 611, "count": 20}]}
  - {"row": 174, "level": 3, "item": 7175, "next": 7176, "materials": [{"item": 700, "count": 30}, {"item": 611, "count": 30}]}
  - {"row": 175, "level": 4, "item": 7176, "next": 7177, "materials": [{"item": 700, "count": 60}, {"item": 611, "count": 40}, {"item": 854, "count": 1}]}
  - {"row": 176, "level": 5, "item": 7177, "next": 7178, "materials": [{"item": 700, "count": 80}, {"item": 611, "count": 50}, {"item": 854, "count": 1}]}
  - {"row": 177, "level": 6, "item": 7178, "next": 7179, "materials": [{"item": 700, "count": 100}, {"item": 611, "count": 60}, {"item": 854, "count": 1}]}
  - {"row": 178, "level": 7, "item": 7179, "next": 7180, "materials": [{"item": 701, "count": 10}, {"item": 612, "count": 10}, {"item": 854, "count": 1}]}
  - {"row": 179, "level": 8, "item": 7180, "next": 7181, "materials": [{"item": 701, "count": 20}, {"item": 612, "count": 15}, {"item": 854, "count": 1}]}
  - {"row": 180, "level": 9, "item": 7181, "next": 0, "materials": [{"item": 701, "count": 30}, {"item": 612, "count": 20}, {"item": 854, "count": 1}]}
kind: "rune_upgrade"
on_failure: "drop_one_level"
max_level: 9
gold_rule: {"per_level_after_upgrade": 1000}
---
<!-- generated:start -->
<!-- generated-keys: title=45f574 type=4389c5 id=cea8be sources=56c6f7 group=9e6a55 rune=2b5980 levels=b2a3c1 kind=6a6d0e -->
|  |  |
|---|---|
|  | ![](../assets/items/7172.png) |
| **Rune line** | `JewelSocketMake` group 18 |
| **Starts at** | [[wiki/items/7172-attack-speed-rune\|Attack Speed(%) Rune]] |
| **Success rates** | unknown (server side; patch notes give only trends) |

### Levels

Each row upgrades the rune to the next item (C->S `0x4a8`). The +9 row has no next item, so its cost is never used. The costs match the 20 Sep 2018 patch table ([[gameplay/reinforce-and-runes|Reinforce and runes]] §1).

| level |  | rune | becomes | materials | row |
|---|---|---|---|---|---|
| +0 | ![](../assets/items/7172.png) | [[wiki/items/7172-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/7173-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 10 | 171 |
| +1 | ![](../assets/items/7173.png) | [[wiki/items/7173-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/7174-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 15, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 15 | 172 |
| +2 | ![](../assets/items/7174.png) | [[wiki/items/7174-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/7175-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 20, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 20 | 173 |
| +3 | ![](../assets/items/7175.png) | [[wiki/items/7175-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/7176-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 30, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 30 | 174 |
| +4 | ![](../assets/items/7176.png) | [[wiki/items/7176-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/7177-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 60, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 40, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 175 |
| +5 | ![](../assets/items/7177.png) | [[wiki/items/7177-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/7178-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 80, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 50, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 176 |
| +6 | ![](../assets/items/7178.png) | [[wiki/items/7178-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/7179-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 100, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 60, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 177 |
| +7 | ![](../assets/items/7179.png) | [[wiki/items/7179-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/7180-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 10, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 178 |
| +8 | ![](../assets/items/7180.png) | [[wiki/items/7180-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/7181-attack-speed-rune\|Attack Speed(%) Rune]] | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 20, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 15, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 179 |
| +9 | ![](../assets/items/7181.png) | [[wiki/items/7181-attack-speed-rune\|Attack Speed(%) Rune]] | – (max) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 30, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 20, [[wiki/items/854-shining-passion\|Shining Passion]] × 1 | 180 |

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
