---
title: "Eternal River - Middle Region"
type: "field"
id: 17
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 17", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 17"]
name_key: "FieldName_17"
kind: "land"
scene_type: 2
max_users: 30
group: 7
scene_c4: 2
neighbours: [12, 18, 23]
zones: [42]
segments: ["ZP17_02"]
worldmap_rect: [621, 456, 706, 516]
gates:
  - {"gate": 222, "x": 4414.97, "z": 683.27, "to_gate": 270, "to_field": 12, "label": "FieldName_17"}
  - {"gate": 280, "x": 4533.9, "z": 676.57, "to_gate": 271, "to_field": 18, "label": "FieldName_17"}
  - {"gate": 330, "x": 4537.91, "z": 567.88, "to_gate": 272, "to_field": 23, "label": "FieldName_17"}
connections:
  - {"to": 12, "gate": 222, "to_gate": 270}
  - {"to": 18, "gate": 280, "to_gate": 271}
  - {"to": 23, "gate": 330, "to_gate": 272}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=2002fa type=7a94db id=0716d9 sources=370880 name_key=5da2df kind=8e3535 scene_type=da4b92 max_users=22d200 group=902ba3 scene_c4=da4b92 neighbours=1f2856 zones=54c441 segments=55a079 worldmap_rect=85fe3d gates=44a3da connections=9b06b5 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 42](wiki/assets/zones/42.png) |
| **Field id** | `17` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 7 (SceneList last column) |
| **Zones** | [[wiki/zones/42-field-17-eternal-river-middle-region\|Field 17 (Eternal River - Middle Region)]] |
| **Terrain segments** | `ZP17_02` |
| **World-map rectangle** | `[621, 456, 706, 516]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_17` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 222 | 4414.97, 683.27 | [[wiki/fields/12-dark-shore\|Dark Shore]] | 270 | FieldName_17 |
| 280 | 4533.9, 676.57 | [[wiki/fields/18-eternal-river-lower-region\|Eternal River - Lower Region]] | 271 | FieldName_17 |
| 330 | 4537.91, 567.88 | [[wiki/fields/23-fairy-s-wood\|Fairy's Wood]] | 272 | FieldName_17 |

Entered from: [[wiki/fields/12-dark-shore|Dark Shore]] (gate 270 → 222), [[wiki/fields/18-eternal-river-lower-region|Eternal River - Lower Region]] (gate 271 → 280), [[wiki/fields/23-fairy-s-wood|Fairy's Wood]] (gate 272 → 330)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/12-dark-shore|Dark Shore]], [[wiki/fields/18-eternal-river-lower-region|Eternal River - Lower Region]], [[wiki/fields/23-fairy-s-wood|Fairy's Wood]]

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
| ZP17_02 | yes | yes |
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
