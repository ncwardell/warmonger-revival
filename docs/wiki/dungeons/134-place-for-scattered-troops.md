---
title: "Place for Scattered troops"
type: "dungeon"
id: 134
status: "stub"
missing: ["boss", "time_limit_s"]
sources: ["client: SceneList.cdb id 134", "client: DungeonAdmission.cdb field 134", "client: Event_Dungeon.cdb"]
field: 134
max_users: 5
entry_cost:
  - {"mode": "normal", "item": 688, "count": 5}
  - {"mode": "hard", "item": 688, "count": 15}
event: true
shown_rewards: []
c17: 2013
schedule:
  - {"from_field": 127, "hour": 21, "minutes": 80, "c2": 1, "c3": 2, "c4": 1}
boss: []
time_limit_s: null
---
<!-- generated:start -->
<!-- generated-keys: title=48ad72 type=3e3f38 id=95e815 sources=09075b field=95e815 max_users=ac3478 entry_cost=fca843 event=5ffe53 shown_rewards=97d170 c17=d08b10 schedule=29f4fc boss=97d170 time_limit_s=2be88c -->
|  |  |
|---|---|
| **Field** | [[wiki/fields/134-place-for-scattered-troops\|Place for Scattered troops (field 134)]] |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | yes |
| **c17 (unknown)** | 2013 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 5 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 15 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

Not known. Add `boss:` (UnitDB ids) with a source.

### Event schedule

`Event_Dungeon` rows. The `hour` value is the number the world map's event list shows ([[gameplay/video-dungeon-run#6. Event dungeon list (world map, Dungeon tab)|Nas Village run §6]]); what it means is not known.

| hour? | open (min) | row field | c2 | c3 | c4 |
|---|---|---|---|---|---|
| 21 | 80 | 127 | 1 | 2 | 1 |

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
