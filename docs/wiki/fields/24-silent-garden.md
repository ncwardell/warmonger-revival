---
title: "Silent Garden"
type: "field"
id: 24
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 24", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 24"]
name_key: "FieldName_24"
kind: "land"
scene_type: 2
max_users: 30
group: 9
scene_c4: 1
neighbours: [19, 20, 30]
zones: [49]
segments: ["ZP04_03"]
worldmap_rect: [826, 467, 884, 534]
gates:
  - {"gate": 292, "x": 1086.09, "z": 970.72, "to_gate": 340, "to_field": 19, "label": "FieldName_24"}
  - {"gate": 302, "x": 1198.73, "z": 872.17, "to_gate": 341, "to_field": 20, "label": "FieldName_24"}
  - {"gate": 400, "x": 1103.9, "z": 848.82, "to_gate": 342, "to_field": 30, "label": "FieldName_24"}
connections:
  - {"to": 19, "gate": 292, "to_gate": 340}
  - {"to": 20, "gate": 302, "to_gate": 341}
  - {"to": 30, "gate": 400, "to_gate": 342}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=b8b028 type=7a94db id=4d134b sources=a3f5bf name_key=8e0137 kind=8e3535 scene_type=da4b92 max_users=22d200 group=0ade7c scene_c4=356a19 neighbours=dbc604 zones=3915bb segments=e76530 worldmap_rect=98ec90 gates=93e9a5 connections=a58481 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 49](wiki/assets/zones/49.png) |
| **Field id** | `24` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 9 (SceneList last column) |
| **Zones** | [[wiki/zones/49-field-24-silent-garden\|Field 24 (Silent Garden)]] |
| **Terrain segments** | `ZP04_03` |
| **World-map rectangle** | `[826, 467, 884, 534]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_24` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 292 | 1086.09, 970.72 | [[wiki/fields/19-death-valley\|Death Valley]] | 340 | FieldName_24 |
| 302 | 1198.73, 872.17 | [[wiki/fields/20-windsong-wood\|Windsong Wood]] | 341 | FieldName_24 |
| 400 | 1103.9, 848.82 | [[wiki/fields/30-wind-valley\|Wind Valley]] | 342 | FieldName_24 |

Entered from: [[wiki/fields/19-death-valley|Death Valley]] (gate 340 → 292), [[wiki/fields/20-windsong-wood|Windsong Wood]] (gate 341 → 302), [[wiki/fields/30-wind-valley|Wind Valley]] (gate 342 → 400)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/19-death-valley|Death Valley]], [[wiki/fields/20-windsong-wood|Windsong Wood]], [[wiki/fields/30-wind-valley|Wind Valley]]

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
| ZP04_03 | yes | yes |
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
