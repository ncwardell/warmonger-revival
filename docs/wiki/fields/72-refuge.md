---
title: "Refuge"
type: "field"
id: 72
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 72", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 72"]
name_key: "FieldName_72"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 2
neighbours: [73, 63, 86]
zones: [87]
segments: ["ZP12_05"]
worldmap_rect: [1365, 331, 1445, 412]
gates:
  - {"gate": 732, "x": 3153.04, "z": 1347.32, "to_gate": 820, "to_field": 63, "label": "FieldName_72"}
  - {"gate": 831, "x": 3134.22, "z": 1449.72, "to_gate": 821, "to_field": 73, "label": "FieldName_72"}
  - {"gate": 960, "x": 3229.2, "z": 1450.35, "to_gate": 822, "to_field": 86, "label": "FieldName_72"}
connections:
  - {"to": 63, "gate": 732, "to_gate": 820}
  - {"to": 73, "gate": 831, "to_gate": 821}
  - {"to": 86, "gate": 960, "to_gate": 822}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=56d17b type=7a94db id=c09763 sources=264c59 name_key=b5f65b kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=da4b92 neighbours=81e600 zones=73d585 segments=05a19d worldmap_rect=229d9b gates=ea2dc6 connections=027ad5 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 87](wiki/assets/zones/87.png) |
| **Field id** | `72` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/87-field-72-refuge\|Field 72 (Refuge)]] |
| **Terrain segments** | `ZP12_05` |
| **World-map rectangle** | `[1365, 331, 1445, 412]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_72` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 732 | 3153.04, 1347.32 | [[wiki/fields/63-cracked-earth\|Cracked Earth]] | 820 | FieldName_72 |
| 831 | 3134.22, 1449.72 | [[wiki/fields/73-left-ground\|Left Ground]] | 821 | FieldName_72 |
| 960 | 3229.2, 1450.35 | [[wiki/fields/86-moonlight-temple\|Moonlight Temple]] | 822 | FieldName_72 |

Entered from: [[wiki/fields/63-cracked-earth|Cracked Earth]] (gate 820 → 732), [[wiki/fields/73-left-ground|Left Ground]] (gate 821 → 831), [[wiki/fields/86-moonlight-temple|Moonlight Temple]] (gate 822 → 960)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/73-left-ground|Left Ground]], [[wiki/fields/63-cracked-earth|Cracked Earth]], [[wiki/fields/86-moonlight-temple|Moonlight Temple]]

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
| ZP12_05 | yes | yes |
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
