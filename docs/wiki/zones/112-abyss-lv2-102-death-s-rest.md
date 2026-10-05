---
title: "Abyss LV2 102 (Death's Rest)"
type: "zone"
id: 112
status: "complete"
missing: []
sources: ["client: ZoneDB.cdb id 112", "client: ZoneDB name 어비스_LV2_102 (abyss zones are named after their field)", "client + image: [[gameplay/abyss-map]] Fields and layout, How the image was read"]
name_kr: "어비스_LV2_102"
terrain: "Abyss_Lv02"
bounds: {"x0": 288, "z0": 2336, "x1": 479, "z1": 2527}
size: [192, 192]
segments: ["ZP01_09"]
fields: [102]
minimap: "map/minimap/minimap_z112_00.dds"
---
<!-- generated:start -->
<!-- generated-keys: title=882de9 type=c899cd id=601ca9 sources=c43dcd name_kr=adf960 terrain=b8c94a bounds=0888b4 size=be57ee segments=28a721 fields=187cfc minimap=d7ee1b -->
|  |  |
|---|---|
|  | ![minimap of Abyss LV2 102 (Death's Rest)](../assets/zones/112.png) |
| **Zone id** | `112` |
| **ZoneDB name** | 어비스_LV2_102 (English gloss: Abyss LV2 102 (Death's Rest)) |
| **Terrain name** | `Abyss_Lv02` |
| **Rectangle** | x 288–479, z 2336–2527 (192 × 192 units) |
| **Fields** | [[wiki/fields/102-death-s-rest\|Death's Rest]] |
| **Minimap** | `map/minimap/minimap_z112_00.dds` |
| **Lighting** | `Setting/weather/Abyss_Lv02.dat` |

### Segments

Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP01_09 | yes | yes |
<!-- generated:end -->

## Notes

- Abyss tile of field 102. Each Abyss field fills one 256-unit segment on a grid from x = 256, z = 2048; the tier is the `LV<n>` in the zone name. On the stitched player map the minimap is north-up (+x right, +z up) and shows about 175 units around the rectangle's centre, at about 1.53 px per unit ([[gameplay/abyss-map|Abyss map]]). *client + image*

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
