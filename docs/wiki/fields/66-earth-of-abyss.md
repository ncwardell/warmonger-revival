---
title: "Earth of Abyss"
type: "field"
id: 66
status: "partial"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 66", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 66", "guess: [[gameplay/maps-and-dungeons]] §1"]
name_key: "FieldName_66"
kind: "land"
scene_type: 2
max_users: 30
group: 2
neighbours: [57, 67, 69]
zones: [28]
segments: ["ZP06_05"]
worldmap_rect: [1430, 668, 1495, 718]
gates:
  - {"gate": 672, "x": 1585.72, "z": 1343.72, "to_gate": 760, "to_field": 57, "label": "FieldName_66"}
  - {"gate": 771, "x": 1704.14, "z": 1443.95, "to_gate": 761, "to_field": 67, "label": "FieldName_66"}
  - {"gate": 791, "x": 1593.26, "z": 1449.73, "to_gate": 762, "to_field": 69, "label": "FieldName_66"}
connections:
  - {"to": 57, "gate": 672, "to_gate": 760}
  - {"to": 67, "gate": 771, "to_gate": 761}
  - {"to": 69, "gate": 791, "to_gate": 762}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=79cc2d type=7a94db id=59129a sources=f1e946 name_key=24c014 kind=8e3535 scene_type=da4b92 max_users=22d200 group=da4b92 neighbours=eddb79 zones=e90c00 segments=5cd95b worldmap_rect=e89342 gates=2b8e31 connections=0166c2 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 28](../assets/zones/28.png) |
| **Field id** | `66` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 2 (SceneList last column) |
| **Zones** | [[wiki/zones/28-field-66-earth-of-abyss\|Field 66 (Earth of Abyss)]] |
| **Terrain segments** | `ZP06_05` |
| **World-map rectangle** | `[1430, 668, 1495, 718]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_66` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 672 | 1585.72, 1343.72 | [[wiki/fields/57-raging-wind\|Raging Wind]] | 760 | FieldName_66 |
| 771 | 1704.14, 1443.95 | [[wiki/fields/67-icethorn-plain\|Icethorn Plain]] | 761 | FieldName_66 |
| 791 | 1593.26, 1449.73 | [[wiki/fields/69-frostwind-west\|Frostwind - West]] | 762 | FieldName_66 |

Entered from: [[wiki/fields/57-raging-wind|Raging Wind]] (gate 760 → 672), [[wiki/fields/67-icethorn-plain|Icethorn Plain]] (gate 761 → 771), [[wiki/fields/69-frostwind-west|Frostwind - West]] (gate 762 → 791)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/57-raging-wind|Raging Wind]], [[wiki/fields/67-icethorn-plain|Icethorn Plain]], [[wiki/fields/69-frostwind-west|Frostwind - West]]

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
| ZP06_05 | yes | yes |

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
<!-- generated:end -->

## Notes

- A Gaia land despite its name; not part of the Abyss farming area ([[gameplay/maps-and-dungeons|Maps and dungeons]] §1, *guess*).

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
