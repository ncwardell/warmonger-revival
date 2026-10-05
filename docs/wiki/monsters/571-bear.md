---
title: "Bear"
type: "monster"
id: 571
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 571", "client: Quest.cdb kill objectives (quests 50)"]
name_key: "UnitName_571"
category: 8
class_mask: 1
kill_group: 571
model: 240
model_name: "MOB_Bear_01"
model_path: "character/npc/monster/mob_bear/mob_bear.mo"
scale: 0.7
radius: 0.7
sounds: [4070083, 4070083, 4070082, 4070082, 4070082, 4070084]
quest_targets:
  - {"quest": 50, "need": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=883f35 type=9bbc46 id=2bfba6 sources=7f422f name_key=817ef7 category=fe5dbb class_mask=356a19 kill_group=2bfba6 model=cae91e model_name=0045be model_path=d24dcb scale=717757 radius=717757 sounds=be766a quest_targets=4541a5 -->
|  |  |
|---|---|
| **Unit id** | `571` |
| **Category** | field monster (inferred: ogres, trolls, bears, phytons) (`category@8a` = 8) |
| **Class mask** | 1 (monster) |
| **Kill group** | `571` with [[wiki/monsters/573-giant-bear\|Giant Bear]], [[wiki/monsters/575-wasteland-ogre\|Wasteland Ogre]], [[wiki/monsters/576-wasteland-giant-ogre\|Wasteland Giant Ogre]], [[wiki/monsters/577-lava-ogre\|Lava Ogre]], [[wiki/monsters/578-lava-giant-ogre\|Lava Giant Ogre]], [[wiki/monsters/579-sulphur-ogre\|Sulphur Ogre]], [[wiki/monsters/580-sulphur-giant-ogre\|Sulphur Giant Ogre]], [[wiki/monsters/581-ice-ogre\|Ice Ogre]], [[wiki/monsters/582-ice-giant-ogre\|Ice Giant Ogre]], [[wiki/monsters/583-troll\|Troll]], [[wiki/monsters/584-troll\|Troll]] |
| **Model** | ObjectList `240` MOB_Bear_01 (`character/npc/monster/mob_bear/mob_bear.mo`) |
| **Scale** | 0.7 (second scale / radius 0.7) |

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

### Quests

- [[wiki/quests/50-war-winning-means|War - Winning means]]: kill 2

### Other units with this name

[[wiki/monsters/572-bear|Bear (572)]]

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
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]] § 2017-02-21 ((t922); Steam 21 Feb) *(name match)*: Costume · "Family Bear" set *staff*
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 8. Jungle and land-war timers *(name match)*: Each battle lasts 40 min. Troll and Ogre first appear at 36:00 and respawn 4 min after dying; the Bear appears at 35:00 and respawns 5 min after dying (blog pv…
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 8. Jungle and land-war timers *(name match)*: TP per kill per the blog: normal 30, elite 100, Ogre/Bear/Troll 1,500 each; tower 500 TP. The definitive and strategy guides give Ogre 2,500 and Bear 3,000, so…
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § 1. Land war (field war) *(name match)*: TP from kills: normal monster 30, elite 100, Troll 1,500, Ogre 2,500, Bear 3,000 (the definitive guide rounds all three to "1,500+"). *guides* strategy guide,…
- [[gameplay/server-rules|Server rules checklist]] § Land war *(name match)*: [ ] TP is a shared team pool. Kill TP: normal 30, elite 100, Troll 1,500, Ogre 2,500, Bear 3,000. — strategy, definitive — M
- [[gameplay/server-rules|Server rules checklist]] § Land war *(name match)*: [ ] Jungle: Troll & Ogre spawn at 36:00 then 4 min after death; Bear at 35:00 then 5 min after death; killed jungle bosses fight for the killer's team (towers,…
- [[gameplay/server-rules|Server rules checklist]] § PvP, events, forts *(name match)*: [ ] Jungle: medium jungle mob spawns at PvP start; Troll/Ogre at 36:00, respawn 4 min; Bear at 35:00, respawn 5 min — WM 0830, blog — M

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@8c | 102 |
| u8@91 | 15 |
| f32@c0 | 4.3 |
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
