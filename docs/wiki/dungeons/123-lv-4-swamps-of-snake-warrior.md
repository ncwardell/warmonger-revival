---
title: "[Lv 4] Swamps of Snake Warrior"
type: "dungeon"
id: 123
status: "stub"
missing: ["time_limit_s"]
sources: ["client: SceneList.cdb id 123", "client: DungeonAdmission.cdb field 123", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 123"]
field: 123
max_users: 5
level: 4
entry_cost:
  - {"mode": "normal", "item": 688, "count": 6}
  - {"mode": "hard", "item": 688, "count": 7}
event: false
shown_rewards: [612, 602, 693, 1932, 2704, 2754]
c17: 2005
image: "UI/FieldImages/4.png"
dungeon_slots:
  - {"group": 0, "slot": 6}
  - {"group": 1, "slot": 6}
  - {"group": 2, "slot": 6}
boss: [675, 736, 1213]
gear_tier: "T1"
gathering: [816, 826, 828]
time_limit_s: null
---
<!-- generated:start -->
<!-- generated-keys: title=e5603a type=3e3f38 id=40bd00 sources=c58ebc field=40bd00 max_users=ac3478 level=1b6453 entry_cost=00381f event=7cb6ef shown_rewards=65b1ed c17=23a053 image=936313 dungeon_slots=679f34 boss=9798c5 gear_tier=13930c gathering=f3c467 time_limit_s=2be88c -->
|  |  |
|---|---|
|  | ![(Lv 4) Swamps of Snake Warrior](wiki/assets/dungeons/123.png) |
| **Field** | [[wiki/fields/123-lv-4-swamps-of-snake-warrior\|(Lv 4) Swamps of Snake Warrior (field 123)]] |
| **Level** | 4 |
| **Gear tier dropped** | T1 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Banner** | `UI/FieldImages/4.png` |
| **c17 (unknown)** | 2005 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 6 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 7 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/675-slayer-komodo|Slayer Komodo]] (main)
- [[wiki/monsters/736-slayer-komodo|Slayer Komodo]] (other id in the guides' list; *client* variant)
- [[wiki/monsters/1213-slayer-komodo|Slayer Komodo]] (other id in the guides' list; *client* variant)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/602-blue-passion-piece-d|Blue Passion Piece (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1932-essence-of-fire|Essence of Fire]], [[wiki/items/2704-horn-of-komodo|Horn of Komodo]], [[wiki/items/2754-the-slayer-komodo-s-sealed-weapon|The Slayer Komodo's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/816-onyx|Onyx]], [[wiki/items/826-borage|Borage]], [[wiki/items/828-spartium|Spartium]]. Positions on the [[wiki/fields/123-lv-4-swamps-of-snake-warrior|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 6, group 1 slot 6, group 2 slot 6

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].
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
