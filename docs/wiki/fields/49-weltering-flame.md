---
title: "Weltering Flame"
type: "field"
id: 49
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 49", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 49"]
name_key: "FieldName_49"
kind: "land"
scene_type: 2
max_users: 30
group: 6
scene_c4: 2
neighbours: [45, 50, 59]
zones: [67]
segments: ["ZP09_04"]
worldmap_rect: [1184, 586, 1257, 638]
gates:
  - {"gate": 552, "x": 2360.92, "z": 1214.16, "to_gate": 590, "to_field": 45, "label": "FieldName_49"}
  - {"gate": 600, "x": 2377.91, "z": 1107.91, "to_gate": 591, "to_field": 50, "label": "FieldName_49"}
  - {"gate": 690, "x": 2469.89, "z": 1207.62, "to_gate": 592, "to_field": 59, "label": "FieldName_49"}
connections:
  - {"to": 45, "gate": 552, "to_gate": 590}
  - {"to": 50, "gate": 600, "to_gate": 591}
  - {"to": 59, "gate": 690, "to_gate": 592}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=9632a6 type=7a94db id=2e01e1 sources=9a25de name_key=f2f96a kind=8e3535 scene_type=da4b92 max_users=22d200 group=c1dfd9 scene_c4=da4b92 neighbours=a5bac5 zones=3bc09d segments=417e8a worldmap_rect=e664a1 gates=d4dbff connections=29d22a npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 67](../assets/zones/67.png) |
| **Field id** | `49` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 6 (SceneList last column) |
| **Zones** | [[wiki/zones/67-field-49-weltering-flame\|Field 49 (Weltering Flame)]] |
| **Terrain segments** | `ZP09_04` |
| **World-map rectangle** | `[1184, 586, 1257, 638]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_49` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 552 | 2360.92, 1214.16 | [[wiki/fields/45-sunstone-hill\|Sunstone Hill]] | 590 | FieldName_49 |
| 600 | 2377.91, 1107.91 | [[wiki/fields/50-eclipsed-road\|Eclipsed Road]] | 591 | FieldName_49 |
| 690 | 2469.89, 1207.62 | [[wiki/fields/59-fire-spirit\|Fire Spirit]] | 592 | FieldName_49 |

Entered from: [[wiki/fields/45-sunstone-hill|Sunstone Hill]] (gate 590 → 552), [[wiki/fields/50-eclipsed-road|Eclipsed Road]] (gate 591 → 600), [[wiki/fields/59-fire-spirit|Fire Spirit]] (gate 592 → 690)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/45-sunstone-hill|Sunstone Hill]], [[wiki/fields/50-eclipsed-road|Eclipsed Road]], [[wiki/fields/59-fire-spirit|Fire Spirit]]

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
| ZP09_04 | yes | yes |
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
