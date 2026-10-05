---
title: "Abyss LV3 111 (The land of Greed)"
type: "zone"
id: 116
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 116", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client + image: [[gameplay/abyss-map]] Fields and layout, How the image was read"]
name_kr: "어비스_LV3_111"
terrain: "Abyss_Lv03"
bounds: {"x0": 1056, "z0": 2592, "x1": 1247, "z1": 2783}
size: [192, 192]
segments: ["ZP04_10"]
fields: [111]
minimap: "map/minimap/minimap_z116_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=31f7dd type=c899cd id=683e72 sources=c227a4 name_kr=225cc2 terrain=9d7327 bounds=dd094f size=be57ee segments=217b74 fields=6d958c minimap=f1bb50 -->
|  |  |
|---|---|
|  | ![minimap of Abyss LV3 111 (The land of Greed)](../assets/zones/116.png) |
| **Zone id** | `116` |
| **ZoneDB name** | 어비스_LV3_111 (English gloss: Abyss LV3 111 (The land of Greed)) |
| **Terrain name** | `Abyss_Lv03` |
| **Rectangle** | x 1056–1247, z 2592–2783 (192 × 192 units) |
| **Fields** | [[wiki/fields/111-the-land-of-greed\|The land of Greed]] |
| **Minimap** | `map/minimap/minimap_z116_00.dds` |
| **Lighting** | `Setting/weather/Abyss_Lv03.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP04_10 | yes | yes |
<!-- generated:end -->

## Notes

- Abyss tile of field 111. Each Abyss field fills one 256-unit segment on a grid from x = 256, z = 2048; the tier is the `LV<n>` in the zone name. On the stitched player map the minimap is north-up (+x right, +z up) and shows about 175 units around the rectangle's centre, at about 1.53 px per unit ([[gameplay/abyss-map|Abyss map]]). *client + image*

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
