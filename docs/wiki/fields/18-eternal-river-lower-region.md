---
title: "Eternal River - Lower Region"
type: "field"
id: 18
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 18", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 18"]
name_key: "FieldName_18"
kind: "land"
scene_type: 2
max_users: 30
group: 7
scene_c4: 1
neighbours: [17, 19]
zones: [43]
segments: ["ZP18_02"]
worldmap_rect: [714, 414, 770, 455]
gates:
  - {"gate": 271, "x": 4662.81, "z": 696.08, "to_gate": 280, "to_field": 17, "label": "FieldName_18"}
  - {"gate": 291, "x": 4790.13, "z": 566.5, "to_gate": 281, "to_field": 19, "label": "FieldName_18"}
connections:
  - {"to": 17, "gate": 271, "to_gate": 280}
  - {"to": 19, "gate": 291, "to_gate": 281}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=c79c18 type=7a94db id=9e6a55 sources=7a1b9b name_key=7b6bf2 kind=8e3535 scene_type=da4b92 max_users=22d200 group=902ba3 scene_c4=356a19 neighbours=fa50c0 zones=6ee44d segments=3d35c4 worldmap_rect=920f7c gates=1dd4b5 connections=cb89c0 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 43](wiki/assets/zones/43.png) |
| **Field id** | `18` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 7 (SceneList last column) |
| **Zones** | [[wiki/zones/43-field-18-eternal-river-lower-region\|Field 18 (Eternal River - Lower Region)]] |
| **Terrain segments** | `ZP18_02` |
| **World-map rectangle** | `[714, 414, 770, 455]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_18` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 271 | 4662.81, 696.08 | [[wiki/fields/17-eternal-river-middle-region\|Eternal River - Middle Region]] | 280 | FieldName_18 |
| 291 | 4790.13, 566.5 | [[wiki/fields/19-death-valley\|Death Valley]] | 281 | FieldName_18 |

Entered from: [[wiki/fields/17-eternal-river-middle-region|Eternal River - Middle Region]] (gate 280 → 271), [[wiki/fields/19-death-valley|Death Valley]] (gate 281 → 291)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/17-eternal-river-middle-region|Eternal River - Middle Region]], [[wiki/fields/19-death-valley|Death Valley]]

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
| ZP18_02 | yes | yes |

### Mentioned in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]] (by name)
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
