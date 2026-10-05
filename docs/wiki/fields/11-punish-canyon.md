---
title: "Punish Canyon"
type: "field"
id: 11
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 11", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 11"]
name_key: "FieldName_11"
kind: "land"
scene_type: 2
max_users: 30
group: 7
scene_c4: 2
neighbours: [8, 12]
zones: [18]
segments: ["ZP11_02"]
worldmap_rect: [502, 297, 650, 350]
gates:
  - {"gate": 181, "x": 2968.18, "z": 689.09, "to_gate": 210, "to_field": 8, "label": "FieldName_11"}
  - {"gate": 220, "x": 2865.16, "z": 577.26, "to_gate": 211, "to_field": 12, "label": "FieldName_11"}
connections:
  - {"to": 8, "gate": 181, "to_gate": 210}
  - {"to": 12, "gate": 220, "to_gate": 211}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=29d875 type=7a94db id=17ba07 sources=e1c441 name_key=423b4c kind=8e3535 scene_type=da4b92 max_users=22d200 group=902ba3 scene_c4=da4b92 neighbours=435895 zones=83a1aa segments=b846d9 worldmap_rect=605c71 gates=7e0285 connections=a4fda8 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 18](wiki/assets/zones/18.png) |
| **Field id** | `11` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 7 (SceneList last column) |
| **Zones** | [[wiki/zones/18-field-11-punish-canyon\|Field 11 (Punish Canyon)]] |
| **Terrain segments** | `ZP11_02` |
| **World-map rectangle** | `[502, 297, 650, 350]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_11` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 181 | 2968.18, 689.09 | [[wiki/fields/8-long-canyon\|Long Canyon]] | 210 | FieldName_11 |
| 220 | 2865.16, 577.26 | [[wiki/fields/12-dark-shore\|Dark Shore]] | 211 | FieldName_11 |

Entered from: [[wiki/fields/8-long-canyon|Long Canyon]] (gate 210 → 181), [[wiki/fields/12-dark-shore|Dark Shore]] (gate 211 → 220)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/8-long-canyon|Long Canyon]], [[wiki/fields/12-dark-shore|Dark Shore]]

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
| ZP11_02 | yes | yes |

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
