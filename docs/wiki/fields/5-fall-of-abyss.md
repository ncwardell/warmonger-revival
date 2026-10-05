---
title: "Fall of Abyss"
type: "field"
id: 5
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 5", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 5"]
name_key: "FieldName_5"
kind: "land"
scene_type: 2
max_users: 30
group: 1
scene_c4: 2
neighbours: [1, 8, 6]
zones: [16]
segments: ["ZP05_02"]
worldmap_rect: [648, 183, 759, 230]
gates:
  - {"gate": 111, "x": 1348.1, "z": 682.8, "to_gate": 150, "to_field": 1, "label": "FieldName_5"}
  - {"gate": 162, "x": 1457.83, "z": 611.49, "to_gate": 151, "to_field": 6, "label": "FieldName_5"}
  - {"gate": 180, "x": 1326.05, "z": 572.65, "to_gate": 152, "to_field": 8, "label": "FieldName_5"}
connections:
  - {"to": 1, "gate": 111, "to_gate": 150}
  - {"to": 6, "gate": 162, "to_gate": 151}
  - {"to": 8, "gate": 180, "to_gate": 152}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=612a53 type=7a94db id=ac3478 sources=2b8c96 name_key=4f1ded kind=8e3535 scene_type=da4b92 max_users=22d200 group=356a19 scene_c4=da4b92 neighbours=e9c432 zones=504845 segments=7af869 worldmap_rect=2cb5ec gates=54b700 connections=7c3426 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 16](wiki/assets/zones/16.png) |
| **Field id** | `5` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 1 (SceneList last column) |
| **Zones** | [[wiki/zones/16-field-05-fall-of-abyss\|Field 05 (Fall of Abyss)]] |
| **Terrain segments** | `ZP05_02` |
| **World-map rectangle** | `[648, 183, 759, 230]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_5` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 111 | 1348.1, 682.8 | [[wiki/fields/1-end-of-earth\|End of Earth]] | 150 | FieldName_5 |
| 162 | 1457.83, 611.49 | [[wiki/fields/6-skywing-yard\|Skywing Yard]] | 151 | FieldName_5 |
| 180 | 1326.05, 572.65 | [[wiki/fields/8-long-canyon\|Long Canyon]] | 152 | FieldName_5 |

Entered from: [[wiki/fields/1-end-of-earth|End of Earth]] (gate 150 → 111), [[wiki/fields/6-skywing-yard|Skywing Yard]] (gate 151 → 162), [[wiki/fields/8-long-canyon|Long Canyon]] (gate 152 → 180)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/1-end-of-earth|End of Earth]], [[wiki/fields/8-long-canyon|Long Canyon]], [[wiki/fields/6-skywing-yard|Skywing Yard]]

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
| ZP05_02 | yes | yes |

### Mentioned in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]] (by name)
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
