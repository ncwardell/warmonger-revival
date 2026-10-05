---
title: "End of Earth"
type: "field"
id: 1
status: "partial"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 1", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 1", "guide: [[gameplay/maps-and-dungeons]] §3 (event dungeons seen here); image: [[gameplay/lords-of-the-land]] §6 (Oct 2016 ownership snapshot)"]
name_key: "FieldName_1"
kind: "land"
scene_type: 2
max_users: 30
group: 1
scene_c4: 1
neighbours: [2, 5]
zones: [14]
segments: ["ZP01_02"]
worldmap_rect: [544, 85, 650, 183]
gates:
  - {"gate": 120, "x": 436.77, "z": 675.76, "to_gate": 110, "to_field": 2, "label": "FieldName_1"}
  - {"gate": 150, "x": 322.09, "z": 557.4, "to_gate": 111, "to_field": 5, "label": "FieldName_1"}
connections:
  - {"to": 2, "gate": 120, "to_gate": 110}
  - {"to": 5, "gate": 150, "to_gate": 111}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=a9033f type=7a94db id=356a19 sources=6909bc name_key=3432dd kind=8e3535 scene_type=da4b92 max_users=22d200 group=356a19 scene_c4=356a19 neighbours=991fa4 zones=76cdc5 segments=6ad877 worldmap_rect=50a6fc gates=b0b06d connections=41622c npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 14](wiki/assets/zones/14.png) |
| **Field id** | `1` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 1 (SceneList last column) |
| **Zones** | [[wiki/zones/14-field-01-end-of-earth\|Field 01 (End of Earth)]] |
| **Terrain segments** | `ZP01_02` |
| **World-map rectangle** | `[544, 85, 650, 183]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_1` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 120 | 436.77, 675.76 | [[wiki/fields/2-exit-of-shadewood\|Exit of Shadewood]] | 110 | FieldName_1 |
| 150 | 322.09, 557.4 | [[wiki/fields/5-fall-of-abyss\|Fall of Abyss]] | 111 | FieldName_1 |

Entered from: [[wiki/fields/2-exit-of-shadewood|Exit of Shadewood]] (gate 110 → 120), [[wiki/fields/5-fall-of-abyss|Fall of Abyss]] (gate 111 → 150)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/2-exit-of-shadewood|Exit of Shadewood]], [[wiki/fields/5-fall-of-abyss|Fall of Abyss]]

### NPCs

None known yet.

### Monsters

None known yet.

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP01_02 | yes | yes |

### Mentioned in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
<!-- generated:end -->

## Notes

- Event dungeons Place for Scattered Troops and Gollam Hill were seen opening on this land ([[gameplay/maps-and-dungeons|Maps and dungeons]] §3). *guide*
- On the October 2016 Crush world map (Erion's view) this land was in the brown NPC-held block on the west ([[gameplay/lords-of-the-land|Lords of the Land]] §6). *image*

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
