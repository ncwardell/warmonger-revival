---
title: "Prison"
type: "field"
id: 110
status: "stub"
missing: ["spawn_points", "monsters", "npcs", "connections"]
sources: ["client: SceneList.cdb id 110", "client: ZoneDB name 어비스_LV3_110 (abyss zones are named after their field)"]
name_key: "FieldName_110"
kind: "field"
scene_type: 5
max_users: 100
group: 12
zones: [115]
segments: ["ZP03_10"]
connections: []
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=16f818 type=7a94db id=5e796e sources=626023 name_key=7f9135 kind=7a94db scene_type=ac3478 max_users=310b86 group=7b5200 zones=4c100a segments=9fb9ce connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 115](../assets/zones/115.png) |
| **Field id** | `110` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 12 (SceneList last column) |
| **Zones** | [[wiki/zones/115-abyss-lv3-110-prison\|Abyss LV3 110 (Prison)]] |
| **Terrain segments** | `ZP03_10` |
| **Name key** | `FieldName_110` |

### Gates and connections

No `Teleport_List` row: the client places no gate here.

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
| ZP03_10 | yes | yes |

### Mentioned in

- [[gameplay/abyss-map#Routes|Abyss map and portal graph § Routes]]
- [[gameplay/npc-locations#8. Still unplaced|NPC and point-of-interest locations § 8. Still unplaced]]
- [[gameplay/server-rules#Added from the source hunt (see ((gameplay/sources/Sources and gaps)))|Server rules checklist § Added from the source hunt (see ((gameplay/sources/Sources and gaps)))]]
- [[gameplay/sources#9. What is still missing|Sources and gaps § 9. What is still missing]]
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
