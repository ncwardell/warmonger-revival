---
title: "Abyss LV5 114 (The way go to devildom)"
type: "zone"
id: 124
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 124", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client + image: [[gameplay/abyss-map]] Fields and layout, How the image was read"]
name_kr: "어비스_LV5_114"
terrain: "Abyss_Lv05"
bounds: {"x0": 288, "z0": 3104, "x1": 479, "z1": 3295}
size: [192, 192]
segments: ["ZP01_12"]
fields: [114]
minimap: "map/minimap/minimap_z124_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=ddacea type=c899cd id=f38cfe sources=21700f name_kr=eec14a terrain=b15de8 bounds=68f2a2 size=be57ee segments=a35b1d fields=6c4502 minimap=f47f8e -->
|  |  |
|---|---|
|  | ![minimap of Abyss LV5 114 (The way go to devildom)](../assets/zones/124.png) |
| **Zone id** | `124` |
| **ZoneDB name** | 어비스_LV5_114 (English gloss: Abyss LV5 114 (The way go to devildom)) |
| **Terrain name** | `Abyss_Lv05` |
| **Rectangle** | x 288–479, z 3104–3295 (192 × 192 units) |
| **Fields** | [[wiki/fields/114-the-way-go-to-devildom\|The way go to devildom]] |
| **Minimap** | `map/minimap/minimap_z124_00.dds` |
| **Lighting** | `Setting/weather/Abyss_Lv05.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP01_12 | yes | yes |
<!-- generated:end -->

## Notes

- Abyss tile of field 114. Each Abyss field fills one 256-unit segment on a grid from x = 256, z = 2048; the tier is the `LV<n>` in the zone name. On the stitched player map the minimap is north-up (+x right, +z up) and shows about 175 units around the rectangle's centre, at about 1.53 px per unit ([[gameplay/abyss-map|Abyss map]]). *client + image*

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
