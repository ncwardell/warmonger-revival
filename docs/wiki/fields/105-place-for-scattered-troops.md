---
title: "Place for Scattered troops"
type: "field"
id: 105
status: "partial"
missing: ["spawn_points", "npcs"]
sources: ["client: SceneList.cdb id 105", "client: Quest.cdb map1..3", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 105", "client: Quest.cdb (quests and objectives in field 105)", "client + image: [[gameplay/abyss-map]] Portal table and Routes (unlabelled portals image-measured ±5 units)", "video: [[gameplay/video-early-quests]] §1 (Fortress → 103 at 51:25) and §2 quest 104 (Lizards in 103/105/107), video"]
name_key: "FieldName_105"
kind: "field"
scene_type: 5
max_users: 100
group: 12
neighbours: [100]
nation: "Erion"
nation_copies: {"Arslan": 103, "Erion": 105, "Armia": 107}
zones: [119]
segments: ["ZP04_09"]
gates:
  - {"gate": 1131, "x": 1084.75, "z": 2361.27, "to_gate": 1125, "to_field": 109, "label": "FieldName_105"}
connections:
  - {"to": 109, "gate": 1131, "to_gate": 1125}
  - {"to": 108, "gate": null, "to_gate": null, "at": [1217, 2365], "to_at": [318, 2755], "source": "image"}
npcs: []
monsters: [650, 651, 652, 653, 10006, 10005]
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=48ad72 type=7a94db id=e114c4 sources=06a77e name_key=7ba97c kind=7a94db scene_type=ac3478 max_users=310b86 group=7b5200 neighbours=023272 nation=069950 nation_copies=364b00 zones=2a6184 segments=1c4a8d gates=ede5fb connections=3e7fc6 npcs=97d170 monsters=6ff0c3 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 119](wiki/assets/zones/119.png) |
| **Field id** | `105` |
| **Kind** | field (SceneList type 5; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 12 (SceneList last column) |
| **Nation** | Erion |
| **Nation copies** | Arslan [[wiki/fields/103-place-for-scattered-troops\|Arslan (103)]], Erion **105**, Armia [[wiki/fields/107-place-for-scattered-troops\|Armia (107)]] |
| **Zones** | [[wiki/zones/119-abyss-lv2-105-place-for-scattered-troops\|Abyss LV2 105 (Place for Scattered troops)]] |
| **Terrain segments** | `ZP04_09` |
| **Name key** | `FieldName_105` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1131 | 1084.75, 2361.27 | [[wiki/fields/109-the-land-of-greed\|The land of Greed]] | 1125 | FieldName_105 |

Other connections (hand-entered): to 108, gate None, to_gate None, at [1217, 2365], to_at [318, 2755], source image

Entered from: [[wiki/fields/109-the-land-of-greed|The land of Greed]] (gate 1125 → 1131), [[wiki/fields/120-fortress|Fortress]] (gate 1902 → ?)

Neighbouring lands (`SceneList` link columns): [[wiki/fields/100-corpse-incineration|Corpse incineration]]

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
| ZP04_09 | yes | yes |

### Mentioned in

- [[gameplay/abyss-map#Ways in and out|Abyss map and portal graph § Ways in and out]]
- [[gameplay/server-rules#Added from the source hunt (see ((gameplay/sources/Sources and gaps)))|Server rules checklist § Added from the source hunt (see ((gameplay/sources/Sources and gaps)))]]
- [[gameplay/video-early-quests#Fortress (levels 12–20)|Video notes: first session, levels 1+ (charmanmugen) § Fortress (levels 12–20)]] — at [42:10](https://www.youtube.com/watch?v=s04CSN16w1s&t=2532s)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (by name)
- [[gameplay/video-dungeon-run|Video notes: Nas Village dungeon run (ZonderCoRe)]] (by name)
<!-- generated:end -->

## Notes

- Abyss level 2 hub; the fortress teleporter's free "Abyss" option probably lands here for Erion players (`Teleport_List` 1901-1903, *guess*, [[gameplay/abyss-map|Abyss map]]). In the June 2018 video the Arslan player arrived in 103 from the Fortress ([[gameplay/video-early-quests|first-session video]] §1). *client + video*
- Portals: bottom-left 1131 → 109 (gate 1125); bottom-right (about 1217, 2365) → 108; top-left (about 1079, 2497) has no line and a blue dot, perhaps the fortress arrival (*guess*) ([[gameplay/abyss-map|Abyss map]]). Route: Fortress → 105 → 108 or 109 → 113 → 114. *client + image*
- Quest 104 "Delivering Punishment" (Haley) sends players here for 10 Lizard (group 10005) and 10 Elite Lizard (group 10006); the video kills Fragile (Elite) Lizard Swordsmen and Lancers. Gem Stone: Blue dropped here ([[gameplay/video-early-quests|first-session video]] §2 item 18, §5, §6). *video + client*
- Abyss rules from the 2018 patches: lower drop rate, kills do not count for the daily kill quest, 5 s immunity after moving, and later a non-PK area ([[gameplay/patch-history|Patch history]], WM 0329/0404/0511). The ES guide says Abyss monsters stop giving loot at level 30 ([[gameplay/maps-and-dungeons|Maps and dungeons]] §1). *guide*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/abyss-map|Abyss map]], [[gameplay/video-early-quests|first-session video]], [[gameplay/patch-history|Patch history]].

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
