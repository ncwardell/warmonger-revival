---
title: "Thunderstorm Ruin - Abaddon"
type: "field"
id: 76
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 76", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 76"]
name_key: "FieldName_76"
kind: "land"
scene_type: 2
max_users: 30
group: 5
scene_c4: 2
neighbours: [75, 77]
zones: [30]
segments: ["ZP16_05"]
worldmap_rect: [1583, 372, 1675, 445]
gates:
  - {"gate": 851, "x": 4139.63, "z": 1402.73, "to_gate": 860, "to_field": 75, "label": "FieldName_76"}
  - {"gate": 853, "x": 4261.12, "z": 1345.79, "to_gate": 856, "to_field": 76, "label": "FiledPortal"}
  - {"gate": 854, "x": 4282.6, "z": 1307.1, "to_gate": 857, "to_field": 76, "label": "FiledPortal"}
  - {"gate": 855, "x": 4303.45, "z": 1315.05, "to_gate": 858, "to_field": 76, "label": "FiledPortal"}
  - {"gate": 856, "x": 4208.98, "z": 1454.63, "to_gate": 853, "to_field": 76, "label": "FiledPortal"}
  - {"gate": 857, "x": 4188.51, "z": 1389.92, "to_gate": 854, "to_field": 76, "label": "FiledPortal"}
  - {"gate": 858, "x": 4234.5, "z": 1394.26, "to_gate": 855, "to_field": 76, "label": "FiledPortal"}
  - {"gate": 871, "x": 4252.52, "z": 1470.35, "to_gate": 861, "to_field": 77, "label": "FieldName_76"}
connections:
  - {"to": 75, "gate": 851, "to_gate": 860}
  - {"to": 77, "gate": 871, "to_gate": 861}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=1c9361 type=7a94db id=d54ad0 sources=529088 name_key=90d2d5 kind=8e3535 scene_type=da4b92 max_users=22d200 group=ac3478 scene_c4=da4b92 neighbours=10f98b zones=82d3dd segments=b40a87 worldmap_rect=6e85d6 gates=8422e2 connections=6a4fbd npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 30](wiki/assets/zones/30.png) |
| **Field id** | `76` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 5 (SceneList last column) |
| **Zones** | [[wiki/zones/30-field-76-thunderstorm-ruin-abaddon\|Field 76 (Thunderstorm Ruin - Abaddon)]] |
| **Terrain segments** | `ZP16_05` |
| **World-map rectangle** | `[1583, 372, 1675, 445]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_76` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 851 | 4139.63, 1402.73 | [[wiki/fields/75-thunderstorm-ruin-abyss\|Thunderstorm Ruin - Abyss]] | 860 | FieldName_76 |
| 853 | 4261.12, 1345.79 | portal to gate 856 in this field | 856 | FiledPortal |
| 854 | 4282.6, 1307.1 | portal to gate 857 in this field | 857 | FiledPortal |
| 855 | 4303.45, 1315.05 | portal to gate 858 in this field | 858 | FiledPortal |
| 856 | 4208.98, 1454.63 | portal to gate 853 in this field | 853 | FiledPortal |
| 857 | 4188.51, 1389.92 | portal to gate 854 in this field | 854 | FiledPortal |
| 858 | 4234.5, 1394.26 | portal to gate 855 in this field | 855 | FiledPortal |
| 871 | 4252.52, 1470.35 | [[wiki/fields/77-sandairvalley\|SandairValley]] | 861 | FieldName_76 |

Entered from: [[wiki/fields/75-thunderstorm-ruin-abyss|Thunderstorm Ruin - Abyss]] (gate 860 → 851), [[wiki/fields/77-sandairvalley|SandairValley]] (gate 861 → 871)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/75-thunderstorm-ruin-abyss|Thunderstorm Ruin - Abyss]], [[wiki/fields/77-sandairvalley|SandairValley]]

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
| ZP16_05 | yes | yes |

### Mentioned in

- [[gameplay/sources|Sources and gaps]] (by name)
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
