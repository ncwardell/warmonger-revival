---
title: "Battlefield tutorial (Sinking Nest)"
type: "zone"
id: 126
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 126", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "doc: gameplay/video-dungeon-run §1 (Nas Village Entrance geometry = ZoneDB 126; guess)", "video: [[gameplay/video-dungeon-run]] §1-§2 (minimap shape; 192-unit square centred on the 192×128 rect)"]
name_kr: "전장 튜토리얼"
terrain: "Battlefield_Tutorial_01"
bounds: {"x0": 1312, "z0": 2848, "x1": 1503, "z1": 2975}
size: [192, 128]
segments: ["ZP05_11"]
fields: [119, 133]
minimap: "map/minimap/minimap_z126_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=38862e type=c899cd id=114d4e sources=45b9e5 name_kr=19e183 terrain=e7f954 bounds=6b1809 size=681360 segments=5a389d fields=1a22c5 minimap=88471b -->
|  |  |
|---|---|
|  | ![minimap of Battlefield tutorial (Sinking Nest)](../assets/zones/126.png) |
| **Zone id** | `126` |
| **ZoneDB name** | 전장 튜토리얼 (English gloss: Battlefield tutorial (Sinking Nest)) |
| **Terrain name** | `Battlefield_Tutorial_01` |
| **Rectangle** | x 1312–1503, z 2848–2975 (192 × 128 units) |
| **Fields** | [[wiki/fields/119-sinking-nest\|Sinking Nest]], [[wiki/fields/133-sinking-nest-crystal\|Sinking Nest (Crystal)]] |
| **Minimap** | `map/minimap/minimap_z126_00.dds` |
| **Fog map** | `map/fogmap/Fog_z126.dds` |
| **Lighting** | `Setting/weather/Battlefield_Tutorial_01.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP05_11 | yes | yes |

### Mentioned in

- [[gameplay/server-rules#Added from the Warmonger forum and videos (round 2)|Server rules checklist § Added from the Warmonger forum and videos (round 2)]]
- [[gameplay/video-dungeon-run#1. Field id and map|Video notes: Nas Village dungeon run (ZonderCoRe) § 1. Field id and map]]
<!-- generated:end -->

## Notes

- Geometry of the event dungeon Nas Village Entrance (field 133): this is the only minimap with a diagonal chain of six round chambers, the shape on the in-game minimap ([[gameplay/video-dungeon-run|dungeon-run video notes]] §1). *client + video*
- The minimap covers a 192 × 192 square centred on the 192 × 128 rectangle: x = 1312 + u·192, z = 3008 − v·192; the portal icon lands within 2 units of gate 1200 ([[gameplay/video-dungeon-run|dungeon-run video notes]] §1). *video + client*

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
