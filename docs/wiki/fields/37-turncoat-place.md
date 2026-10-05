---
title: "Turncoat Place"
type: "field"
id: 37
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 37", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 37"]
name_key: "FieldName_37"
kind: "land"
scene_type: 2
max_users: 30
group: 0
scene_c4: 2
neighbours: [35, 36, 85]
zones: [24]
segments: ["ZP17_03"]
worldmap_rect: [726, 846, 826, 907]
gates:
  - {"gate": 451, "x": 4405.35, "z": 924.92, "to_gate": 470, "to_field": 35, "label": "FieldName_37"}
  - {"gate": 461, "x": 4534.69, "z": 932.53, "to_gate": 471, "to_field": 36, "label": "FieldName_37"}
  - {"gate": 950, "x": 4451.93, "z": 815.91, "to_gate": 472, "to_field": 85, "label": "FieldName_37"}
connections:
  - {"to": 35, "gate": 451, "to_gate": 470}
  - {"to": 36, "gate": 461, "to_gate": 471}
  - {"to": 85, "gate": 950, "to_gate": 472}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=9e5156 type=7a94db id=cb7a1d sources=2c221f name_key=231505 kind=8e3535 scene_type=da4b92 max_users=22d200 group=b6589f scene_c4=da4b92 neighbours=8fd743 zones=624df8 segments=c22969 worldmap_rect=64fc71 gates=1a7626 connections=ac4293 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 24](../assets/zones/24.png) |
| **Field id** | `37` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 0 (SceneList last column) |
| **Zones** | [[wiki/zones/24-field-37-turncoat-place\|Field 37 (Turncoat Place)]] |
| **Terrain segments** | `ZP17_03` |
| **World-map rectangle** | `[726, 846, 826, 907]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_37` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 451 | 4405.35, 924.92 | [[wiki/fields/35-skymist-temple\|Skymist Temple]] | 470 | FieldName_37 |
| 461 | 4534.69, 932.53 | [[wiki/fields/36-firepillar-plain\|Firepillar Plain]] | 471 | FieldName_37 |
| 950 | 4451.93, 815.91 | [[wiki/fields/85-dark-gateway\|Dark Gateway]] | 472 | FieldName_37 |

Entered from: [[wiki/fields/35-skymist-temple|Skymist Temple]] (gate 470 → 451), [[wiki/fields/36-firepillar-plain|Firepillar Plain]] (gate 471 → 461), [[wiki/fields/85-dark-gateway|Dark Gateway]] (gate 472 → 950)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/35-skymist-temple|Skymist Temple]], [[wiki/fields/36-firepillar-plain|Firepillar Plain]], [[wiki/fields/85-dark-gateway|Dark Gateway]]

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
| ZP17_03 | yes | yes |
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
