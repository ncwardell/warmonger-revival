---
title: "Angry River - Lower Region"
type: "field"
id: 38
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 38", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 38"]
name_key: "FieldName_38"
kind: "land"
scene_type: 2
max_users: 30
group: 6
scene_c4: 2
neighbours: [36, 39]
zones: [58]
segments: ["ZP18_03"]
worldmap_rect: [881, 712, 960, 793]
gates:
  - {"gate": 462, "x": 4672.39, "z": 814.48, "to_gate": 480, "to_field": 36, "label": "FieldName_38"}
  - {"gate": 491, "x": 4767.74, "z": 947.98, "to_gate": 481, "to_field": 39, "label": "FieldName_38"}
connections:
  - {"to": 36, "gate": 462, "to_gate": 480}
  - {"to": 39, "gate": 491, "to_gate": 481}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=1e52e5 type=7a94db id=5b384c sources=0de86a name_key=365ae1 kind=8e3535 scene_type=da4b92 max_users=22d200 group=c1dfd9 scene_c4=da4b92 neighbours=f71f81 zones=5719a7 segments=e65663 worldmap_rect=780b54 gates=3d9c12 connections=0a672e npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 58](../assets/zones/58.png) |
| **Field id** | `38` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 6 (SceneList last column) |
| **Zones** | [[wiki/zones/58-field-38-angry-river-lower-region\|Field 38 (Angry River - Lower Region)]] |
| **Terrain segments** | `ZP18_03` |
| **World-map rectangle** | `[881, 712, 960, 793]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_38` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 462 | 4672.39, 814.48 | [[wiki/fields/36-firepillar-plain\|Firepillar Plain]] | 480 | FieldName_38 |
| 491 | 4767.74, 947.98 | [[wiki/fields/39-sunstone-gateway\|Sunstone gateway]] | 481 | FieldName_38 |

Entered from: [[wiki/fields/36-firepillar-plain|Firepillar Plain]] (gate 480 → 462), [[wiki/fields/39-sunstone-gateway|Sunstone gateway]] (gate 481 → 491)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/36-firepillar-plain|Firepillar Plain]], [[wiki/fields/39-sunstone-gateway|Sunstone gateway]]

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
| ZP18_03 | yes | yes |

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
