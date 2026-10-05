---
title: "Moonlight Plain - West"
type: "field"
id: 82
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 82", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 82"]
name_key: "FieldName_82"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 1
neighbours: [81, 83]
zones: [95]
segments: ["ZP02_06"]
worldmap_rect: [1576, 125, 1681, 184]
gates:
  - {"gate": 912, "x": 597.95, "z": 1701.04, "to_gate": 920, "to_field": 81, "label": "FieldName_82"}
  - {"gate": 932, "x": 662.02, "z": 1586.98, "to_gate": 921, "to_field": 83, "label": "FieldName_82"}
connections:
  - {"to": 81, "gate": 912, "to_gate": 920}
  - {"to": 83, "gate": 932, "to_gate": 921}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=d34353 type=7a94db id=76546f sources=178719 name_key=1467f9 kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=356a19 neighbours=4c8cf0 zones=8c0b2e segments=3f4db3 worldmap_rect=cc54a3 gates=b811f3 connections=ce82a5 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 95](../assets/zones/95.png) |
| **Field id** | `82` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/95-field-82-moonlight-plain-west\|Field 82 (Moonlight Plain - West)]] |
| **Terrain segments** | `ZP02_06` |
| **World-map rectangle** | `[1576, 125, 1681, 184]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_82` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 912 | 597.95, 1701.04 | [[wiki/fields/81-windmist-hill\|Windmist Hill]] | 920 | FieldName_82 |
| 932 | 662.02, 1586.98 | [[wiki/fields/83-moonlight-plain-east\|Moonlight Plain - East]] | 921 | FieldName_82 |

Entered from: [[wiki/fields/81-windmist-hill|Windmist Hill]] (gate 920 → 912), [[wiki/fields/83-moonlight-plain-east|Moonlight Plain - East]] (gate 921 → 932)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/81-windmist-hill|Windmist Hill]], [[wiki/fields/83-moonlight-plain-east|Moonlight Plain - East]]

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
| ZP02_06 | yes | yes |
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
