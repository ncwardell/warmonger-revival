---
title: "Moonlight Temple"
type: "field"
id: 86
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 86", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 86"]
name_key: "FieldName_86"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 1
neighbours: [79, 72, 78]
zones: [100]
segments: ["ZP06_06"]
worldmap_rect: [1431, 302, 1511, 350]
gates:
  - {"gate": 822, "x": 1618.64, "z": 1624.02, "to_gate": 960, "to_field": 72, "label": "FieldName_86"}
  - {"gate": 880, "x": 1713.43, "z": 1632.12, "to_gate": 961, "to_field": 78, "label": "FieldName_86"}
  - {"gate": 890, "x": 1675.03, "z": 1733.17, "to_gate": 962, "to_field": 79, "label": "FieldName_86"}
connections:
  - {"to": 72, "gate": 822, "to_gate": 960}
  - {"to": 78, "gate": 880, "to_gate": 961}
  - {"to": 79, "gate": 890, "to_gate": 962}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=cc25da type=7a94db id=3c26df sources=533d7c name_key=1a0b26 kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=356a19 neighbours=35047f zones=023272 segments=fb728b worldmap_rect=4e964a gates=10027c connections=e436b7 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 100](wiki/assets/zones/100.png) |
| **Field id** | `86` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/100-field-86-moonlight-temple\|Field 86 (Moonlight Temple)]] |
| **Terrain segments** | `ZP06_06` |
| **World-map rectangle** | `[1431, 302, 1511, 350]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_86` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 822 | 1618.64, 1624.02 | [[wiki/fields/72-refuge\|Refuge]] | 960 | FieldName_86 |
| 880 | 1713.43, 1632.12 | [[wiki/fields/78-moonlight-garden\|Moonlight Garden]] | 961 | FieldName_86 |
| 890 | 1675.03, 1733.17 | [[wiki/fields/79-moon-lake\|Moon Lake]] | 962 | FieldName_86 |

Entered from: [[wiki/fields/72-refuge|Refuge]] (gate 960 → 822), [[wiki/fields/78-moonlight-garden|Moonlight Garden]] (gate 961 → 880), [[wiki/fields/79-moon-lake|Moon Lake]] (gate 962 → 890)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/79-moon-lake|Moon Lake]], [[wiki/fields/72-refuge|Refuge]], [[wiki/fields/78-moonlight-garden|Moonlight Garden]]

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
| ZP06_06 | yes | yes |

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
