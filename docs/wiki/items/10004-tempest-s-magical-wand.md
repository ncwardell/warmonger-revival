---
title: "Tempest's magical wand"
type: "item"
id: 10004
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 10004"]
name_key: "ItemName_10004"
kind: 31
kind_name: "Weapon"
classes: ["Saint"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
rarity: 1
weapon_base: 5
stats:
  - {"code": 1, "stat": "Attack", "value": 2, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 8, "scale": "level"}
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "tier"}
options:
  - {"code": 200, "value": 5}
skills: [5303, 5304, 5305, 5306]
reinforce: 32
icon: {"file": "Weapon_PCE_01.dds", "index": 36}
obtained_from:
  - {"how": "craft", "recipe": 929}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=2ac65d type=d36ca9 id=75186a sources=256f7c name_key=6b3e75 kind=632667 kind_name=631b4f classes=30141f bind=883bf8 price=6961f8 cost_pair=5b5722 rarity=356a19 weapon_base=ac3478 stats=977f84 options=59d394 skills=1f1f61 reinforce=cb4e52 icon=f31993 obtained_from=7907a5 -->
|  |  |
|---|---|
|  | ![Tempest's magical wand](wiki/assets/items/10004.png) |
| **Item id** | `10004` |
| **Kind** | Weapon (31) |
| **Classes** | Saint |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Rarity (guessed column)** | 1 |
| **Icon** | `ui/icons/Weapon_PCE_01.dds` cell 36 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +2 | × (tier × 15 + reinforce level) | 1 |
| Ability Power | +8 | × (tier × 15 + reinforce level) | 2 |
| Ability Power | +10 | × tier | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 5 | WeaponBase row |

### Weapon base

WeaponBase row 5. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 90, `c3` = 130, `c4` = 750, `c5` = 380.

### Weapon skills

Weapon base 5. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5303-thunder-bolt|Thunder bolt]]
2. [[wiki/skills/5304-lightning-strike|Lightning Strike]]
3. [[wiki/skills/5305-ball-of-lighting|Ball of Lighting]]
4. [[wiki/skills/5306-punishment|Punishment]]

### Reinforcement

ItemSancMet row 32 (inferred from Item_Base +0x92), 5,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 8 |
| 2 | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 10 |
| 3 | [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 10 |
| 4 | [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 15 |
| 5 | [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 16 |
| 6 | [[wiki/items/617-red-passion-fragments-a\|Red Passion Fragments (A)]] × 16 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 929 | [[wiki/items/2753-the-tempest-fisher-s-sealed-weapon\|The Tempest Fisher's Sealed Weapon]] × 1, [[wiki/items/2703-fin-of-fisher\|Fin of Fisher]] × 1, [[wiki/items/1933-essence-of-water\|Essence of Water]] × 2 | 0 | 40 |

### Where to get it

- Hero gacha pool 02, grade 1 (Gacha_02.cdb; odds are server side)
- Hero gacha pool 05, grade 2 (Gacha_05.cdb; odds are server side)
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
