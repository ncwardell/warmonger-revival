---
title: "SandairValley"
type: "field"
id: 77
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 77", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 77"]
name_key: "FieldName_77"
kind: "land"
scene_type: 2
max_users: 30
group: 5
scene_c4: 1
neighbours: [75, 76, 83]
zones: [90]
segments: ["ZP17_05"]
worldmap_rect: [1625, 296, 1747, 374]
gates:
  - {"gate": 852, "x": 4425.55, "z": 1328.6, "to_gate": 870, "to_field": 75, "label": "FieldName_77"}
  - {"gate": 861, "x": 4505.85, "z": 1342.76, "to_gate": 871, "to_field": 76, "label": "FieldName_77"}
  - {"gate": 930, "x": 4530.22, "z": 1433.53, "to_gate": 872, "to_field": 83, "label": "FieldName_77"}
connections:
  - {"to": 75, "gate": 852, "to_gate": 870}
  - {"to": 76, "gate": 861, "to_gate": 871}
  - {"to": 83, "gate": 930, "to_gate": 872}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=8e54e2 type=7a94db id=d321d6 sources=9be3e9 name_key=d85b35 kind=8e3535 scene_type=da4b92 max_users=22d200 group=ac3478 scene_c4=356a19 neighbours=f6604a zones=1aa4a6 segments=16d4d9 worldmap_rect=b9821a gates=f3c7ac connections=bbc353 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 90](wiki/assets/zones/90.png) |
| **Field id** | `77` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 5 (SceneList last column) |
| **Zones** | [[wiki/zones/90-field-77-sandairvalley\|Field 77 (SandairValley)]] |
| **Terrain segments** | `ZP17_05` |
| **World-map rectangle** | `[1625, 296, 1747, 374]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_77` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 852 | 4425.55, 1328.6 | [[wiki/fields/75-thunderstorm-ruin-abyss\|Thunderstorm Ruin - Abyss]] | 870 | FieldName_77 |
| 861 | 4505.85, 1342.76 | [[wiki/fields/76-thunderstorm-ruin-abaddon\|Thunderstorm Ruin - Abaddon]] | 871 | FieldName_77 |
| 930 | 4530.22, 1433.53 | [[wiki/fields/83-moonlight-plain-east\|Moonlight Plain - East]] | 872 | FieldName_77 |

Entered from: [[wiki/fields/75-thunderstorm-ruin-abyss|Thunderstorm Ruin - Abyss]] (gate 870 → 852), [[wiki/fields/76-thunderstorm-ruin-abaddon|Thunderstorm Ruin - Abaddon]] (gate 871 → 861), [[wiki/fields/83-moonlight-plain-east|Moonlight Plain - East]] (gate 872 → 930)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/75-thunderstorm-ruin-abyss|Thunderstorm Ruin - Abyss]], [[wiki/fields/76-thunderstorm-ruin-abaddon|Thunderstorm Ruin - Abaddon]], [[wiki/fields/83-moonlight-plain-east|Moonlight Plain - East]]

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
| ZP17_05 | yes | yes |
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
