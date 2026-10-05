---
title: "Skywing Yard"
type: "field"
id: 6
status: "partial"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 6", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 6", "guide: [[gameplay/maps-and-dungeons]] §3 (event dungeons seen here)"]
name_key: "FieldName_6"
kind: "land"
scene_type: 2
max_users: 30
group: 1
neighbours: [3, 5, 84]
zones: [34]
segments: ["ZP06_02"]
worldmap_rect: [768, 165, 827, 193]
gates:
  - {"gate": 132, "x": 1700.19, "z": 690.42, "to_gate": 161, "to_field": 3, "label": "FieldName_6"}
  - {"gate": 151, "x": 1582.38, "z": 688.4, "to_gate": 162, "to_field": 5, "label": "FieldName_6"}
  - {"gate": 940, "x": 1715.81, "z": 566.39, "to_gate": 160, "to_field": 84, "label": "FieldName_6"}
connections:
  - {"to": 3, "gate": 132, "to_gate": 161}
  - {"to": 5, "gate": 151, "to_gate": 162}
  - {"to": 84, "gate": 940, "to_gate": 160}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=b3e4f2 type=7a94db id=c1dfd9 sources=49542b name_key=33a2d4 kind=8e3535 scene_type=da4b92 max_users=22d200 group=356a19 neighbours=cd0d61 zones=91a33c segments=918b6b worldmap_rect=ff83b2 gates=b4bade connections=f05a89 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 34](wiki/assets/zones/34.png) |
| **Field id** | `6` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 1 (SceneList last column) |
| **Zones** | [[wiki/zones/34-field-06-skywing-yard\|Field 06 (Skywing Yard)]] |
| **Terrain segments** | `ZP06_02` |
| **World-map rectangle** | `[768, 165, 827, 193]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_6` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 132 | 1700.19, 690.42 | [[wiki/fields/3-shade-wood\|Shade Wood]] | 161 | FieldName_6 |
| 151 | 1582.38, 688.4 | [[wiki/fields/5-fall-of-abyss\|Fall of Abyss]] | 162 | FieldName_6 |
| 940 | 1715.81, 566.39 | [[wiki/fields/84-eternal-lake\|Eternal Lake]] | 160 | FieldName_6 |

Entered from: [[wiki/fields/3-shade-wood|Shade Wood]] (gate 161 → 132), [[wiki/fields/5-fall-of-abyss|Fall of Abyss]] (gate 162 → 151), [[wiki/fields/84-eternal-lake|Eternal Lake]] (gate 160 → 940)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/3-shade-wood|Shade Wood]], [[wiki/fields/5-fall-of-abyss|Fall of Abyss]], [[wiki/fields/84-eternal-lake|Eternal Lake]]

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
| ZP06_02 | yes | yes |

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
<!-- generated:end -->

## Notes

- Event dungeons The Avenue of Spirit and Nas Village were seen opening on this land ([[gameplay/maps-and-dungeons|Maps and dungeons]] §3). *guide*

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
