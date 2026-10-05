---
title: "Frostwind - East"
type: "field"
id: 68
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 68", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 68"]
name_key: "FieldName_68"
kind: "land"
scene_type: 2
max_users: 30
group: 2
scene_c4: 2
neighbours: [67, 69, 70]
zones: [83]
segments: ["ZP08_05"]
worldmap_rect: [1566, 593, 1679, 674]
gates:
  - {"gate": 772, "x": 2225.03, "z": 1343.04, "to_gate": 780, "to_field": 67, "label": "FieldName_68"}
  - {"gate": 792, "x": 2093.1, "z": 1344.07, "to_gate": 781, "to_field": 69, "label": "FieldName_68"}
  - {"gate": 800, "x": 2167.02, "z": 1444.19, "to_gate": 782, "to_field": 70, "label": "FieldName_68"}
connections:
  - {"to": 67, "gate": 772, "to_gate": 780}
  - {"to": 69, "gate": 792, "to_gate": 781}
  - {"to": 70, "gate": 800, "to_gate": 782}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=729c1b type=7a94db id=b4c96d sources=9e0052 name_key=247885 kind=8e3535 scene_type=da4b92 max_users=22d200 group=da4b92 scene_c4=da4b92 neighbours=5a2319 zones=e6a935 segments=bf9970 worldmap_rect=29a8ba gates=4a55ac connections=11893c npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 83](../assets/zones/83.png) |
| **Field id** | `68` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 2 (SceneList last column) |
| **Zones** | [[wiki/zones/83-field-68-frostwind-east\|Field 68 (Frostwind - East)]] |
| **Terrain segments** | `ZP08_05` |
| **World-map rectangle** | `[1566, 593, 1679, 674]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_68` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 772 | 2225.03, 1343.04 | [[wiki/fields/67-icethorn-plain\|Icethorn Plain]] | 780 | FieldName_68 |
| 792 | 2093.1, 1344.07 | [[wiki/fields/69-frostwind-west\|Frostwind - West]] | 781 | FieldName_68 |
| 800 | 2167.02, 1444.19 | [[wiki/fields/70-cold-breath\|Cold Breath]] | 782 | FieldName_68 |

Entered from: [[wiki/fields/67-icethorn-plain|Icethorn Plain]] (gate 780 → 772), [[wiki/fields/69-frostwind-west|Frostwind - West]] (gate 781 → 792), [[wiki/fields/70-cold-breath|Cold Breath]] (gate 782 → 800)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/67-icethorn-plain|Icethorn Plain]], [[wiki/fields/69-frostwind-west|Frostwind - West]], [[wiki/fields/70-cold-breath|Cold Breath]]

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
| ZP08_05 | yes | yes |
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
