---
title: "Wasteland Ogre"
type: "monster"
id: 575
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 575", "client: Quest.cdb kill objectives (quests 50)"]
name_key: "UnitName_575"
category: 8
class_mask: 1
kill_group: 571
model: 286
model_name: "MOB_Oger_Forest_01"
model_path: "character/npc/monster/mob_oger/mob_oger_wasteland_01.mo"
scale: 1
radius: 1
sounds: [4070010, 4070010, 4070120]
quest_targets:
  - {"quest": 50, "need": 2, "group": 571}
---
<!-- generated:start -->
<!-- generated-keys: title=46223f type=9bbc46 id=05a53e sources=cc85f0 name_key=4966cc category=fe5dbb class_mask=356a19 kill_group=2bfba6 model=7edab1 model_name=9801db model_path=981715 scale=356a19 radius=356a19 sounds=e32a74 quest_targets=8e43ed -->
|  |  |
|---|---|
| **Unit id** | `575` |
| **Category** | field monster (inferred: ogres, trolls, bears, phytons) (`category@8a` = 8) |
| **Class mask** | 1 (monster) |
| **Kill group** | `571` with [[wiki/monsters/571-bear\|Bear]], [[wiki/monsters/573-giant-bear\|Giant Bear]], [[wiki/monsters/576-wasteland-giant-ogre\|Wasteland Giant Ogre]], [[wiki/monsters/577-lava-ogre\|Lava Ogre]], [[wiki/monsters/578-lava-giant-ogre\|Lava Giant Ogre]], [[wiki/monsters/579-sulphur-ogre\|Sulphur Ogre]], [[wiki/monsters/580-sulphur-giant-ogre\|Sulphur Giant Ogre]], [[wiki/monsters/581-ice-ogre\|Ice Ogre]], [[wiki/monsters/582-ice-giant-ogre\|Ice Giant Ogre]], [[wiki/monsters/583-troll\|Troll]], [[wiki/monsters/584-troll\|Troll]] |
| **Model** | ObjectList `286` MOB_Oger_Forest_01 (`character/npc/monster/mob_oger/mob_oger_wasteland_01.mo`) |
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

### Quests

- [[wiki/quests/50-war-winning-means|War - Winning means]]: kill 2 — via kill group `571` (*inferred* from UnitDB `i32@80`)

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 2 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 6 | 0 | 4070120 | `Unit/UE4070120.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@8c | 103 |
| u8@91 | 15 |
| f32@c0 | 4.5 |
| f32@10c | 1 |
<!-- generated:end -->

## Notes

- [[gameplay/pvp-and-matches]] §1 lists this unit among the land-war **jungle bosses** (Ogre) (client ids; the guides do not say which id spawns on which land).
- The same war video shows a second jungle camp (Ogre) cleared at 38:51–38:35 on the war clock in Eternal River – Upper Region (video, [[gameplay/video-fort-war]] §5).

## Behaviour

- Spawns first at 36:00 on the 40:00 war clock, then 4 minutes after each death (guides, [[gameplay/pvp-and-matches]] §1; blog, [[gameplay/events-and-schedules]] §8).
- When killed it joins the killer's team and pushes the nearest enemy towers, then the nexus (guides, [[gameplay/pvp-and-matches]] §1).
- TP for the kill: 2,500 (strategy guide) or 1,500 (blog) (guides, [[gameplay/pvp-and-matches]] §1; [[gameplay/events-and-schedules]] §8).

## Sources

- [[gameplay/pvp-and-matches]] §1; [[gameplay/events-and-schedules]] §8; [[gameplay/video-fort-war]]

## Open questions

- Which jungle id spawns where is unknown, so no `spawns` are set.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
