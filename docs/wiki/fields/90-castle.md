---
title: "Castle"
type: "field"
id: 90
status: "complete"
missing: []
sources: ["client: SceneList.cdb id 90", "client: Quest.cdb map1..3", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 90", "client: Quest.cdb (quests and objectives in field 90)", "video: [[gameplay/video-early-quests]] §3 NPCs, Castle 90 positions (Bernice, Patrick, Krister, Kesley, Bell Thain), video-measured ±4-8 units", "video: [[gameplay/video-tutorial-walkthrough]] §1 step 29 (Imperial Guards at the entrance), video", "client + video: [[gameplay/npc-locations]] §6 (gates, portal offering 'move to Fortress')"]
name_key: "FieldName_90"
kind: "town"
scene_type: 1
max_users: 100
group: 13
nation: "Arslan"
nation_copies: {"Arslan": 90, "Erion": 94, "Armia": 98}
zones: [144]
segments: ["ZP01_16"]
worldmap_rect: [1172, 35, 1240, 76]
gates:
  - {"gate": 1199, "x": 318.07, "z": 4135.37, "to_gate": 0, "to_field": 88, "label": "FieldName_90"}
  - {"gate": 1410, "x": 315.24, "z": 4140.56, "to_gate": 1410, "to_field": 90, "label": "FieldName_90"}
connections:
  - {"to": 88, "gate": 1199, "to_gate": 1198, "paired": true}
  - {"to": 88, "gate": 1199, "to_gate": 0}
npcs: [219, 242, 327, 2001, 199, 224, 208]
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=b1fd66 type=7a94db id=2d0c8a sources=4fafc5 name_key=8f3ae6 kind=da9544 scene_type=356a19 max_users=310b86 group=bd307a nation=a20b0f nation_copies=95169d zones=610dd1 segments=ee0f85 worldmap_rect=e9d9e1 gates=5ed218 connections=fd2af1 npcs=540523 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 144](../assets/zones/144.png) |
| **Field id** | `90` |
| **Kind** | town (SceneList type 1; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 13 (SceneList last column) |
| **Nation** | Arslan |
| **Nation copies** | Arslan **90**, Erion [[wiki/fields/94-castle\|Erion (94)]], Armia [[wiki/fields/98-castle\|Armia (98)]] |
| **Zones** | [[wiki/zones/144-a-castle-big-city\|A Castle (big city)]] |
| **Terrain segments** | `ZP01_16` |
| **World-map rectangle** | `[1172, 35, 1240, 76]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_90` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1199 | 318.07, 4135.37 | [[wiki/fields/88-training-camp\|Training Camp]] | 1198 (paired, *inferred*) | FieldName_90 |
| 1410 | 315.24, 4140.56 | arrival / spawn point only | 1410 | FieldName_90 |

Entered from: [[wiki/fields/88-training-camp|Training Camp]] (gate 1198 → 1199)

### NPCs

Positions come from the NPC's own page (`x`, `z`). The client does not place town NPCs; the server spawns them ([[gameplay/npc-locations|NPC locations]] §1).

| NPC | unit | position | why it is listed |
|---|---|---|---|
| [[wiki/npcs/219-krister\|Krister]] | 219 | 489.7, 4139.6 | quests [[wiki/quests/106-talk-to-krister\|106]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/242-raon\|Raon]] | 242 |  | quests [[wiki/quests/1530-legion-create-core\|1530]] |
| [[wiki/npcs/327-aenes\|Aenes]] | 327 |  | quests [[wiki/quests/38-innocence-s-recovery-operation\|38]], [[wiki/quests/44-innocence-report\|44]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/2001-corpse-bride\|Corpse Bride]] | 2001 |  | quests [[wiki/quests/901-trick-or-treat\|901]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/199-patrick\|Patrick]] | 199 | 486.1, 4292.5 | NPC page (`map` / `positions`) |
| [[wiki/npcs/224-bernice\|Bernice]] | 224 | 493.8, 4285.8 | NPC page (`map` / `positions`) |

### Monsters

None known yet.

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Quests in this field

[[wiki/quests/38-innocence-s-recovery-operation|Innocence's recovery operation]], [[wiki/quests/106-talk-to-krister|Talk to Krister]], [[wiki/quests/901-trick-or-treat|Trick or Treat!!]]

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP01_16 | yes | yes |

### Mentioned in

- [[gameplay/maps-and-dungeons#1. The world (Gaia)|Maps and dungeons § 1. The world (Gaia)]]
- [[gameplay/npc-locations#6. Village (87/91/95), Castle (90/94/98), tutorial (117)|NPC and point-of-interest locations § 6. Village (87/91/95), Castle (90/94/98), tutorial (117)]]
- [[gameplay/video-tutorial-walkthrough#Steps|Video notes: tutorial walkthrough (Bravely Forward 2) § Steps]] — at [31:10](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1870s)
<!-- generated:end -->

## Notes

- Arslan copy of the Castle. NPC positions (measured here): Bernice (224) 493.8, 4285.8; Patrick (199) 486.1, 4292.5; Krister (219) 489.7, 4139.6; Kesley 480.8, 4146.2; Bell Thain (208) about 482, 4122 ([[gameplay/video-early-quests|first-session video]] §3, [58:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=3480s)-[59:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=3541s)). Bell Thain (Training Officer, 208) is listed here from that sighting; he also stands in the Fortress. *video*
- Imperial Guards (red armour, halberds; UnitDB 189-197) stand at the entrance from the Training Camp, and four or more stand on the plaza near Bernice ([[gameplay/video-tutorial-walkthrough|tutorial walkthrough video]] §1 step 29; [[gameplay/video-early-quests|first-session video]] §3). *video*
- A portal in the Castle offers "move to Fortress" ([video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=1876s), [[gameplay/npc-locations|NPC locations]] §6). Players also arrive by Scroll: Castle (quest 19) or Haley's Castle teleport (10,000 gold) ([[gameplay/video-early-quests|first-session video]] §1; [[gameplay/maps-and-dungeons|Maps and dungeons]] §1). *video + image*
- Bernice offers a nation change to a disaffected player; the nation is per account and is changed at the castle ([[gameplay/video-early-quests|first-session video]] §2 quest 22; [[gameplay/classes-and-legions|Classes and legions]] §2). Gear, weapons and elixirs could also be crafted at the nation castle ([[gameplay/events-and-schedules|Events and schedules]]). *video + guide*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/video-early-quests|first-session video]], [[gameplay/video-tutorial-walkthrough|tutorial walkthrough video]], [[gameplay/npc-locations|NPC locations]], [[gameplay/classes-and-legions|Classes and legions]].

## Open questions

- The Castle's Kesley (Legion Administrator) may be unit 210 (the Fortress Kesley) or 318, a second Kesley row in UnitDB; the video page leaves it as "210 (318?)" ([[gameplay/video-early-quests|first-session video]] §3), so neither id is listed here yet.
- Which of the nine Imperial Guard rows (189-197, three models) belong to which nation's castle is not known.
- The position of the "move to Fortress" portal was not measured.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
