---
title: "Cracked Earth"
type: "field"
id: 63
status: "partial"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 63", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 63", "video: [[gameplay/video-character-creation-and-tutorial]] §3 step 23 (Erion Scroll: Gaia arrival beside a Nexus that moves the player to the Fortress), video"]
name_key: "FieldName_63"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 1
scene_c10: 1
neighbours: [60, 72, 64]
zones: [80]
segments: ["ZP03_05"]
worldmap_rect: [1323, 433, 1384, 487]
gates:
  - {"gate": 702, "x": 862.81, "z": 1359.98, "to_gate": 730, "to_field": 60, "label": "FieldName_63"}
  - {"gate": 741, "x": 941.13, "z": 1370.6, "to_gate": 731, "to_field": 64, "label": "FieldName_63"}
  - {"gate": 820, "x": 904.15, "z": 1462.26, "to_gate": 732, "to_field": 72, "label": "FieldName_63"}
connections:
  - {"to": 60, "gate": 702, "to_gate": 730}
  - {"to": 64, "gate": 741, "to_gate": 731}
  - {"to": 72, "gate": 820, "to_gate": 732}
  - {"to": 120, "gate": null, "to_gate": null, "via": "nexus", "source": "video"}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=a8f177 type=7a94db id=a17554 sources=ecacf1 name_key=43dc7e kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=356a19 scene_c10=356a19 neighbours=f4e308 zones=0bda79 segments=fb777a worldmap_rect=991ecd gates=38ad42 connections=67c207 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 80](wiki/assets/zones/80.png) |
| **Field id** | `63` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/80-field-63-cracked-earth\|Field 63 (Cracked Earth)]] |
| **Terrain segments** | `ZP03_05` |
| **World-map rectangle** | `[1323, 433, 1384, 487]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_63` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 702 | 862.81, 1359.98 | [[wiki/fields/60-volcano-heart\|Volcano Heart]] | 730 | FieldName_63 |
| 741 | 941.13, 1370.6 | [[wiki/fields/64-thunderstorm-canyon\|Thunderstorm Canyon]] | 731 | FieldName_63 |
| 820 | 904.15, 1462.26 | [[wiki/fields/72-refuge\|Refuge]] | 732 | FieldName_63 |

Other connections (hand-entered): to 120, gate None, to_gate None, via nexus, source video

Entered from: [[wiki/fields/60-volcano-heart|Volcano Heart]] (gate 730 → 702), [[wiki/fields/64-thunderstorm-canyon|Thunderstorm Canyon]] (gate 731 → 741), [[wiki/fields/72-refuge|Refuge]] (gate 732 → 820)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/60-volcano-heart|Volcano Heart]], [[wiki/fields/72-refuge|Refuge]], [[wiki/fields/64-thunderstorm-canyon|Thunderstorm Canyon]]

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
| ZP03_05 | yes | yes |

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial#Training Camp (field 92) and back|Video notes: character creation and tutorial (ZonderCoRe, June 2018) § Training Camp (field 92) and back]] — at [21:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1270s)
<!-- generated:end -->

## Notes

- The Erion player of the June 2018 relaunch landed here with the first Scroll: Gaia, standing beside a Nexus; clicking it opened the world map with a Fortress / Owner Legion panel and moved the player to the Fortress ([[gameplay/video-character-creation-and-tutorial|character-creation video]] §3 step 23). *video*

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
