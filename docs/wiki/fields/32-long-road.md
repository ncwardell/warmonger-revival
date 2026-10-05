---
title: "Long Road"
type: "field"
id: 32
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 32", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 32"]
name_key: "FieldName_32"
kind: "land"
scene_type: 2
max_users: 30
group: 8
neighbours: [25, 39, 46]
zones: [22]
segments: ["ZP12_03"]
worldmap_rect: [985, 565, 1058, 634]
gates:
  - {"gate": 351, "x": 3150.17, "z": 944.28, "to_gate": 420, "to_field": 25, "label": "FieldName_32"}
  - {"gate": 490, "x": 3176.63, "z": 847.14, "to_gate": 421, "to_field": 39, "label": "FieldName_32"}
  - {"gate": 561, "x": 3276.86, "z": 957.09, "to_gate": 422, "to_field": 46, "label": "FieldName_32"}
connections:
  - {"to": 25, "gate": 351, "to_gate": 420}
  - {"to": 39, "gate": 490, "to_gate": 421}
  - {"to": 46, "gate": 561, "to_gate": 422}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=fea1f4 type=7a94db id=cb4e52 sources=01d193 name_key=e846c2 kind=8e3535 scene_type=da4b92 max_users=22d200 group=fe5dbb neighbours=bd168e zones=5c6c1d segments=3d3ce5 worldmap_rect=34c430 gates=733c7b connections=4d067e npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 22](../assets/zones/22.png) |
| **Field id** | `32` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 8 (SceneList last column) |
| **Zones** | [[wiki/zones/22-field-32-long-road\|Field 32 (Long Road)]] |
| **Terrain segments** | `ZP12_03` |
| **World-map rectangle** | `[985, 565, 1058, 634]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_32` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 351 | 3150.17, 944.28 | [[wiki/fields/25-mist-wood\|Mist Wood]] | 420 | FieldName_32 |
| 490 | 3176.63, 847.14 | [[wiki/fields/39-sunstone-gateway\|Sunstone gateway]] | 421 | FieldName_32 |
| 561 | 3276.86, 957.09 | [[wiki/fields/46-spider-nest\|Spider Nest]] | 422 | FieldName_32 |

Entered from: [[wiki/fields/25-mist-wood|Mist Wood]] (gate 420 → 351), [[wiki/fields/39-sunstone-gateway|Sunstone gateway]] (gate 421 → 490), [[wiki/fields/46-spider-nest|Spider Nest]] (gate 422 → 561)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/25-mist-wood|Mist Wood]], [[wiki/fields/39-sunstone-gateway|Sunstone gateway]], [[wiki/fields/46-spider-nest|Spider Nest]]

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
| ZP12_03 | yes | yes |

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/skull-artifact-set|Skull artifact set tooltips (Crush Online, Feb 2017)]] (by name)
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
