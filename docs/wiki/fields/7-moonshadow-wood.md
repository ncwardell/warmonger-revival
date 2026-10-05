---
title: "Moonshadow Wood"
type: "field"
id: 7
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 7", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 7"]
name_key: "FieldName_7"
kind: "land"
scene_type: 2
max_users: 30
group: 7
scene_c4: 1
neighbours: [4, 9, 10]
zones: [35]
segments: ["ZP07_02"]
worldmap_rect: [867, 161, 942, 218]
gates:
  - {"gate": 141, "x": 1931.08, "z": 712.79, "to_gate": 170, "to_field": 4, "label": "FieldName_7"}
  - {"gate": 190, "x": 1872.94, "z": 602.98, "to_gate": 171, "to_field": 9, "label": "FieldName_7"}
  - {"gate": 200, "x": 1970.26, "z": 613.69, "to_gate": 172, "to_field": 10, "label": "FieldName_7"}
connections:
  - {"to": 4, "gate": 141, "to_gate": 170}
  - {"to": 9, "gate": 190, "to_gate": 171}
  - {"to": 10, "gate": 200, "to_gate": 172}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=e97cb0 type=7a94db id=902ba3 sources=6e0a2b name_key=d210d4 kind=8e3535 scene_type=da4b92 max_users=22d200 group=902ba3 scene_c4=356a19 neighbours=c3af13 zones=5c3c3a segments=405cb5 worldmap_rect=e83163 gates=2f2fa0 connections=af8757 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 35](wiki/assets/zones/35.png) |
| **Field id** | `7` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 7 (SceneList last column) |
| **Zones** | [[wiki/zones/35-field-07-moonshadow-wood\|Field 07 (Moonshadow Wood)]] |
| **Terrain segments** | `ZP07_02` |
| **World-map rectangle** | `[867, 161, 942, 218]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_7` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 141 | 1931.08, 712.79 | [[wiki/fields/4-enter-of-shadewood\|Enter of Shadewood]] | 170 | FieldName_7 |
| 190 | 1872.94, 602.98 | [[wiki/fields/9-thornsbush-peak\|Thornsbush peak]] | 171 | FieldName_7 |
| 200 | 1970.26, 613.69 | [[wiki/fields/10-shaking-earth\|Shaking Earth]] | 172 | FieldName_7 |

Entered from: [[wiki/fields/4-enter-of-shadewood|Enter of Shadewood]] (gate 170 → 141), [[wiki/fields/9-thornsbush-peak|Thornsbush peak]] (gate 171 → 190), [[wiki/fields/10-shaking-earth|Shaking Earth]] (gate 172 → 200)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/4-enter-of-shadewood|Enter of Shadewood]], [[wiki/fields/9-thornsbush-peak|Thornsbush peak]], [[wiki/fields/10-shaking-earth|Shaking Earth]]

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
| ZP07_02 | yes | yes |
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
