---
title: "Sunstone gateway"
type: "field"
id: 39
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 39", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 39"]
name_key: "FieldName_39"
kind: "land"
scene_type: 2
max_users: 30
group: 8
scene_c4: 1
neighbours: [32, 38, 45]
zones: [31]
segments: ["ZP19_03"]
worldmap_rect: [950, 659, 1037, 728]
gates:
  - {"gate": 421, "x": 4932.25, "z": 941.07, "to_gate": 490, "to_field": 32, "label": "FieldName_39"}
  - {"gate": 481, "x": 4910.97, "z": 820.95, "to_gate": 491, "to_field": 38, "label": "FieldName_39"}
  - {"gate": 550, "x": 5040.23, "z": 941.03, "to_gate": 541, "to_field": 45, "label": "FieldName_39"}
connections:
  - {"to": 32, "gate": 421, "to_gate": 490}
  - {"to": 38, "gate": 481, "to_gate": 491}
  - {"to": 45, "gate": 550, "to_gate": 541}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=f24ebd type=7a94db id=ca3512 sources=00ab26 name_key=e51bac kind=8e3535 scene_type=da4b92 max_users=22d200 group=fe5dbb scene_c4=356a19 neighbours=b417f8 zones=2dfe62 segments=0a2f9d worldmap_rect=f63e30 gates=af713d connections=7d0ec3 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 31](wiki/assets/zones/31.png) |
| **Field id** | `39` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 8 (SceneList last column) |
| **Zones** | [[wiki/zones/31-field-39-sunstone-gateway\|Field 39 (Sunstone gateway)]] |
| **Terrain segments** | `ZP19_03` |
| **World-map rectangle** | `[950, 659, 1037, 728]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_39` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 421 | 4932.25, 941.07 | [[wiki/fields/32-long-road\|Long Road]] | 490 | FieldName_39 |
| 481 | 4910.97, 820.95 | [[wiki/fields/38-angry-river-lower-region\|Angry River - Lower Region]] | 491 | FieldName_39 |
| 550 | 5040.23, 941.03 | [[wiki/fields/45-sunstone-hill\|Sunstone Hill]] | 541 | FieldName_39 |

Entered from: [[wiki/fields/32-long-road|Long Road]] (gate 490 → 421), [[wiki/fields/38-angry-river-lower-region|Angry River - Lower Region]] (gate 491 → 481), [[wiki/fields/45-sunstone-hill|Sunstone Hill]] (gate 541 → 550)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/32-long-road|Long Road]], [[wiki/fields/38-angry-river-lower-region|Angry River - Lower Region]], [[wiki/fields/45-sunstone-hill|Sunstone Hill]]

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
| ZP19_03 | yes | yes |

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
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
