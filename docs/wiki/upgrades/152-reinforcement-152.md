---
title: "Reinforcement 152"
type: "upgrade"
id: 152
status: "partial"
missing: ["success_rates"]
sources: ["client: ItemSancMet.cdb id 152", "client: Item_Base.cdb c41@92 (inferred link to ItemSancMet)", "contract: items.yaml reinforce 0x436, server_rules craft_reinforce_rune_odds", "notes: [[gameplay/reinforce-and-runes]] §4 (WM 0412: a failed reinforce drops the item one level and uses up the materials; Reinforcing Adjuvants, item 1100, prevent the drop)"]
gold: 10000
steps:
  - {"step": 1, "materials": [{"item": 631, "count": 20}, {"item": 1933, "count": 4}]}
  - {"step": 2, "materials": [{"item": 632, "count": 40}, {"item": 1933, "count": 10}]}
  - {"step": 3, "materials": [{"item": 633, "count": 60}, {"item": 1933, "count": 20}, {"item": 857, "count": 5}]}
  - {"step": 4, "materials": [{"item": 634, "count": 80}, {"item": 1933, "count": 40}]}
  - {"step": 5, "materials": [{"item": 635, "count": 100}, {"item": 1933, "count": 100}]}
  - {"step": 6, "materials": []}
used_by: []
kind: "reinforcement"
on_failure: "drop_one_level"
failure_protection_item: 1100
---
<!-- generated:start -->
<!-- generated-keys: title=ed75cf type=4389c5 id=ac2646 sources=96074e gold=8a12a3 steps=f075eb used_by=97d170 kind=701a6f -->
|  |  |
|---|---|
| **Table** | `ItemSancMet` row 152 |
| **Gold per attempt** | 10,000 |
| **Success rates** | unknown (server side) |
| **Used by** | 0 items |

### Materials per step

Six material steps per row. Whether a step is a reinforce level band or a tier is not settled: the patch notes' six planned tiers fit six steps ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *guess*). One 2018 screenshot shows a T1 weapon +0→+1 costing 1,000 gold + 3 Red Passion Fragments [D].

| step | materials |
|---|---|
| 1 | [[wiki/items/631-violet-passion-fragments-d\|Violet Passion Fragments (D)]] × 20, [[wiki/items/1933-essence-of-water\|Essence of Water]] × 4 |
| 2 | [[wiki/items/632-violet-passion-piece-d\|Violet Passion Piece (D)]] × 40, [[wiki/items/1933-essence-of-water\|Essence of Water]] × 10 |
| 3 | [[wiki/items/633-violet-passion-fragments-c\|Violet Passion Fragments (C)]] × 60, [[wiki/items/1933-essence-of-water\|Essence of Water]] × 20, [[wiki/items/857-amplifying-passion\|Amplifying Passion]] × 5 |
| 4 | [[wiki/items/634-violet-passion-piece-c\|Violet Passion Piece (C)]] × 80, [[wiki/items/1933-essence-of-water\|Essence of Water]] × 40 |
| 5 | [[wiki/items/635-violet-passion-fragments-b\|Violet Passion Fragments (B)]] × 100, [[wiki/items/1933-essence-of-water\|Essence of Water]] × 100 |
| 6 | – |

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
