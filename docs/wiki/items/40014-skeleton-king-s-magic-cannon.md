---
title: "Skeleton King's Magic Cannon"
type: "item"
id: 40014
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 40014"]
name_key: "ItemName_40014"
kind: 31
kind_name: "Weapon"
classes: ["Guardian"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
rarity: 2
weapon_base: 56
stats:
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
options:
  - {"code": 200, "value": 56}
skills: [5133, 5134, 5136, 5137]
reinforce: 33
icon: {"file": "Weapon_PCD_01.dds", "index": 4}
obtained_from:
  - {"how": "craft", "recipe": 928}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=b216d1 type=d36ca9 id=3d68fd sources=758836 name_key=916b6a kind=632667 kind_name=631b4f classes=2160c0 bind=883bf8 price=6961f8 cost_pair=5b5722 rarity=da4b92 weapon_base=54ceb9 stats=db11c4 options=779c28 skills=75caca reinforce=b6692e icon=a19198 obtained_from=122bfe -->
|  |  |
|---|---|
|  | ![Skeleton King's Magic Cannon](../assets/items/40014.png) |
| **Item id** | `40014` |
| **Kind** | Weapon (31) |
| **Classes** | Guardian |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Rarity (guessed column)** | 2 |
| **Icon** | `ui/icons/Weapon_PCD_01.dds` cell 4 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +10 | × (tier × 15 + reinforce level) | 1 |
| Attack | +10 | × tier | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 56 | WeaponBase row |

### Weapon base

WeaponBase row 56. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 160, `c3` = 40, `c4` = 700, `c5` = 380.

### Weapon skills

Weapon base 56. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5133-rocket-shot|Rocket Shot]]
2. [[wiki/skills/5134-smoke-screen|Smoke Screen]]
3. [[wiki/skills/5136-step-back|Step Back]]
4. [[wiki/skills/5137-wild-launch|Wild Launch]]

### Reinforcement

ItemSancMet row 33 (inferred from Item_Base +0x92), 5,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 15 |
| 2 | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 20 |
| 3 | [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 20 |
| 4 | [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 30 |
| 5 | [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 32 |
| 6 | [[wiki/items/617-red-passion-fragments-a\|Red Passion Fragments (A)]] × 32 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 928 | [[wiki/items/2751-the-death-head-s-sealed-weapon\|The Death Head's Sealed Weapon]] × 1, [[wiki/items/2701-deathhead-horn\|DeathHead Horn]] × 1, [[wiki/items/1930-essence-of-darkness\|essence of Darkness]] × 2 | 0 | 40 |

### Where to get it

- Hero gacha pool 02, grade 1 (Gacha_02.cdb; odds are server side)
- Hero gacha pool 05, grade 3 (Gacha_05.cdb; odds are server side)

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]]
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
