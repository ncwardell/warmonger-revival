---
title: "[Lv 9] Dragon Island"
type: "dungeon"
id: 142
status: "partial"
missing: ["boss", "time_limit_s"]
sources: ["client: SceneList.cdb id 142", "client: DungeonAdmission.cdb field 142", "client: Dungeon.cdb", "client: Trigger.cdb field 142"]
field: 142
max_users: 5
level: 9
entry_cost:
  - {"mode": "normal", "item": 688, "count": 10}
  - {"mode": "hard", "item": 688, "count": 23}
event: false
shown_rewards: [613, 603, 694, 695, 1930, 1931, 1932, 1933, 1934, 1935]
c17: 2015
image: "UI/FieldImages/5.png"
dungeon_slots:
  - {"group": 0, "slot": 11}
  - {"group": 0, "slot": 12}
  - {"group": 0, "slot": 13}
  - {"group": 0, "slot": 14}
  - {"group": 0, "slot": 15}
  - {"group": 1, "slot": 11}
  - {"group": 1, "slot": 12}
  - {"group": 1, "slot": 13}
  - {"group": 1, "slot": 14}
  - {"group": 1, "slot": 15}
  - {"group": 2, "slot": 11}
  - {"group": 2, "slot": 12}
  - {"group": 2, "slot": 13}
  - {"group": 2, "slot": 14}
  - {"group": 2, "slot": 15}
boss: []
gathering: [806, 822, 824]
time_limit_s: null
---
<!-- generated:start -->
<!-- generated-keys: title=b263a8 type=3e3f38 id=2a2b47 sources=7280df field=2a2b47 max_users=ac3478 level=0ade7c entry_cost=13237d event=7cb6ef shown_rewards=4fa050 c17=9cdda6 image=fe7704 dungeon_slots=825448 boss=97d170 gathering=0cbe10 time_limit_s=2be88c -->
|  |  |
|---|---|
|  | ![(Lv 9) Dragon Island](../assets/dungeons/142.png) |
| **Field** | [[wiki/fields/142-lv-9-dragon-island\|(Lv 9) Dragon Island (field 142)]] |
| **Level** | 9 |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Banner** | `UI/FieldImages/5.png` |
| **c17 (unknown)** | 2015 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 10 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 23 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

Not known. Add `boss:` (UnitDB ids) with a source.

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]], [[wiki/items/603-blue-passion-fragments-c|Blue Passion Fragments (C)]], [[wiki/items/694-gem-stone-yellow|Gem Stone : Yellow]], [[wiki/items/695-gem-stone-red|Gem Stone : Red]], [[wiki/items/1930-essence-of-darkness|essence of Darkness]], [[wiki/items/1931-essence-of-wind|Essence of Wind]], [[wiki/items/1932-essence-of-fire|Essence of Fire]], [[wiki/items/1933-essence-of-water|Essence of Water]], [[wiki/items/1934-essence-of-earth|Essence of Earth]], [[wiki/items/1935-essence-of-light|Essence of Light]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/806-emerald|Emerald]], [[wiki/items/822-rosemary|Rosemary]], [[wiki/items/824-jasmine|Jasmine]]. Positions on the [[wiki/fields/142-lv-9-dragon-island|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 11, group 0 slot 12, group 0 slot 13, group 0 slot 14, group 0 slot 15, group 1 slot 11, group 1 slot 12, group 1 slot 13, group 1 slot 14, group 1 slot 15, group 2 slot 11, group 2 slot 12, group 2 slot 13, group 2 slot 14, group 2 slot 15

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].

### Mentioned in

- [[gameplay/dungeon-drops#2. Where the sheet disagrees with the client|Dungeon drops (ores and herbs) § 2. Where the sheet disagrees with the client]]
- [[gameplay/patch-history#Dungeons and world|Patch notes and other sources § Dungeons and world]]
<!-- generated:end -->

## Notes

- Warmonger patch 0920 made Dragon Island reachable only through a field dimension gate (notes, [[gameplay/patch-history]] § Dungeons and world).
- No 2018 guide and not the Crush Online sheet covers it; its level (9), cost and advertised rewards are client only ([[gameplay/dungeon-drops]] §1–2, [[gameplay/maps-and-dungeons]] §2).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/patch-history]] § Dungeons and world, [[gameplay/dungeon-drops]] §1–2, [[gameplay/maps-and-dungeons]] §2

## Open questions

- Boss unknown ([[gameplay/dungeon-drops]] §1 lists "?").
- Time limit: Warmonger patch 0402 (15 min) predates this dungeon (added by 0920), so it is not copied here.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
