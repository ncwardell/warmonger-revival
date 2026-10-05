---
title: "Corpse incineration"
type: "field"
id: 100
status: "partial"
missing: ["spawn_points", "npcs"]
sources: ["client: SceneList.cdb id 100", "client: Quest.cdb map1..3", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 100", "client: Quest.cdb (quests and objectives in field 100)", "client: Trigger.cdb field 100", "client + image: [[gameplay/abyss-map]] Portal table (BR portal ≈ (718, 2104) to 104 TR, image-measured ±5 units)", "video: [[gameplay/npc-locations]] §2 and §7 (player talking to the Scout within about 6 units of Trigger 10001)", "video: [[gameplay/video-character-creation-and-tutorial]] §3 step 14 (Erion camp portal leads here)"]
name_key: "FieldName_100"
kind: "field"
scene_type: 5
max_users: 100
group: 12
neighbours: [104, 105]
nation: "Erion"
nation_copies: {"Arslan": 99, "Erion": 100, "Armia": 101}
zones: [110]
segments: ["ZP02_08"]
gates:
  - {"gate": 1501, "x": 567.98, "z": 2100.77, "to_gate": 1501, "to_field": 92, "label": "FieldName_100"}
connections:
  - {"to": 92, "gate": 1501, "to_gate": 1501}
  - {"to": 104, "gate": null, "to_gate": null, "at": [718, 2104], "to_at": [962, 2499], "source": "image"}
npcs: []
monsters: [700, 701, 702, 703, 704, 705, 10003, 10004]
spawn_points: []
triggers:
  - {"id": 10001, "type": 1, "shape": 4, "x": 558.98, "z": 2257.79, "name_key": "UnitName_238", "model": 178}
---
<!-- generated:start -->
<!-- generated-keys: title=c2a1e0 type=7a94db id=310b86 sources=f16ef9 name_key=efd112 kind=7a94db scene_type=ac3478 max_users=310b86 group=7b5200 neighbours=1a82a8 nation=069950 nation_copies=5497e0 zones=e04b44 segments=468d55 gates=461eaf connections=f51a17 npcs=97d170 monsters=2f4123 spawn_points=97d170 triggers=0e63f2 -->
|  |  |
|---|---|
|  | ![minimap of zone 110](../assets/zones/110.png) |
| **Field id** | `100` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 12 (SceneList last column) |
| **Nation** | Erion |
| **Nation copies** | Arslan [[wiki/fields/99-corpse-incineration\|Arslan (99)]], Erion **100**, Armia [[wiki/fields/101-corpse-incineration\|Armia (101)]] |
| **Zones** | [[wiki/zones/110-abyss-lv1-100-corpse-incineration\|Abyss LV1 100 (Corpse incineration)]] |
| **Terrain segments** | `ZP02_08` |
| **Name key** | `FieldName_100` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1501 | 567.98, 2100.77 | [[wiki/fields/92-training-camp\|Training Camp]] | 1501 | FieldName_100 |

Entered from: [[wiki/fields/92-training-camp|Training Camp]] (gate 1504 → 1504)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/104-place-for-scattered-troops|Place for Scattered troops]], [[wiki/fields/105-place-for-scattered-troops|Place for Scattered troops]]

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
| [[wiki/nodes/10001-scout\|10001]] | talk/device | Scout |  | 558.98, 2257.79 | 1 | 178 |

### Quests in this field

[[wiki/quests/10-find-the-secret-document|Find the Secret Document]], [[wiki/quests/107-hunting-skeletons|Hunting Skeletons]]

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP02_08 | yes | yes |

### Mentioned in

- [[gameplay/npc-locations#2. How coordinates were derived|NPC and point-of-interest locations § 2. How coordinates were derived]]
- [[gameplay/server-rules#Added from the source hunt (see ((gameplay/sources/Sources and gaps)))|Server rules checklist § Added from the source hunt (see ((gameplay/sources/Sources and gaps)))]]
- [[gameplay/video-character-creation-and-tutorial#Training Camp (field 92) and back|Video notes: character creation and tutorial (ZonderCoRe, June 2018) § Training Camp (field 92) and back]] — at [9:05](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=545s)
- [[gameplay/abyss-map|Abyss map and portal graph]] (by name)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/sources|Sources and gaps]] (by name)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] (by name)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] (by name)
<!-- generated:end -->

## Notes

- Abyss level 1, Erion entrance: entered from Training Camp 92 (gate 1504); the exit 1501 sits bottom-left at (567.98, 2100.77) ([[gameplay/abyss-map|Abyss map]]; [[gameplay/video-character-creation-and-tutorial|character-creation video]] §3 step 14). *client + video*
- Bottom-right portal at about (718, 2104) leads to Place for Scattered troops 104 (top-right, about (962, 2499)); no gate id is known for it ([[gameplay/abyss-map|Abyss map]]). Erion route down: 100 → 104 → 111 → 113 → 114. *image*
- The Scout here is Trigger 10001; a video player talking to him stood within about 6 units of it ([[gameplay/npc-locations|NPC locations]] §2, [video](https://www.youtube.com/watch?v=E-87WgbO_vo&t=1215s)). *video*
- Same monsters as the Arslan copy (skeletons 700-705) per the quest objectives. *client*
- Abyss rules from the 2018 patches: lower drop rate, kills do not count for the daily kill quest, 5 s immunity after moving, and later a non-PK area ([[gameplay/patch-history|Patch history]], WM 0329/0404/0511). The ES guide says Abyss monsters stop giving loot at level 30 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §1). *guide*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/abyss-map|Abyss map]], [[gameplay/npc-locations|NPC locations]], [[gameplay/video-character-creation-and-tutorial|character-creation video]].

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
