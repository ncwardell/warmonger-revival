---
title: "Training Ground"
type: "field"
id: 93
status: "stub"
missing: ["spawn_points"]
sources: ["client: SceneList.cdb id 93", "client: Quest.cdb map1..3", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 93", "client: Quest.cdb (quests and objectives in field 93)", "doc: gameplay/npc-locations § 5. Training Ground (fields 89 / 93 / 97)"]
name_key: "FieldName_93"
kind: "field"
scene_type: 5
max_users: 100
group: 13
nation: "Erion"
nation_copies: {"Arslan": 89, "Erion": 93, "Armia": 97}
zones: [131]
segments: ["ZP02_14"]
gates:
  - {"gate": 1206, "x": 708.78, "z": 3630.78, "to_gate": 0, "to_field": 92, "label": "FieldName_93"}
  - {"gate": 1408, "x": 595.55, "z": 3781.26, "to_gate": 1409, "to_field": 93, "label": "FiledPortal"}
  - {"gate": 1409, "x": 704.68, "z": 3775.97, "to_gate": 1408, "to_field": 93, "label": "FiledPortal"}
connections:
  - {"to": 92, "gate": 1206, "to_gate": 1205, "paired": true}
  - {"to": 92, "gate": 1206, "to_gate": 0}
npcs: [198, 201, 239]
monsters: [604, 710, 711, 727, 728, 731, 732]
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=7295a2 type=7a94db id=08a352 sources=c74d3a name_key=e69f00 kind=7a94db scene_type=ac3478 max_users=310b86 group=bd307a nation=069950 nation_copies=0d80c7 zones=dd4512 segments=772a13 gates=9648e9 connections=c6874d npcs=2f2b06 monsters=c10cb0 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 131](wiki/assets/zones/131.png) |
| **Field id** | `93` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 13 (SceneList last column) |
| **Nation** | Erion |
| **Nation copies** | Arslan [[wiki/fields/89-training-ground\|Arslan (89)]], Erion **93**, Armia [[wiki/fields/97-training-ground\|Armia (97)]] |
| **Zones** | [[wiki/zones/131-training-ground-b\|Training Ground B]] |
| **Terrain segments** | `ZP02_14` |
| **Name key** | `FieldName_93` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1206 | 708.78, 3630.78 | [[wiki/fields/92-training-camp\|Training Camp]] | 1205 (paired, *inferred*) | FieldName_93 |
| 1408 | 595.55, 3781.26 | portal to gate 1409 in this field | 1409 | FiledPortal |
| 1409 | 704.68, 3775.97 | portal to gate 1408 in this field | 1408 | FiledPortal |

Entered from: [[wiki/fields/92-training-camp|Training Camp]] (gate 1205 → 1206)

### NPCs

Positions come from the NPC's own page (`x`, `z`). The client does not place town NPCs; the server spawns them ([[gameplay/npc-locations|NPC locations]] §1).

| NPC | unit | position | why it is listed |
|---|---|---|---|
| [[wiki/npcs/198-frei\|Frei]] | 198 |  | quests [[wiki/quests/6-the-1st-challenge-chepas-ahead\|6]] |
| [[wiki/npcs/201-shaia\|Shaia]] | 201 | 680, 3663.5 | quests [[wiki/quests/1-on-to-a-promising-start\|1]], [[wiki/quests/2-the-slime-is-mine\|2]], [[wiki/quests/5-united-problem-solvers\|5]], [[wiki/quests/7-the-1st-challenge-chepas-ahead\|7]], [[wiki/quests/45-the-1st-challenge-chepas-ahead\|45]]; [[gameplay/npc-locations#5. Training Ground (fields 89 / 93 / 97)\|NPC locations § 5. Training Ground (fields 89 / 93 / 97)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/239-floyd\|Floyd]] | 239 | 625.9, 3660.5 | quests [[wiki/quests/3-the-task-at-hand\|3]], [[wiki/quests/4-go-to-shaia\|4]]; [[gameplay/npc-locations#5. Training Ground (fields 89 / 93 / 97)\|NPC locations § 5. Training Ground (fields 89 / 93 / 97)]]; NPC page (`map` / `positions`) |

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

### Quests in this field

[[wiki/quests/1-on-to-a-promising-start|On to a promising start]], [[wiki/quests/2-the-slime-is-mine|The Slime is mine]], [[wiki/quests/3-the-task-at-hand|The task at hand]], [[wiki/quests/4-go-to-shaia|Go to Shaia]], [[wiki/quests/5-united-problem-solvers|United Problem Solvers]], [[wiki/quests/7-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]]

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP02_14 | yes | yes |

### Mentioned in

- [[gameplay/maps-and-dungeons#1. The world (Gaia)|Maps and dungeons § 1. The world (Gaia)]]
- [[gameplay/npc-locations#5. Training Ground (fields 89 / 93 / 97)|NPC and point-of-interest locations § 5. Training Ground (fields 89 / 93 / 97)]]
- [[gameplay/video-character-creation-and-tutorial#Video notes: character creation and tutorial (ZonderCoRe, June 2018)|Video notes: character creation and tutorial (ZonderCoRe, June 2018) § Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/video-character-creation-and-tutorial#Training Ground (field 93)|Video notes: character creation and tutorial (ZonderCoRe, June 2018) § Training Ground (field 93)]]
- [[gameplay/video-character-creation-and-tutorial#6. Differences from other builds|Video notes: character creation and tutorial (ZonderCoRe, June 2018) § 6. Differences from other builds]]
- [[gameplay/README|Gameplay]] (by name)
- [[gameplay/patch-history|Patch notes and other sources]] (by name)
- [[gameplay/sources|Sources and gaps]] (by name)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] (by name)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] (by name)
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
