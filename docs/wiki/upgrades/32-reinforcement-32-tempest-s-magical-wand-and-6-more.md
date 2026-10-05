---
title: "Reinforcement 32: Tempest's magical wand and 6 more"
type: "upgrade"
id: 32
status: "partial"
missing: ["success_rates"]
sources: ["client: ItemSancMet.cdb id 32", "client: Item_Base.cdb c41@92 (inferred link to ItemSancMet)", "contract: items.yaml reinforce 0x436, server_rules craft_reinforce_rune_odds", "notes: [[gameplay/reinforce-and-runes]] §4 (WM 0412: a failed reinforce drops the item one level and uses up the materials; Reinforcing Adjuvants, item 1100, prevent the drop)"]
gold: 5000
steps:
  - {"step": 1, "materials": [{"item": 612, "count": 8}]}
  - {"step": 2, "materials": [{"item": 613, "count": 10}]}
  - {"step": 3, "materials": [{"item": 614, "count": 10}]}
  - {"step": 4, "materials": [{"item": 615, "count": 15}]}
  - {"step": 5, "materials": [{"item": 616, "count": 16}]}
  - {"step": 6, "materials": [{"item": 617, "count": 16}]}
used_by: [10004, 10005, 10014, 15005, 15009, 20004, 20014]
kind: "reinforcement"
on_failure: "drop_one_level"
failure_protection_item: 1100
---
<!-- generated:start -->
<!-- generated-keys: title=7c5fde type=4389c5 id=cb4e52 sources=769646 gold=f8237d steps=37e747 used_by=77bb7d kind=701a6f -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/10004.png) |
| **Table** | `ItemSancMet` row 32 |
| **Gold per attempt** | 5,000 |
| **Success rates** | unknown (server side) |
| **Used by** | 7 items |

### Materials per step

Six material steps per row. Whether a step is a reinforce level band or a tier is not settled: the patch notes' six planned tiers fit six steps ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *guess*). One 2018 screenshot shows a T1 weapon +0→+1 costing 1,000 gold + 3 Red Passion Fragments [D].

| step | materials |
|---|---|
| 1 | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 8 |
| 2 | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 10 |
| 3 | [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 10 |
| 4 | [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 15 |
| 5 | [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 16 |
| 6 | [[wiki/items/617-red-passion-fragments-a\|Red Passion Fragments (A)]] × 16 |

### Items that use it

[[wiki/items/10004-tempest-s-magical-wand|Tempest's magical wand]], [[wiki/items/10005-magical-blade-shield-flame|Magical Blade Shield : Flame]], [[wiki/items/10014-skeleton-king-s-magic-gun|Skeleton king's Magic Gun]], [[wiki/items/15005-skeleton-king-s-vision-bow|Skeleton king's Vision Bow]], [[wiki/items/15009-skeleton-king-s-magic-dagger|Skeleton King's Magic Dagger]], [[wiki/items/20004-skeleton-king-s-magic-hammer|Skeleton King's Magic Hammer]], [[wiki/items/20014-skeleton-king-s-magic-cannon|Skeleton King's Magic Cannon]]

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
