---
title: "Skymist Lake"
type: "field"
id: 34
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 34", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 34"]
name_key: "FieldName_34"
kind: "land"
scene_type: 2
max_users: 30
group: 3
neighbours: [33, 36, 31]
zones: [56]
segments: ["ZP14_03"]
worldmap_rect: [774, 662, 865, 722]
gates:
  - {"gate": 412, "x": 3742.02, "z": 942.9, "to_gate": 440, "to_field": 31, "label": "FieldName_34"}
  - {"gate": 431, "x": 3627.43, "z": 830.48, "to_gate": 441, "to_field": 33, "label": "FieldName_34"}
  - {"gate": 460, "x": 3761.07, "z": 833.82, "to_gate": 442, "to_field": 36, "label": "FieldName_34"}
connections:
  - {"to": 31, "gate": 412, "to_gate": 440}
  - {"to": 33, "gate": 431, "to_gate": 441}
  - {"to": 36, "gate": 460, "to_gate": 442}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=24d1c4 type=7a94db id=f1f836 sources=a472b7 name_key=c5f8fd kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 neighbours=7c11db zones=584499 segments=57c2a0 worldmap_rect=db3619 gates=4a9a3f connections=04e467 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 56](../assets/zones/56.png) |
| **Field id** | `34` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/56-field-34-skymist-lake\|Field 34 (Skymist Lake)]] |
| **Terrain segments** | `ZP14_03` |
| **World-map rectangle** | `[774, 662, 865, 722]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_34` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 412 | 3742.02, 942.9 | [[wiki/fields/31-mist-lake\|Mist Lake]] | 440 | FieldName_34 |
| 431 | 3627.43, 830.48 | [[wiki/fields/33-dreamer-s-refuge\|Dreamer's Refuge]] | 441 | FieldName_34 |
| 460 | 3761.07, 833.82 | [[wiki/fields/36-firepillar-plain\|Firepillar Plain]] | 442 | FieldName_34 |

Entered from: [[wiki/fields/31-mist-lake|Mist Lake]] (gate 440 → 412), [[wiki/fields/33-dreamer-s-refuge|Dreamer's Refuge]] (gate 441 → 431), [[wiki/fields/36-firepillar-plain|Firepillar Plain]] (gate 442 → 460)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/33-dreamer-s-refuge|Dreamer's Refuge]], [[wiki/fields/36-firepillar-plain|Firepillar Plain]], [[wiki/fields/31-mist-lake|Mist Lake]]

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
| ZP14_03 | yes | yes |
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
