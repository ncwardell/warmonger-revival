---
title: "Reinforcement 3"
type: "upgrade"
id: 3
status: "partial"
missing: ["success_rates"]
sources: ["client: ItemSancMet.cdb id 3", "client: Item_Base.cdb c41@92 (inferred link to ItemSancMet)", "contract: items.yaml reinforce 0x436, server_rules craft_reinforce_rune_odds", "notes: [[gameplay/reinforce-and-runes]] §4 (WM 0412: a failed reinforce drops the item one level and uses up the materials; Reinforcing Adjuvants, item 1100, prevent the drop)"]
gold: 1000
steps:
  - {"step": 1, "materials": [{"item": 601, "count": 8}]}
  - {"step": 2, "materials": [{"item": 602, "count": 8}]}
  - {"step": 3, "materials": [{"item": 603, "count": 10}]}
  - {"step": 4, "materials": [{"item": 604, "count": 20}]}
  - {"step": 5, "materials": [{"item": 605, "count": 20}]}
  - {"step": 6, "materials": [{"item": 606, "count": 30}]}
used_by: []
kind: "reinforcement"
on_failure: "drop_one_level"
failure_protection_item: 1100
---
<!-- generated:start -->
<!-- generated-keys: title=f4bb0e type=4389c5 id=77de68 sources=15468e gold=e3cbba steps=1ad139 used_by=97d170 kind=701a6f -->
|  |  |
|---|---|
| **Table** | `ItemSancMet` row 3 |
| **Gold per attempt** | 1,000 |
| **Success rates** | unknown (server side) |
| **Used by** | 0 items |

### Materials per step

Six material steps per row. Whether a step is a reinforce level band or a tier is not settled: the patch notes' six planned tiers fit six steps ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *guess*). One 2018 screenshot shows a T1 weapon +0→+1 costing 1,000 gold + 3 Red Passion Fragments [D].

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 8 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 8 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 10 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 20 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 20 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 30 |

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
