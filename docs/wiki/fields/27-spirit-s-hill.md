---
title: "Spirit's Hill"
type: "field"
id: 27
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 27", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 27"]
name_key: "FieldName_27"
kind: "land"
scene_type: 2
max_users: 30
group: 9
scene_c4: 2
neighbours: [23, 28]
zones: [50]
segments: ["ZP07_03"]
worldmap_rect: [528, 559, 650, 644]
gates:
  - {"gate": 331, "x": 1971.28, "z": 934.87, "to_gate": 370, "to_field": 23, "label": "FieldName_27"}
  - {"gate": 380, "x": 1835.56, "z": 824.22, "to_gate": 371, "to_field": 28, "label": "FieldName_27"}
connections:
  - {"to": 23, "gate": 331, "to_gate": 370}
  - {"to": 28, "gate": 380, "to_gate": 371}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=5a96c0 type=7a94db id=bc33ea sources=1da657 name_key=959b60 kind=8e3535 scene_type=da4b92 max_users=22d200 group=0ade7c scene_c4=da4b92 neighbours=689e62 zones=d59264 segments=308920 worldmap_rect=7a6a4e gates=eb3d19 connections=85a50d npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 50](../assets/zones/50.png) |
| **Field id** | `27` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 9 (SceneList last column) |
| **Zones** | [[wiki/zones/50-field-27-spirit-s-hill\|Field 27 (Spirit's Hill)]] |
| **Terrain segments** | `ZP07_03` |
| **World-map rectangle** | `[528, 559, 650, 644]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_27` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 331 | 1971.28, 934.87 | [[wiki/fields/23-fairy-s-wood\|Fairy's Wood]] | 370 | FieldName_27 |
| 380 | 1835.56, 824.22 | [[wiki/fields/28-spirit-s-refuge\|Spirit's Refuge]] | 371 | FieldName_27 |

Entered from: [[wiki/fields/23-fairy-s-wood|Fairy's Wood]] (gate 370 → 331), [[wiki/fields/28-spirit-s-refuge|Spirit's Refuge]] (gate 371 → 380)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/23-fairy-s-wood|Fairy's Wood]], [[wiki/fields/28-spirit-s-refuge|Spirit's Refuge]]

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
| ZP07_03 | yes | yes |

### Mentioned in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]] (by name)
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
