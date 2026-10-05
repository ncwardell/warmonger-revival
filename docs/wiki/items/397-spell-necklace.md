---
title: "Spell Necklace"
type: "item"
id: 397
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 397"]
name_key: "ItemName_397"
kind: 54
kind_name: "Necklace"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 150}
cost_pair:
  - {"currency": 2, "amount": 150}
stats:
  - {"code": 2, "stat": "Ability Power", "value": 4, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "level"}
  - {"code": 32, "stat": "Health Regeneration", "value": 1, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "tier"}
  - {"code": 32, "stat": "Health Regeneration", "value": 2, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 30, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 200, "scale": "flat"}
  - {"code": 32, "stat": "Health Regeneration", "value": 8, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_10.png", "index": 24}
obtained_from:
  - {"how": "shop", "shop": 27}
  - {"how": "shop", "shop": 39}
  - {"how": "shop", "shop": 51}
  - {"how": "shop", "shop": 72}
  - {"how": "shop", "shop": 84}
  - {"how": "shop", "shop": 96}
  - {"how": "shop", "shop": 108}
  - {"how": "shop", "shop": 211}
  - {"how": "craft", "recipe": 1}
  - {"how": "craft", "recipe": 2001}
  - {"how": "quest_reward", "quest": 100, "count": 1}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=0d54f4 type=d36ca9 id=20387d sources=23732e name_key=f5e2f7 kind=80e28a kind_name=7b4b74 classes=92d079 bind=2be88c price=6d19d1 cost_pair=ca8a4e stats=f66d39 reinforce=356a19 icon=d73da3 obtained_from=b1284b -->
|  |  |
|---|---|
|  | ![Spell Necklace](wiki/assets/items/397.png) |
| **Item id** | `397` |
| **Kind** | Necklace (54) |
| **Classes** | all |
| **Buy price** | 150 Gold |
| **Icon** | `ui/icons/Items_10.png` cell 24 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +4 | × (tier × 15 + reinforce level) | 2 |
| Health | +10 | × (tier × 15 + reinforce level) | 31 |
| Health Regeneration | +1 | × (tier × 15 + reinforce level) | 32 |
| Health | +20 | × tier | 31 |
| Health Regeneration | +2 | × tier | 32 |
| Ability Power | +30 | flat | 2 |
| Health | +200 | flat | 31 |
| Health Regeneration | +8 | flat | 32 |

### Reinforcement

ItemSancMet row 1 (inferred from Item_Base +0x92), 1,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 1 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 1 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 1 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 2 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 5 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 7 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |
| 2001 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |

### Where to get it

- Sold in [[wiki/shops/27-shop-27-no-npc|Shop 27 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/39-shop-39-no-npc|Shop 39 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/51-shop-51-no-npc|Shop 51 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/72-shop-72-no-npc|Shop 72 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/84-shop-84-no-npc|Shop 84 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/96-shop-96-no-npc|Shop 96 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/108-shop-108-no-npc|Shop 108 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/211-shop-211-no-npc|Shop 211 (no NPC)]] (no NPC found)
- Reward of quest [[wiki/quests/100-hunting-for-furs|Hunting for Furs]] × 1
- Hero gacha pool 00, grade 3 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]
<!-- generated:end -->

## Notes

<!-- hand-written: add what you know, with a source -->

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
