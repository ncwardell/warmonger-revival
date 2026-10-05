---
title: "Place for Scattered troops"
type: "dungeon"
id: 134
status: "partial"
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

- The world map's Event Dungeon list shows "Place for Scattered troops" with the number 21, which only this field's `Event_Dungeon` row has, so 134 is the guides' **Place for Scattered Troops** event dungeon (video + client, [[gameplay/video-dungeon-run]] §6 at [0:03](https://www.youtube.com/watch?v=eL5hx5C9iZw&t=3s)).
- Guides: seen on End of Earth; drops Orange Passion T1, Yellow and Blue crystals, T2 Red/Blue and T1 Blue Passion (guides, [[gameplay/maps-and-dungeons]] §3).
- Warmonger patch 0412 opened Scattered Troops and Avenue of Spirit to both nations (notes, [[gameplay/patch-history]] § Dungeons and world).

## Behaviour

- Event dungeons pop up on random lands of either nation on a schedule; the world map's Dungeon tab lists the active ones and the land they are on (guides, [[gameplay/maps-and-dungeons]] §3).
- Respawn and loot rules of the border-area dungeons apply as far as the guides say (party respawn, shared loot; [[gameplay/maps-and-dungeons]] §2).

## Sources

- [[gameplay/video-dungeon-run]] §6, [[gameplay/maps-and-dungeons]] §2–3, [[gameplay/patch-history]] § Dungeons and world

## Open questions

- Entry cost: client 5 / 15 Dimensional Energy; guides 5 normal and 20 hard (spring 2018: 5 + 3 bronze Time Energy) ([[gameplay/maps-and-dungeons]] §2). The client value is used.
- No source names a boss or a time limit; the `Event_Dungeon` window is 80 minutes (client).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
