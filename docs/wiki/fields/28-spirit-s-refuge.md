---
title: "Spirit's Refuge"
type: "field"
id: 28
status: "partial"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 28", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 28", "image + guide: [[gameplay/maps-and-dungeons]] §4 (Holy Thing example)"]
name_key: "FieldName_28"
kind: "land"
scene_type: 2
max_users: 30
group: 9
scene_c4: 1
neighbours: [27, 29, 33]
zones: [51]
segments: ["ZP08_03"]
worldmap_rect: [532, 680, 675, 734]
gates:
  - {"gate": 371, "x": 2089.15, "z": 824.84, "to_gate": 380, "to_field": 27, "label": "FieldName_28"}
  - {"gate": 390, "x": 2160.22, "z": 934.37, "to_gate": 381, "to_field": 29, "label": "FieldName_28"}
  - {"gate": 430, "x": 2228.84, "z": 823.38, "to_gate": 382, "to_field": 33, "label": "FieldName_28"}
connections:
  - {"to": 27, "gate": 371, "to_gate": 380}
  - {"to": 29, "gate": 390, "to_gate": 381}
  - {"to": 33, "gate": 430, "to_gate": 382}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=a8bfe2 type=7a94db id=0a57cb sources=e0a9ab name_key=25386b kind=8e3535 scene_type=da4b92 max_users=22d200 group=0ade7c scene_c4=356a19 neighbours=38a47a zones=c6af6d segments=f66a0c worldmap_rect=8b3f39 gates=7aafa5 connections=3d6475 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 51](../assets/zones/51.png) |
| **Field id** | `28` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 9 (SceneList last column) |
| **Zones** | [[wiki/zones/51-field-28-spirit-s-refuge\|Field 28 (Spirit's Refuge)]] |
| **Terrain segments** | `ZP08_03` |
| **World-map rectangle** | `[532, 680, 675, 734]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_28` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 371 | 2089.15, 824.84 | [[wiki/fields/27-spirit-s-hill\|Spirit's Hill]] | 380 | FieldName_28 |
| 390 | 2160.22, 934.37 | [[wiki/fields/29-spirit-s-temple\|Spirit's Temple]] | 381 | FieldName_28 |
| 430 | 2228.84, 823.38 | [[wiki/fields/33-dreamer-s-refuge\|Dreamer's Refuge]] | 382 | FieldName_28 |

Entered from: [[wiki/fields/27-spirit-s-hill|Spirit's Hill]] (gate 380 → 371), [[wiki/fields/29-spirit-s-temple|Spirit's Temple]] (gate 381 → 390), [[wiki/fields/33-dreamer-s-refuge|Dreamer's Refuge]] (gate 382 → 430)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/27-spirit-s-hill|Spirit's Hill]], [[wiki/fields/29-spirit-s-temple|Spirit's Temple]], [[wiki/fields/33-dreamer-s-refuge|Dreamer's Refuge]]

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
| ZP08_03 | yes | yes |

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
<!-- generated:end -->

## Notes

- Example of a land carrying a "Holy Thing" (blue triangle icon); while grey it could be farmed like a T7/T8 grey land for red or blue T3 fragments ([[gameplay/maps-and-dungeons|Maps and dungeons]] §4). *image + guide*

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
