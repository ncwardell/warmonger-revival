---
title: "Hill of Gollam"
type: "dungeon"
id: 115
status: "partial"
missing: ["boss", "time_limit_s"]
sources: ["client: SceneList.cdb id 115", "client: DungeonAdmission.cdb field 115", "client: Event_Dungeon.cdb"]
field: 115
max_users: 5
entry_cost:
  - {"mode": "normal", "item": 688, "count": 5}
  - {"mode": "hard", "item": 688, "count": 5}
event: true
shown_rewards: []
c17: 2010
schedule:
  - {"from_field": 127, "hour": 12, "minutes": 180, "c2": 1, "c3": 4, "c4": 1}
boss: []
time_limit_s: null
---
<!-- generated:start -->
<!-- generated-keys: title=e984f5 type=3e3f38 id=efa6e4 sources=a50fd1 field=efa6e4 max_users=ac3478 entry_cost=6dc8ea event=5ffe53 shown_rewards=97d170 c17=e22cd4 schedule=d8c18a boss=97d170 time_limit_s=2be88c -->
|  |  |
|---|---|
| **Field** | [[wiki/fields/115-hill-of-gollam\|Hill of Gollam (field 115)]] |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | yes |
| **c17 (unknown)** | 2010 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 5 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 5 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

Not known. Add `boss:` (UnitDB ids) with a source.

### Event schedule

`Event_Dungeon` rows. The `hour` value is the number the world map's event list shows ([[gameplay/video-dungeon-run#6. Event dungeon list (world map, Dungeon tab)|Nas Village run §6]]); what it means is not known.

| hour? | open (min) | row field | c2 | c3 | c4 |
|---|---|---|---|---|---|
| 12 | 180 | 127 | 1 | 4 | 1 |

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].

### Mentioned in

- [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost (Dimensional Energy, item 688)]]
<!-- generated:end -->

## Notes

- Guides call it Gollam Hill (*Hill of Gollam*), seen on the land End of Earth; it drops Red Bloodstone, Diamond, Garnet and Topaz (guides, [[gameplay/maps-and-dungeons]] §3).
- The world map's Event Dungeon list shows "Hill of Gollam" with the number 12, which matches this field's `Event_Dungeon` hour value 12 (video + client, [[gameplay/video-dungeon-run]] §6 at [0:03](https://www.youtube.com/watch?v=eL5hx5C9iZw&t=3s)).

## Behaviour

- Event dungeons pop up on random lands of either nation on a schedule; the world map's Dungeon tab lists the active ones and the land they are on (guides, [[gameplay/maps-and-dungeons]] §3).
- Respawn and loot rules of the border-area dungeons apply as far as the guides say (party respawn, shared loot; [[gameplay/maps-and-dungeons]] §2).

## Sources

- [[gameplay/maps-and-dungeons]] §2–3, [[gameplay/video-dungeon-run]] §6

## Open questions

- Entry cost: client 5 / 5 Dimensional Energy (normal / hard); the 2018 guide table and Warmonger patch 0726 give 5 / 10 ([[gameplay/maps-and-dungeons]] §2; [[gameplay/patch-history]] § Dungeons and world). The client value is used.
- No source names a boss or shows a time limit for this dungeon.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
