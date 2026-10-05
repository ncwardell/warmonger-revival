---
title: "Cold Breath"
type: "field"
id: 70
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 70", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 70"]
name_key: "FieldName_70"
kind: "land"
scene_type: 2
max_users: 30
group: 2
scene_c4: 2
neighbours: [71, 68]
zones: [85]
segments: ["ZP10_05"]
worldmap_rect: [1475, 518, 1603, 565]
gates:
  - {"gate": 782, "x": 2737.51, "z": 1352.61, "to_gate": 800, "to_field": 68, "label": "FieldName_70"}
  - {"gate": 811, "x": 2612.98, "z": 1437.41, "to_gate": 801, "to_field": 71, "label": "FieldName_70"}
connections:
  - {"to": 68, "gate": 782, "to_gate": 800}
  - {"to": 71, "gate": 811, "to_gate": 801}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=b6fac0 type=7a94db id=b7103c sources=220232 name_key=5d9644 kind=8e3535 scene_type=da4b92 max_users=22d200 group=da4b92 scene_c4=da4b92 neighbours=1ec4da zones=8d17eb segments=98cf56 worldmap_rect=c0673d gates=09c0e9 connections=19f756 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 85](../assets/zones/85.png) |
| **Field id** | `70` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 2 (SceneList last column) |
| **Zones** | [[wiki/zones/85-field-70-cold-breath\|Field 70 (Cold Breath)]] |
| **Terrain segments** | `ZP10_05` |
| **World-map rectangle** | `[1475, 518, 1603, 565]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_70` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 782 | 2737.51, 1352.61 | [[wiki/fields/68-frostwind-east\|Frostwind - East]] | 800 | FieldName_70 |
| 811 | 2612.98, 1437.41 | [[wiki/fields/71-thunderstorm-door\|Thunderstorm door]] | 801 | FieldName_70 |

Entered from: [[wiki/fields/68-frostwind-east|Frostwind - East]] (gate 800 → 782), [[wiki/fields/71-thunderstorm-door|Thunderstorm door]] (gate 801 → 811)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/71-thunderstorm-door|Thunderstorm door]], [[wiki/fields/68-frostwind-east|Frostwind - East]]

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
| ZP10_05 | yes | yes |

### Mentioned in

- [[gameplay/precept-shop#6. Other numbers in the screenshot|Precept shop and precept quests § 6. Other numbers in the screenshot]]
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
