---
title: "Training Ground"
type: "field"
id: 97
status: "partial"
missing: ["spawn_points"]
sources: ["client: SceneList.cdb id 97", "client: Quest.cdb map1..3", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 97", "client: Quest.cdb (quests and objectives in field 97)", "doc: gameplay/npc-locations § 5. Training Ground (fields 89 / 93 / 97)", "video: [[gameplay/video-tutorial-walkthrough]] §1 steps 2-18 and §3 Monsters (monster areas), video", "video: [[gameplay/video-character-creation-and-tutorial]] §3-§6 (Erion copy: spawn, Shaia, Floyd, officers in the north arena), video-measured", "video: [[gameplay/video-early-quests]] §1 map order, §2 quests 1-7, §3 Shaia/Floyd sightings, video"]
name_key: "FieldName_97"
kind: "field"
scene_type: 5
max_users: 100
group: 13
nation: "Armia"
nation_copies: {"Arslan": 89, "Erion": 93, "Armia": 97}
zones: [132]
segments: ["ZP03_14"]
gates:
  - {"gate": 1209, "x": 965.08, "z": 3630.76, "to_gate": 0, "to_field": 96, "label": "FieldName_97"}
  - {"gate": 1404, "x": 853.96, "z": 3781.87, "to_gate": 1405, "to_field": 97, "label": "FiledPortal"}
  - {"gate": 1405, "x": 960.05, "z": 3776.06, "to_gate": 1404, "to_field": 97, "label": "FiledPortal"}
connections:
  - {"to": 96, "gate": 1209, "to_gate": 1208, "paired": true}
  - {"to": 96, "gate": 1209, "to_gate": 0}
npcs: [198, 201, 239]
monsters: [604, 710, 711, 727, 728, 731, 732]
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=7295a2 type=7a94db id=812ed4 sources=35bffa name_key=a7a879 kind=7a94db scene_type=ac3478 max_users=310b86 group=bd307a nation=b0e09b nation_copies=0d80c7 zones=67f0ac segments=de7743 gates=600dea connections=6a1bb5 npcs=2f2b06 monsters=c10cb0 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 132](../assets/zones/132.png) |
| **Field id** | `97` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 13 (SceneList last column) |
| **Nation** | Armia |
| **Nation copies** | Arslan [[wiki/fields/89-training-ground\|Arslan (89)]], Erion [[wiki/fields/93-training-ground\|Erion (93)]], Armia **97** |
| **Zones** | [[wiki/zones/132-training-ground-c\|Training Ground C]] |
| **Terrain segments** | `ZP03_14` |
| **Name key** | `FieldName_97` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1209 | 965.08, 3630.76 | [[wiki/fields/96-training-camp\|Training Camp]] | 1208 (paired, *inferred*) | FieldName_97 |
| 1404 | 853.96, 3781.87 | portal to gate 1405 in this field | 1405 | FiledPortal |
| 1405 | 960.05, 3776.06 | portal to gate 1404 in this field | 1404 | FiledPortal |

Entered from: [[wiki/fields/96-training-camp|Training Camp]] (gate 1208 → 1209)

### NPCs

Positions come from the NPC's own page (`x`, `z`). The client does not place town NPCs; the server spawns them ([[gameplay/npc-locations|NPC locations]] §1).

| NPC | unit | position | why it is listed |
|---|---|---|---|
| [[wiki/npcs/198-frei\|Frei]] | 198 |  | quests [[wiki/quests/6-the-1st-challenge-chepas-ahead\|6]] |
| [[wiki/npcs/201-shaia\|Shaia]] | 201 | 935.9, 3664.8 | quests [[wiki/quests/1-on-to-a-promising-start\|1]], [[wiki/quests/2-the-slime-is-mine\|2]], [[wiki/quests/5-united-problem-solvers\|5]], [[wiki/quests/7-the-1st-challenge-chepas-ahead\|7]], [[wiki/quests/45-the-1st-challenge-chepas-ahead\|45]]; [[gameplay/npc-locations#5. Training Ground (fields 89 / 93 / 97)\|NPC locations § 5. Training Ground (fields 89 / 93 / 97)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/239-floyd\|Floyd]] | 239 | 882.5, 3660.6 | quests [[wiki/quests/3-the-task-at-hand\|3]], [[wiki/quests/4-go-to-shaia\|4]]; [[gameplay/npc-locations#5. Training Ground (fields 89 / 93 / 97)\|NPC locations § 5. Training Ground (fields 89 / 93 / 97)]]; NPC page (`map` / `positions`) |

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
| ZP03_14 | yes | yes |

### Mentioned in

- [[gameplay/maps-and-dungeons#1. The world (Gaia)|Maps and dungeons § 1. The world (Gaia)]]
- [[gameplay/npc-locations#5. Training Ground (fields 89 / 93 / 97)|NPC and point-of-interest locations § 5. Training Ground (fields 89 / 93 / 97)]]
- [[gameplay/video-character-creation-and-tutorial#6. Differences from other builds|Video notes: character creation and tutorial (ZonderCoRe, June 2018) § 6. Differences from other builds]]
- [[gameplay/README|Gameplay]] (by name)
- [[gameplay/patch-history|Patch notes and other sources]] (by name)
- [[gameplay/sources|Sources and gaps]] (by name)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] (by name)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] (by name)
<!-- generated:end -->

## Notes

- New characters start here, not in field 117: both 2018 launch videos load the character straight into the Training Ground with quest 1 active ([[gameplay/video-tutorial-walkthrough|tutorial walkthrough video]] §1, [[gameplay/video-early-quests|first-session video]] §1, [[gameplay/video-character-creation-and-tutorial|character-creation video]] §6). This is the Armia copy; no video was recorded here. With the Erion spawn at local (174.3, 68.3) the spawn is about (942.3, 3652.3) (derived: all three copies share one mesh, [[gameplay/npc-locations|NPC locations]] §2)..
- Monster areas, in the order the quests send players: Slime (604) in the south; Bee (731) and Cobra (732) in the middle, on the "training hill"; Chepa Warrior (727) and Chepa Archer (728) in the round clearings of the northern lobes; the Chepa Warrior Officer (710) and Chepa Archer Officer (711) in the north-west clearing, among normal Chepas ([[gameplay/video-tutorial-walkthrough|tutorial walkthrough video]] §3 Monsters, step 18; [[gameplay/video-early-quests|first-session video]] §2 item 7 "spiral circle"; [[gameplay/video-character-creation-and-tutorial|character-creation video]] §3 step 15 "round stone arena in the north"). *video*
- Gate to the Training Camp is the south-east portal labelled "Training Camp"; every gate asks "Do you want to leave the area?" first ([[gameplay/video-tutorial-walkthrough|tutorial walkthrough video]] §3 Teleports used; [[gameplay/video-early-quests|first-session video]] §1). *video*
- On the world map the Training Camp, Castle and Training Ground form an island at the top ([[gameplay/video-tutorial-walkthrough|tutorial walkthrough video]] §3 UI). *video*
- Segment origin of this copy: (768, 3584). Positions in one copy carry over to the others by adding the origin difference ([[gameplay/npc-locations|NPC locations]] §2). *client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/video-tutorial-walkthrough|tutorial walkthrough video]], [[gameplay/video-early-quests|first-session video]], [[gameplay/video-character-creation-and-tutorial|character-creation video]]; segment origins from [[gameplay/npc-locations|NPC locations]] §2.

## Open questions

- Shaia: two 2018 videos measure her at about (433.5-433.8, 3662) in the Arslan copy, about 10 units east of the table value (423.9, 3664.8) in [[gameplay/npc-locations|NPC locations]] §5; the Erion-copy sighting (local 168.0, 79.5) agrees with the table ([[gameplay/video-tutorial-walkthrough|tutorial walkthrough video]] §2, [[gameplay/video-early-quests|first-session video]] §3, [[gameplay/video-character-creation-and-tutorial|character-creation video]] §4).
- Spawn points: the videos give the areas above but no per-monster coordinates, counts or respawn times.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
