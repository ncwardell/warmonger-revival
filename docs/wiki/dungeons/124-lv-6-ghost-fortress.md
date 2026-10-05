---
title: "[Lv 6] Ghost Fortress"
type: "dungeon"
id: 124
status: "complete"
missing: []
sources: ["client: SceneList.cdb id 124", "client: DungeonAdmission.cdb field 124", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 124", "doc: gameplay/video-dungeon-run §5 (Crush Online 2016 video: the instance timer counts down from 20:00)"]
field: 124
max_users: 5
level: 6
entry_cost:
  - {"mode": "normal", "item": 688, "count": 8}
  - {"mode": "hard", "item": 688, "count": 12}
event: false
shown_rewards: [612, 693, 694, 1934, 2705, 2755]
c17: 2007
image: "UI/FieldImages/6.png"
dungeon_slots:
  - {"group": 0, "slot": 8}
  - {"group": 1, "slot": 8}
  - {"group": 2, "slot": 8}
boss: [676, 743, 1218]
gear_tier: "T2"
gathering: [808, 818, 820]
time_limit_s: 1200
---
<!-- generated:start -->
<!-- generated-keys: title=6a2ed2 type=3e3f38 id=f38cfe sources=3e10ee field=f38cfe max_users=ac3478 level=c1dfd9 entry_cost=215a89 event=7cb6ef shown_rewards=51a1e7 c17=aca6d6 image=41ca94 dungeon_slots=e54862 boss=d1729a gear_tier=7b5982 gathering=020cf6 time_limit_s=73ee49 -->
|  |  |
|---|---|
|  | ![(Lv 6) Ghost Fortress](../assets/dungeons/124.png) |
| **Field** | [[wiki/fields/124-lv-6-ghost-fortress\|(Lv 6) Ghost Fortress (field 124)]] |
| **Level** | 6 |
| **Gear tier dropped** | T2 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Time limit** | 20 min |
| **Banner** | `UI/FieldImages/6.png` |
| **c17 (unknown)** | 2007 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 8 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 12 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/676-great-summoner-spectre|Great Summoner Spectre]] (main)
- [[wiki/monsters/743-great-summoner-spectre|Great Summoner Spectre]] (other id in the guides' list; *client* variant)
- [[wiki/monsters/1218-great-summoner-spectre|Great Summoner Spectre]] (other id in the guides' list; *client* variant)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/694-gem-stone-yellow|Gem Stone : Yellow]], [[wiki/items/1934-essence-of-earth|Essence of Earth]], [[wiki/items/2705-bone-of-spector|Bone of Spector]], [[wiki/items/2755-the-wizard-spector-s-sealed-weapon|The Wizard Spector's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/808-moonstone|Moonstone]], [[wiki/items/818-lavender|Lavender]], [[wiki/items/820-peppermint|Peppermint]]. Positions on the [[wiki/fields/124-lv-6-ghost-fortress|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 8, group 1 slot 8, group 2 slot 8

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].

### Mentioned in

- [[gameplay/crush-mechanics#9. Dungeons, bosses, farming|Crush Online mechanics from the forum § 9. Dungeons, bosses, farming]]
- [[gameplay/precept-shop#3. Example rolled quest (screenshot)|Precept shop and precept quests § 3. Example rolled quest (screenshot)]]
- [[gameplay/video-dungeon-run#Video notes: Nas Village dungeon run (ZonderCoRe)|Video notes: Nas Village dungeon run (ZonderCoRe) § Video notes: Nas Village dungeon run (ZonderCoRe)]]
- [[gameplay/video-dungeon-run#1. Field id and map|Video notes: Nas Village dungeon run (ZonderCoRe) § 1. Field id and map]]
- [[gameplay/video-dungeon-run#5. Gathering in a dungeon (Crush Online, field 124)|Video notes: Nas Village dungeon run (ZonderCoRe) § 5. Gathering in a dungeon (Crush Online, field 124)]]
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
