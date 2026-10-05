---
title: "Firepillar Plain"
type: "field"
id: 36
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 36", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 36"]
name_key: "FieldName_36"
kind: "land"
scene_type: 2
max_users: 30
group: 6
neighbours: [34, 38, 37]
zones: [57]
segments: ["ZP16_03"]
worldmap_rect: [754, 756, 864, 818]
gates:
  - {"gate": 442, "x": 4225.84, "z": 943.46, "to_gate": 460, "to_field": 34, "label": "FieldName_36"}
  - {"gate": 471, "x": 4144.76, "z": 825.28, "to_gate": 461, "to_field": 37, "label": "FieldName_36"}
  - {"gate": 480, "x": 4274.82, "z": 834.92, "to_gate": 462, "to_field": 38, "label": "FieldName_36"}
connections:
  - {"to": 34, "gate": 442, "to_gate": 460}
  - {"to": 37, "gate": 471, "to_gate": 461}
  - {"to": 38, "gate": 480, "to_gate": 462}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=6a1a46 type=7a94db id=fc074d sources=29936b name_key=155dc1 kind=8e3535 scene_type=da4b92 max_users=22d200 group=c1dfd9 neighbours=4ed7de zones=404a1a segments=128f5b worldmap_rect=841786 gates=c29fe3 connections=16833c npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 57](wiki/assets/zones/57.png) |
| **Field id** | `36` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 6 (SceneList last column) |
| **Zones** | [[wiki/zones/57-field-36-firepillar-plain\|Field 36 (Firepillar Plain)]] |
| **Terrain segments** | `ZP16_03` |
| **World-map rectangle** | `[754, 756, 864, 818]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_36` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 442 | 4225.84, 943.46 | [[wiki/fields/34-skymist-lake\|Skymist Lake]] | 460 | FieldName_36 |
| 471 | 4144.76, 825.28 | [[wiki/fields/37-turncoat-place\|Turncoat Place]] | 461 | FieldName_36 |
| 480 | 4274.82, 834.92 | [[wiki/fields/38-angry-river-lower-region\|Angry River - Lower Region]] | 462 | FieldName_36 |

Entered from: [[wiki/fields/34-skymist-lake|Skymist Lake]] (gate 460 → 442), [[wiki/fields/37-turncoat-place|Turncoat Place]] (gate 461 → 471), [[wiki/fields/38-angry-river-lower-region|Angry River - Lower Region]] (gate 462 → 480)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/34-skymist-lake|Skymist Lake]], [[wiki/fields/38-angry-river-lower-region|Angry River - Lower Region]], [[wiki/fields/37-turncoat-place|Turncoat Place]]

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
| ZP16_03 | yes | yes |
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
