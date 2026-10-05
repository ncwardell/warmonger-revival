---
title: "Ashes Ruin"
type: "field"
id: 48
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 48", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 48"]
name_key: "FieldName_48"
kind: "land"
scene_type: 2
max_users: 30
group: 6
scene_c4: 1
neighbours: [46, 47, 60]
zones: [66]
segments: ["ZP08_04"]
worldmap_rect: [1172, 524, 1231, 569]
gates:
  - {"gate": 562, "x": 2134.33, "z": 1100.21, "to_gate": 580, "to_field": 46, "label": "FieldName_48"}
  - {"gate": 571, "x": 2186.82, "z": 1231.97, "to_gate": 581, "to_field": 47, "label": "FieldName_48"}
  - {"gate": 700, "x": 2221.84, "z": 1104.77, "to_gate": 582, "to_field": 60, "label": "FieldName_48"}
connections:
  - {"to": 46, "gate": 562, "to_gate": 580}
  - {"to": 47, "gate": 571, "to_gate": 581}
  - {"to": 60, "gate": 700, "to_gate": 582}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=c45f8f type=7a94db id=64e095 sources=2149f1 name_key=bdb81a kind=8e3535 scene_type=da4b92 max_users=22d200 group=c1dfd9 scene_c4=356a19 neighbours=f1b4b5 zones=09000c segments=241cc3 worldmap_rect=49a40c gates=4ff2db connections=935003 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 66](wiki/assets/zones/66.png) |
| **Field id** | `48` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 6 (SceneList last column) |
| **Zones** | [[wiki/zones/66-field-48-ashes-ruin\|Field 48 (Ashes Ruin)]] |
| **Terrain segments** | `ZP08_04` |
| **World-map rectangle** | `[1172, 524, 1231, 569]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_48` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 562 | 2134.33, 1100.21 | [[wiki/fields/46-spider-nest\|Spider Nest]] | 580 | FieldName_48 |
| 571 | 2186.82, 1231.97 | [[wiki/fields/47-burning-earth\|Burning Earth]] | 581 | FieldName_48 |
| 700 | 2221.84, 1104.77 | [[wiki/fields/60-volcano-heart\|Volcano Heart]] | 582 | FieldName_48 |

Entered from: [[wiki/fields/46-spider-nest|Spider Nest]] (gate 580 → 562), [[wiki/fields/47-burning-earth|Burning Earth]] (gate 581 → 571), [[wiki/fields/60-volcano-heart|Volcano Heart]] (gate 582 → 700)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/46-spider-nest|Spider Nest]], [[wiki/fields/47-burning-earth|Burning Earth]], [[wiki/fields/60-volcano-heart|Volcano Heart]]

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
| ZP08_04 | yes | yes |
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
