---
title: "Magical Vision Bow"
type: "item"
id: 15002
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 15002"]
name_key: "ItemName_15002"
kind: 31
kind_name: "Weapon"
classes: ["Punisher"]
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 500}
cost_pair:
  - {"currency": 2, "amount": 500}
weapon_base: 24
stats:
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "level"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "tier"}
options:
  - {"code": 200, "value": 24}
skills: [5063, 5064, 5065, 5066]
reinforce: 11
icon: {"file": "Weapon_PCM_01.dds", "index": 2}
obtained_from:
  - {"how": "craft", "recipe": 906}
  - {"how": "random_box", "box": 2}
  - {"how": "random_box", "box": 3}
  - {"how": "gacha", "pool": 2}
  - {"how": "gacha", "pool": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=0eeb7f type=d36ca9 id=97a0ea sources=d28785 name_key=582085 kind=632667 kind_name=631b4f classes=51f98f bind=883bf8 price=6961f8 cost_pair=5b5722 weapon_base=4d134b stats=db11c4 options=fb4042 skills=a6981e reinforce=17ba07 icon=007e55 obtained_from=3a5514 -->
|  |  |
|---|---|
|  | ![Magical Vision Bow](../assets/items/15002.png) |
| **Item id** | `15002` |
| **Kind** | Weapon (31) |
| **Classes** | Punisher |
| **Bind** | on pickup |
| **Buy price** | 500 Gold |
| **Icon** | `ui/icons/Weapon_PCM_01.dds` cell 2 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +10 | × (tier × 15 + reinforce level) | 1 |
| Attack | +10 | × tier | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 200 | 24 | WeaponBase row |

### Weapon base

WeaponBase row 24. The client adds these to the wielder's stats (`FUN_004410d6`; which stat each one is, is not decoded yet): `c2` = 140, `c3` = 10, `c4` = 750, `c5` = 340.

### Weapon skills

Weapon base 24. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones.

1. [[wiki/skills/5063-mystic-arrow|Mystic Arrow]]
2. [[wiki/skills/5064-essence-manipulation|Essence Manipulation]]
3. [[wiki/skills/5065-vision-move|Vision Move]]
4. [[wiki/skills/5066-essence-wave|Essence Wave]]

### Reinforcement

ItemSancMet row 11 (inferred from Item_Base +0x92), 1,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] × 1 |
| 2 | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] × 1 |
| 3 | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] × 2 |
| 4 | [[wiki/items/614-red-passion-piece-c\|Red Passion Piece (C)]] × 3 |
| 5 | [[wiki/items/615-red-passion-fragments-b\|Red Passion Fragments (B)]] × 7 |
| 6 | [[wiki/items/616-red-passion-piece-b\|Red Passion Piece (B)]] × 8 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 906 | [[wiki/items/854-shining-passion\|Shining Passion]] × 5, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 70 | 0 | 100 |

### Where to get it

- In random box table row 2 (RandomBox.cdb; odds are server side)
- In random box table row 3 (RandomBox.cdb; odds are server side)
- Hero gacha pool 02, grade 2 (Gacha_02.cdb; odds are server side)
- Hero gacha pool 05, grade 3 (Gacha_05.cdb; odds are server side)
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
