---
title: "Thornsbush peak"
type: "field"
id: 9
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 9", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 9"]
name_key: "FieldName_9"
kind: "land"
scene_type: 2
max_users: 30
group: 7
scene_c4: 2
neighbours: [7, 15]
zones: [17]
segments: ["ZP09_02"]
worldmap_rect: [853, 268, 895, 321]
gates:
  - {"gate": 171, "x": 2471.89, "z": 686.04, "to_gate": 190, "to_field": 7, "label": "FieldName_9"}
  - {"gate": 250, "x": 2389.71, "z": 596.43, "to_gate": 191, "to_field": 15, "label": "FieldName_9"}
connections:
  - {"to": 7, "gate": 171, "to_gate": 190}
  - {"to": 15, "gate": 250, "to_gate": 191}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=d391ec type=7a94db id=0ade7c sources=317625 name_key=21fdf5 kind=8e3535 scene_type=da4b92 max_users=22d200 group=902ba3 scene_c4=da4b92 neighbours=4bfd7a zones=79d296 segments=44c6fd worldmap_rect=997c77 gates=0fc6f9 connections=65750d npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 17](../assets/zones/17.png) |
| **Field id** | `9` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 7 (SceneList last column) |
| **Zones** | [[wiki/zones/17-field-09-thornsbush-peak\|Field 09 (Thornsbush peak)]] |
| **Terrain segments** | `ZP09_02` |
| **World-map rectangle** | `[853, 268, 895, 321]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_9` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 171 | 2471.89, 686.04 | [[wiki/fields/7-moonshadow-wood\|Moonshadow Wood]] | 190 | FieldName_9 |
| 250 | 2389.71, 596.43 | [[wiki/fields/15-twisting-valley\|Twisting Valley]] | 191 | FieldName_9 |

Entered from: [[wiki/fields/7-moonshadow-wood|Moonshadow Wood]] (gate 190 → 171), [[wiki/fields/15-twisting-valley|Twisting Valley]] (gate 191 → 250)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/7-moonshadow-wood|Moonshadow Wood]], [[wiki/fields/15-twisting-valley|Twisting Valley]]

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
| ZP09_02 | yes | yes |

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
