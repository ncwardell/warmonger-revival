---
title: "Burning Earth"
type: "field"
id: 47
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 47", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 47"]
name_key: "FieldName_47"
kind: "land"
scene_type: 2
max_users: 30
group: 6
neighbours: [22, 48, 61]
zones: [65]
segments: ["ZP07_04"]
worldmap_rect: [1134, 398, 1199, 477]
gates:
  - {"gate": 322, "x": 1860.95, "z": 1226.31, "to_gate": 570, "to_field": 22, "label": "FieldName_47"}
  - {"gate": 581, "x": 1920.3, "z": 1098.42, "to_gate": 571, "to_field": 48, "label": "FieldName_47"}
  - {"gate": 710, "x": 1975.87, "z": 1180.02, "to_gate": 572, "to_field": 61, "label": "FieldName_47"}
connections:
  - {"to": 22, "gate": 322, "to_gate": 570}
  - {"to": 48, "gate": 581, "to_gate": 571}
  - {"to": 61, "gate": 710, "to_gate": 572}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=787ea7 type=7a94db id=827bfc sources=d89304 name_key=8b66d3 kind=8e3535 scene_type=da4b92 max_users=22d200 group=c1dfd9 neighbours=62e4a2 zones=cfd5b8 segments=5e2a45 worldmap_rect=fc60ec gates=dd471d connections=59ade6 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 65](../assets/zones/65.png) |
| **Field id** | `47` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 6 (SceneList last column) |
| **Zones** | [[wiki/zones/65-field-47-burning-earth\|Field 47 (Burning Earth)]] |
| **Terrain segments** | `ZP07_04` |
| **World-map rectangle** | `[1134, 398, 1199, 477]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_47` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 322 | 1860.95, 1226.31 | [[wiki/fields/22-afterlife-hill\|Afterlife Hill]] | 570 | FieldName_47 |
| 581 | 1920.3, 1098.42 | [[wiki/fields/48-ashes-ruin\|Ashes Ruin]] | 571 | FieldName_47 |
| 710 | 1975.87, 1180.02 | [[wiki/fields/61-fire-calling\|Fire Calling]] | 572 | FieldName_47 |

Entered from: [[wiki/fields/22-afterlife-hill|Afterlife Hill]] (gate 570 → 322), [[wiki/fields/48-ashes-ruin|Ashes Ruin]] (gate 571 → 581), [[wiki/fields/61-fire-calling|Fire Calling]] (gate 572 → 710)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/22-afterlife-hill|Afterlife Hill]], [[wiki/fields/48-ashes-ruin|Ashes Ruin]], [[wiki/fields/61-fire-calling|Fire Calling]]

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
| ZP07_04 | yes | yes |
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
