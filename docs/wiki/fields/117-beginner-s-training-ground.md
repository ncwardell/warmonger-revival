---
title: "Beginner's Training Ground"
type: "field"
id: 117
status: "stub"
missing: ["spawn_points", "monsters", "connections"]
sources: ["client: SceneList.cdb id 117", "doc: spec/navmesh (tutorial spawn in ZoneDB 2 tutorial_map_01)"]
name_key: "FieldName_117"
kind: "dungeon"
scene_type: 3
max_users: 100
group: 0
zones: [2]
segments: ["ZP05_01"]
connections: []
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=59109e type=7a94db id=d0e2db sources=491986 name_key=263464 kind=3e3f38 scene_type=77de68 max_users=310b86 group=b6589f zones=249983 segments=0fbb4f connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 2](wiki/assets/zones/2.png) |
| **Field id** | `117` |
| **Kind** | dungeon (SceneList type 3; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 0 (SceneList last column) |
| **Zones** | [[wiki/zones/2-tutorial-map-01-beginner-s-training-ground\|Tutorial map 01 (Beginner's Training Ground)]] |
| **Terrain segments** | `ZP05_01` |
| **Name key** | `FieldName_117` |

### Gates and connections

No `Teleport_List` row: the client places no gate here.

### NPCs

None known yet.

### Monsters

None known yet.

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

Current server (`server/world.py`, our choice, not original data): players appear at (1427, 429) in scene 87. The tutorial monsters are placed around it: Slime (604) at offset 10.3, -1, Slime (604) at offset 9, 8, Slime (604) at offset 13, -7, Cobra (732) at offset -11, 10, Cobra (732) at offset -13, 3, Bee (731) at offset 5, -13, Bee (731) at offset 2.7, -13, Great Slime (605) at offset -5.8, 20.4.

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP05_01 | yes | yes |

### Mentioned in

- [[gameplay/npc-locations#6. Village (87/91/95), Castle (90/94/98), tutorial (117)|NPC and point-of-interest locations § 6. Village (87/91/95), Castle (90/94/98), tutorial (117)]]
- [[gameplay/sources#9. What is still missing|Sources and gaps § 9. What is still missing]]
- [[gameplay/video-character-creation-and-tutorial#Video notes: character creation and tutorial (ZonderCoRe, June 2018)|Video notes: character creation and tutorial (ZonderCoRe, June 2018) § Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/video-character-creation-and-tutorial#6. Differences from other builds|Video notes: character creation and tutorial (ZonderCoRe, June 2018) § 6. Differences from other builds]]
- [[gameplay/video-early-quests#Video notes: first session, levels 1+ (charmanmugen)|Video notes: first session, levels 1+ (charmanmugen) § Video notes: first session, levels 1+ (charmanmugen)]] — at [3:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=210s)
- [[gameplay/video-tutorial-walkthrough#1. Tutorial and early quest flow|Video notes: tutorial walkthrough (Bravely Forward 2) § 1. Tutorial and early quest flow]]
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
