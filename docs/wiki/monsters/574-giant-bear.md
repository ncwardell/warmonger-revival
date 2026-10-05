---
title: "Giant Bear"
type: "monster"
id: 574
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 574"]
name_key: "UnitName_574"
category: 8
class_mask: 1
model: 445
model_name: "MOB_Bear_0_0_0_00_01"
model_path: "character/npc/monster/mob_bear/mob_bear.mo"
scale: 1
radius: 1
sounds: [4070083, 4070083, 4070082, 4070082, 4070082, 4070084]
---
<!-- generated:start -->
<!-- generated-keys: title=b74445 type=9bbc46 id=fa1a65 sources=93ff49 name_key=2ba9d9 category=fe5dbb class_mask=356a19 model=ac9c95 model_name=535d4d model_path=d24dcb scale=356a19 radius=356a19 sounds=be766a -->
|  |  |
|---|---|
| **Unit id** | `574` |
| **Category** | field monster (inferred: ogres, trolls, bears, phytons) (`category@8a` = 8) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `445` MOB_Bear_0_0_0_00_01 (`character/npc/monster/mob_bear/mob_bear.mo`) |
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

[[wiki/monsters/573-giant-bear|Giant Bear (573)]], [[wiki/monsters/601-giant-bear|Giant Bear (601)]], [[wiki/monsters/602-giant-bear|Giant Bear (602)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070083 | `Unit/UE4070083.wav` |
| 2 | 0 | 4070083 | `Unit/UE4070083.wav` |
| 3 | 0 | 4070082 | `Unit/UE4070082.wav` |
| 4 | 0 | 4070082 | `Unit/UE4070082.wav` |
| 5 | 0 | 4070082 | `Unit/UE4070082.wav` |
| 6 | 0 | 4070084 | `Unit/UE4070084.wav` |

### Seen in

- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § 1. Land war (field war): Jungle bosses (Troll, Ogre, Bear): when killed they join the killer's team and push the nearest enemy towers, then the nexus once the towers are gone. Spawn ti…
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § Eternal River – Upper Region (field 14, ZoneDB 39, rectangle x 3616–3775, z 544–703) at [0:47](https://www.youtube.com/watch?v=XoSM3RbZon0&t=47s) *(name match)*: Giant Bear jungle camp · about 3748, 636 · P1 0:35–0:47 · video
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § 4. Timestamped log at [0:52](https://www.youtube.com/watch?v=XoSM3RbZon0&t=52s) *(name match)*: P1 0:24–0:52 · 39:27–39:03 · Group kills the Giant Bear jungle mob next to a tower; TP +1,500 at 39:06
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § War and siege timers *(name match)*: Jungle respawn · "The Jungle monsters have returned" at 35:03; the Giant Bear camp was cleared at about 39:03, so about 4 min · P1 0:52, P2 0:36 · video + guess
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § TP *(name match)*: Gain as the Giant Bear jungle camp dies · +1,500 (2,630 → 4,130 at 39:06) · P1 0:47 · video; cause is a guess

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 5 |
| f32@10c | 1 |
<!-- generated:end -->

## Notes

- [[gameplay/pvp-and-matches]] §1 lists this unit among the land-war **jungle bosses** (Giant Bear) (client ids; the guides do not say which id spawns on which land).
- A June 2018 war video shows a Giant Bear jungle camp at about (3748, 636) in [[wiki/fields/14-eternal-river-upper-region|Eternal River – Upper Region (14)]]; the side's TP rose by 1,500 as it died (cause a *guess*) (video, [[gameplay/video-fort-war]] §1–2).

## Behaviour

- Spawns first at 35:00 on the 40:00 war clock, then 5 minutes after each death (guides, [[gameplay/pvp-and-matches]] §1; blog, [[gameplay/events-and-schedules]] §8).
- When killed it joins the killer's team and pushes the nearest enemy towers, then the nexus (guides, [[gameplay/pvp-and-matches]] §1).
- TP for the kill: 3,000 for a Bear (strategy guide) or 1,500 (blog) (guides, [[gameplay/pvp-and-matches]] §1; [[gameplay/events-and-schedules]] §8).

## Sources

- [[gameplay/pvp-and-matches]] §1; [[gameplay/events-and-schedules]] §8; [[gameplay/video-fort-war]]

## Open questions

- Which jungle id spawns where is unknown, so no `spawns` are set.
- Respawn: the guides say 5 min for the Bear; in the war video the jungle returned about 4 min after the Giant Bear camp died (video + guess, [[gameplay/video-fort-war]] §1).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
