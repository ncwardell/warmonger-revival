---
title: "Twisting Valley"
type: "field"
id: 15
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 15", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 15"]
name_key: "FieldName_15"
kind: "land"
scene_type: 2
max_users: 30
group: 7
scene_c4: 1
neighbours: [9, 20]
zones: [40]
segments: ["ZP15_02"]
worldmap_rect: [863, 331, 927, 388]
gates:
  - {"gate": 191, "x": 3911.82, "z": 699.52, "to_gate": 250, "to_field": 9, "label": "FieldName_15"}
  - {"gate": 300, "x": 4011.43, "z": 593.27, "to_gate": 251, "to_field": 20, "label": "FieldName_15"}
connections:
  - {"to": 9, "gate": 191, "to_gate": 250}
  - {"to": 20, "gate": 300, "to_gate": 251}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=c479c0 type=7a94db id=f1abd6 sources=e7f4c7 name_key=f60347 kind=8e3535 scene_type=da4b92 max_users=22d200 group=902ba3 scene_c4=356a19 neighbours=7b7c99 zones=7b279c segments=debec8 worldmap_rect=9759a6 gates=076949 connections=23239a npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 40](wiki/assets/zones/40.png) |
| **Field id** | `15` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 7 (SceneList last column) |
| **Zones** | [[wiki/zones/40-field-15-twisting-valley\|Field 15 (Twisting Valley)]] |
| **Terrain segments** | `ZP15_02` |
| **World-map rectangle** | `[863, 331, 927, 388]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_15` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 191 | 3911.82, 699.52 | [[wiki/fields/9-thornsbush-peak\|Thornsbush peak]] | 250 | FieldName_15 |
| 300 | 4011.43, 593.27 | [[wiki/fields/20-windsong-wood\|Windsong Wood]] | 251 | FieldName_15 |

Entered from: [[wiki/fields/9-thornsbush-peak|Thornsbush peak]] (gate 250 → 191), [[wiki/fields/20-windsong-wood|Windsong Wood]] (gate 251 → 300)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/9-thornsbush-peak|Thornsbush peak]], [[wiki/fields/20-windsong-wood|Windsong Wood]]

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
| ZP15_02 | yes | yes |
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
