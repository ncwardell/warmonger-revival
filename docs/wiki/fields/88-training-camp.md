---
title: "Training Camp"
type: "field"
id: 88
status: "complete"
missing: []
sources: ["client: SceneList.cdb id 88", "client: Quest.cdb map1..3", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 88", "client: Quest.cdb (quests and objectives in field 88)", "doc: gameplay/npc-locations § 4. Training Camp (fields 88 / 92 / 96)"]
name_key: "FieldName_88"
kind: "town"
scene_type: 1
max_users: 100
group: 13
nation: "Arslan"
nation_copies: {"Arslan": 88, "Erion": 92, "Armia": 96}
zones: [128]
segments: ["ZP01_13"]
worldmap_rect: [1074, 34, 1160, 80]
gates:
  - {"gate": 1198, "x": 403.96, "z": 3492.28, "to_gate": 0, "to_field": 90, "label": "FieldName_88"}
  - {"gate": 1201, "x": 356.65, "z": 3502.59, "to_gate": 0, "to_field": 87, "label": "FieldName_88"}
  - {"gate": 1202, "x": 325.8, "z": 3438.9, "to_gate": 0, "to_field": 89, "label": "FieldName_88"}
  - {"gate": 1503, "x": 391.21, "z": 3436.26, "to_gate": 1503, "to_field": 99, "label": "FieldName_88"}
connections:
  - {"to": 90, "gate": 1198, "to_gate": 1199, "paired": true}
  - {"to": 87, "gate": 1201, "to_gate": null}
  - {"to": 89, "gate": 1202, "to_gate": 1203, "paired": true}
  - {"to": 99, "gate": 1503, "to_gate": 1503}
  - {"to": 90, "gate": 1198, "to_gate": 0}
  - {"to": 87, "gate": 1201, "to_gate": 0}
  - {"to": 89, "gate": 1202, "to_gate": 0}
npcs: [198, 215, 238, 315, 335, 218, 337]
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=908c23 type=7a94db id=b37f6d sources=5cfc41 name_key=3d0534 kind=da9544 scene_type=356a19 max_users=310b86 group=bd307a nation=a20b0f nation_copies=908462 zones=c9e1d0 segments=e346a8 worldmap_rect=16b133 gates=781748 connections=3b90dd npcs=724d9d monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 128](wiki/assets/zones/128.png) |
| **Field id** | `88` |
| **Kind** | town (SceneList type 1; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 13 (SceneList last column) |
| **Nation** | Arslan |
| **Nation copies** | Arslan **88**, Erion [[wiki/fields/92-training-camp\|Erion (92)]], Armia [[wiki/fields/96-training-camp\|Armia (96)]] |
| **Zones** | [[wiki/zones/128-training-camp-a\|Training Camp A]] |
| **Terrain segments** | `ZP01_13` |
| **World-map rectangle** | `[1074, 34, 1160, 80]` (WorldmapData, panel pixels) |
| **Name key** | `FieldName_88` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1198 | 403.96, 3492.28 | [[wiki/fields/90-castle\|Castle]] | 1199 (paired, *inferred*) | FieldName_88 |
| 1201 | 356.65, 3502.59 | [[wiki/fields/87-village\|Village]] | — | FieldName_88 |
| 1202 | 325.8, 3438.9 | [[wiki/fields/89-training-ground\|Training Ground]] | 1203 (paired, *inferred*) | FieldName_88 |
| 1503 | 391.21, 3436.26 | [[wiki/fields/99-corpse-incineration\|Corpse incineration]] | 1503 | FieldName_88 |

Entered from: [[wiki/fields/89-training-ground|Training Ground]] (gate 1203 → 1202), [[wiki/fields/90-castle|Castle]] (gate 1199 → 1198), [[wiki/fields/99-corpse-incineration|Corpse incineration]] (gate 1500 → 1500)

### NPCs

Positions come from the NPC's own page (`x`, `z`). The client does not place town NPCs; the server spawns them ([[gameplay/npc-locations|NPC locations]] §1).

| NPC | unit | position | why it is listed |
|---|---|---|---|
| [[wiki/npcs/198-frei\|Frei]] | 198 | 358.8, 3469.1 | quests [[wiki/quests/9-find-the-missing-scout\|9]], [[wiki/quests/11-an-urgent-message\|11]], [[wiki/quests/45-the-1st-challenge-chepas-ahead\|45]]; [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)\|NPC locations § 4. Training Camp (fields 88 / 92 / 96)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/215-guard\|Guard]] | 215 | 385, 3436.4 | quests [[wiki/quests/9-find-the-missing-scout\|9]]; [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)\|NPC locations § 4. Training Camp (fields 88 / 92 / 96)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/238-wren\|Wren]] | 238 | 373.8, 3479.5 | quests [[wiki/quests/28-what-does-wren-do\|28]], [[wiki/quests/102-wren-s-sister-wren\|102]]; [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)\|NPC locations § 4. Training Camp (fields 88 / 92 / 96)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/315-lewellyn\|Lewellyn]] | 315 | 378.9, 3478.9 | quests [[wiki/quests/100-hunting-for-furs\|100]]; [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)\|NPC locations § 4. Training Camp (fields 88 / 92 / 96)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/335-odin\|Odin]] | 335 | 387.1, 3478.9 | quests [[wiki/quests/101-all-sorts-of-fragile-bones\|101]]; [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)\|NPC locations § 4. Training Camp (fields 88 / 92 / 96)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/218-mail-box\|Mail box]] | 218 | 347.6, 3464.2 | [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)\|NPC locations § 4. Training Camp (fields 88 / 92 / 96)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/337-owen\|Owen]] | 337 | 393.7, 3470.4 | [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)\|NPC locations § 4. Training Camp (fields 88 / 92 / 96)]]; NPC page (`map` / `positions`) |

### Monsters

None known yet.

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

Current server (`server/world.py`, our choice, not original data): players appear at (325.8, 3438.9) in scene 88.

### Quests in this field

[[wiki/quests/9-find-the-missing-scout|Find the missing Scout]], [[wiki/quests/11-an-urgent-message|An urgent message]], [[wiki/quests/45-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]], [[wiki/quests/100-hunting-for-furs|Hunting for Furs]], [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]], [[wiki/quests/102-wren-s-sister-wren|Wren's sister Wren?]]

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP01_13 | yes | yes |

### Mentioned in

- [[gameplay/abyss-map#Ways in and out|Abyss map and portal graph § Ways in and out]]
- [[gameplay/maps-and-dungeons#1. The world (Gaia)|Maps and dungeons § 1. The world (Gaia)]]
- [[gameplay/npc-locations#2. How coordinates were derived|NPC and point-of-interest locations § 2. How coordinates were derived]]
- [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)|NPC and point-of-interest locations § 4. Training Camp (fields 88 / 92 / 96)]]
- [[gameplay/consumables|Consumables and clickables]] (by name)
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]] (by name)
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] (by name)
- [[gameplay/server-rules|Server rules checklist]] (by name)
- [[gameplay/sources|Sources and gaps]] (by name)
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] (by name)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] (by name)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] (by name)
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
