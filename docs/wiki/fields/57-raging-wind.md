---
title: "Raging Wind"
type: "field"
id: 57
status: "stub"
missing: ["spawn_points", "monsters"]
sources: ["client: SceneList.cdb id 57", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 57"]
name_key: "FieldName_57"
kind: "land"
scene_type: 2
max_users: 30
group: 3
scene_c4: 2
neighbours: [54, 58, 66]
zones: [74]
segments: ["ZP17_04"]
worldmap_rect: [1349, 709, 1409, 761]
gates:
  - {"gate": 642, "x": 4394.02, "z": 1084.51, "to_gate": 670, "to_field": 54, "label": "FieldName_57"}
  - {"gate": 681, "x": 4458.27, "z": 1195.36, "to_gate": 671, "to_field": 58, "label": "FieldName_57"}
  - {"gate": 760, "x": 4507.83, "z": 1066.55, "to_gate": 672, "to_field": 66, "label": "FieldName_57"}
connections:
  - {"to": 54, "gate": 642, "to_gate": 670}
  - {"to": 58, "gate": 681, "to_gate": 671}
  - {"to": 66, "gate": 760, "to_gate": 672}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=305095 type=7a94db id=9109c8 sources=1a4654 name_key=7c7611 kind=8e3535 scene_type=da4b92 max_users=22d200 group=77de68 scene_c4=da4b92 neighbours=d5e0a7 zones=2895ec segments=4f60f3 worldmap_rect=15fa37 gates=94078f connections=b8ddf7 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 74](../assets/zones/74.png) |
| **Field id** | `57` |
| **Kind** | land (SceneList type 2; name *inferred*) |
| **Max users** | 30 (SceneList, column meaning *guessed*) |
| **Region group** | 3 (SceneList last column) |
| **Zones** | [[wiki/zones/74-field-57-raging-wind\|Field 57 (Raging Wind)]] |
| **Terrain segments** | `ZP17_04` |
| **World-map rectangle** | `[1349, 709, 1409, 761]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_57` |

A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 642 | 4394.02, 1084.51 | [[wiki/fields/54-rotten-twig-wood\|Rotten Twig Wood]] | 670 | FieldName_57 |
| 681 | 4458.27, 1195.36 | [[wiki/fields/58-evil-s-wood\|Evil's Wood]] | 671 | FieldName_57 |
| 760 | 4507.83, 1066.55 | [[wiki/fields/66-earth-of-abyss\|Earth of Abyss]] | 672 | FieldName_57 |

Entered from: [[wiki/fields/54-rotten-twig-wood|Rotten Twig Wood]] (gate 670 → 642), [[wiki/fields/58-evil-s-wood|Evil's Wood]] (gate 671 → 681), [[wiki/fields/66-earth-of-abyss|Earth of Abyss]] (gate 672 → 760)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/54-rotten-twig-wood|Rotten Twig Wood]], [[wiki/fields/58-evil-s-wood|Evil's Wood]], [[wiki/fields/66-earth-of-abyss|Earth of Abyss]]

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
| ZP17_04 | yes | yes |

### Mentioned in

- [[gameplay/video-dungeon-run#1. Field id and map|Video notes: Nas Village dungeon run (ZonderCoRe) § 1. Field id and map]]
- [[gameplay/video-dungeon-run#7. Timestamped log|Video notes: Nas Village dungeon run (ZonderCoRe) § 7. Timestamped log]]
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
