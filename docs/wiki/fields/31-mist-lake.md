---
title: "Mist Lake"
type: "field"
id: 31
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 31", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 31"]
name_key: "FieldName_31"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 1
neighbours: [30, 34, 25]
zones: [54]
segments: ["ZP11_03"]
worldmap_rect: [858, 525, 940, 651]
gates:
  - {"gate": 350, "x": 2981.74, "z": 939.55, "to_gate": 410, "to_field": 25, "label": "FieldName_31"}
  - {"gate": 402, "x": 2886.19, "z": 943.19, "to_gate": 411, "to_field": 30, "label": "FieldName_31"}
  - {"gate": 440, "x": 2859.26, "z": 830.68, "to_gate": 412, "to_field": 34, "label": "FieldName_31"}
connections:
  - {"to": 25, "gate": 350, "to_gate": 410}
  - {"to": 30, "gate": 402, "to_gate": 411}
  - {"to": 34, "gate": 440, "to_gate": 412}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=e51503 type=7a94db id=632667 sources=78ef0f name_key=00e1bd kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=356a19 neighbours=900e7f zones=ab43c2 segments=cb1397 worldmap_rect=4a4fce gates=185f7d connections=da602f npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 54](wiki/assets/zones/54.png) |
| **Field id** | `31` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/54-field-31-mist-lake\|Field 31 (Mist Lake)]] |
| **Terrain segments** | `ZP11_03` |
| **World-map rectangle** | `[858, 525, 940, 651]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_31` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 350 | 2981.74, 939.55 | [[wiki/fields/25-mist-wood\|Mist Wood]] | 410 | FieldName_31 |
| 402 | 2886.19, 943.19 | [[wiki/fields/30-wind-valley\|Wind Valley]] | 411 | FieldName_31 |
| 440 | 2859.26, 830.68 | [[wiki/fields/34-skymist-lake\|Skymist Lake]] | 412 | FieldName_31 |

Entered from: [[wiki/fields/25-mist-wood|Mist Wood]] (gate 410 → 350), [[wiki/fields/30-wind-valley|Wind Valley]] (gate 411 → 402), [[wiki/fields/34-skymist-lake|Skymist Lake]] (gate 412 → 440)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/30-wind-valley|Wind Valley]], [[wiki/fields/34-skymist-lake|Skymist Lake]], [[wiki/fields/25-mist-wood|Mist Wood]]

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
| ZP11_03 | yes | yes |

### Mentioned in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] (by name)
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
