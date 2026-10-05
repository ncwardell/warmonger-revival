---
title: "Wind Valley"
type: "field"
id: 30
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 30", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 30"]
name_key: "FieldName_30"
kind: "land"
scene_type: 2
max_users: 30
group: 9
scene_c4: 2
neighbours: [24, 29, 31]
zones: [53]
segments: ["ZP10_03"]
worldmap_rect: [776, 555, 862, 604]
gates:
  - {"gate": 342, "x": 2722.29, "z": 946.5, "to_gate": 400, "to_field": 24, "label": "FieldName_30"}
  - {"gate": 391, "x": 2633.84, "z": 830.02, "to_gate": 401, "to_field": 29, "label": "FieldName_30"}
  - {"gate": 411, "x": 2748.06, "z": 812.76, "to_gate": 402, "to_field": 31, "label": "FieldName_30"}
connections:
  - {"to": 24, "gate": 342, "to_gate": 400}
  - {"to": 29, "gate": 391, "to_gate": 401}
  - {"to": 31, "gate": 411, "to_gate": 402}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=d64ca6 type=7a94db id=22d200 sources=23a632 name_key=c3ef45 kind=8e3535 scene_type=da4b92 max_users=22d200 group=0ade7c scene_c4=da4b92 neighbours=f0d850 zones=ef9592 segments=ae7b5d worldmap_rect=07bc36 gates=0dd824 connections=1899f7 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 53](wiki/assets/zones/53.png) |
| **Field id** | `30` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 9 (SceneList last column) |
| **Zones** | [[wiki/zones/53-field-30-wind-valley\|Field 30 (Wind Valley)]] |
| **Terrain segments** | `ZP10_03` |
| **World-map rectangle** | `[776, 555, 862, 604]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_30` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 342 | 2722.29, 946.5 | [[wiki/fields/24-silent-garden\|Silent Garden]] | 400 | FieldName_30 |
| 391 | 2633.84, 830.02 | [[wiki/fields/29-spirit-s-temple\|Spirit's Temple]] | 401 | FieldName_30 |
| 411 | 2748.06, 812.76 | [[wiki/fields/31-mist-lake\|Mist Lake]] | 402 | FieldName_30 |

Entered from: [[wiki/fields/24-silent-garden|Silent Garden]] (gate 400 → 342), [[wiki/fields/29-spirit-s-temple|Spirit's Temple]] (gate 401 → 391), [[wiki/fields/31-mist-lake|Mist Lake]] (gate 402 → 411)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/24-silent-garden|Silent Garden]], [[wiki/fields/29-spirit-s-temple|Spirit's Temple]], [[wiki/fields/31-mist-lake|Mist Lake]]

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
| ZP10_03 | yes | yes |
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
