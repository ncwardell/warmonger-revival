---
title: "Reinforcement 312"
type: "upgrade"
id: 312
status: "partial"
missing: ["success_rates"]
sources: ["client: ItemSancMet.cdb id 312", "client: Item_Base.cdb c41@92 (inferred link to ItemSancMet)", "contract: items.yaml reinforce 0x436, server_rules craft_reinforce_rune_odds", "notes: [[gameplay/reinforce-and-runes]] §4 (WM 0412: a failed reinforce drops the item one level and uses up the materials; Reinforcing Adjuvants, item 1100, prevent the drop)"]
gold: 10000
steps:
  - {"step": 1, "materials": [{"item": 602, "count": 60}, {"item": 612, "count": 60}, {"item": 622, "count": 6}, {"item": 1931, "count": 2}]}
  - {"step": 2, "materials": [{"item": 603, "count": 80}, {"item": 613, "count": 80}, {"item": 623, "count": 8}, {"item": 1931, "count": 4}]}
  - {"step": 3, "materials": [{"item": 604, "count": 100}, {"item": 624, "count": 10}, {"item": 856, "count": 3}, {"item": 1931, "count": 6}]}
  - {"step": 4, "materials": [{"item": 605, "count": 120}, {"item": 615, "count": 120}, {"item": 625, "count": 12}, {"item": 1931, "count": 8}]}
  - {"step": 5, "materials": [{"item": 606, "count": 150}, {"item": 616, "count": 150}, {"item": 626, "count": 15}, {"item": 1931, "count": 10}]}
  - {"step": 6, "materials": [{"item": 607, "count": 160}, {"item": 617, "count": 160}, {"item": 627, "count": 16}, {"item": 1931, "count": 12}]}
used_by: []
kind: "reinforcement"
on_failure: "drop_one_level"
failure_protection_item: 1100
---
<!-- generated:start -->
<!-- generated-keys: title=9ad614 type=4389c5 id=a93c16 sources=ae66dc gold=8a12a3 steps=fbe1b9 used_by=97d170 kind=701a6f -->
|  |  |
|---|---|
| **Table** | `ItemSancMet` row 312 |
| **Gold per attempt** | 10,000 |
| **Success rates** | unknown (server side) |
| **Used by** | 0 items |

### Materials per step

Six material steps per row. Whether a step is a reinforce level band or a tier is not settled: the patch notes' six planned tiers fit six steps ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *guess*). One 2018 screenshot shows a T1 weapon +0→+1 costing 1,000 gold + 3 Red Passion Fragments [D].

| step | materials |
|---|---|
| 1 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 60, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 60, [[wiki/items/622-orange-passion-piece-d\|Orange Passion Piece (D)]] × 6, [[wiki/items/1931-essence-of-wind\|Essence of Wind]] × 2 |
| 2 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 80, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 80, [[wiki/items/623-orange-passion-fragments-c\|Orange Passion Fragments (C)]] × 8, [[wiki/items/1931-essence-of-wind\|Essence of Wind]] × 4 |
| 3 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 100, [[wiki/items/624-orange-passion-piece-c\|Orange Passion Piece (C)]] × 10, [[wiki/items/856-brilliant-passion\|Brilliant Passion]] × 3, [[wiki/items/1931-essence-of-wind\|Essence of Wind]] × 6 |
| 4 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 120, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 120, [[wiki/items/625-orange-passion-fragments-b\|Orange Passion Fragments (B)]] × 12, [[wiki/items/1931-essence-of-wind\|Essence of Wind]] × 8 |
| 5 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 150, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 150, [[wiki/items/626-orange-passion-piece-b\|Orange Passion Piece (B)]] × 15, [[wiki/items/1931-essence-of-wind\|Essence of Wind]] × 10 |
| 6 | [[wiki/items/607-blue-passion-fragments-a\|Blue Passion Fragments (A)]] × 160, [[wiki/items/617-red-passion-fragments-a\|Red Passion Fragments (A)]] × 160, [[wiki/items/627-orange-passion-fragments-a\|Orange Passion Fragments (A)]] × 16, [[wiki/items/1931-essence-of-wind\|Essence of Wind]] × 12 |

### Rules from the patch notes

- A failed reinforce drops the item one level and uses up the materials; Reinforcing Adjuvants (item 1100) prevent the drop (WM 0412).
- Success falls slowly with tier and rarity; Rainbow Reinforcing Stones only work on their own rarity (WM 0406 / 0420).
- Source: [[gameplay/reinforce-and-runes|Reinforce and runes]] §4.
<!-- generated:end -->

## Notes

Each tier runs +0…+15 and is reinforced with gold + passion; Red Passion is for weapons, Blue Passion for gear, and amounts grow each level ([[gameplay/items-and-crafting|Items and crafting]] §1, *guides*). Tier-up (+15 → next tier +0) also consumes a second identical +15 item plus Orange Passion and gold ([[gameplay/items-and-crafting|Items and crafting]] §1; per-tier Orange / Brilliant Passion table in [[gameplay/reinforce-and-runes|Reinforce and runes]] §4).

## Behaviour

Before WM 0412 a failed reinforce destroyed the item; after it, the item **drops one level** (+3 → +2) and the materials are used up. **Reinforcing Adjuvants** (item 1100) prevent the drop ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *notes*).

Success falls slowly with tier and rarity, starting at a lower tier for rarer items (WM 0406); Rainbow Reinforcing Stones (641–646) only work on items of their own rarity (WM 0420); a notice appears before reinforcing items of different rarities (WM 0621) ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *notes*). No rates were published.

## Sources

- notes: [[gameplay/reinforce-and-runes]] §4 (WM 0412: a failed reinforce drops the item one level and uses up the materials; Reinforcing Adjuvants, item 1100, prevent the drop)

## Open questions

The 2018 guides say reinforcing "never fails" ([[gameplay/items-and-crafting|Items and crafting]] §1), while the WM 0406/0412 patch notes describe falling success and a one-level drop on failure ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4). This page follows the patch notes.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
