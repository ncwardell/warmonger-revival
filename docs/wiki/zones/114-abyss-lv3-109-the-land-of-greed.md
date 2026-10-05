---
title: "Abyss LV3 109 (The land of Greed)"
type: "zone"
id: 114
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 114", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client + image: [[gameplay/abyss-map]] Fields and layout, How the image was read"]
name_kr: "어비스_LV3_109"
terrain: "Abyss_Lv03"
bounds: {"x0": 544, "z0": 2592, "x1": 735, "z1": 2783}
size: [192, 192]
segments: ["ZP02_10"]
fields: [109]
minimap: "map/minimap/minimap_z114_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=6c7f23 type=c899cd id=ecb793 sources=093943 name_kr=ee45c7 terrain=9d7327 bounds=0d1b8f size=be57ee segments=8c2f3b fields=4d9714 minimap=ca2c06 -->
|  |  |
|---|---|
|  | ![minimap of Abyss LV3 109 (The land of Greed)](wiki/assets/zones/114.png) |
| **Zone id** | `114` |
| **ZoneDB name** | 어비스_LV3_109 (English gloss: Abyss LV3 109 (The land of Greed)) |
| **Terrain name** | `Abyss_Lv03` |
| **Rectangle** | x 544–735, z 2592–2783 (192 × 192 units) |
| **Fields** | [[wiki/fields/109-the-land-of-greed\|The land of Greed]] |
| **Minimap** | `map/minimap/minimap_z114_00.dds` |
| **Lighting** | `Setting/weather/Abyss_Lv03.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP02_10 | yes | yes |
<!-- generated:end -->

## Notes

- Abyss tile of field 109. Each Abyss field fills one 256-unit segment on a grid from x = 256, z = 2048; the tier is the `LV<n>` in the zone name. On the stitched player map the minimap is north-up (+x right, +z up) and shows about 175 units around the rectangle's centre, at about 1.53 px per unit ([[gameplay/abyss-map|Abyss map]]). *client + image*

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
