---
title: "Death's Rest"
type: "dungeon"
id: 135
status: "partial"
missing: ["boss", "time_limit_s"]
sources: ["client: SceneList.cdb id 135", "client: DungeonAdmission.cdb field 135", "client: Event_Dungeon.cdb"]
field: 135
max_users: 5
entry_cost:
  - {"mode": "normal", "item": 688, "count": 5}
  - {"mode": "hard", "item": 688, "count": 15}
event: true
shown_rewards: []
c17: 2014
schedule:
  - {"from_field": 127, "hour": 24, "minutes": 80, "c2": 1, "c3": 2, "c4": 2}
boss: []
time_limit_s: null
---
<!-- generated:start -->
<!-- generated-keys: title=5991de type=3e3f38 id=40f7c0 sources=910787 field=40f7c0 max_users=ac3478 entry_cost=fca843 event=5ffe53 shown_rewards=97d170 c17=39e214 schedule=feb453 boss=97d170 time_limit_s=2be88c -->
|  |  |
|---|---|
| **Field** | [[wiki/fields/135-death-s-rest\|Death's Rest (field 135)]] |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | yes |
| **c17 (unknown)** | 2014 |

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
| 24 | 80 | 127 | 1 | 2 | 2 |

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].
<!-- generated:end -->

## Notes

- The world map's Event Dungeon list shows "The avenue of spirit" with the number 24, which only this field's `Event_Dungeon` row has, so 135 is the guides' **Avenue of Spirit** event dungeon even though the client names the field "Death's Rest" (video + client, [[gameplay/video-dungeon-run]] §6 at [0:03](https://www.youtube.com/watch?v=eL5hx5C9iZw&t=3s)).
- Guides: seen on Skywing Yard; drops Orange Passion T1, Yellow and Red crystals, T2 Red/Blue Passion (guides, [[gameplay/maps-and-dungeons]] §3).
- Warmonger patch 0412 opened Scattered Troops and Avenue of Spirit to both nations (notes, [[gameplay/patch-history]] § Dungeons and world).

## Behaviour

- Event dungeons pop up on random lands of either nation on a schedule; the world map's Dungeon tab lists the active ones and the land they are on (guides, [[gameplay/maps-and-dungeons]] §3).
- Respawn and loot rules of the border-area dungeons apply as far as the guides say (party respawn, shared loot; [[gameplay/maps-and-dungeons]] §2).

## Sources

- [[gameplay/video-dungeon-run]] §6, [[gameplay/maps-and-dungeons]] §2–3, [[gameplay/patch-history]] § Dungeons and world

## Open questions

- Entry cost: client 5 / 15 Dimensional Energy; guides 5 normal and 20 hard (spring 2018: 5 + 3 bronze Time Energy) ([[gameplay/maps-and-dungeons]] §2). The client value is used.
- Name: the client calls field 135 "Death's Rest", the in-game event list "The avenue of spirit" ([[gameplay/video-dungeon-run]] §6).
- No source names a boss or a time limit; the `Event_Dungeon` window is 80 minutes (client).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
