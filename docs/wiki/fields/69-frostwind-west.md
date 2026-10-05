---
title: "Frostwind - West"
type: "field"
id: 69
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 69", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 69"]
name_key: "FieldName_69"
kind: "land"
scene_type: 2
max_users: 30
group: 2
scene_c4: 1
neighbours: [65, 66, 68]
zones: [84]
segments: ["ZP09_05"]
worldmap_rect: [1484, 619, 1550, 661]
gates:
  - {"gate": 751, "x": 2476.72, "z": 1437.82, "to_gate": 790, "to_field": 65, "label": "FieldName_69"}
  - {"gate": 762, "x": 2348.5, "z": 1374.09, "to_gate": 791, "to_field": 66, "label": "FieldName_69"}
  - {"gate": 781, "x": 2475.51, "z": 1331.22, "to_gate": 792, "to_field": 68, "label": "FieldName_69"}
connections:
  - {"to": 65, "gate": 751, "to_gate": 790}
  - {"to": 66, "gate": 762, "to_gate": 791}
  - {"to": 68, "gate": 781, "to_gate": 792}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=b2e617 type=7a94db id=a72b20 sources=3588d2 name_key=544202 kind=8e3535 scene_type=da4b92 max_users=22d200 group=da4b92 scene_c4=356a19 neighbours=551e17 zones=8cfff9 segments=b0bb9f worldmap_rect=b067ae gates=d127e8 connections=f10827 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 84](../assets/zones/84.png) |
| **Field id** | `69` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 2 (SceneList last column) |
| **Zones** | [[wiki/zones/84-field-69-frostwind-west\|Field 69 (Frostwind - West)]] |
| **Terrain segments** | `ZP09_05` |
| **World-map rectangle** | `[1484, 619, 1550, 661]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_69` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 751 | 2476.72, 1437.82 | [[wiki/fields/65-canyon-of-earth\|Canyon of Earth]] | 790 | FieldName_69 |
| 762 | 2348.5, 1374.09 | [[wiki/fields/66-earth-of-abyss\|Earth of Abyss]] | 791 | FieldName_69 |
| 781 | 2475.51, 1331.22 | [[wiki/fields/68-frostwind-east\|Frostwind - East]] | 792 | FieldName_69 |

Entered from: [[wiki/fields/65-canyon-of-earth|Canyon of Earth]] (gate 790 → 751), [[wiki/fields/66-earth-of-abyss|Earth of Abyss]] (gate 791 → 762), [[wiki/fields/68-frostwind-east|Frostwind - East]] (gate 792 → 781)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/65-canyon-of-earth|Canyon of Earth]], [[wiki/fields/66-earth-of-abyss|Earth of Abyss]], [[wiki/fields/68-frostwind-east|Frostwind - East]]

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
| ZP09_05 | yes | yes |
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
