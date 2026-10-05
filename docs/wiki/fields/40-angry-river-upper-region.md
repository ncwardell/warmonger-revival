---
title: "Angry River - Upper Region"
type: "field"
id: 40
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 40", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 40"]
name_key: "FieldName_40"
kind: "land"
scene_type: 2
max_users: 30
group: 6
scene_c4: 2
neighbours: [85, 41, 42]
zones: [59]
segments: ["ZP20_03"]
worldmap_rect: [888, 839, 993, 907]
gates:
  - {"gate": 510, "x": 5282.58, "z": 947.19, "to_gate": 501, "to_field": 41, "label": "FieldName_40"}
  - {"gate": 520, "x": 5293.8, "z": 829.16, "to_gate": 502, "to_field": 42, "label": "FieldName_40"}
  - {"gate": 951, "x": 5182.04, "z": 818.06, "to_gate": 500, "to_field": 85, "label": "FieldName_40"}
connections:
  - {"to": 41, "gate": 510, "to_gate": 501}
  - {"to": 42, "gate": 520, "to_gate": 502}
  - {"to": 85, "gate": 951, "to_gate": 500}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=f6f73f type=7a94db id=af3e13 sources=a792b5 name_key=8e2cda kind=8e3535 scene_type=da4b92 max_users=22d200 group=c1dfd9 scene_c4=da4b92 neighbours=42b213 zones=b5f6b5 segments=3c8749 worldmap_rect=1d0869 gates=234f48 connections=b883e5 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 59](../assets/zones/59.png) |
| **Field id** | `40` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 6 (SceneList last column) |
| **Zones** | [[wiki/zones/59-field-40-angry-river-upper-region\|Field 40 (Angry River - Upper Region)]] |
| **Terrain segments** | `ZP20_03` |
| **World-map rectangle** | `[888, 839, 993, 907]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_40` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 510 | 5282.58, 947.19 | [[wiki/fields/41-enter-of-twilight\|Enter of Twilight]] | 501 | FieldName_40 |
| 520 | 5293.8, 829.16 | [[wiki/fields/42-crater-of-abaddon\|Crater of Abaddon]] | 502 | FieldName_40 |
| 951 | 5182.04, 818.06 | [[wiki/fields/85-dark-gateway\|Dark Gateway]] | 500 | FieldName_40 |

Entered from: [[wiki/fields/41-enter-of-twilight|Enter of Twilight]] (gate 501 → 510), [[wiki/fields/42-crater-of-abaddon|Crater of Abaddon]] (gate 502 → 520), [[wiki/fields/85-dark-gateway|Dark Gateway]] (gate 500 → 951)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/85-dark-gateway|Dark Gateway]], [[wiki/fields/41-enter-of-twilight|Enter of Twilight]], [[wiki/fields/42-crater-of-abaddon|Crater of Abaddon]]

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
| ZP20_03 | yes | yes |
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
