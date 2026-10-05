---
title: "Sunstone Temple"
type: "field"
id: 44
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 44", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 44"]
name_key: "FieldName_44"
kind: "land"
scene_type: 2
max_users: 30
group: 4
scene_c4: 2
neighbours: [41, 45]
zones: [63]
segments: ["ZP04_04"]
worldmap_rect: [1007, 722, 1114, 776]
gates:
  - {"gate": 512, "x": 1195.96, "z": 1104.8, "to_gate": 540, "to_field": 41, "label": "FieldName_44"}
  - {"gate": 551, "x": 1081.99, "z": 1216.98, "to_gate": 492, "to_field": 45, "label": "FieldName_44"}
connections:
  - {"to": 41, "gate": 512, "to_gate": 540}
  - {"to": 45, "gate": 551, "to_gate": 492}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=b94bf7 type=7a94db id=98fbc4 sources=77bb0c name_key=d7ae48 kind=8e3535 scene_type=da4b92 max_users=22d200 group=1b6453 scene_c4=da4b92 neighbours=780b70 zones=c04d62 segments=5bbc63 worldmap_rect=d836d3 gates=80e17c connections=57fdb6 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 63](../assets/zones/63.png) |
| **Field id** | `44` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 4 (SceneList last column) |
| **Zones** | [[wiki/zones/63-field-44-sunstone-temple\|Field 44 (Sunstone Temple)]] |
| **Terrain segments** | `ZP04_04` |
| **World-map rectangle** | `[1007, 722, 1114, 776]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_44` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 512 | 1195.96, 1104.8 | [[wiki/fields/41-enter-of-twilight\|Enter of Twilight]] | 540 | FieldName_44 |
| 551 | 1081.99, 1216.98 | [[wiki/fields/45-sunstone-hill\|Sunstone Hill]] | 492 | FieldName_44 |

Entered from: [[wiki/fields/41-enter-of-twilight|Enter of Twilight]] (gate 540 → 512), [[wiki/fields/45-sunstone-hill|Sunstone Hill]] (gate 492 → 551)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/41-enter-of-twilight|Enter of Twilight]], [[wiki/fields/45-sunstone-hill|Sunstone Hill]]

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
| ZP04_04 | yes | yes |
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
