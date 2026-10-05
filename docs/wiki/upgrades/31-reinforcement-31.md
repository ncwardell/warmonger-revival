---
title: "Reinforcement 31"
type: "upgrade"
id: 31
status: "partial"
missing: ["success_rates"]
sources: ["client: ItemSancMet.cdb id 31", "client: Item_Base.cdb c41@92 (inferred link to ItemSancMet)", "contract: items.yaml reinforce 0x436, server_rules craft_reinforce_rune_odds", "notes: [[gameplay/reinforce-and-runes]] §4 (WM 0412: a failed reinforce drops the item one level and uses up the materials; Reinforcing Adjuvants, item 1100, prevent the drop)"]
gold: 5000
steps:
  - {"step": 1, "materials": [{"item": 612, "count": 4}]}
  - {"step": 2, "materials": [{"item": 613, "count": 5}]}
  - {"step": 3, "materials": [{"item": 614, "count": 5}]}
  - {"step": 4, "materials": [{"item": 615, "count": 7}]}
  - {"step": 5, "materials": [{"item": 616, "count": 8}]}
  - {"step": 6, "materials": [{"item": 617, "count": 8}]}
used_by: []
kind: "reinforcement"
on_failure: "drop_one_level"
failure_protection_item: 1100
---
<!-- generated:start -->
<!-- generated-keys: title=dcf37d type=4389c5 id=632667 sources=f42fb7 gold=f8237d steps=80f222 used_by=97d170 kind=701a6f -->
|  |  |
|---|---|
| **Table** | `ItemSancMet` row 31 |
| **Gold per attempt** | 5,000 |
| **Success rates** | unknown (server side) |
| **Used by** | 0 items |

### Materials per step

Six material steps per row. Whether a step is a reinforce level band or a tier is not settled: the patch notes' six planned tiers fit six steps ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *guess*). One 2018 screenshot shows a T1 weapon +0→+1 costing 1,000 gold + 3 Red Passion Fragments [D].

| step | materials |
|---|---|
| 1 | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 4 |
| 2 | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 5 |
| 3 | [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 5 |
| 4 | [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 7 |
| 5 | [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 8 |
| 6 | [[wiki/items/617-red-passion-fragments-a\|Red Passion Fragments (A)]] × 8 |

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
