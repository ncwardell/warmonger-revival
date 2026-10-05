---
title: "Sinking Nest (Crystal)"
type: "field"
id: 133
status: "stub"
missing: ["spawn_points", "monsters", "connections"]
sources: ["client: SceneList.cdb id 133", "doc: gameplay/video-dungeon-run §1 (Nas Village Entrance geometry = ZoneDB 126; guess)"]
name_key: "FieldName_133"
kind: "event_dungeon"
scene_type: 6
max_users: 100
group: 41
zones: [126]
segments: ["ZP05_11"]
connections: []
npcs: []
monsters: []
spawn_points: []
dungeon: 133
---
<!-- generated:start -->
<!-- generated-keys: title=7f851f type=7a94db id=d30f79 sources=93d02e name_key=9c77e6 kind=884439 scene_type=c1dfd9 max_users=310b86 group=761f22 zones=d9b420 segments=5a389d connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 dungeon=d30f79 -->
|  |  |
|---|---|
|  | ![minimap of zone 126](../assets/zones/126.png) |
|  | ![Sinking Nest (Crystal)](../assets/dungeons/133.png) |
| **Field id** | `133` |
| **Kind** | event dungeon (SceneList type 6; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 41 (SceneList last column) |
| **Zones** | [[wiki/zones/126-battlefield-tutorial-sinking-nest\|Battlefield tutorial (Sinking Nest)]] |
| **Terrain segments** | `ZP05_11` |
| **Dungeon** | [[wiki/dungeons/133-sinking-nest-crystal\|dungeon page]] |
| **Name key** | `FieldName_133` |

### Gates and connections

No `Teleport_List` row: the client places no gate here.

### NPCs

None known yet.

### Monsters

None known yet.

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Dungeon

Entry cost, rewards, boss and schedule: [[wiki/dungeons/133-sinking-nest-crystal|Sinking Nest (Crystal)]].

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP05_11 | yes | yes |

### Mentioned in

- [[gameplay/patch-history#Dungeons and world|Patch notes and other sources § Dungeons and world]]
- [[gameplay/server-rules#Added from the Warmonger forum and videos (round 2)|Server rules checklist § Added from the Warmonger forum and videos (round 2)]]
- [[gameplay/video-dungeon-run#2. Pack positions (field 133)|Video notes: Nas Village dungeon run (ZonderCoRe) § 2. Pack positions (field 133)]]
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
