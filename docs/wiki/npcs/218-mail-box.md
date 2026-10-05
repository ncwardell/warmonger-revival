---
title: "Mail box"
type: "npc"
id: 218
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 218", "gameplay/npc-locations §3 (role)", "gameplay/npc-locations §3", "gameplay/npc-locations §4", "gameplay/video-tutorial-walkthrough §2"]
name_key: "UnitName_218"
category: 50
class_mask: 2
model: 1080
scale: 1.5
functions:
  - {"code": 9, "function": "none"}
role: "Mail"
map: 120
x: 1928.0
z: 1642.0
positions:
  - {"field": 120, "x": 1928.0, "z": 1642.0, "source": "gameplay/npc-locations §3", "confidence": "image"}
  - {"field": 88, "x": 347.6, "z": 3464.2, "source": "gameplay/npc-locations §4", "confidence": "video"}
  - {"field": 88, "x": 352.8, "z": 3463.9, "source": "gameplay/video-tutorial-walkthrough §2", "confidence": "video", "seen": ["12:40"]}
  - {"field": 120, "x": 2184.0, "z": 1642.0, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2440.0, "z": 1642.0, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=9b3350 type=3664ce id=3d5bdf sources=dae171 name_key=c94144 category=e1822d class_mask=da4b92 model=0cf950 scale=aa8f28 functions=2a3d19 role=8445b6 map=775bc5 x=419c56 z=a12d18 positions=dfdca5 -->
|  |  |
|---|---|
| **Unit id** | `218` |
| **Role** | Mail |
| **Category** | NPC (category 50) |
| **Menu** | no menu entry (code `9`) |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1928.0, 1642.0) |
| **Model** | ObjectList `1080`, scale 1.5 |

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1928.0 | 1642.0 | image | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/88-training-camp\|Training Camp]] | 347.6 | 3464.2 | video | [[gameplay/npc-locations\|npc-locations]] §4 |
| [[wiki/fields/88-training-camp\|Training Camp]] | 352.8 | 3463.9 | video | [[gameplay/video-tutorial-walkthrough\|video-tutorial-walkthrough]] §2 at 12:40 |
| [[wiki/fields/120-fortress\|Fortress]] | 2184.0 | 1642.0 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2440.0 | 1642.0 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120); 4. Training Camp (fields 88 / 92 / 96))
- [[gameplay/arena-ranking-rewards|Battle Arena monthly ranking rewards]] (Fortress scene details from the screenshots; Client cross-reference)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (5. Fortress layout (town))
- [[gameplay/precept-shop|Precept shop and precept quests]] (5. Freya, Oracle of Knowledge: location)
- [[gameplay/server-rules|Server rules checklist]] (Added from the source hunt (see [[gameplay/sources|Sources and gaps]]))
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] (4. NPC positions (Erion copy))
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] at 12:40 (2. NPC positions)
<!-- generated:end -->

## Notes

- The Mail box is a unit in the Fortress plaza and the Training Camp ([[gameplay/npc-locations|NPC locations]] §3, §4). Its target frame reads 10000 / 10000 (+500), while `UnitDB` row 218 holds 1080, so the server set its HP ([[gameplay/arena-ranking-rewards|Arena ranking rewards]]; [[gameplay/server-rules|Server rules]]). A summon scroll for it is item 923 ([[gameplay/arena-ranking-rewards|Arena ranking rewards]]). *image + client*
- Mail cost rose from 100 to 1,000 gold (with a package 5,000 → 10,000) in WM 0404, and mail between nations was blocked in WM 0802 ([[gameplay/events-and-schedules|Events and schedules]] §9). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/npc-locations|NPC locations]]
- [[gameplay/arena-ranking-rewards|Arena ranking rewards]]
- [[gameplay/server-rules|Server rules]]
- [[gameplay/events-and-schedules|Events and schedules]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
