---
title: "[Lv 1] Chepa Village"
type: "dungeon"
id: 127
status: "stub"
missing: ["time_limit_s"]
sources: ["client: SceneList.cdb id 127", "client: DungeonAdmission.cdb field 127", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 127"]
field: 127
max_users: 5
level: 1
entry_cost:
  - {"mode": "normal", "item": 688, "count": 2}
  - {"mode": "hard", "item": 688, "count": 2}
event: false
shown_rewards: [611, 601, 693, 1931, 2709, 2759]
c17: 2001
image: "UI/FieldImages/0.png"
dungeon_slots:
  - {"group": 0, "slot": 1}
  - {"group": 0, "slot": 2}
  - {"group": 1, "slot": 1}
  - {"group": 1, "slot": 2}
  - {"group": 2, "slot": 1}
boss: [870, 950]
gear_tier: "T1"
gathering: [818, 820]
time_limit_s: null
---
<!-- generated:start -->
<!-- generated-keys: title=a46136 type=3e3f38 id=008451 sources=e5a418 field=008451 max_users=ac3478 level=356a19 entry_cost=6d13a2 event=7cb6ef shown_rewards=82c08d c17=9195f8 image=c57209 dungeon_slots=969ce3 boss=00cb4f gear_tier=13930c gathering=3a8b4c time_limit_s=2be88c -->
|  |  |
|---|---|
|  | ![(Lv 1) Chepa Village](wiki/assets/dungeons/127.png) |
| **Field** | [[wiki/fields/127-lv-1-chepa-village\|(Lv 1) Chepa Village (field 127)]] |
| **Level** | 1 |
| **Gear tier dropped** | T1 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Banner** | `UI/FieldImages/0.png` |
| **c17 (unknown)** | 2001 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 2 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 2 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/870-chepa-sorcerer|Chepa Sorcerer]] (main)
- [[wiki/monsters/950-chepa-sorcerer|Chepa Sorcerer]] (other id in the guides' list; *client* variant)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]], [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1931-essence-of-wind|Essence of Wind]], [[wiki/items/2709-drop-of-chepa-sorcerer|Drop of Chepa Sorcerer]], [[wiki/items/2759-the-chepa-sorcerer-s-sealed-weapon|The Chepa Sorcerer's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/818-lavender|Lavender]], [[wiki/items/820-peppermint|Peppermint]]. Positions on the [[wiki/fields/127-lv-1-chepa-village|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 1, group 0 slot 2, group 1 slot 1, group 1 slot 2, group 2 slot 1

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
