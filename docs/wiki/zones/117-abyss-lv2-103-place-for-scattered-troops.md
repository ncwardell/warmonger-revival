---
title: "Abyss LV2 103 (Place for Scattered troops)"
type: "zone"
id: 117
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 117", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client + image: [[gameplay/abyss-map]] Fields and layout, How the image was read"]
name_kr: "어비스_LV2_103"
terrain: "Abyss_Lv02"
bounds: {"x0": 544, "z0": 2336, "x1": 735, "z1": 2527}
size: [192, 192]
segments: ["ZP02_09"]
fields: [103]
minimap: "map/minimap/minimap_z117_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=4ec317 type=c899cd id=d0e2db sources=d4b1c3 name_kr=def003 terrain=b8c94a bounds=15901d size=be57ee segments=f311d2 fields=435205 minimap=1e4aea -->
|  |  |
|---|---|
|  | ![minimap of Abyss LV2 103 (Place for Scattered troops)](../assets/zones/117.png) |
| **Zone id** | `117` |
| **ZoneDB name** | 어비스_LV2_103 (English gloss: Abyss LV2 103 (Place for Scattered troops)) |
| **Terrain name** | `Abyss_Lv02` |
| **Rectangle** | x 544–735, z 2336–2527 (192 × 192 units) |
| **Fields** | [[wiki/fields/103-place-for-scattered-troops\|Place for Scattered troops]] |
| **Minimap** | `map/minimap/minimap_z117_00.dds` |
| **Lighting** | `Setting/weather/Abyss_Lv02.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP02_09 | yes | yes |
<!-- generated:end -->

## Notes

- Abyss tile of field 103. Each Abyss field fills one 256-unit segment on a grid from x = 256, z = 2048; the tier is the `LV<n>` in the zone name. On the stitched player map the minimap is north-up (+x right, +z up) and shows about 175 units around the rectangle's centre, at about 1.53 px per unit ([[gameplay/abyss-map|Abyss map]]). *client + image*

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
