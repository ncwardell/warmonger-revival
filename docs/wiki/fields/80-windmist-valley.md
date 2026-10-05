---
title: "Windmist Valley"
type: "field"
id: 80
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 80", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 80"]
name_key: "FieldName_80"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 1
neighbours: [74, 79, 81]
zones: [93]
segments: ["ZP20_05"]
worldmap_rect: [1309, 142, 1405, 192]
gates:
  - {"gate": 841, "x": 5174.87, "z": 1331.38, "to_gate": 900, "to_field": 74, "label": "FieldName_80"}
  - {"gate": 891, "x": 5292.98, "z": 1334.15, "to_gate": 901, "to_field": 79, "label": "FieldName_80"}
  - {"gate": 911, "x": 5287.8, "z": 1444.44, "to_gate": 902, "to_field": 81, "label": "FieldName_80"}
connections:
  - {"to": 74, "gate": 841, "to_gate": 900}
  - {"to": 79, "gate": 891, "to_gate": 901}
  - {"to": 81, "gate": 911, "to_gate": 902}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=ee395d type=7a94db id=b888b2 sources=a3a884 name_key=63656c kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=356a19 neighbours=436eb0 zones=a7533a segments=40e8e1 worldmap_rect=489e34 gates=8d670b connections=3f7d3f npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 93](wiki/assets/zones/93.png) |
| **Field id** | `80` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/93-field-80-windmist-valley\|Field 80 (Windmist Valley)]] |
| **Terrain segments** | `ZP20_05` |
| **World-map rectangle** | `[1309, 142, 1405, 192]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_80` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 841 | 5174.87, 1331.38 | [[wiki/fields/74-whistle-hill\|Whistle Hill]] | 900 | FieldName_80 |
| 891 | 5292.98, 1334.15 | [[wiki/fields/79-moon-lake\|Moon Lake]] | 901 | FieldName_80 |
| 911 | 5287.8, 1444.44 | [[wiki/fields/81-windmist-hill\|Windmist Hill]] | 902 | FieldName_80 |

Entered from: [[wiki/fields/74-whistle-hill|Whistle Hill]] (gate 900 → 841), [[wiki/fields/79-moon-lake|Moon Lake]] (gate 901 → 891), [[wiki/fields/81-windmist-hill|Windmist Hill]] (gate 902 → 911)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/74-whistle-hill|Whistle Hill]], [[wiki/fields/79-moon-lake|Moon Lake]], [[wiki/fields/81-windmist-hill|Windmist Hill]]

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
| ZP20_05 | yes | yes |

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
