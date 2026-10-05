---
title: "Abyss LV2 105 (Place for Scattered troops)"
type: "zone"
id: 119
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 119", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client + image: [[gameplay/abyss-map]] Fields and layout, How the image was read"]
name_kr: "어비스_LV2_105"
terrain: "Abyss_Lv02"
bounds: {"x0": 1056, "z0": 2336, "x1": 1247, "z1": 2527}
size: [192, 192]
segments: ["ZP04_09"]
fields: [105]
minimap: "map/minimap/minimap_z119_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=cad9b1 type=c899cd id=a2e33d sources=33cca3 name_kr=1ff268 terrain=b8c94a bounds=d8cb63 size=be57ee segments=1c4a8d fields=355b7f minimap=9f4f34 -->
|  |  |
|---|---|
|  | ![minimap of Abyss LV2 105 (Place for Scattered troops)](../assets/zones/119.png) |
| **Zone id** | `119` |
| **ZoneDB name** | 어비스_LV2_105 (English gloss: Abyss LV2 105 (Place for Scattered troops)) |
| **Terrain name** | `Abyss_Lv02` |
| **Rectangle** | x 1056–1247, z 2336–2527 (192 × 192 units) |
| **Fields** | [[wiki/fields/105-place-for-scattered-troops\|Place for Scattered troops]] |
| **Minimap** | `map/minimap/minimap_z119_00.dds` |
| **Lighting** | `Setting/weather/Abyss_Lv02.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP04_09 | yes | yes |
<!-- generated:end -->

## Notes

- Abyss tile of field 105. Each Abyss field fills one 256-unit segment on a grid from x = 256, z = 2048; the tier is the `LV<n>` in the zone name. On the stitched player map the minimap is north-up (+x right, +z up) and shows about 175 units around the rectangle's centre, at about 1.53 px per unit ([[gameplay/abyss-map|Abyss map]]). *client + image*

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
