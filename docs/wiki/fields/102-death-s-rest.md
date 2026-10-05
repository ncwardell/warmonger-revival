---
title: "Death's Rest"
type: "field"
id: 102
status: "partial"
missing: ["spawn_points", "monsters", "npcs"]
sources: ["client: FieldNames.cdb id 102 (no SceneList row)", "client: ZoneDB name 어비스_LV2_102 (abyss zones are named after their field)", "client + image: [[gameplay/abyss-map]] Portal table (gate 1100 named by 1106, position ≈ (309, 2497); BR portal ≈ (451, 2365) to 109 TL), image-measured ±5 units"]
name_key: "FieldName_102"
kind: null
zones: [112]
segments: ["ZP01_09"]
connections:
  - {"to": 99, "gate": 1100, "to_gate": 1106, "at": [309, 2497], "source": "client link, image position"}
  - {"to": 109, "gate": null, "to_gate": null, "at": [451, 2365], "to_at": [574, 2758], "source": "image"}
npcs: []
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=5991de type=7a94db id=c8306a sources=4308f9 name_key=26e10a kind=2be88c zones=48700a segments=28a721 connections=97d170 npcs=97d170 monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 112](../assets/zones/112.png) |
| **Field id** | `102` |
| **Zones** | [[wiki/zones/112-abyss-lv2-102-death-s-rest\|Abyss LV2 102 (Death's Rest)]] |
| **Terrain segments** | `ZP01_09` |
| **Name key** | `FieldName_102` |

### Gates and connections

No `Teleport_List` row: the client places no gate here.

Entered from: [[wiki/fields/99-corpse-incineration|Corpse incineration]] (gate 1106 → 1100)

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
| ZP01_09 | yes | yes |

### Mentioned in

- [[gameplay/abyss-map#Open questions|Abyss map and portal graph § Open questions]]
- [[gameplay/server-rules#Added from the source hunt (see ((gameplay/sources/Sources and gaps)))|Server rules checklist § Added from the source hunt (see ((gameplay/sources/Sources and gaps)))]]
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/patch-history|Patch notes and other sources]] (by name)
- [[gameplay/sources|Sources and gaps]] (by name)
<!-- generated:end -->

## Notes

- Abyss level 2 on the Arslan route (99 → 102 → 109). Top-left portal (gate 1100, about (309, 2497)) links to Corpse incineration 99 gate 1106; bottom-right portal (about (451, 2365)) links to The land of Greed 109 ([[gameplay/abyss-map|Abyss map]]). *client + image*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

- FieldNames calls this field "Death's Rest", but its minimap title reads "Place for Scattered troops" ([[gameplay/abyss-map|Abyss map]] Open questions).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
