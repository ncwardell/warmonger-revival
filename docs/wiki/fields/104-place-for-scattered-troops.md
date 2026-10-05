---
title: "Place for Scattered troops"
type: "field"
id: 104
status: "partial"
missing: ["spawn_points", "monsters", "npcs"]
sources: ["client: SceneList.cdb id 104", "client: ZoneDB name 어비스_LV2_104 (abyss zones are named after their field)", "image: [[gameplay/abyss-map]] Portal table (TR ≈ (962, 2499) to 100, BL ≈ (828, 2361) to 111), image-measured ±5 units"]
name_key: "FieldName_104"
kind: "field"
scene_type: 5
max_users: 100
group: 12
neighbours: [100]
zones: [118]
segments: ["ZP03_09"]
connections:
  - {"to": 100, "gate": null, "to_gate": null, "at": [962, 2499], "to_at": [718, 2104], "source": "image"}
  - {"to": 111, "gate": null, "to_gate": null, "at": [828, 2361], "to_at": [1215, 2623], "source": "image"}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=48ad72 type=7a94db id=78a8ef sources=84686a name_key=3cfc03 kind=7a94db scene_type=ac3478 max_users=310b86 group=7b5200 neighbours=023272 zones=9adea6 segments=cf1cca connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 118](../assets/zones/118.png) |
| **Field id** | `104` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 12 (SceneList last column) |
| **Zones** | [[wiki/zones/118-abyss-lv2-104-place-for-scattered-troops\|Abyss LV2 104 (Place for Scattered troops)]] |
| **Terrain segments** | `ZP03_09` |
| **Name key** | `FieldName_104` |

### Gates and connections

No `Teleport_List` row: the client places no gate here.

Neighbouring lands (`SceneList` link columns): [[wiki/fields/100-corpse-incineration|Corpse incineration]]

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
| ZP03_09 | yes | yes |

### Mentioned in

- [[gameplay/server-rules#Added from the source hunt (see ((gameplay/sources/Sources and gaps)))|Server rules checklist § Added from the source hunt (see ((gameplay/sources/Sources and gaps)))]]
- [[gameplay/abyss-map|Abyss map and portal graph]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/video-dungeon-run|Video notes: Nas Village dungeon run (ZonderCoRe)]] (by name)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] (by name)
<!-- generated:end -->

## Notes

- Abyss level 2 on the Erion route (100 → 104 → 111 → 113 → 114). Top-right portal (about 962, 2499) links to Corpse incineration 100; bottom-left portal (about 828, 2361) links to The land of Greed 111. Neither has a gate id in the client table ([[gameplay/abyss-map|Abyss map]]). *image*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

- Gate ids for both portals are missing from `Teleport_List` ([[gameplay/abyss-map|Abyss map]]: the real ids were probably server data).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
