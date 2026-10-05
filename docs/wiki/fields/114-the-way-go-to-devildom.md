---
title: "The way go to devildom"
type: "field"
id: 114
status: "stub"
missing: ["spawn_points", "npcs"]
sources: ["client: SceneList.cdb id 114", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 114", "client: Quest.cdb (quests and objectives in field 114)", "client: Trigger.cdb field 114"]
name_key: "FieldName_114"
kind: "field"
scene_type: 5
max_users: 100
group: 12
zones: [124]
segments: ["ZP01_12"]
gates:
  - {"gate": 1136, "x": 455.13, "z": 3271.86, "to_gate": 1139, "to_field": 113, "label": "FieldName_114"}
connections:
  - {"to": 113, "gate": 1136, "to_gate": 1139}
npcs: []
monsters: [828, 829, 10033, 10034]
spawn_points: []
triggers:
  - {"id": 11406, "type": 6, "shape": 4, "x": 315.92, "z": 3273.45, "name_key": "UnitName_244", "model": 187}
  - {"id": 11407, "type": 6, "shape": 4, "x": 305.42, "z": 3127.78, "name_key": "UnitName_244", "model": 187}
  - {"id": 11408, "type": 6, "shape": 4, "x": 451.65, "z": 3130.35, "name_key": "UnitName_244", "model": 187}
---
<!-- generated:start -->
<!-- generated-keys: title=bd8009 type=7a94db id=ecb793 sources=312271 name_key=bf8330 kind=7a94db scene_type=ac3478 max_users=310b86 group=7b5200 zones=181a14 segments=a35b1d gates=15e89e connections=3b9ab2 npcs=97d170 monsters=bb6537 spawn_points=97d170 triggers=12b60e -->
|  |  |
|---|---|
|  | ![minimap of zone 124](../assets/zones/124.png) |
| **Field id** | `114` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 12 (SceneList last column) |
| **Zones** | [[wiki/zones/124-abyss-lv5-114-the-way-go-to-devildom\|Abyss LV5 114 (The way go to devildom)]] |
| **Terrain segments** | `ZP01_12` |
| **Name key** | `FieldName_114` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1136 | 455.13, 3271.86 | [[wiki/fields/113-the-avenue-of-spirit\|The avenue of spirit]] | 1139 | FieldName_114 |

Entered from: [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] (gate 1139 → 1136)

### NPCs

None known yet.

### Monsters

| monster | unit | why it is listed |
|---|---|---|
| [[wiki/monsters/828-fragile-demon-hunter\|Fragile Demon Hunter]] | 828 | kill objective of quest [[wiki/quests/751-kill-monster-of-the-way-go-to-devildom\|751]], [[wiki/quests/1103-the-way-go-to-devildom-kill-monster\|1103]] (kill group 10033, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/829-fragile-elite-demon-hunter\|Fragile Elite Demon Hunter]] | 829 | kill objective of quest [[wiki/quests/40-innocence-s-recovery-operation\|40]], [[wiki/quests/751-kill-monster-of-the-way-go-to-devildom\|751]], [[wiki/quests/1103-the-way-go-to-devildom-kill-monster\|1103]] (kill group 10034, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| unit 10033 (not in UnitDB) | 10033 | hand-entered |
| unit 10034 (not in UnitDB) | 10034 | hand-entered |

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Client-placed objects (`Trigger`)

Talk devices (shape 4) and gathering nodes (type 0, shape 5: the item is what gathering gives). The server can load these as they are; the video check in [[gameplay/video-dungeon-run|Nas Village dungeon run]] §5 matched them within 5 units.

| trigger | kind | name | gives | at (x, z) | type | model |
|---|---|---|---|---|---|---|
| [[wiki/nodes/11406-knightage-s-leader\|11406]] | talk/device | Knightage's Leader |  | 315.92, 3273.45 | 6 | 187 |
| [[wiki/nodes/11407-knightage-s-leader\|11407]] | talk/device | Knightage's Leader |  | 305.42, 3127.78 | 6 | 187 |
| [[wiki/nodes/11408-knightage-s-leader\|11408]] | talk/device | Knightage's Leader |  | 451.65, 3130.35 | 6 | 187 |

### Quests in this field

[[wiki/quests/40-innocence-s-recovery-operation|Innocence's recovery operation]]

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP01_12 | yes | yes |

### Mentioned in

- [[gameplay/server-rules#Added from the source hunt (see ((gameplay/sources/Sources and gaps)))|Server rules checklist § Added from the source hunt (see ((gameplay/sources/Sources and gaps)))]]
- [[gameplay/abyss-map|Abyss map and portal graph]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
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
