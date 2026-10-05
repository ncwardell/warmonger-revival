---
title: "Abyss LV3 110 (Prison)"
type: "zone"
id: 115
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 115", "client: ZoneDB name 어비스_LV3_110 (abyss zones are named after their field)", "client + image: [[gameplay/abyss-map]] Fields and layout, How the image was read"]
name_kr: "어비스_LV3_110"
terrain: "Abyss_Lv03"
bounds: {"x0": 800, "z0": 2592, "x1": 991, "z1": 2783}
size: [192, 192]
segments: ["ZP03_10"]
fields: [110]
minimap: "map/minimap/minimap_z115_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=2fc736 type=c899cd id=efa6e4 sources=62ba9d name_kr=7d0c7a terrain=9d7327 bounds=018daa size=be57ee segments=9fb9ce fields=e04b44 minimap=024e87 -->
|  |  |
|---|---|
|  | ![minimap of Abyss LV3 110 (Prison)](../assets/zones/115.png) |
| **Zone id** | `115` |
| **ZoneDB name** | 어비스_LV3_110 (English gloss: Abyss LV3 110 (Prison)) |
| **Terrain name** | `Abyss_Lv03` |
| **Rectangle** | x 800–991, z 2592–2783 (192 × 192 units) |
| **Fields** | [[wiki/fields/110-prison\|Prison]] |
| **Minimap** | `map/minimap/minimap_z115_00.dds` |
| **Lighting** | `Setting/weather/Abyss_Lv03.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP03_10 | yes | yes |
<!-- generated:end -->

## Notes

- Abyss tile of field 110. Each Abyss field fills one 256-unit segment on a grid from x = 256, z = 2048; the tier is the `LV<n>` in the zone name. On the stitched player map the minimap is north-up (+x right, +z up) and shows about 175 units around the rectangle's centre, at about 1.53 px per unit ([[gameplay/abyss-map|Abyss map]]). *client + image*

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
