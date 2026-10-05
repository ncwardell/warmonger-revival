---
title: "Place for Scattered troops"
type: "field"
id: 103
status: "stub"
missing: ["spawn_points", "npcs"]
sources: ["client: SceneList.cdb id 103", "client: Quest.cdb map1..3", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 103", "client: Quest.cdb (quests and objectives in field 103)"]
name_key: "FieldName_103"
kind: "field"
scene_type: 5
max_users: 100
group: 12
neighbours: [99, 108]
nation: "Arslan"
nation_copies: {"Arslan": 103, "Erion": 105, "Armia": 107}
zones: [117]
segments: ["ZP02_09"]
gates:
  - {"gate": 1122, "x": 566.51, "z": 2496.4, "to_gate": 1109, "to_field": 108, "label": "FieldName_103"}
connections:
  - {"to": 108, "gate": 1122, "to_gate": 1109}
npcs: []
monsters: [650, 651, 652, 653, 10006, 10005]
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=48ad72 type=7a94db id=934385 sources=f6ccf8 name_key=7bf5b8 kind=7a94db scene_type=ac3478 max_users=310b86 group=7b5200 neighbours=7df4d2 nation=a20b0f nation_copies=364b00 zones=23ae40 segments=f311d2 gates=f8f178 connections=45f5b8 npcs=97d170 monsters=6ff0c3 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 117](../assets/zones/117.png) |
| **Field id** | `103` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 12 (SceneList last column) |
| **Nation** | Arslan |
| **Nation copies** | Arslan **103**, Erion [[wiki/fields/105-place-for-scattered-troops\|Erion (105)]], Armia [[wiki/fields/107-place-for-scattered-troops\|Armia (107)]] |
| **Zones** | [[wiki/zones/117-abyss-lv2-103-place-for-scattered-troops\|Abyss LV2 103 (Place for Scattered troops)]] |
| **Terrain segments** | `ZP02_09` |
| **Name key** | `FieldName_103` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1122 | 566.51, 2496.4 | [[wiki/fields/108-the-land-of-greed\|The land of Greed]] | 1109 | FieldName_103 |

Entered from: [[wiki/fields/108-the-land-of-greed|The land of Greed]] (gate 1109 → 1122), [[wiki/fields/120-fortress|Fortress]] (gate 1901 → ?)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/99-corpse-incineration|Corpse incineration]], [[wiki/fields/108-the-land-of-greed|The land of Greed]]

### NPCs

None known yet.

### Monsters

| monster | unit | why it is listed |
|---|---|---|
| [[wiki/monsters/650-fragile-lizard-swordsman\|Fragile Lizard Swordsman]] | 650 | kill objective of quest [[wiki/quests/104-delivering-punishment\|104]] (kill group 10005, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/651-fragile-lizard-swordsman\|Fragile Lizard Swordsman]] | 651 | kill objective of quest [[wiki/quests/104-delivering-punishment\|104]] (kill group 10005, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/652-fragile-elite-lizard-swordsman\|Fragile Elite Lizard Swordsman]] | 652 | kill objective of quest [[wiki/quests/104-delivering-punishment\|104]] (kill group 10006, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/653-fragile-elite-lizard-lancer\|Fragile Elite Lizard Lancer]] | 653 | kill objective of quest [[wiki/quests/104-delivering-punishment\|104]] (kill group 10006, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/npcs/10006\|NPC 10006]] | 10006 | kill objective of quest [[wiki/quests/104-delivering-punishment\|104]] |
| unit 10005 (not in UnitDB) | 10005 | hand-entered |

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP02_09 | yes | yes |

### Mentioned in

- [[gameplay/abyss-map#Ways in and out|Abyss map and portal graph § Ways in and out]]
- [[gameplay/abyss-map#Portal table|Abyss map and portal graph § Portal table]]
- [[gameplay/server-rules#Added from the source hunt (see ((gameplay/sources/Sources and gaps)))|Server rules checklist § Added from the source hunt (see ((gameplay/sources/Sources and gaps)))]]
- [[gameplay/video-early-quests#Fortress (levels 12–20)|Video notes: first session, levels 1+ (charmanmugen) § Fortress (levels 12–20)]] — at [42:10](https://www.youtube.com/watch?v=s04CSN16w1s&t=2532s)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/video-dungeon-run|Video notes: Nas Village dungeon run (ZonderCoRe)]] (by name)
<!-- generated:end -->

## Notes

<!-- hand-written: add what you know, with a source -->

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
