---
title: "Refuge of old dragon"
type: "field"
id: 16
status: "partial"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 16", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 16", "image: [[gameplay/maps-and-dungeons]] §1 (grey band, spring 2018)"]
name_key: "FieldName_16"
kind: "land"
scene_type: 2
max_users: 30
group: 5
scene_c4: 1
neighbours: [10, 22]
zones: [41]
segments: ["ZP16_02"]
worldmap_rect: [974, 276, 1077, 343]
gates:
  - {"gate": 201, "x": 4152.48, "z": 705.2, "to_gate": 260, "to_field": 10, "label": "FieldName_16"}
  - {"gate": 320, "x": 4268.3, "z": 590.46, "to_gate": 261, "to_field": 22, "label": "FieldName_16"}
connections:
  - {"to": 10, "gate": 201, "to_gate": 260}
  - {"to": 22, "gate": 320, "to_gate": 261}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=a2f705 type=7a94db id=1574bd sources=2445b0 name_key=37eba2 kind=8e3535 scene_type=da4b92 max_users=22d200 group=ac3478 scene_c4=356a19 neighbours=ccb70c zones=8f80dd segments=fe3195 worldmap_rect=7ad43e gates=0f1fb4 connections=a586d3 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 41](../assets/zones/41.png) |
| **Field id** | `16` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 5 (SceneList last column) |
| **Zones** | [[wiki/zones/41-field-16-refuge-of-old-dragon\|Field 16 (Refuge of old dragon)]] |
| **Terrain segments** | `ZP16_02` |
| **World-map rectangle** | `[974, 276, 1077, 343]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_16` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 201 | 4152.48, 705.2 | [[wiki/fields/10-shaking-earth\|Shaking Earth]] | 260 | FieldName_16 |
| 320 | 4268.3, 590.46 | [[wiki/fields/22-afterlife-hill\|Afterlife Hill]] | 261 | FieldName_16 |

Entered from: [[wiki/fields/10-shaking-earth|Shaking Earth]] (gate 260 → 201), [[wiki/fields/22-afterlife-hill|Afterlife Hill]] (gate 261 → 320)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/10-shaking-earth|Shaking Earth]], [[wiki/fields/22-afterlife-hill|Afterlife Hill]]

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
| ZP16_02 | yes | yes |

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
<!-- generated:end -->

## Notes

- Part of the grey (monster-held) band between Arslan (west) and Erion (east) on the spring 2018 world map ([[gameplay/maps-and-dungeons|Maps and dungeons]] §1). *image*

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
