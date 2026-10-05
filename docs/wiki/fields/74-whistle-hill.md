---
title: "Whistle Hill"
type: "field"
id: 74
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 74", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 74"]
name_key: "FieldName_74"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 2
neighbours: [73, 80]
zones: [13]
segments: ["ZP14_05"]
worldmap_rect: [1325, 238, 1402, 275]
gates:
  - {"gate": 832, "x": 3634.5, "z": 1358.85, "to_gate": 840, "to_field": 73, "label": "FieldName_74"}
  - {"gate": 900, "x": 3740.98, "z": 1437.27, "to_gate": 841, "to_field": 80, "label": "FieldName_74"}
connections:
  - {"to": 73, "gate": 832, "to_gate": 840}
  - {"to": 80, "gate": 900, "to_gate": 841}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=ef3241 type=7a94db id=1f1362 sources=44011f name_key=a89d2a kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=da4b92 neighbours=4c88c6 zones=758a13 segments=24b770 worldmap_rect=c085eb gates=7b0a48 connections=71bbee npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 13](wiki/assets/zones/13.png) |
| **Field id** | `74` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/13-field-74-whistle-hill\|Field 74 (Whistle Hill)]] |
| **Terrain segments** | `ZP14_05` |
| **World-map rectangle** | `[1325, 238, 1402, 275]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_74` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 832 | 3634.5, 1358.85 | [[wiki/fields/73-left-ground\|Left Ground]] | 840 | FieldName_74 |
| 900 | 3740.98, 1437.27 | [[wiki/fields/80-windmist-valley\|Windmist Valley]] | 841 | FieldName_74 |

Entered from: [[wiki/fields/73-left-ground|Left Ground]] (gate 840 → 832), [[wiki/fields/80-windmist-valley|Windmist Valley]] (gate 841 → 900)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/73-left-ground|Left Ground]], [[wiki/fields/80-windmist-valley|Windmist Valley]]

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
| ZP14_05 | yes | yes |
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
