---
title: "Sunup Campsite"
type: "field"
id: 51
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 51", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 51"]
name_key: "FieldName_51"
kind: "land"
scene_type: 2
max_users: 30
group: 4
scene_c4: 2
neighbours: [43, 52, 50]
zones: [69]
segments: ["ZP11_04"]
worldmap_rect: [1109, 769, 1173, 821]
gates:
  - {"gate": 532, "x": 2872.69, "z": 1209.49, "to_gate": 610, "to_field": 43, "label": "FieldName_51"}
  - {"gate": 601, "x": 2980.93, "z": 1229.86, "to_gate": 611, "to_field": 50, "label": "FieldName_51"}
  - {"gate": 620, "x": 2985.35, "z": 1105.48, "to_gate": 612, "to_field": 52, "label": "FieldName_51"}
connections:
  - {"to": 43, "gate": 532, "to_gate": 610}
  - {"to": 50, "gate": 601, "to_gate": 611}
  - {"to": 52, "gate": 620, "to_gate": 612}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=648e15 type=7a94db id=b7eb6c sources=834a6e name_key=a50eb3 kind=8e3535 scene_type=da4b92 max_users=22d200 group=1b6453 scene_c4=da4b92 neighbours=a15c94 zones=bf79f8 segments=c6981f worldmap_rect=38763b gates=4b2738 connections=6a4735 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 69](../assets/zones/69.png) |
| **Field id** | `51` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 4 (SceneList last column) |
| **Zones** | [[wiki/zones/69-field-51-sunup-campsite\|Field 51 (Sunup Campsite)]] |
| **Terrain segments** | `ZP11_04` |
| **World-map rectangle** | `[1109, 769, 1173, 821]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_51` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 532 | 2872.69, 1209.49 | [[wiki/fields/43-floor-of-twilight\|Floor of Twilight]] | 610 | FieldName_51 |
| 601 | 2980.93, 1229.86 | [[wiki/fields/50-eclipsed-road\|Eclipsed Road]] | 611 | FieldName_51 |
| 620 | 2985.35, 1105.48 | [[wiki/fields/52-totem-pole-peak\|Totem Pole Peak]] | 612 | FieldName_51 |

Entered from: [[wiki/fields/43-floor-of-twilight|Floor of Twilight]] (gate 610 → 532), [[wiki/fields/50-eclipsed-road|Eclipsed Road]] (gate 611 → 601), [[wiki/fields/52-totem-pole-peak|Totem Pole Peak]] (gate 612 → 620)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/43-floor-of-twilight|Floor of Twilight]], [[wiki/fields/52-totem-pole-peak|Totem Pole Peak]], [[wiki/fields/50-eclipsed-road|Eclipsed Road]]

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
| ZP11_04 | yes | yes |
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
