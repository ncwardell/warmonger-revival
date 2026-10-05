---
title: "Guardian Gloves"
type: "item"
id: 412
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 412", "image: [[gameplay/maps-and-dungeons]] §2 (2018 dungeons guide loot grids; Lv 1–4 drop T1, Lv 5–8 T2, pre-reinforced +0…+11; 2–3 rarer drops per dungeon missing)"]
name_key: "ItemName_412"
kind: 52
kind_name: "Gloves"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 120}
cost_pair:
  - {"currency": 2, "amount": 120}
stats:
  - {"code": 6, "stat": "Armor", "value": 4, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 2, "scale": "level"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 40, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 20, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 40, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 9, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_09.png", "index": 38}
obtained_from:
  - {"how": "shop", "shop": 28}
  - {"how": "shop", "shop": 43}
  - {"how": "shop", "shop": 56}
  - {"how": "shop", "shop": 59}
  - {"how": "shop", "shop": 73}
  - {"how": "shop", "shop": 92}
  - {"how": "shop", "shop": 101}
  - {"how": "shop", "shop": 104}
  - {"how": "shop", "shop": 109}
  - {"how": "shop", "shop": 215}
  - {"how": "craft", "recipe": 16}
  - {"how": "craft", "recipe": 2016}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
  - {"how": "dungeon_drop", "field": 127, "tier": 1}
  - {"how": "dungeon_drop", "field": 129, "tier": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=13db69 type=d36ca9 id=6e9b99 sources=b2a531 name_key=b8a4fe kind=a93349 kind_name=f6564c classes=92d079 bind=2be88c price=401276 cost_pair=7638f4 stats=14e736 reinforce=356a19 icon=acb972 obtained_from=90650d -->
|  |  |
|---|---|
|  | ![Guardian Gloves](wiki/assets/items/412.png) |
| **Item id** | `412` |
| **Kind** | Gloves (52) |
| **Category** | [[wiki/items/armor-gloves\|Gloves]] |
| **Classes** | all |
| **Buy price** | 120 Gold |
| **Icon** | `ui/icons/Items_09.png` cell 38 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +4 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +2 | × (tier × 15 + reinforce level) | 7 |
| Mana | +10 | × (tier × 15 + reinforce level) | 33 |
| Armor | +10 | × tier | 6 |
| Magic Resist | +10 | × tier | 7 |
| Mana | +10 | × tier | 33 |
| Armor | +40 | flat | 6 |
| Magic Resist | +20 | flat | 7 |
| Mana | +40 | flat | 33 |
| Movement(%) | Movement +9% | flat | 105 |

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
| 16 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 12 | 180 | 100 |
| 2016 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 12 | 180 | 100 |

### Where to get it

- Sold in [[wiki/shops/28-shop-28-no-npc|Shop 28 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/43-shop-43-no-npc|Shop 43 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/56-shop-56-no-npc|Shop 56 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/59-shop-59-no-npc|Shop 59 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/73-shop-73-no-npc|Shop 73 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/92-shop-92-no-npc|Shop 92 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/101-shop-101-no-npc|Shop 101 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/104-shop-104-no-npc|Shop 104 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/109-shop-109-no-npc|Shop 109 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/215-shop-215-no-npc|Shop 215 (no NPC)]] (no NPC found)
- Hero gacha pool 00, grade 2 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)
- how dungeon_drop, field 127, tier 1 (hand-entered)
- how dungeon_drop, field 129, tier 2 (hand-entered)

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]]
<!-- generated:end -->

## Notes

Drops in the border dungeons Chepa Village (127), Thorn's Hell (129), already reinforced at a random level (+0 up to +11 seen); Lv 1–4 dungeons drop it at tier 1, Lv 5–8 at tier 2 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §2, *image*). Sockets are rolled when the item drops ([[gameplay/items-and-crafting|Items and crafting]] §2).

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
