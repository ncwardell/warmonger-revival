---
title: "Canyon of Earth"
type: "field"
id: 65
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 65", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 65"]
name_key: "FieldName_65"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 1
neighbours: [58, 69]
zones: [27]
segments: ["ZP05_05"]
worldmap_rect: [1394, 554, 1486, 611]
gates:
  - {"gate": 682, "x": 1375.14, "z": 1325.03, "to_gate": 750, "to_field": 58, "label": "FieldName_65"}
  - {"gate": 790, "x": 1466.53, "z": 1444.41, "to_gate": 751, "to_field": 69, "label": "FieldName_65"}
connections:
  - {"to": 58, "gate": 682, "to_gate": 750}
  - {"to": 69, "gate": 790, "to_gate": 751}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=4444ce type=7a94db id=2a4593 sources=d5e918 name_key=beaa39 kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=356a19 neighbours=190325 zones=c75897 segments=e1066a worldmap_rect=f92600 gates=b8ef4d connections=b2bf1f npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 27](wiki/assets/zones/27.png) |
| **Field id** | `65` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/27-field-65-canyon-of-earth\|Field 65 (Canyon of Earth)]] |
| **Terrain segments** | `ZP05_05` |
| **World-map rectangle** | `[1394, 554, 1486, 611]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_65` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 682 | 1375.14, 1325.03 | [[wiki/fields/58-evil-s-wood\|Evil's Wood]] | 750 | FieldName_65 |
| 790 | 1466.53, 1444.41 | [[wiki/fields/69-frostwind-west\|Frostwind - West]] | 751 | FieldName_65 |

Entered from: [[wiki/fields/58-evil-s-wood|Evil's Wood]] (gate 750 → 682), [[wiki/fields/69-frostwind-west|Frostwind - West]] (gate 751 → 790)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/58-evil-s-wood|Evil's Wood]], [[wiki/fields/69-frostwind-west|Frostwind - West]]

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
| ZP05_05 | yes | yes |
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
