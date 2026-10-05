---
title: "Training Ground"
type: "field"
id: 89
status: "stub"
missing: ["spawn_points"]
sources: ["client: SceneList.cdb id 89", "client: Quest.cdb map1..3", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 89", "client: Quest.cdb (quests and objectives in field 89)", "doc: gameplay/npc-locations § 5. Training Ground (fields 89 / 93 / 97)"]
name_key: "FieldName_89"
kind: "field"
scene_type: 5
max_users: 100
group: 13
nation: "Arslan"
nation_copies: {"Arslan": 89, "Erion": 93, "Armia": 97}
zones: [127]
segments: ["ZP01_14"]
worldmap_rect: [1074, 34, 1124, 126]
gates:
  - {"gate": 1203, "x": 451.64, "z": 3629.45, "to_gate": 0, "to_field": 88, "label": "FieldName_89"}
  - {"gate": 1406, "x": 341.41, "z": 3784.99, "to_gate": 1407, "to_field": 89, "label": "FiledPortal"}
  - {"gate": 1407, "x": 448.52, "z": 3776.57, "to_gate": 1406, "to_field": 89, "label": "FiledPortal"}
connections:
  - {"to": 88, "gate": 1203, "to_gate": 1202, "paired": true}
  - {"to": 88, "gate": 1203, "to_gate": 0}
npcs: [198, 201, 239]
monsters: [604, 710, 711, 727, 728, 731, 732]
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=7295a2 type=7a94db id=16b06b sources=2f5ad7 name_key=ac3dd6 kind=7a94db scene_type=ac3478 max_users=310b86 group=bd307a nation=a20b0f nation_copies=0d80c7 zones=cf6862 segments=155293 worldmap_rect=3fc9a3 gates=bbedb3 connections=e238b5 npcs=2f2b06 monsters=c10cb0 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 127](../assets/zones/127.png) |
| **Field id** | `89` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 13 (SceneList last column) |
| **Nation** | Arslan |
| **Nation copies** | Arslan **89**, Erion [[wiki/fields/93-training-ground\|Erion (93)]], Armia [[wiki/fields/97-training-ground\|Armia (97)]] |
| **Zones** | [[wiki/zones/127-training-ground-a\|Training Ground A]] |
| **Terrain segments** | `ZP01_14` |
| **World-map rectangle** | `[1074, 34, 1124, 126]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_89` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1203 | 451.64, 3629.45 | [[wiki/fields/88-training-camp\|Training Camp]] | 1202 (paired, *inferred*) | FieldName_89 |
| 1406 | 341.41, 3784.99 | portal to gate 1407 in this field | 1407 | FiledPortal |
| 1407 | 448.52, 3776.57 | portal to gate 1406 in this field | 1406 | FiledPortal |

Entered from: [[wiki/fields/88-training-camp|Training Camp]] (gate 1202 → 1203)

### NPCs

Positions come from the NPC's own page (`x`, `z`). The client does not place town NPCs; the server spawns them ([[gameplay/npc-locations|NPC locations]] §1).

| NPC | unit | position | why it is listed |
|---|---|---|---|
| [[wiki/npcs/198-frei\|Frei]] | 198 |  | quests [[wiki/quests/6-the-1st-challenge-chepas-ahead\|6]] |
| [[wiki/npcs/201-shaia\|Shaia]] | 201 | 423.9, 3664.8 | quests [[wiki/quests/1-on-to-a-promising-start\|1]], [[wiki/quests/2-the-slime-is-mine\|2]], [[wiki/quests/5-united-problem-solvers\|5]], [[wiki/quests/7-the-1st-challenge-chepas-ahead\|7]], [[wiki/quests/45-the-1st-challenge-chepas-ahead\|45]] …; [[gameplay/npc-locations#5. Training Ground (fields 89 / 93 / 97)\|NPC locations § 5. Training Ground (fields 89 / 93 / 97)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/239-floyd\|Floyd]] | 239 | 370.5, 3660.6 | quests [[wiki/quests/3-the-task-at-hand\|3]], [[wiki/quests/4-go-to-shaia\|4]]; [[gameplay/npc-locations#5. Training Ground (fields 89 / 93 / 97)\|NPC locations § 5. Training Ground (fields 89 / 93 / 97)]]; NPC page (`map` / `positions`) |

### Monsters

| monster | unit | why it is listed |
|---|---|---|
| [[wiki/monsters/604-slime\|Slime]] | 604 | kill objective of quest [[wiki/quests/2-the-slime-is-mine\|2]]; monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/710-chepa-warrior-officer\|Chepa Warrior Officer]] | 710 | kill objective of quest [[wiki/quests/7-the-1st-challenge-chepas-ahead\|7]]; monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/711-chepa-archer-officer\|Chepa Archer Officer]] | 711 | kill objective of quest [[wiki/quests/7-the-1st-challenge-chepas-ahead\|7]]; monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/727-chepa-warrior\|Chepa Warrior]] | 727 | kill objective of quest [[wiki/quests/100-hunting-for-furs\|100]]; monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/728-chepa-archer\|Chepa Archer]] | 728 | kill objective of quest [[wiki/quests/100-hunting-for-furs\|100]]; monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/731-bee\|Bee]] | 731 | kill objective of quest [[wiki/quests/3-the-task-at-hand\|3]]; monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/732-cobra\|Cobra]] | 732 | kill objective of quest [[wiki/quests/3-the-task-at-hand\|3]]; monster page (`spawns` / `spawn_fields`) |

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

Current server (`server/world.py`, our choice, not original data): players appear at (419, 3661) in scene 89.

### Quests in this field

[[wiki/quests/1-on-to-a-promising-start|On to a promising start]], [[wiki/quests/2-the-slime-is-mine|The Slime is mine]], [[wiki/quests/3-the-task-at-hand|The task at hand]], [[wiki/quests/4-go-to-shaia|Go to Shaia]], [[wiki/quests/5-united-problem-solvers|United Problem Solvers]], [[wiki/quests/7-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]]

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP01_14 | yes | yes |

### Mentioned in

- [[gameplay/README#Pages|Gameplay § Pages]]
- [[gameplay/maps-and-dungeons#1. The world (Gaia)|Maps and dungeons § 1. The world (Gaia)]]
- [[gameplay/npc-locations#5. Training Ground (fields 89 / 93 / 97)|NPC and point-of-interest locations § 5. Training Ground (fields 89 / 93 / 97)]]
- [[gameplay/video-character-creation-and-tutorial#6. Differences from other builds|Video notes: character creation and tutorial (ZonderCoRe, June 2018) § 6. Differences from other builds]]
- [[gameplay/video-early-quests#Video notes: first session, levels 1+ (charmanmugen)|Video notes: first session, levels 1+ (charmanmugen) § Video notes: first session, levels 1+ (charmanmugen)]] — at [3:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=210s)
- [[gameplay/video-tutorial-walkthrough#1. Tutorial and early quest flow|Video notes: tutorial walkthrough (Bravely Forward 2) § 1. Tutorial and early quest flow]]
- [[gameplay/patch-history|Patch notes and other sources]] (by name)
- [[gameplay/sources|Sources and gaps]] (by name)
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
