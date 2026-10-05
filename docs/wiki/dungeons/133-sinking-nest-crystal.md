---
title: "Sinking Nest (Crystal)"
type: "dungeon"
id: 133
status: "stub"
missing: ["boss"]
sources: ["client: SceneList.cdb id 133", "client: DungeonAdmission.cdb field 133", "client: Event_Dungeon.cdb", "client: GUI_FieldIDX_133 \"Time limit : 3 hours\" (entry-panel text)"]
field: 133
max_users: 100
entry_cost:
  - {"mode": "normal", "item": 688, "count": 4}
  - {"mode": "hard", "item": 688, "count": 4}
event: true
shown_rewards: [700, 701, 702, 693, 694, 695]
c17: 2012
image: "UI/FieldImages/52.png"
notice_key: "GUI_FieldIDX_133"
schedule:
  - {"from_field": 127, "hour": 12, "minutes": 180, "c2": 1, "c3": 4, "c4": 2}
boss: []
time_limit_s: 10800
---
<!-- generated:start -->
<!-- generated-keys: title=7f851f type=3e3f38 id=d30f79 sources=46748f field=d30f79 max_users=310b86 entry_cost=70723b event=5ffe53 shown_rewards=f62141 c17=084b3a image=34756c notice_key=87226b schedule=803f37 boss=97d170 time_limit_s=1d5529 -->
|  |  |
|---|---|
|  | ![Sinking Nest (Crystal)](wiki/assets/dungeons/133.png) |
| **Field** | [[wiki/fields/133-sinking-nest-crystal\|Sinking Nest (Crystal) (field 133)]] |
| **Max players** | 100 (SceneList) |
| **Event dungeon** | yes |
| **Time limit** | 180 min |
| **Panel notice** | Time limit : 3 hours (`GUI_FieldIDX_133`) |
| **Banner** | `UI/FieldImages/52.png` |
| **c17 (unknown)** | 2012 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 4 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 4 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

Not known. Add `boss:` (UnitDB ids) with a source.

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/700-crystal-blue|Crystal : Blue]], [[wiki/items/701-crystal-yellow|Crystal : Yellow]], [[wiki/items/702-crystal-red|Crystal : Red]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/694-gem-stone-yellow|Gem Stone : Yellow]], [[wiki/items/695-gem-stone-red|Gem Stone : Red]]

### Event schedule

`Event_Dungeon` rows. The `hour` value is the number the world map's event list shows ([[gameplay/video-dungeon-run#6. Event dungeon list (world map, Dungeon tab)|Nas Village run §6]]); what it means is not known.

| hour? | open (min) | row field | c2 | c3 | c4 |
|---|---|---|---|---|---|
| 12 | 180 | 127 | 1 | 4 | 2 |

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].

### Mentioned in

- [[gameplay/patch-history#Dungeons and world|Patch notes and other sources § Dungeons and world]]
- [[gameplay/server-rules#Added from the Warmonger forum and videos (round 2)|Server rules checklist § Added from the Warmonger forum and videos (round 2)]]
- [[gameplay/video-dungeon-run#2. Pack positions (field 133)|Video notes: Nas Village dungeon run (ZonderCoRe) § 2. Pack positions (field 133)]]
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
