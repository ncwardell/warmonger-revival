---
title: "Belt of Transcendency"
type: "item"
id: 426
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 426", "image: [[gameplay/maps-and-dungeons]] §2 (2018 dungeons guide loot grids; Lv 1–4 drop T1, Lv 5–8 T2, pre-reinforced +0…+11; 2–3 rarer drops per dungeon missing)"]
name_key: "ItemName_426"
kind: 55
kind_name: "Belt"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 150}
cost_pair:
  - {"currency": 2, "amount": 150}
stats:
  - {"code": 2, "stat": "Ability Power", "value": 3, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "level"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 1, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "tier"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 3, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 3, "scale": "tier"}
  - {"code": 2, "stat": "Ability Power", "value": 15, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 180, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 2, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_08.png", "index": 61}
obtained_from:
  - {"how": "shop", "shop": 35}
  - {"how": "shop", "shop": 51}
  - {"how": "shop", "shop": 80}
  - {"how": "shop", "shop": 96}
  - {"how": "shop", "shop": 213}
  - {"how": "craft", "recipe": 30}
  - {"how": "craft", "recipe": 2030}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
  - {"how": "dungeon_drop", "field": 126, "tier": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=a50bd0 type=d36ca9 id=62866a sources=07b2a6 name_key=cd99bc kind=8effee kind_name=ddf027 classes=92d079 bind=2be88c price=6d19d1 cost_pair=ca8a4e stats=10d4a4 reinforce=356a19 icon=3849bb obtained_from=e90e41 -->
|  |  |
|---|---|
|  | ![Belt of Transcendency](wiki/assets/items/426.png) |
| **Item id** | `426` |
| **Kind** | Belt (55) |
| **Classes** | all |
| **Buy price** | 150 Gold |
| **Icon** | `ui/icons/Items_08.png` cell 61 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +3 | × (tier × 15 + reinforce level) | 2 |
| Mana | +10 | × (tier × 15 + reinforce level) | 33 |
| Mana Regeneration | +1 | × (tier × 15 + reinforce level) | 34 |
| Ability Power | +10 | × tier | 2 |
| Mana Regeneration | +3 | × tier | 34 |
| Mana | +3 | × tier | 33 |
| Ability Power | +15 | flat | 2 |
| Mana | +180 | flat | 33 |
| Mana Regeneration | +2 | flat | 34 |

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
| 30 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 20 | 300 | 100 |
| 2030 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 20 | 300 | 100 |

### Where to get it

- Sold in [[wiki/shops/35-shop-35-no-npc|Shop 35 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/51-shop-51-no-npc|Shop 51 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/80-shop-80-no-npc|Shop 80 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/96-shop-96-no-npc|Shop 96 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/213-shop-213-no-npc|Shop 213 (no NPC)]] (no NPC found)
- Hero gacha pool 00, grade 1 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)
- how dungeon_drop, field 126, tier 2 (hand-entered)
<!-- generated:end -->

## Notes

Drops in the border dungeons Demon Hell (126), already reinforced at a random level (+0 up to +11 seen); Lv 1–4 dungeons drop it at tier 1, Lv 5–8 at tier 2 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §2, *image*). Sockets are rolled when the item drops ([[gameplay/items-and-crafting|Items and crafting]] §2).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- image: [[gameplay/maps-and-dungeons]] §2 (2018 dungeons guide loot grids; Lv 1–4 drop T1, Lv 5–8 T2, pre-reinforced +0…+11; 2–3 rarer drops per dungeon missing)

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
