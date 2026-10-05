---
title: "[Lv 2] Skull Cemetery"
type: "dungeon"
id: 128
status: "stub"
missing: ["time_limit_s"]
sources: ["client: SceneList.cdb id 128", "client: DungeonAdmission.cdb field 128", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 128"]
field: 128
max_users: 5
level: 2
entry_cost:
  - {"mode": "normal", "item": 688, "count": 3}
  - {"mode": "hard", "item": 688, "count": 5}
event: false
shown_rewards: [611, 693, 1930, 2702, 2752]
c17: 2003
image: "UI/FieldImages/2.png"
dungeon_slots:
  - {"group": 0, "slot": 4}
  - {"group": 1, "slot": 4}
  - {"group": 2, "slot": 4}
boss: [673, 809, 1205]
gear_tier: "T1"
gathering: [814, 804, 822, 824]
time_limit_s: null
---
<!-- generated:start -->
<!-- generated-keys: title=006667 type=3e3f38 id=b4182b sources=cb6130 field=b4182b max_users=ac3478 level=da4b92 entry_cost=3354a5 event=7cb6ef shown_rewards=ee6072 c17=ab165c image=d3bc8e dungeon_slots=079694 boss=0c12c5 gear_tier=13930c gathering=83d28e time_limit_s=2be88c -->
|  |  |
|---|---|
|  | ![(Lv 2) Skull Cemetery](../assets/dungeons/128.png) |
| **Field** | [[wiki/fields/128-lv-2-skull-cemetery\|(Lv 2) Skull Cemetery (field 128)]] |
| **Level** | 2 |
| **Gear tier dropped** | T1 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Banner** | `UI/FieldImages/2.png` |
| **c17 (unknown)** | 2003 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 3 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 5 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/673-dark-knight-skull|Dark Knight Skull]] (main)
- [[wiki/monsters/809-dark-knight-skull|Dark Knight Skull]] (other id in the guides' list; *client* variant)
- [[wiki/monsters/1205-dark-knight-skull|Dark Knight Skull]] (other id in the guides' list; *client* variant)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1930-essence-of-darkness|essence of Darkness]], [[wiki/items/2702-skull-horn|Skull Horn]], [[wiki/items/2752-the-dark-knight-s-sealed-weapon|The Dark Knight.'s Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/814-topaz|Topaz]], [[wiki/items/804-blue-bloodstone|Blue bloodstone]], [[wiki/items/822-rosemary|Rosemary]], [[wiki/items/824-jasmine|Jasmine]]. Positions on the [[wiki/fields/128-lv-2-skull-cemetery|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 4, group 1 slot 4, group 2 slot 4

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
