---
title: "Sun Hill"
type: "field"
id: 55
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 55", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 55"]
name_key: "FieldName_55"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 2
neighbours: [52, 54, 56]
zones: [73]
segments: ["ZP15_04"]
worldmap_rect: [1287, 815, 1369, 933]
gates:
  - {"gate": 621, "x": 3890.28, "z": 1083.69, "to_gate": 650, "to_field": 52, "label": "FieldName_55"}
  - {"gate": 641, "x": 3898.66, "z": 1187.16, "to_gate": 651, "to_field": 54, "label": "FieldName_55"}
  - {"gate": 660, "x": 4016.1, "z": 1078.2, "to_gate": 652, "to_field": 56, "label": "FieldName_55"}
connections:
  - {"to": 52, "gate": 621, "to_gate": 650}
  - {"to": 54, "gate": 641, "to_gate": 651}
  - {"to": 56, "gate": 660, "to_gate": 652}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=301d1b type=7a94db id=8effee sources=c28125 name_key=ff8edb kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=da4b92 neighbours=3d3c89 zones=9af767 segments=bc353d worldmap_rect=38b4cd gates=3e184d connections=359162 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 73](wiki/assets/zones/73.png) |
| **Field id** | `55` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/73-field-55-sun-hill\|Field 55 (Sun Hill)]] |
| **Terrain segments** | `ZP15_04` |
| **World-map rectangle** | `[1287, 815, 1369, 933]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_55` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 621 | 3890.28, 1083.69 | [[wiki/fields/52-totem-pole-peak\|Totem Pole Peak]] | 650 | FieldName_55 |
| 641 | 3898.66, 1187.16 | [[wiki/fields/54-rotten-twig-wood\|Rotten Twig Wood]] | 651 | FieldName_55 |
| 660 | 4016.1, 1078.2 | [[wiki/fields/56-snowflower-plain\|Snowflower Plain]] | 652 | FieldName_55 |

Entered from: [[wiki/fields/52-totem-pole-peak|Totem Pole Peak]] (gate 650 → 621), [[wiki/fields/54-rotten-twig-wood|Rotten Twig Wood]] (gate 651 → 641), [[wiki/fields/56-snowflower-plain|Snowflower Plain]] (gate 652 → 660)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/52-totem-pole-peak|Totem Pole Peak]], [[wiki/fields/54-rotten-twig-wood|Rotten Twig Wood]], [[wiki/fields/56-snowflower-plain|Snowflower Plain]]

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
| ZP15_04 | yes | yes |
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
