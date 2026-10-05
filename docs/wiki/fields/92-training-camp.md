---
title: "Training Camp"
type: "field"
id: 92
status: "complete"
missing: []
sources: ["client: SceneList.cdb id 92", "client: Quest.cdb map1..3", "client: Teleport_List / Trigger positions inside ZoneDB rectangles", "client: Teleport_List.cdb field 92", "client: Quest.cdb (quests and objectives in field 92)", "doc: gameplay/npc-locations § 4. Training Camp (fields 88 / 92 / 96)"]
name_key: "FieldName_92"
kind: "town"
scene_type: 1
max_users: 100
group: 13
nation: "Erion"
nation_copies: {"Arslan": 88, "Erion": 92, "Armia": 96}
zones: [129]
segments: ["ZP02_13"]
gates:
  - {"gate": 1196, "x": 660.8, "z": 3492, "to_gate": 0, "to_field": 94, "label": "FieldName_92"}
  - {"gate": 1204, "x": 612.6, "z": 3502.3, "to_gate": 0, "to_field": 87, "label": "FieldName_92"}
  - {"gate": 1205, "x": 581.31, "z": 3439.3, "to_gate": 0, "to_field": 93, "label": "FieldName_92"}
  - {"gate": 1504, "x": 647.43, "z": 3436.47, "to_gate": 1504, "to_field": 100, "label": "FieldName_92"}
connections:
  - {"to": 94, "gate": 1196, "to_gate": 1197, "paired": true}
  - {"to": 87, "gate": 1204, "to_gate": null}
  - {"to": 93, "gate": 1205, "to_gate": 1206, "paired": true}
  - {"to": 100, "gate": 1504, "to_gate": 1504}
  - {"to": 94, "gate": 1196, "to_gate": 0}
  - {"to": 87, "gate": 1204, "to_gate": 0}
  - {"to": 93, "gate": 1205, "to_gate": 0}
npcs: [198, 215, 238, 315, 335, 218, 337]
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=908c23 type=7a94db id=8ee51c sources=09cbd7 name_key=4c95bf kind=da9544 scene_type=356a19 max_users=310b86 group=bd307a nation=069950 nation_copies=908462 zones=0ae2ea segments=a9a20c gates=e4ed8d connections=99fdb5 npcs=724d9d monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 129](../assets/zones/129.png) |
| **Field id** | `92` |
| **Kind** | town (SceneList type 1; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 13 (SceneList last column) |
| **Nation** | Erion |
| **Nation copies** | Arslan [[wiki/fields/88-training-camp\|Arslan (88)]], Erion **92**, Armia [[wiki/fields/96-training-camp\|Armia (96)]] |
| **Zones** | [[wiki/zones/129-training-camp-b\|Training Camp B]] |
| **Terrain segments** | `ZP02_13` |
| **Name key** | `FieldName_92` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1196 | 660.8, 3492 | [[wiki/fields/94-castle\|Castle]] | 1197 (paired, *inferred*) | FieldName_92 |
| 1204 | 612.6, 3502.3 | [[wiki/fields/87-village\|Village]] | — | FieldName_92 |
| 1205 | 581.31, 3439.3 | [[wiki/fields/93-training-ground\|Training Ground]] | 1206 (paired, *inferred*) | FieldName_92 |
| 1504 | 647.43, 3436.47 | [[wiki/fields/100-corpse-incineration\|Corpse incineration]] | 1504 | FieldName_92 |

Entered from: [[wiki/fields/93-training-ground|Training Ground]] (gate 1206 → 1205), [[wiki/fields/94-castle|Castle]] (gate 1197 → 1196), [[wiki/fields/100-corpse-incineration|Corpse incineration]] (gate 1501 → 1501)

### NPCs

Positions come from the NPC's own page (`x`, `z`). The client does not place town NPCs; the server spawns them ([[gameplay/npc-locations|NPC locations]] §1).

| NPC | unit | position | why it is listed |
|---|---|---|---|
| [[wiki/npcs/198-frei\|Frei]] | 198 | 614.8, 3469.1 | quests [[wiki/quests/9-find-the-missing-scout\|9]], [[wiki/quests/11-an-urgent-message\|11]], [[wiki/quests/45-the-1st-challenge-chepas-ahead\|45]]; [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)\|NPC locations § 4. Training Camp (fields 88 / 92 / 96)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/215-guard\|Guard]] | 215 | 641, 3436.4 | quests [[wiki/quests/9-find-the-missing-scout\|9]]; [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)\|NPC locations § 4. Training Camp (fields 88 / 92 / 96)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/238-wren\|Wren]] | 238 | 629.8, 3479.5 | quests [[wiki/quests/28-what-does-wren-do\|28]], [[wiki/quests/102-wren-s-sister-wren\|102]]; [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)\|NPC locations § 4. Training Camp (fields 88 / 92 / 96)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/315-lewellyn\|Lewellyn]] | 315 | 634.9, 3478.9 | quests [[wiki/quests/100-hunting-for-furs\|100]]; [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)\|NPC locations § 4. Training Camp (fields 88 / 92 / 96)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/335-odin\|Odin]] | 335 | 643.1, 3478.9 | quests [[wiki/quests/101-all-sorts-of-fragile-bones\|101]]; [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)\|NPC locations § 4. Training Camp (fields 88 / 92 / 96)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/218-mail-box\|Mail box]] | 218 |  | [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)\|NPC locations § 4. Training Camp (fields 88 / 92 / 96)]] |
| [[wiki/npcs/337-owen\|Owen]] | 337 | 649.7, 3470.4 | [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)\|NPC locations § 4. Training Camp (fields 88 / 92 / 96)]]; NPC page (`map` / `positions`) |

### Monsters

None known yet.

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Quests in this field

[[wiki/quests/9-find-the-missing-scout|Find the missing Scout]], [[wiki/quests/11-an-urgent-message|An urgent message]], [[wiki/quests/45-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]], [[wiki/quests/100-hunting-for-furs|Hunting for Furs]], [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]], [[wiki/quests/102-wren-s-sister-wren|Wren's sister Wren?]]

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP02_13 | yes | yes |

### Mentioned in

- [[gameplay/abyss-map#Ways in and out|Abyss map and portal graph § Ways in and out]]
- [[gameplay/maps-and-dungeons#1. The world (Gaia)|Maps and dungeons § 1. The world (Gaia)]]
- [[gameplay/npc-locations#4. Training Camp (fields 88 / 92 / 96)|NPC and point-of-interest locations § 4. Training Camp (fields 88 / 92 / 96)]]
- [[gameplay/video-character-creation-and-tutorial#Training Camp (field 92) and back|Video notes: character creation and tutorial (ZonderCoRe, June 2018) § Training Camp (field 92) and back]]
- [[gameplay/consumables|Consumables and clickables]] (by name)
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]] (by name)
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] (by name)
- [[gameplay/server-rules|Server rules checklist]] (by name)
- [[gameplay/sources|Sources and gaps]] (by name)
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
