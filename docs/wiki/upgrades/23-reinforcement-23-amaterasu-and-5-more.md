---
title: "Reinforcement 23: Amaterasu and 5 more"
type: "upgrade"
id: 23
status: "partial"
missing: ["success_rates"]
sources: ["client: ItemSancMet.cdb id 23", "client: Item_Base.cdb c41@92 (inferred link to ItemSancMet)", "contract: items.yaml reinforce 0x436, server_rules craft_reinforce_rune_odds", "notes: [[gameplay/reinforce-and-runes]] §4 (WM 0412: a failed reinforce drops the item one level and uses up the materials; Reinforcing Adjuvants, item 1100, prevent the drop)"]
gold: 5000
steps:
  - {"step": 1, "materials": [{"item": 601, "count": 20}, {"item": 611, "count": 20}, {"item": 621, "count": 8}]}
  - {"step": 2, "materials": [{"item": 602, "count": 20}, {"item": 612, "count": 20}, {"item": 622, "count": 8}]}
  - {"step": 3, "materials": [{"item": 603, "count": 25}, {"item": 613, "count": 25}, {"item": 623, "count": 10}]}
  - {"step": 4, "materials": [{"item": 604, "count": 32}, {"item": 614, "count": 32}, {"item": 624, "count": 10}]}
  - {"step": 5, "materials": [{"item": 605, "count": 32}, {"item": 615, "count": 32}, {"item": 625, "count": 15}]}
  - {"step": 6, "materials": [{"item": 606, "count": 32}, {"item": 616, "count": 32}, {"item": 626, "count": 15}]}
used_by: [8002, 8003, 8004, 8502, 8503, 8504]
kind: "reinforcement"
on_failure: "drop_one_level"
failure_protection_item: 1100
---
<!-- generated:start -->
<!-- generated-keys: title=2944a7 type=4389c5 id=d435a6 sources=0b80ac gold=f8237d steps=a6a2da used_by=3ead90 kind=701a6f -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/8002.png) |
| **Table** | `ItemSancMet` row 23 |
| **Gold per attempt** | 5,000 |
| **Success rates** | unknown (server side) |
| **Used by** | 6 items |

### Materials per step

Six material steps per row. Whether a step is a reinforce level band or a tier is not settled: the patch notes' six planned tiers fit six steps ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *guess*). One 2018 screenshot shows a T1 weapon +0→+1 costing 1,000 gold + 3 Red Passion Fragments [D].

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 20, [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 20, [[wiki/items/621-orange-passion-fragments-d\|Orange Passion Fragments (D)]] × 8 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 20, [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 20, [[wiki/items/622-orange-passion-piece-d\|Orange Passion Piece (D)]] × 8 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 25, [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 25, [[wiki/items/623-orange-passion-fragments-c\|Orange Passion Fragments (C)]] × 10 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 32, [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 32, [[wiki/items/624-orange-passion-piece-c\|Orange Passion Piece (C)]] × 10 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 32, [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 32, [[wiki/items/625-orange-passion-fragments-b\|Orange Passion Fragments (B)]] × 15 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 32, [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 32, [[wiki/items/626-orange-passion-piece-b\|Orange Passion Piece (B)]] × 15 |

### Items that use it

[[wiki/items/8002-amaterasu|Amaterasu]], [[wiki/items/8003-sarasvati|Sarasvati]], [[wiki/items/8004-artamos|Artamos]], [[wiki/items/8502-crystal-amaterasu|Crystal : Amaterasu]], [[wiki/items/8503-crystal-sarasvati|Crystal : Sarasvati]], [[wiki/items/8504-crystal-artamos|Crystal : Artamos]]

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
