---
title: "Helmet of Honor"
type: "item"
id: 417
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 417", "image: [[gameplay/maps-and-dungeons]] §2 (2018 dungeons guide loot grids; Lv 1–4 drop T1, Lv 5–8 T2, pre-reinforced +0…+11; 2–3 rarer drops per dungeon missing)"]
name_key: "ItemName_417"
kind: 50
kind_name: "Helmet"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 100}
cost_pair:
  - {"currency": 2, "amount": 100}
stats:
  - {"code": 6, "stat": "Armor", "value": 4, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 3, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "level"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "tier"}
  - {"code": 7, "stat": "Magic Resist", "value": 10, "scale": "tier"}
  - {"code": 31, "stat": "Health", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 40, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 20, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 85, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 13, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_08.png", "index": 39}
obtained_from:
  - {"how": "shop", "shop": 31}
  - {"how": "shop", "shop": 40}
  - {"how": "shop", "shop": 48}
  - {"how": "shop", "shop": 76}
  - {"how": "shop", "shop": 85}
  - {"how": "shop", "shop": 89}
  - {"how": "shop", "shop": 212}
  - {"how": "shop", "shop": 223}
  - {"how": "craft", "recipe": 21}
  - {"how": "craft", "recipe": 2021}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
  - {"how": "dungeon_drop", "field": 123, "tier": 1}
  - {"how": "dungeon_drop", "field": 124, "tier": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=eff2d4 type=d36ca9 id=4dc778 sources=bda9c7 name_key=e966a6 kind=e1822d kind_name=c90f98 classes=92d079 bind=2be88c price=936627 cost_pair=ebf7c2 stats=9a84fa reinforce=356a19 icon=a06501 obtained_from=1299b0 -->
|  |  |
|---|---|
|  | ![Helmet of Honor](wiki/assets/items/417.png) |
| **Item id** | `417` |
| **Kind** | Helmet (50) |
| **Classes** | all |
| **Buy price** | 100 Gold |
| **Icon** | `ui/icons/Items_08.png` cell 39 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +4 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +3 | × (tier × 15 + reinforce level) | 7 |
| Health | +10 | × (tier × 15 + reinforce level) | 31 |
| Armor | +10 | × tier | 6 |
| Magic Resist | +10 | × tier | 7 |
| Health | +10 | × tier | 31 |
| Armor | +40 | flat | 6 |
| Magic Resist | +20 | flat | 7 |
| Mana | +85 | flat | 33 |
| Movement(%) | Movement +13% | flat | 105 |

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
| 21 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |
| 2021 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |

### Where to get it

- Sold in [[wiki/shops/31-shop-31-no-npc|Shop 31 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/40-shop-40-no-npc|Shop 40 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/48-shop-48-no-npc|Shop 48 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/76-shop-76-no-npc|Shop 76 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/85-shop-85-no-npc|Shop 85 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/89-shop-89-no-npc|Shop 89 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/212-shop-212-no-npc|Shop 212 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/223-shop-223-no-npc|Shop 223 (no NPC)]] (no NPC found)
- Hero gacha pool 00, grade 2 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)
- how dungeon_drop, field 123, tier 1 (hand-entered)
- how dungeon_drop, field 124, tier 2 (hand-entered)

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]
<!-- generated:end -->

## Notes

Drops in the border dungeons Swamps of Snake Warrior (123), Ghost Fortress (124), already reinforced at a random level (+0 up to +11 seen); Lv 1–4 dungeons drop it at tier 1, Lv 5–8 at tier 2 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §2, *image*). Sockets are rolled when the item drops ([[gameplay/items-and-crafting|Items and crafting]] §2).

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
