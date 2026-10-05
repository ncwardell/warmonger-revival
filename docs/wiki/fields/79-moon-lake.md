---
title: "Moon Lake"
type: "field"
id: 79
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 79", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 79"]
name_key: "FieldName_79"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 2
neighbours: [80, 86]
zones: [92]
segments: ["ZP19_05"]
worldmap_rect: [1422, 241, 1505, 281]
gates:
  - {"gate": 901, "x": 4919.52, "z": 1436.52, "to_gate": 891, "to_field": 80, "label": "FieldName_79"}
  - {"gate": 962, "x": 5028.95, "z": 1326.29, "to_gate": 890, "to_field": 86, "label": "FieldName_79"}
connections:
  - {"to": 80, "gate": 901, "to_gate": 891}
  - {"to": 86, "gate": 962, "to_gate": 890}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=69e866 type=7a94db id=b74f5e sources=4ea4d6 name_key=aa7339 kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=da4b92 neighbours=d8bc3e zones=5877c3 segments=af805c worldmap_rect=598d54 gates=fe7891 connections=f4bddc npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 92](../assets/zones/92.png) |
| **Field id** | `79` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/92-field-79-moon-lake\|Field 79 (Moon Lake)]] |
| **Terrain segments** | `ZP19_05` |
| **World-map rectangle** | `[1422, 241, 1505, 281]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_79` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 901 | 4919.52, 1436.52 | [[wiki/fields/80-windmist-valley\|Windmist Valley]] | 891 | FieldName_79 |
| 962 | 5028.95, 1326.29 | [[wiki/fields/86-moonlight-temple\|Moonlight Temple]] | 890 | FieldName_79 |

Entered from: [[wiki/fields/80-windmist-valley|Windmist Valley]] (gate 891 → 901), [[wiki/fields/86-moonlight-temple|Moonlight Temple]] (gate 890 → 962)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/80-windmist-valley|Windmist Valley]], [[wiki/fields/86-moonlight-temple|Moonlight Temple]]

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
| ZP19_05 | yes | yes |
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
