---
title: "Death's Rest"
type: "field"
id: 112
status: "partial"
missing: ["spawn_points", "monsters", "npcs", "connections"]
sources: ["client: FieldNames.cdb id 112 (no SceneList row)", "client: ZoneDB name 어비스_LV4_112 (abyss zones are named after their field)", "image + guess: [[gameplay/abyss-map]] Routes (not in the image, no gate touches it)"]
name_key: "FieldName_112"
kind: null
zones: [122]
segments: ["ZP01_11"]
connections: []
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=5991de type=7a94db id=601ca9 sources=44562f name_key=5ed3e6 kind=2be88c zones=d4ee27 segments=14e8a7 connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 122](wiki/assets/zones/122.png) |
| **Field id** | `112` |
| **Zones** | [[wiki/zones/122-abyss-lv4-112-death-s-rest\|Abyss LV4 112 (Death's Rest)]] |
| **Terrain segments** | `ZP01_11` |
| **Name key** | `FieldName_112` |

### Gates and connections

No `Teleport_List` row: the client places no gate here.

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
| ZP01_11 | yes | yes |

### Mentioned in

- [[gameplay/server-rules#Added from the source hunt (see ((gameplay/sources/Sources and gaps)))|Server rules checklist § Added from the source hunt (see ((gameplay/sources/Sources and gaps)))]]
- [[gameplay/abyss-map|Abyss map and portal graph]] (by name)
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/patch-history|Patch notes and other sources]] (by name)
- [[gameplay/sources|Sources and gaps]] (by name)
<!-- generated:end -->

## Notes

- Abyss level 4 by its ZoneDB name. Not in the stitched Abyss image, and no gate in the client table touches it ([[gameplay/abyss-map|Abyss map]]); the server notes say to keep it closed until a source turns up ([[gameplay/server-rules|Server rules]]). *client + guess*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

- Way in and contents unknown; forum threads make-abyss-great-again.338 and stay-afk-in-abyss.686 are the leads ([[gameplay/sources]] gap 11).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
