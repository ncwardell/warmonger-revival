---
title: "Windsong Wood"
type: "field"
id: 20
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 20", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 20"]
name_key: "FieldName_20"
kind: "land"
scene_type: 2
max_users: 30
group: 7
neighbours: [15, 21, 24]
zones: [45]
segments: ["ZP20_02"]
worldmap_rect: [849, 414, 934, 463]
gates:
  - {"gate": 251, "x": 5247.41, "z": 686.98, "to_gate": 300, "to_field": 15, "label": "FieldName_20"}
  - {"gate": 310, "x": 5298.26, "z": 573.81, "to_gate": 301, "to_field": 21, "label": "FieldName_20"}
  - {"gate": 341, "x": 5175.04, "z": 563.37, "to_gate": 302, "to_field": 24, "label": "FieldName_20"}
connections:
  - {"to": 15, "gate": 251, "to_gate": 300}
  - {"to": 21, "gate": 310, "to_gate": 301}
  - {"to": 24, "gate": 341, "to_gate": 302}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=2ea789 type=7a94db id=91032a sources=fbc159 name_key=866a18 kind=8e3535 scene_type=da4b92 max_users=22d200 group=902ba3 neighbours=400211 zones=02fb80 segments=d2c7e3 worldmap_rect=bab870 gates=169267 connections=66409b npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 45](../assets/zones/45.png) |
| **Field id** | `20` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 7 (SceneList last column) |
| **Zones** | [[wiki/zones/45-field-20-windsong-wood\|Field 20 (Windsong Wood)]] |
| **Terrain segments** | `ZP20_02` |
| **World-map rectangle** | `[849, 414, 934, 463]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_20` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 251 | 5247.41, 686.98 | [[wiki/fields/15-twisting-valley\|Twisting Valley]] | 300 | FieldName_20 |
| 310 | 5298.26, 573.81 | [[wiki/fields/21-vortex-plain\|Vortex Plain]] | 301 | FieldName_20 |
| 341 | 5175.04, 563.37 | [[wiki/fields/24-silent-garden\|Silent Garden]] | 302 | FieldName_20 |

Entered from: [[wiki/fields/15-twisting-valley|Twisting Valley]] (gate 300 → 251), [[wiki/fields/21-vortex-plain|Vortex Plain]] (gate 301 → 310), [[wiki/fields/24-silent-garden|Silent Garden]] (gate 302 → 341)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/15-twisting-valley|Twisting Valley]], [[wiki/fields/21-vortex-plain|Vortex Plain]], [[wiki/fields/24-silent-garden|Silent Garden]]

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
| ZP20_02 | yes | yes |
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
