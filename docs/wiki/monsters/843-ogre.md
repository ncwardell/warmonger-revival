---
title: "Ogre"
type: "monster"
id: 843
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 843"]
name_key: "UnitName_835"
category: 8
class_mask: 1
model: 292
model_name: "MOB_Oger_Rava_01"
model_path: "character/npc/monster/mob_oger/mob_oger_wasteland_01.mo"
scale: 1
radius: 1
sounds: [4070010, 4070010, 4070120]
---
<!-- generated:start -->
<!-- generated-keys: title=2e3a83 type=9bbc46 id=c02b74 sources=f95aae name_key=839cf1 category=fe5dbb class_mask=356a19 model=85f100 model_name=d4b189 model_path=981715 scale=356a19 radius=356a19 sounds=e32a74 -->
|  |  |
|---|---|
| **Unit id** | `843` |
| **Category** | field monster (inferred: ogres, trolls, bears, phytons) (`category@8a` = 8) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `292` MOB_Oger_Rava_01 (`character/npc/monster/mob_oger/mob_oger_wasteland_01.mo`) |
| **Scale** | 1 (second scale / radius 1) |

*No image: the client has no 2-D monster art (only the 3-D model).*

### Server stats

None of these is in the client; they were server data. Fill them in the front matter with a source (`drops: [{"item": id, "rate": %, "count": [min, max]}]`, `spawns: [{"field": id, "x": .., "z": .., "count": n, "respawn_s": s}]`).

| field | value |
|---|---|
| hp | **missing** |
| level | **missing** |
| attack | **missing** |
| armor | **missing** |
| magic_resist | **missing** |
| move_speed | **missing** |
| attack_speed | **missing** |
| attack_range | **missing** |
| kill_exp | **missing** |
| kill_gold | **missing** |
| drops | **missing** |
| spawns | **missing** |

### Other units with this name

[[wiki/monsters/548-ogre|Ogre (548)]], [[wiki/monsters/549-ogre|Ogre (549)]], [[wiki/monsters/550-ogre|Ogre (550)]], [[wiki/monsters/551-ogre|Ogre (551)]], [[wiki/monsters/552-ogre|Ogre (552)]], [[wiki/monsters/553-ogre|Ogre (553)]], [[wiki/monsters/554-ogre|Ogre (554)]], [[wiki/monsters/555-ogre|Ogre (555)]], [[wiki/monsters/564-ogre|Ogre (564)]], [[wiki/monsters/565-ogre|Ogre (565)]], [[wiki/monsters/839-ogre|Ogre (839)]], [[wiki/monsters/840-ogre|Ogre (840)]], [[wiki/monsters/841-ogre|Ogre (841)]], [[wiki/monsters/842-ogre|Ogre (842)]], [[wiki/monsters/844-ogre|Ogre (844)]], [[wiki/monsters/845-ogre|Ogre (845)]], [[wiki/monsters/846-ogre|Ogre (846)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 2 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 6 | 0 | 4070120 | `Unit/UE4070120.wav` |

### Seen in

- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § 4. Timestamped log at [1:20](https://www.youtube.com/watch?v=XoSM3RbZon0&t=80s) *(name match)*: P1 1:00–1:20 · 38:51–38:35 · Second jungle camp (Ogre)
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 8. Jungle and land-war timers *(name match)*: Each battle lasts 40 min. Troll and Ogre first appear at 36:00 and respawn 4 min after dying; the Bear appears at 35:00 and respawns 5 min after dying (blog pv…
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 8. Jungle and land-war timers *(name match)*: TP per kill per the blog: normal 30, elite 100, Ogre/Bear/Troll 1,500 each; tower 500 TP. The definitive and strategy guides give Ogre 2,500 and Bear 3,000, so…
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § 1. Land war (field war) *(name match)*: TP from kills: normal monster 30, elite 100, Troll 1,500, Ogre 2,500, Bear 3,000 (the definitive guide rounds all three to "1,500+"). *guides* strategy guide,…
- [[gameplay/server-rules|Server rules checklist]] § Land war *(name match)*: [ ] TP is a shared team pool. Kill TP: normal 30, elite 100, Troll 1,500, Ogre 2,500, Bear 3,000. — strategy, definitive — M
- [[gameplay/server-rules|Server rules checklist]] § Land war *(name match)*: [ ] Jungle: Troll & Ogre spawn at 36:00 then 4 min after death; Bear at 35:00 then 5 min after death; killed jungle bosses fight for the killer's team (towers,…
- [[gameplay/server-rules|Server rules checklist]] § PvP, events, forts *(name match)*: [ ] Jungle: medium jungle mob spawns at PvP start; Troll/Ogre at 36:00, respawn 4 min; Bear at 35:00, respawn 5 min — WM 0830, blog — M
- [[gameplay/sources|Sources and gaps]] § 3. Player screenshots (image sets that still load) *(name match)*: Abaddon jungle mob: imgur 0vlsbUT · EN · Ogre jungle spot, tower and crystal positions on the Thunderstorm Ruin – Abaddon minimap · medium · catalogued

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@8c | 112 |
| u8@91 | 15 |
| f32@c0 | 4.5 |
| f32@10c | 1 |
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
