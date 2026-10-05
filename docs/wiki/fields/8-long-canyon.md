---
title: "Long Canyon"
type: "field"
id: 8
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 8", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 8"]
name_key: "FieldName_8"
kind: "land"
scene_type: 2
max_users: 30
group: 7
scene_c4: 1
neighbours: [5, 11]
zones: [36]
segments: ["ZP08_02"]
worldmap_rect: [693, 269, 754, 312]
gates:
  - {"gate": 152, "x": 2117.12, "z": 687.49, "to_gate": 180, "to_field": 5, "label": "FieldName_8"}
  - {"gate": 210, "x": 2230.65, "z": 573.87, "to_gate": 181, "to_field": 11, "label": "FieldName_8"}
connections:
  - {"to": 5, "gate": 152, "to_gate": 180}
  - {"to": 11, "gate": 210, "to_gate": 181}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=a33659 type=7a94db id=fe5dbb sources=b9d9cd name_key=fcfc93 kind=8e3535 scene_type=da4b92 max_users=22d200 group=902ba3 scene_c4=356a19 neighbours=05c7fe zones=f7a9ff segments=feb24e worldmap_rect=80bc7a gates=4f1452 connections=44aba3 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 36](../assets/zones/36.png) |
| **Field id** | `8` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 7 (SceneList last column) |
| **Zones** | [[wiki/zones/36-field-08-long-canyon\|Field 08 (Long Canyon)]] |
| **Terrain segments** | `ZP08_02` |
| **World-map rectangle** | `[693, 269, 754, 312]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_8` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 152 | 2117.12, 687.49 | [[wiki/fields/5-fall-of-abyss\|Fall of Abyss]] | 180 | FieldName_8 |
| 210 | 2230.65, 573.87 | [[wiki/fields/11-punish-canyon\|Punish Canyon]] | 181 | FieldName_8 |

Entered from: [[wiki/fields/5-fall-of-abyss|Fall of Abyss]] (gate 180 → 152), [[wiki/fields/11-punish-canyon|Punish Canyon]] (gate 181 → 210)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/5-fall-of-abyss|Fall of Abyss]], [[wiki/fields/11-punish-canyon|Punish Canyon]]

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
| ZP08_02 | yes | yes |

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
