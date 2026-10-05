---
title: "Sad Swamp"
type: "field"
id: 62
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 62", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 62"]
name_key: "FieldName_62"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 2
neighbours: [61, 73]
zones: [79]
segments: ["ZP02_05"]
worldmap_rect: [1239, 297, 1320, 402]
gates:
  - {"gate": 711, "x": 572.91, "z": 1467.41, "to_gate": 720, "to_field": 61, "label": "FieldName_62"}
  - {"gate": 830, "x": 690.3, "z": 1454.93, "to_gate": 721, "to_field": 73, "label": "FieldName_62"}
connections:
  - {"to": 61, "gate": 711, "to_gate": 720}
  - {"to": 73, "gate": 830, "to_gate": 721}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=936091 type=7a94db id=511a41 sources=a589a7 name_key=c5e30e kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=da4b92 neighbours=249bea zones=614ccd segments=5f3793 worldmap_rect=dd95e5 gates=cc138c connections=be7c52 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 79](wiki/assets/zones/79.png) |
| **Field id** | `62` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/79-field-62-sad-swamp\|Field 62 (Sad Swamp)]] |
| **Terrain segments** | `ZP02_05` |
| **World-map rectangle** | `[1239, 297, 1320, 402]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_62` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 711 | 572.91, 1467.41 | [[wiki/fields/61-fire-calling\|Fire Calling]] | 720 | FieldName_62 |
| 830 | 690.3, 1454.93 | [[wiki/fields/73-left-ground\|Left Ground]] | 721 | FieldName_62 |

Entered from: [[wiki/fields/61-fire-calling|Fire Calling]] (gate 720 → 711), [[wiki/fields/73-left-ground|Left Ground]] (gate 721 → 830)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/61-fire-calling|Fire Calling]], [[wiki/fields/73-left-ground|Left Ground]]

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
| ZP02_05 | yes | yes |
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
