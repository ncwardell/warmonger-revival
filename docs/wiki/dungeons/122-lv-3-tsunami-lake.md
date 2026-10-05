---
title: "[Lv 3] Tsunami Lake"
type: "dungeon"
id: 122
status: "stub"
missing: ["time_limit_s"]
sources: ["client: SceneList.cdb id 122", "client: DungeonAdmission.cdb field 122", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 122"]
field: 122
max_users: 5
level: 3
entry_cost:
  - {"mode": "normal", "item": 688, "count": 5}
  - {"mode": "hard", "item": 688, "count": 5}
event: false
shown_rewards: [612, 602, 693, 1933, 2703, 2753]
c17: 2004
image: "UI/FieldImages/3.png"
dungeon_slots:
  - {"group": 0, "slot": 5}
  - {"group": 1, "slot": 5}
  - {"group": 2, "slot": 5}
boss: [674, 733, 1209]
gear_tier: "T1"
gathering: [814, 804, 822, 824]
time_limit_s: null
---
<!-- generated:start -->
<!-- generated-keys: title=a1b133 type=3e3f38 id=05a8ea sources=462a80 field=05a8ea max_users=ac3478 level=77de68 entry_cost=6dc8ea event=7cb6ef shown_rewards=8750e7 c17=667e62 image=2f6ead dungeon_slots=d63727 boss=a4d2f8 gear_tier=13930c gathering=83d28e time_limit_s=2be88c -->
|  |  |
|---|---|
|  | ![(Lv 3) Tsunami Lake](../assets/dungeons/122.png) |
| **Field** | [[wiki/fields/122-lv-3-tsunami-lake\|(Lv 3) Tsunami Lake (field 122)]] |
| **Level** | 3 |
| **Gear tier dropped** | T1 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Banner** | `UI/FieldImages/3.png` |
| **c17 (unknown)** | 2004 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 5 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 5 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/674-tempest-fisher|Tempest Fisher]] (main)
- [[wiki/monsters/733-tempest-fisher|Tempest Fisher]] (other id in the guides' list; *client* variant)
- [[wiki/monsters/1209-tempest-fisher|Tempest Fisher]] (other id in the guides' list; *client* variant)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/602-blue-passion-piece-d|Blue Passion Piece (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1933-essence-of-water|Essence of Water]], [[wiki/items/2703-fin-of-fisher|Fin of Fisher]], [[wiki/items/2753-the-tempest-fisher-s-sealed-weapon|The Tempest Fisher's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/814-topaz|Topaz]], [[wiki/items/804-blue-bloodstone|Blue bloodstone]], [[wiki/items/822-rosemary|Rosemary]], [[wiki/items/824-jasmine|Jasmine]]. Positions on the [[wiki/fields/122-lv-3-tsunami-lake|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 5, group 1 slot 5, group 2 slot 5

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
