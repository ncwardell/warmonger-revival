---
title: "Corpse incineration"
type: "field"
id: 99
status: "stub"
missing: ["spawn_points", "npcs"]
sources: ["client: SceneList.cdb id 99", "client: Quest.cdb map1..3", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 99", "client: Quest.cdb (quests and objectives in field 99)", "client: Trigger.cdb field 99"]
name_key: "FieldName_99"
kind: "field"
scene_type: 5
max_users: 100
group: 12
neighbours: [102, 103]
nation: "Arslan"
nation_copies: {"Arslan": 99, "Erion": 100, "Armia": 101}
zones: [108]
segments: ["ZP01_08"]
gates:
  - {"gate": 1106, "x": 312.96, "z": 2102.09, "to_gate": 1100, "to_field": 102, "label": "FieldName_99"}
  - {"gate": 1500, "x": 306.03, "z": 2254.17, "to_gate": 1500, "to_field": 88, "label": "FieldName_99"}
connections:
  - {"to": 102, "gate": 1106, "to_gate": 1100}
  - {"to": 88, "gate": 1500, "to_gate": 1500}
npcs: []
monsters: [700, 701, 702, 703, 704, 705, 10003, 10004]
spawn_points: []
triggers:
  - {"id": 9901, "type": 1, "shape": 4, "x": 465.27, "z": 2259.45, "name_key": "UnitName_238", "model": 178}
---
<!-- generated:start -->
<!-- generated-keys: title=c2a1e0 type=7a94db id=9a79be sources=9b55ff name_key=2d783c kind=7a94db scene_type=ac3478 max_users=310b86 group=7b5200 neighbours=152227 nation=a20b0f nation_copies=5497e0 zones=a52acc segments=9d8c24 gates=87ac5b connections=43fed2 npcs=97d170 monsters=2f4123 spawn_points=97d170 triggers=41f524 -->
|  |  |
|---|---|
|  | ![minimap of zone 108](wiki/assets/zones/108.png) |
| **Field id** | `99` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 12 (SceneList last column) |
| **Nation** | Arslan |
| **Nation copies** | Arslan **99**, Erion [[wiki/fields/100-corpse-incineration\|Erion (100)]], Armia [[wiki/fields/101-corpse-incineration\|Armia (101)]] |
| **Zones** | [[wiki/zones/108-abyss-lv1-099-corpse-incineration\|Abyss LV1 099 (Corpse incineration)]] |
| **Terrain segments** | `ZP01_08` |
| **Name key** | `FieldName_99` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1106 | 312.96, 2102.09 | [[wiki/fields/102-death-s-rest\|Death's Rest]] | 1100 | FieldName_99 |
| 1500 | 306.03, 2254.17 | [[wiki/fields/88-training-camp\|Training Camp]] | 1500 | FieldName_99 |

Entered from: [[wiki/fields/88-training-camp|Training Camp]] (gate 1503 → 1503)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/102-death-s-rest|Death's Rest]], [[wiki/fields/103-place-for-scattered-troops|Place for Scattered troops]]

### NPCs

None known yet.

### Monsters

| monster | unit | why it is listed |
|---|---|---|
| [[wiki/monsters/700-skeleton-warrior\|Skeleton Warrior]] | 700 | kill objective of quest [[wiki/quests/101-all-sorts-of-fragile-bones\|101]] (kill group 10003, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/701-skeleton-archer\|Skeleton Archer]] | 701 | kill objective of quest [[wiki/quests/101-all-sorts-of-fragile-bones\|101]] (kill group 10003, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/702-elite-skeleton-warrior\|Elite Skeleton Warrior]] | 702 | kill objective of quest [[wiki/quests/101-all-sorts-of-fragile-bones\|101]] (kill group 10004, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/703-elite-skeleton-archer\|Elite Skeleton Archer]] | 703 | kill objective of quest [[wiki/quests/101-all-sorts-of-fragile-bones\|101]] (kill group 10004, UnitDB i32@80); monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/704-skeleton-warrior-officer\|Skeleton Warrior Officer]] | 704 | kill objective of quest [[wiki/quests/10-find-the-secret-document\|10]], [[wiki/quests/107-hunting-skeletons\|107]]; monster page (`spawns` / `spawn_fields`) |
| [[wiki/monsters/705-skeleton-archer-officer\|Skeleton Archer Officer]] | 705 | kill objective of quest [[wiki/quests/107-hunting-skeletons\|107]]; monster page (`spawns` / `spawn_fields`) |
| unit 10003 (not in UnitDB) | 10003 | hand-entered |
| unit 10004 (not in UnitDB) | 10004 | hand-entered |

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Client-placed objects (`Trigger`)

Talk devices (shape 4) and gathering nodes (type 0, shape 5: the item is what gathering gives). The server can load these as they are; the video check in [[gameplay/video-dungeon-run|Nas Village dungeon run]] §5 matched them within 5 units.

| trigger | kind | name | gives | at (x, z) | type | model |
|---|---|---|---|---|---|---|
| [[wiki/nodes/9901-scout\|9901]] | talk/device | Scout |  | 465.27, 2259.45 | 1 | 178 |

### Quests in this field

[[wiki/quests/10-find-the-secret-document|Find the Secret Document]], [[wiki/quests/107-hunting-skeletons|Hunting Skeletons]]

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP01_08 | yes | yes |

### Mentioned in

- [[gameplay/abyss-map#Portal table|Abyss map and portal graph § Portal table]]
- [[gameplay/server-rules#Added from the source hunt (see ((gameplay/sources/Sources and gaps)))|Server rules checklist § Added from the source hunt (see ((gameplay/sources/Sources and gaps)))]]
- [[gameplay/video-tutorial-walkthrough#Steps|Video notes: tutorial walkthrough (Bravely Forward 2) § Steps]] — at [24:12](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1452s)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/npc-locations|NPC and point-of-interest locations]] (by name)
- [[gameplay/sources|Sources and gaps]] (by name)
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] (by name)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] (by name)
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
