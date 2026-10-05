---
title: "[Lv 7] Demon Hell"
type: "dungeon"
id: 126
status: "stub"
missing: ["time_limit_s"]
sources: ["client: SceneList.cdb id 126", "client: DungeonAdmission.cdb field 126", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 126"]
field: 126
max_users: 5
level: 7
entry_cost:
  - {"mode": "normal", "item": 688, "count": 9}
  - {"mode": "hard", "item": 688, "count": 15}
event: false
shown_rewards: [612, 613, 693, 694, 1935, 2707, 2757]
c17: 2008
image: "UI/FieldImages/7.png"
dungeon_slots:
  - {"group": 0, "slot": 9}
  - {"group": 1, "slot": 9}
  - {"group": 2, "slot": 9}
boss: [678, 740, 739]
gear_tier: "T2"
gathering: [810, 826, 828]
time_limit_s: null
---
<!-- generated:start -->
<!-- generated-keys: title=12597b type=3e3f38 id=114d4e sources=cef1ec field=114d4e max_users=ac3478 level=902ba3 entry_cost=992c16 event=7cb6ef shown_rewards=d3c68f c17=527dc6 image=168686 dungeon_slots=899470 boss=33e996 gear_tier=7b5982 gathering=a8425a time_limit_s=2be88c -->
|  |  |
|---|---|
|  | ![(Lv 7) Demon Hell](wiki/assets/dungeons/126.png) |
| **Field** | [[wiki/fields/126-lv-7-demon-hell\|(Lv 7) Demon Hell (field 126)]] |
| **Level** | 7 |
| **Gear tier dropped** | T2 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Banner** | `UI/FieldImages/7.png` |
| **c17 (unknown)** | 2008 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 9 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 15 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/678-reviatan-shadow|Reviatan Shadow]] (main)
- [[wiki/monsters/740-reviatan-shadow|Reviatan Shadow]] (other id in the guides' list; *client* variant)
- [[wiki/monsters/739-commander-reviatan|Commander Reviatan]] (other id in the guides' list; *client* variant)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/694-gem-stone-yellow|Gem Stone : Yellow]], [[wiki/items/1935-essence-of-light|Essence of Light]], [[wiki/items/2707-horn-of-leviathan|Horn of Leviathan]], [[wiki/items/2757-the-devil-commander-leviathan-s-sealed-weapon|The Devil commander Leviathan's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/810-diamond|Diamond]], [[wiki/items/826-borage|Borage]], [[wiki/items/828-spartium|Spartium]]. Positions on the [[wiki/fields/126-lv-7-demon-hell|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 9, group 1 slot 9, group 2 slot 9

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
