---
title: "The avenue of spirit"
type: "field"
id: 113
status: "stub"
missing: ["spawn_points", "npcs"]
sources: ["client: SceneList.cdb id 113", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 113", "client: Quest.cdb (quests and objectives in field 113)"]
name_key: "FieldName_113"
kind: "field"
scene_type: 5
max_users: 100
group: 12
zones: [123]
segments: ["ZP02_11"]
gates:
  - {"gate": 1138, "x": 562.83, "z": 2896.42, "to_gate": 1135, "to_field": 109, "label": "FieldName_113"}
  - {"gate": 1134, "x": 558.93, "z": 3004.09, "to_gate": 1140, "to_field": 108, "label": "FieldName_113"}
  - {"gate": 1139, "x": 664.27, "z": 2890.44, "to_gate": 1136, "to_field": 114, "label": "FieldName_113"}
  - {"gate": 1142, "x": 688.29, "z": 3008.59, "to_gate": 1137, "to_field": 111, "label": "FieldName_113"}
connections:
  - {"to": 109, "gate": 1138, "to_gate": 1135}
  - {"to": 108, "gate": 1134, "to_gate": 1140}
  - {"to": 114, "gate": 1139, "to_gate": 1136}
  - {"to": 111, "gate": 1142, "to_gate": 1137}
npcs: []
monsters: [715, 716, 717, 718, 827, 10007, 10008]
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=6578ce type=7a94db id=e99321 sources=a498a9 name_key=84984a kind=7a94db scene_type=ac3478 max_users=310b86 group=7b5200 zones=4feada segments=b2863e gates=beff76 connections=7e86e5 npcs=97d170 monsters=b6e91b spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 123](../assets/zones/123.png) |
| **Field id** | `113` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 12 (SceneList last column) |
| **Zones** | [[wiki/zones/123-abyss-lv4-113-the-avenue-of-spirit\|Abyss LV4 113 (The avenue of spirit)]] |
| **Terrain segments** | `ZP02_11` |
| **Name key** | `FieldName_113` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1138 | 562.83, 2896.42 | [[wiki/fields/109-the-land-of-greed\|The land of Greed]] | 1135 | FieldName_113 |
| 1134 | 558.93, 3004.09 | [[wiki/fields/108-the-land-of-greed\|The land of Greed]] | 1140 | FieldName_113 |
| 1139 | 664.27, 2890.44 | [[wiki/fields/114-the-way-go-to-devildom\|The way go to devildom]] | 1136 | FieldName_113 |
| 1142 | 688.29, 3008.59 | [[wiki/fields/111-the-land-of-greed\|The land of Greed]] | 1137 | FieldName_113 |

Entered from: [[wiki/fields/108-the-land-of-greed|The land of Greed]] (gate 1140 → 1134), [[wiki/fields/109-the-land-of-greed|The land of Greed]] (gate 1135 → 1138), [[wiki/fields/111-the-land-of-greed|The land of Greed]] (gate 1137 → 1142), [[wiki/fields/114-the-way-go-to-devildom|The way go to devildom]] (gate 1136 → 1139)

### NPCs

None known yet.

### Monsters

| monster | unit | why it is listed |
|---|---|---|
| [[wiki/monsters/715-fragile-black-ghost\|Fragile Black Ghost]] | 715 | kill objective of quest [[wiki/quests/108-hunting-ghosts-spirit-avenue\|108]], [[wiki/quests/750-kill-monster-of-the-avenue-of-spirit\|750]], [[wiki/quests/1102-the-avenue-of-spirit-kill-monster\|1102]] (kill group 10007, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/716-fragile-red-ghost\|Fragile Red Ghost]] | 716 | kill objective of quest [[wiki/quests/108-hunting-ghosts-spirit-avenue\|108]], [[wiki/quests/750-kill-monster-of-the-avenue-of-spirit\|750]], [[wiki/quests/1102-the-avenue-of-spirit-kill-monster\|1102]] (kill group 10007, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/717-fragile-elite-black-ghost\|Fragile Elite Black Ghost]] | 717 | kill objective of quest [[wiki/quests/108-hunting-ghosts-spirit-avenue\|108]], [[wiki/quests/750-kill-monster-of-the-avenue-of-spirit\|750]], [[wiki/quests/1102-the-avenue-of-spirit-kill-monster\|1102]] (kill group 10008, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/718-fragile-elite-red-ghost\|Fragile Elite Red Ghost]] | 718 | kill objective of quest [[wiki/quests/108-hunting-ghosts-spirit-avenue\|108]], [[wiki/quests/750-kill-monster-of-the-avenue-of-spirit\|750]], [[wiki/quests/1102-the-avenue-of-spirit-kill-monster\|1102]] (kill group 10008, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/827-ancient-ghost\|Ancient Ghost]] | 827 | kill objective of quest [[wiki/quests/21-group-ancient-ghosts\|21]]; monster page (`spawns` / `spawn_fields`) |
| unit 10007 (not in UnitDB) | 10007 | hand-entered |
| unit 10008 (not in UnitDB) | 10008 | hand-entered |

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP02_11 | yes | yes |

### Mentioned in

- [[gameplay/server-rules#Added from the source hunt (see ((gameplay/sources/Sources and gaps)))|Server rules checklist § Added from the source hunt (see ((gameplay/sources/Sources and gaps)))]]
- [[gameplay/abyss-map|Abyss map and portal graph]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/video-dungeon-run|Video notes: Nas Village dungeon run (ZonderCoRe)]] (by name)
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
