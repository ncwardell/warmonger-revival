---
title: "Ashcolor Hill"
type: "field"
id: 53
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 53", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 53"]
name_key: "FieldName_53"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 2
neighbours: [50, 54, 58]
zones: [71]
segments: ["ZP13_04"]
worldmap_rect: [1243, 644, 1307, 695]
gates:
  - {"gate": 602, "x": 3394.06, "z": 1146.04, "to_gate": 630, "to_field": 50, "label": "FieldName_53"}
  - {"gate": 640, "x": 3487.21, "z": 1086.45, "to_gate": 631, "to_field": 54, "label": "FieldName_53"}
  - {"gate": 680, "x": 3471.42, "z": 1192.87, "to_gate": 632, "to_field": 58, "label": "FieldName_53"}
connections:
  - {"to": 50, "gate": 602, "to_gate": 630}
  - {"to": 54, "gate": 640, "to_gate": 631}
  - {"to": 58, "gate": 680, "to_gate": 632}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=577ab7 type=7a94db id=c5b76d sources=d89fe1 name_key=b8711a kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=da4b92 neighbours=58ede3 zones=c845c2 segments=69ba53 worldmap_rect=aa6245 gates=845dd2 connections=b96b81 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 71](../assets/zones/71.png) |
| **Field id** | `53` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/71-field-53-ashcolor-hill\|Field 53 (Ashcolor Hill)]] |
| **Terrain segments** | `ZP13_04` |
| **World-map rectangle** | `[1243, 644, 1307, 695]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_53` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 602 | 3394.06, 1146.04 | [[wiki/fields/50-eclipsed-road\|Eclipsed Road]] | 630 | FieldName_53 |
| 640 | 3487.21, 1086.45 | [[wiki/fields/54-rotten-twig-wood\|Rotten Twig Wood]] | 631 | FieldName_53 |
| 680 | 3471.42, 1192.87 | [[wiki/fields/58-evil-s-wood\|Evil's Wood]] | 632 | FieldName_53 |

Entered from: [[wiki/fields/50-eclipsed-road|Eclipsed Road]] (gate 630 → 602), [[wiki/fields/54-rotten-twig-wood|Rotten Twig Wood]] (gate 631 → 640), [[wiki/fields/58-evil-s-wood|Evil's Wood]] (gate 632 → 680)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/50-eclipsed-road|Eclipsed Road]], [[wiki/fields/54-rotten-twig-wood|Rotten Twig Wood]], [[wiki/fields/58-evil-s-wood|Evil's Wood]]

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
| ZP13_04 | yes | yes |

### Mentioned in

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
