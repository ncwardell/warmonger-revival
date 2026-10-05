---
title: "Thunderstorm Ruin - Abyss"
type: "field"
id: 75
status: "partial"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 75", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 75", "guess: [[gameplay/maps-and-dungeons]] §1"]
name_key: "FieldName_75"
kind: "land"
scene_type: 2
max_users: 30
group: 5
neighbours: [71, 76, 77]
zones: [29]
segments: ["ZP15_05"]
worldmap_rect: [1516, 295, 1585, 386]
gates:
  - {"gate": 812, "x": 3896.64, "z": 1444.54, "to_gate": 850, "to_field": 71, "label": "FieldName_75"}
  - {"gate": 860, "x": 4015.33, "z": 1338.09, "to_gate": 851, "to_field": 76, "label": "FieldName_75"}
  - {"gate": 870, "x": 4000.71, "z": 1450.59, "to_gate": 852, "to_field": 77, "label": "FieldName_75"}
connections:
  - {"to": 71, "gate": 812, "to_gate": 850}
  - {"to": 76, "gate": 860, "to_gate": 851}
  - {"to": 77, "gate": 870, "to_gate": 852}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=f9ff7b type=7a94db id=450dde sources=ede226 name_key=e95179 kind=8e3535 scene_type=da4b92 max_users=22d200 group=ac3478 neighbours=388a40 zones=f7cf3c segments=f5c0e3 worldmap_rect=8a39c3 gates=9b3b20 connections=67d34a npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 29](wiki/assets/zones/29.png) |
| **Field id** | `75` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 5 (SceneList last column) |
| **Zones** | [[wiki/zones/29-field-75-thunderstorm-ruin-abyss\|Field 75 (Thunderstorm Ruin - Abyss)]] |
| **Terrain segments** | `ZP15_05` |
| **World-map rectangle** | `[1516, 295, 1585, 386]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_75` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 812 | 3896.64, 1444.54 | [[wiki/fields/71-thunderstorm-door\|Thunderstorm door]] | 850 | FieldName_75 |
| 860 | 4015.33, 1338.09 | [[wiki/fields/76-thunderstorm-ruin-abaddon\|Thunderstorm Ruin - Abaddon]] | 851 | FieldName_75 |
| 870 | 4000.71, 1450.59 | [[wiki/fields/77-sandairvalley\|SandairValley]] | 852 | FieldName_75 |

Entered from: [[wiki/fields/71-thunderstorm-door|Thunderstorm door]] (gate 850 → 812), [[wiki/fields/76-thunderstorm-ruin-abaddon|Thunderstorm Ruin - Abaddon]] (gate 851 → 860), [[wiki/fields/77-sandairvalley|SandairValley]] (gate 852 → 870)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/71-thunderstorm-door|Thunderstorm door]], [[wiki/fields/76-thunderstorm-ruin-abaddon|Thunderstorm Ruin - Abaddon]], [[wiki/fields/77-sandairvalley|SandairValley]]

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
| ZP15_05 | yes | yes |

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
<!-- generated:end -->

## Notes

- A Gaia land despite its name; not part of the Abyss farming area ([[gameplay/maps-and-dungeons|Maps and dungeons]] §1, *guess*).

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
