---
title: "[Lv 5] Tow Canyon"
type: "dungeon"
id: 125
status: "stub"
missing: ["time_limit_s"]
sources: ["client: SceneList.cdb id 125", "client: DungeonAdmission.cdb field 125", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 125"]
field: 125
max_users: 5
level: 5
entry_cost:
  - {"mode": "normal", "item": 688, "count": 7}
  - {"mode": "hard", "item": 688, "count": 9}
event: false
shown_rewards: [602, 693, 1935, 2706, 2756]
c17: 2006
image: "UI/FieldImages/5.png"
dungeon_slots:
  - {"group": 0, "slot": 7}
  - {"group": 1, "slot": 7}
  - {"group": 2, "slot": 7}
boss: [677, 822, 1223]
gear_tier: "T2"
gathering: [806, 822, 824]
time_limit_s: null
---
<!-- generated:start -->
<!-- generated-keys: title=0f8440 type=3e3f38 id=0ca927 sources=024730 field=0ca927 max_users=ac3478 level=ac3478 entry_cost=11406a event=7cb6ef shown_rewards=3a1a59 c17=1938b7 image=fe7704 dungeon_slots=01fff0 boss=6d768e gear_tier=7b5982 gathering=0cbe10 time_limit_s=2be88c -->
|  |  |
|---|---|
|  | ![(Lv 5) Tow Canyon](wiki/assets/dungeons/125.png) |
| **Field** | [[wiki/fields/125-lv-5-tow-canyon\|(Lv 5) Tow Canyon (field 125)]] |
| **Level** | 5 |
| **Gear tier dropped** | T2 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Banner** | `UI/FieldImages/5.png` |
| **c17 (unknown)** | 2006 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 7 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 9 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/677-war-chief-garon|War Chief Garon]] (main)
- [[wiki/monsters/822-war-chief-garon|War Chief Garon]] (other id in the guides' list; *client* variant)
- [[wiki/monsters/1223-war-chief-garon|War Chief Garon]] (other id in the guides' list; *client* variant)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/602-blue-passion-piece-d|Blue Passion Piece (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1935-essence-of-light|Essence of Light]], [[wiki/items/2706-horn-of-garon|Horn of Garon]], [[wiki/items/2756-the-war-hammer-garon-s-sealed-weapon|The War hammer Garon's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/806-emerald|Emerald]], [[wiki/items/822-rosemary|Rosemary]], [[wiki/items/824-jasmine|Jasmine]]. Positions on the [[wiki/fields/125-lv-5-tow-canyon|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 7, group 1 slot 7, group 2 slot 7

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].

### Mentioned in

- [[gameplay/crush-mechanics#9. Dungeons, bosses, farming|Crush Online mechanics from the forum § 9. Dungeons, bosses, farming]]
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
