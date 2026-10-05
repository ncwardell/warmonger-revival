---
title: "Dark Gateway"
type: "field"
id: 85
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 85", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 85"]
name_key: "FieldName_85"
kind: "land"
scene_type: 2
max_users: 30
group: 6
scene_c4: 1
neighbours: [37, 40]
zones: [99]
segments: ["ZP05_06"]
worldmap_rect: [839, 915, 922, 1010]
gates:
  - {"gate": 472, "x": 1343.91, "z": 1581.79, "to_gate": 950, "to_field": 37, "label": "FieldName_85"}
  - {"gate": 500, "x": 1460.81, "z": 1699.87, "to_gate": 951, "to_field": 40, "label": "FieldName_85"}
connections:
  - {"to": 37, "gate": 472, "to_gate": 950}
  - {"to": 40, "gate": 500, "to_gate": 951}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=6d114d type=7a94db id=135224 sources=a5eb86 name_key=a5f5e9 kind=8e3535 scene_type=da4b92 max_users=22d200 group=c1dfd9 scene_c4=356a19 neighbours=54a726 zones=b99fbc segments=df42c3 worldmap_rect=34b2c0 gates=857bdd connections=93d312 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 99](wiki/assets/zones/99.png) |
| **Field id** | `85` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 6 (SceneList last column) |
| **Zones** | [[wiki/zones/99-field-85-dark-gateway\|Field 85 (Dark Gateway)]] |
| **Terrain segments** | `ZP05_06` |
| **World-map rectangle** | `[839, 915, 922, 1010]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_85` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 472 | 1343.91, 1581.79 | [[wiki/fields/37-turncoat-place\|Turncoat Place]] | 950 | FieldName_85 |
| 500 | 1460.81, 1699.87 | [[wiki/fields/40-angry-river-upper-region\|Angry River - Upper Region]] | 951 | FieldName_85 |

Entered from: [[wiki/fields/37-turncoat-place|Turncoat Place]] (gate 950 → 472), [[wiki/fields/40-angry-river-upper-region|Angry River - Upper Region]] (gate 951 → 500)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/37-turncoat-place|Turncoat Place]], [[wiki/fields/40-angry-river-upper-region|Angry River - Upper Region]]

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
| ZP05_06 | yes | yes |
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
