---
title: "Spell Ring"
type: "item"
id: 400
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 400", "image: [[gameplay/maps-and-dungeons]] §2 (2018 dungeons guide loot grids; Lv 1–4 drop T1, Lv 5–8 T2, pre-reinforced +0…+11; 2–3 rarer drops per dungeon missing)"]
name_key: "ItemName_400"
kind: 57
kind_name: "Ring"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 110}
cost_pair:
  - {"currency": 2, "amount": 110}
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
icon: {"file": "Items_10.png", "index": 27}
obtained_from:
  - {"how": "shop", "shop": 35}
  - {"how": "shop", "shop": 43}
  - {"how": "shop", "shop": 59}
  - {"how": "shop", "shop": 80}
  - {"how": "shop", "shop": 92}
  - {"how": "shop", "shop": 104}
  - {"how": "shop", "shop": 112}
  - {"how": "shop", "shop": 116}
  - {"how": "shop", "shop": 213}
  - {"how": "craft", "recipe": 4}
  - {"how": "craft", "recipe": 2004}
  - {"how": "quest_reward", "quest": 7, "count": 1}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
  - {"how": "dungeon_drop", "field": 121, "tier": 1}
  - {"how": "dungeon_drop", "field": 125, "tier": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=b64d0c type=d36ca9 id=ab7f7b sources=078cb6 name_key=d98a89 kind=9109c8 kind_name=8ad6b7 classes=92d079 bind=2be88c price=76d727 cost_pair=d2f20b stats=f66d39 reinforce=356a19 icon=8d54f0 obtained_from=bcbea4 -->
|  |  |
|---|---|
|  | ![Spell Ring](wiki/assets/items/400.png) |
| **Item id** | `400` |
| **Kind** | Ring (57) |
| **Classes** | all |
| **Buy price** | 110 Gold |
| **Icon** | `ui/icons/Items_10.png` cell 27 |

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
| 4 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |
| 2004 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |

### Where to get it

- Sold in [[wiki/shops/35-shop-35-no-npc|Shop 35 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/43-shop-43-no-npc|Shop 43 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/59-shop-59-no-npc|Shop 59 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/80-shop-80-no-npc|Shop 80 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/92-shop-92-no-npc|Shop 92 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/104-shop-104-no-npc|Shop 104 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/112-shop-112-no-npc|Shop 112 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/116-shop-116-no-npc|Shop 116 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/213-shop-213-no-npc|Shop 213 (no NPC)]] (no NPC found)
- Reward of quest [[wiki/quests/7-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]] × 1
- Hero gacha pool 00, grade 3 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)
- how dungeon_drop, field 121, tier 1 (hand-entered)
- how dungeon_drop, field 125, tier 2 (hand-entered)

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]
<!-- generated:end -->

## Notes

Drops in the border dungeons Skull Temple (121), Tow Canyon (125), already reinforced at a random level (+0 up to +11 seen); Lv 1–4 dungeons drop it at tier 1, Lv 5–8 at tier 2 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §2, *image*). Sockets are rolled when the item drops ([[gameplay/items-and-crafting|Items and crafting]] §2).

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
