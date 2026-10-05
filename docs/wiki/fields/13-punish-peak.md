---
title: "Punish Peak"
type: "field"
id: 13
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 13", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 13"]
name_key: "FieldName_13"
kind: "land"
scene_type: 2
max_users: 30
group: 7
scene_c4: 2
neighbours: [12, 14]
zones: [38]
segments: ["ZP13_02"]
worldmap_rect: [668, 363, 722, 393]
gates:
  - {"gate": 221, "x": 3383.93, "z": 584.39, "to_gate": 230, "to_field": 12, "label": "FieldName_13"}
  - {"gate": 241, "x": 3489.9, "z": 683, "to_gate": 231, "to_field": 14, "label": "FieldName_13"}
connections:
  - {"to": 12, "gate": 221, "to_gate": 230}
  - {"to": 14, "gate": 241, "to_gate": 231}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=b77d87 type=7a94db id=bd307a sources=2554fb name_key=55ccd5 kind=8e3535 scene_type=da4b92 max_users=22d200 group=902ba3 scene_c4=da4b92 neighbours=c62836 zones=429a2a segments=9b2e5d worldmap_rect=340b12 gates=9942f6 connections=e5c338 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 38](../assets/zones/38.png) |
| **Field id** | `13` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 7 (SceneList last column) |
| **Zones** | [[wiki/zones/38-field-13-punish-peak\|Field 13 (Punish Peak)]] |
| **Terrain segments** | `ZP13_02` |
| **World-map rectangle** | `[668, 363, 722, 393]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_13` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 221 | 3383.93, 584.39 | [[wiki/fields/12-dark-shore\|Dark Shore]] | 230 | FieldName_13 |
| 241 | 3489.9, 683 | [[wiki/fields/14-eternal-river-upper-region\|Eternal River - Upper Region]] | 231 | FieldName_13 |

Entered from: [[wiki/fields/12-dark-shore|Dark Shore]] (gate 230 → 221), [[wiki/fields/14-eternal-river-upper-region|Eternal River - Upper Region]] (gate 231 → 241)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/12-dark-shore|Dark Shore]], [[wiki/fields/14-eternal-river-upper-region|Eternal River - Upper Region]]

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
| ZP13_02 | yes | yes |

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
