---
title: "The avenue of spirit"
type: "field"
id: 106
status: "stub"
missing: ["spawn_points", "monsters", "npcs", "connections"]
sources: ["client: SceneList.cdb id 106", "client: ZoneDB name 어비스_LV2_106 (abyss zones are named after their field)"]
name_key: "FieldName_116"
kind: "field"
scene_type: 5
max_users: 100
group: 12
neighbours: [101, 110]
zones: [120]
segments: ["ZP05_09"]
connections: []
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=6578ce type=7a94db id=7224f9 sources=99bc42 name_key=1f1141 kind=7a94db scene_type=ac3478 max_users=310b86 group=7b5200 neighbours=573523 zones=6c3da9 segments=b46245 connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 120](../assets/zones/120.png) |
| **Field id** | `106` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 12 (SceneList last column) |
| **Zones** | [[wiki/zones/120-abyss-lv2-106-the-avenue-of-spirit\|Abyss LV2 106 (The avenue of spirit)]] |
| **Terrain segments** | `ZP05_09` |
| **Name key** | `FieldName_116` |

### Gates and connections

No `Teleport_List` row: the client places no gate here.

Entered from: [[wiki/fields/109-the-land-of-greed|The land of Greed]] (gate 1114 → 1126)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/101-corpse-incineration|Corpse incineration]], [[wiki/fields/110-prison|Prison]]

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
| ZP05_09 | yes | yes |

### Mentioned in

- [[gameplay/abyss-map#Fields and layout|Abyss map and portal graph § Fields and layout]]
- [[gameplay/server-rules#Added from the source hunt (see ((gameplay/sources/Sources and gaps)))|Server rules checklist § Added from the source hunt (see ((gameplay/sources/Sources and gaps)))]]
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
