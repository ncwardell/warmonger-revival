---
title: "Enter of Shadewood"
type: "field"
id: 4
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 4", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 4"]
name_key: "FieldName_4"
kind: "land"
scene_type: 2
max_users: 30
group: 1
scene_c4: 2
neighbours: [3, 7]
zones: [33]
segments: ["ZP04_02"]
worldmap_rect: [854, 17, 942, 128]
gates:
  - {"gate": 131, "x": 1086.11, "z": 684.75, "to_gate": 140, "to_field": 3, "label": "FieldName_4"}
  - {"gate": 170, "x": 1201.88, "z": 577.53, "to_gate": 141, "to_field": 7, "label": "FieldName_4"}
connections:
  - {"to": 3, "gate": 131, "to_gate": 140}
  - {"to": 7, "gate": 170, "to_gate": 141}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=f769be type=7a94db id=1b6453 sources=a78e21 name_key=bc8a6b kind=8e3535 scene_type=da4b92 max_users=22d200 group=356a19 scene_c4=da4b92 neighbours=bc1c0d zones=78415f segments=dbbdf7 worldmap_rect=69bebe gates=cdd111 connections=5f2fd6 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 33](../assets/zones/33.png) |
| **Field id** | `4` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 1 (SceneList last column) |
| **Zones** | [[wiki/zones/33-field-04-enter-of-shadewood\|Field 04 (Enter of Shadewood)]] |
| **Terrain segments** | `ZP04_02` |
| **World-map rectangle** | `[854, 17, 942, 128]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_4` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 131 | 1086.11, 684.75 | [[wiki/fields/3-shade-wood\|Shade Wood]] | 140 | FieldName_4 |
| 170 | 1201.88, 577.53 | [[wiki/fields/7-moonshadow-wood\|Moonshadow Wood]] | 141 | FieldName_4 |

Entered from: [[wiki/fields/3-shade-wood|Shade Wood]] (gate 140 → 131), [[wiki/fields/7-moonshadow-wood|Moonshadow Wood]] (gate 141 → 170)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/3-shade-wood|Shade Wood]], [[wiki/fields/7-moonshadow-wood|Moonshadow Wood]]

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
| ZP04_02 | yes | yes |
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
