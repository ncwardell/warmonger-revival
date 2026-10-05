---
title: "Reinforcement 1: Spell Necklace and 49 more"
type: "upgrade"
id: 1
status: "partial"
missing: ["success_rates"]
sources: ["client: ItemSancMet.cdb id 1", "client: Item_Base.cdb c41@92 (inferred link to ItemSancMet)", "contract: items.yaml reinforce 0x436, server_rules craft_reinforce_rune_odds", "notes: [[gameplay/reinforce-and-runes]] §4 (WM 0412: a failed reinforce drops the item one level and uses up the materials; Reinforcing Adjuvants, item 1100, prevent the drop)"]
gold: 1000
steps:
  - {"step": 1, "materials": [{"item": 601, "count": 1}]}
  - {"step": 2, "materials": [{"item": 602, "count": 1}]}
  - {"step": 3, "materials": [{"item": 603, "count": 1}]}
  - {"step": 4, "materials": [{"item": 604, "count": 2}]}
  - {"step": 5, "materials": [{"item": 605, "count": 5}]}
  - {"step": 6, "materials": [{"item": 606, "count": 7}]}
used_by: [1, 2, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444]
kind: "reinforcement"
on_failure: "drop_one_level"
failure_protection_item: 1100
---
<!-- generated:start -->
<!-- generated-keys: title=f931c9 type=4389c5 id=356a19 sources=de7f5f gold=e3cbba steps=041219 used_by=3c6beb kind=701a6f -->
|  |  |
|---|---|
|  | ![](wiki/assets/items/397.png) |
| **Table** | `ItemSancMet` row 1 |
| **Gold per attempt** | 1,000 |
| **Success rates** | unknown (server side) |
| **Used by** | 50 items |

### Materials per step

Six material steps per row. Whether a step is a reinforce level band or a tier is not settled: the patch notes' six planned tiers fit six steps ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *guess*). One 2018 screenshot shows a T1 weapon +0→+1 costing 1,000 gold + 3 Red Passion Fragments [D].

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 1 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 1 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 1 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 2 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 5 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 7 |

### Items that use it

[[wiki/items/1|Item 1]], [[wiki/items/2|Item 2]], [[wiki/items/397-spell-necklace|Spell Necklace]], [[wiki/items/398-spell-belt|Spell Belt]], [[wiki/items/399-spell-bracelet|Spell Bracelet]], [[wiki/items/400-spell-ring|Spell Ring]], [[wiki/items/401-helmet-of-life|Helmet of Life]], [[wiki/items/402-armor-of-life|Armor of Life]], [[wiki/items/403-gloves-of-life|Gloves of Life]], [[wiki/items/404-shoes-of-life|Shoes of Life]], [[wiki/items/405-necklace-of-life|Necklace of Life]], [[wiki/items/406-belt-of-life|Belt of Life]], [[wiki/items/407-bracelet-of-life|Bracelet of Life]], [[wiki/items/408-ring-of-life|Ring of Life]], [[wiki/items/409-guardian-helmet|Guardian Helmet]], [[wiki/items/410-guardian-armor|Guardian Armor]], [[wiki/items/411-guardian-shoes|Guardian Shoes]], [[wiki/items/412-guardian-gloves|Guardian Gloves]], [[wiki/items/413-spirit-earring|Spirit Earring]], [[wiki/items/414-spirit-robe|Spirit Robe]], [[wiki/items/415-spirit-shoes|Spirit Shoes]], [[wiki/items/416-spirit-gloves|Spirit Gloves]], [[wiki/items/417-helmet-of-honor|Helmet of Honor]], [[wiki/items/418-armor-of-honor|Armor of Honor]], [[wiki/items/419-shoes-of-honor|Shoes of Honor]], [[wiki/items/420-gloves-of-honor|Gloves of Honor]], [[wiki/items/421-necklace-of-mediation|Necklace of Mediation]], [[wiki/items/422-belt-of-mediation|Belt of Mediation]], [[wiki/items/423-bracelet-of-mediation|Bracelet of Mediation]], [[wiki/items/424-ring-of-mediation|Ring of Mediation]], [[wiki/items/425-necklace-of-transcendency|Necklace of Transcendency]], [[wiki/items/426-belt-of-transcendency|Belt of Transcendency]], [[wiki/items/427-bracelet-of-transcendency|Bracelet of Transcendency]], [[wiki/items/428-ring-of-transcendency|Ring of Transcendency]], [[wiki/items/429-bandolier-necklace|Bandolier Necklace]], [[wiki/items/430-bandolier-belt|Bandolier Belt]], [[wiki/items/431-bandolier-bracelet|Bandolier Bracelet]], [[wiki/items/432-bandolier-ring|Bandolier Ring]], [[wiki/items/433-barrier-necklace|Barrier Necklace]], [[wiki/items/434-barrier-belt|Barrier Belt]], [[wiki/items/435-barrier-bracelet|Barrier Bracelet]], [[wiki/items/436-barrier-ring|Barrier Ring]], [[wiki/items/437-necklace-of-courage|Necklace of Courage]], [[wiki/items/438-belt-of-courage|Belt of Courage]], [[wiki/items/439-bracelet-of-courage|Bracelet of Courage]], [[wiki/items/440-ring-of-courage|Ring of Courage]], [[wiki/items/441-necklace-of-rise|Necklace of Rise]], [[wiki/items/442-belt-of-rise|Belt of Rise]], [[wiki/items/443-bracelet-of-rise|Bracelet of Rise]], [[wiki/items/444-ring-of-rise|Ring of Rise]]

### Rules from the patch notes

- A failed reinforce drops the item one level and uses up the materials; Reinforcing Adjuvants (item 1100) prevent the drop (WM 0412).
- Success falls slowly with tier and rarity; Rainbow Reinforcing Stones only work on their own rarity (WM 0406 / 0420).
- Source: [[gameplay/reinforce-and-runes|Reinforce and runes]] §4.
<!-- generated:end -->

## Notes

Each tier runs +0…+15 and is reinforced with gold + passion; Red Passion is for weapons, Blue Passion for gear, and amounts grow each level ([[gameplay/items-and-crafting|Items and crafting]] §1, *guides*). Tier-up (+15 → next tier +0) also consumes a second identical +15 item plus Orange Passion and gold ([[gameplay/items-and-crafting|Items and crafting]] §1; per-tier Orange / Brilliant Passion table in [[gameplay/reinforce-and-runes|Reinforce and runes]] §4).

Seen in game (mid-2018): a T1 helmet +0→+1 cost **1,000 gold + 2 Blue Passion Fragments [D]**; Armor 40→44, MR 20→23, HP +10 ([[gameplay/items-and-crafting|Items and crafting]] §1, *image*).

## Behaviour

Before WM 0412 a failed reinforce destroyed the item; after it, the item **drops one level** (+3 → +2) and the materials are used up. **Reinforcing Adjuvants** (item 1100) prevent the drop ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *notes*).

Success falls slowly with tier and rarity, starting at a lower tier for rarer items (WM 0406); Rainbow Reinforcing Stones (641–646) only work on items of their own rarity (WM 0420); a notice appears before reinforcing items of different rarities (WM 0621) ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *notes*). No rates were published.

## Sources

- notes: [[gameplay/reinforce-and-runes]] §4 (WM 0412: a failed reinforce drops the item one level and uses up the materials; Reinforcing Adjuvants, item 1100, prevent the drop)

## Open questions

The screenshot's 2 Blue Passion Fragments [D] for +0→+1 do not match step 1 of this row (1 × 601); which helmet it was, and how steps map to levels, is not known.

The 2018 guides say reinforcing "never fails" ([[gameplay/items-and-crafting|Items and crafting]] §1), while the WM 0406/0412 patch notes describe falling success and a one-level drop on failure ([[gameplay/reinforce-and-runes|Reinforce and runes]] §4). This page follows the patch notes.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
