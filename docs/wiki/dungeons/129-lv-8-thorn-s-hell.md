---
title: "[Lv 8] Thorn's Hell"
type: "dungeon"
id: 129
status: "stub"
missing: ["time_limit_s"]
sources: ["client: SceneList.cdb id 129", "client: DungeonAdmission.cdb field 129", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 129"]
field: 129
max_users: 5
level: 8
entry_cost:
  - {"mode": "normal", "item": 688, "count": 10}
  - {"mode": "hard", "item": 688, "count": 19}
event: false
shown_rewards: [602, 603, 693, 694, 695, 1932, 2708, 2758]
c17: 2009
image: "UI/FieldImages/8.png"
dungeon_slots:
  - {"group": 0, "slot": 10}
  - {"group": 1, "slot": 10}
  - {"group": 2, "slot": 10}
boss: [849]
gear_tier: "T2"
gathering: [806, 822, 824]
time_limit_s: null
---
<!-- generated:start -->
<!-- generated-keys: title=0bf214 type=3e3f38 id=8b7471 sources=f70cd9 field=8b7471 max_users=ac3478 level=fe5dbb entry_cost=3f4f04 event=7cb6ef shown_rewards=342901 c17=7263d6 image=6fb519 dungeon_slots=9a35e1 boss=f97f7d gear_tier=7b5982 gathering=0cbe10 time_limit_s=2be88c -->
|  |  |
|---|---|
|  | ![(Lv 8) Thorn's Hell](../assets/dungeons/129.png) |
| **Field** | [[wiki/fields/129-lv-8-thorn-s-hell\|(Lv 8) Thorn's Hell (field 129)]] |
| **Level** | 8 |
| **Gear tier dropped** | T2 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Banner** | `UI/FieldImages/8.png` |
| **c17 (unknown)** | 2009 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 10 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 19 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/849-akasha|Akasha]] (main)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/602-blue-passion-piece-d|Blue Passion Piece (D)]], [[wiki/items/603-blue-passion-fragments-c|Blue Passion Fragments (C)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/694-gem-stone-yellow|Gem Stone : Yellow]], [[wiki/items/695-gem-stone-red|Gem Stone : Red]], [[wiki/items/1932-essence-of-fire|Essence of Fire]], [[wiki/items/2708-horn-of-akasha|Horn of Akasha]], [[wiki/items/2758-the-arch-devil-akasha-s-sealed-weapon|The Arch devil Akasha's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/806-emerald|Emerald]], [[wiki/items/822-rosemary|Rosemary]], [[wiki/items/824-jasmine|Jasmine]]. Positions on the [[wiki/fields/129-lv-8-thorn-s-hell|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 10, group 1 slot 10, group 2 slot 10

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
