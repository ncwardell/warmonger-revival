---
title: "Mist Wood"
type: "field"
id: 25
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 25", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 25"]
name_key: "FieldName_25"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 2
neighbours: [31, 32]
zones: [20]
segments: ["ZP05_03"]
worldmap_rect: [937, 489, 1012, 570]
gates:
  - {"gate": 410, "x": 1347, "z": 864, "to_gate": 350, "to_field": 31, "label": "FieldName_25"}
  - {"gate": 420, "x": 1442.39, "z": 960, "to_gate": 351, "to_field": 32, "label": "FieldName_25"}
connections:
  - {"to": 31, "gate": 410, "to_gate": 350}
  - {"to": 32, "gate": 420, "to_gate": 351}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=b43fe4 type=7a94db id=f6e112 sources=a39654 name_key=f83c89 kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=da4b92 neighbours=a0c7ea zones=6a5bf6 segments=3f5ef2 worldmap_rect=0fe6ea gates=1e7beb connections=e5fe5a npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 20](wiki/assets/zones/20.png) |
| **Field id** | `25` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/20-field-25-mist-wood\|Field 25 (Mist Wood)]] |
| **Terrain segments** | `ZP05_03` |
| **World-map rectangle** | `[937, 489, 1012, 570]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_25` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 410 | 1347, 864 | [[wiki/fields/31-mist-lake\|Mist Lake]] | 350 | FieldName_25 |
| 420 | 1442.39, 960 | [[wiki/fields/32-long-road\|Long Road]] | 351 | FieldName_25 |

Entered from: [[wiki/fields/31-mist-lake|Mist Lake]] (gate 350 → 410), [[wiki/fields/32-long-road|Long Road]] (gate 351 → 420)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/31-mist-lake|Mist Lake]], [[wiki/fields/32-long-road|Long Road]]

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
| ZP05_03 | yes | yes |
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
