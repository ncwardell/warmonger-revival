---
title: "Vortex Plain"
type: "field"
id: 21
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 21", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 21"]
name_key: "FieldName_21"
kind: "land"
scene_type: 2
max_users: 30
group: 5
scene_c4: 2
neighbours: [20, 26]
zones: [46]
segments: ["ZP01_03"]
worldmap_rect: [955, 419, 1016, 482]
gates:
  - {"gate": 301, "x": 327.92, "z": 956.35, "to_gate": 310, "to_field": 20, "label": "FieldName_21"}
  - {"gate": 360, "x": 427.51, "z": 849.44, "to_gate": 311, "to_field": 26, "label": "FieldName_21"}
connections:
  - {"to": 20, "gate": 301, "to_gate": 310}
  - {"to": 26, "gate": 360, "to_gate": 311}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=b0d8ee type=7a94db id=472b07 sources=be13f4 name_key=766ea4 kind=8e3535 scene_type=da4b92 max_users=22d200 group=ac3478 scene_c4=da4b92 neighbours=c0de27 zones=10537b segments=c094f9 worldmap_rect=895e82 gates=6ec65b connections=35c2ee npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 46](../assets/zones/46.png) |
| **Field id** | `21` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 5 (SceneList last column) |
| **Zones** | [[wiki/zones/46-field-21-vortex-plain\|Field 21 (Vortex Plain)]] |
| **Terrain segments** | `ZP01_03` |
| **World-map rectangle** | `[955, 419, 1016, 482]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_21` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 301 | 327.92, 956.35 | [[wiki/fields/20-windsong-wood\|Windsong Wood]] | 310 | FieldName_21 |
| 360 | 427.51, 849.44 | [[wiki/fields/26-echo-of-earth\|Echo of Earth]] | 311 | FieldName_21 |

Entered from: [[wiki/fields/20-windsong-wood|Windsong Wood]] (gate 310 → 301), [[wiki/fields/26-echo-of-earth|Echo of Earth]] (gate 311 → 360)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/20-windsong-wood|Windsong Wood]], [[wiki/fields/26-echo-of-earth|Echo of Earth]]

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
| ZP01_03 | yes | yes |
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
