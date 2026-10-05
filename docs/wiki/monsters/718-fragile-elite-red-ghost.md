---
title: "Fragile Elite Red Ghost"
type: "monster"
id: 718
status: "stub"
missing: ["level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 718", "client: Quest.cdb kill objectives (quests 108, 750, 1102)", "video: [[gameplay/video-early-quests|Video notes: the first 20 levels]] §5, target frame at [83:15](https://www.youtube.com/watch?v=s04CSN16w1s&t=4995s): HP 2000, regen +40/tick (2% of max) (Fragile Elite Black / Red Ghost)"]
name_key: "UnitName_718"
category: 1
class_mask: 1
kill_group: 10008
model: 16
model_name: "NPC_Evil002_0_1_0_00_00"
model_path: "character/npc/monster/npc_evil/npc_evil002.mo"
scale: 2
radius: 1
sounds: [4000004, 4000004, 4020004, 4020004, 4030004, 4040004]
quest_targets:
  - {"quest": 108, "need": 10, "group": 10008}
  - {"quest": 750, "need": 50, "group": 10008}
  - {"quest": 1102, "need": 50, "group": 10008}
spawn_fields: [113]
hp: 2000
hp_regen: 40
---
<!-- generated:start -->
<!-- generated-keys: title=5bfe0d type=9bbc46 id=395ea6 sources=38cbdf name_key=572846 category=356a19 class_mask=356a19 kill_group=e3a530 model=1574bd model_name=18b713 model_path=9fb616 scale=da4b92 radius=356a19 sounds=2135c0 quest_targets=935e48 spawn_fields=85c8ae hp=a4ac91 hp_regen=af3e13 -->
|  |  |
|---|---|
| **Unit id** | `718` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10008` with [[wiki/monsters/717-fragile-elite-black-ghost\|Fragile Elite Black Ghost]] |
| **Model** | ObjectList `16` NPC_Evil002_0_1_0_00_00 (`character/npc/monster/npc_evil/npc_evil002.mo`) |
| **Scale** | 2 (second scale / radius 1) |

*No image: the client has no 2-D monster art (only the 3-D model).*

### Server stats

None of these is in the client; they were server data. Fill them in the front matter with a source (`drops: [{"item": id, "rate": %, "count": [min, max]}]`, `spawns: [{"field": id, "x": .., "z": .., "count": n, "respawn_s": s}]`).

| field | value |
|---|---|
| hp | 2,000 |
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
| hp_regen | 40 |

### Quests

- [[wiki/quests/108-hunting-ghosts-spirit-avenue|Hunting Ghosts (Spirit Avenue)]]: kill 10 in [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] — via kill group `10008` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/750-kill-monster-of-the-avenue-of-spirit|Kill monster of The avenue of spirit]]: kill 50 in [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] — via kill group `10008` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1102-the-avenue-of-spirit-kill-monster|The Avenue of spirit : Kill monster]]: kill 50 in [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] — via kill group `10008` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] — quest map of [[wiki/quests/108-hunting-ghosts-spirit-avenue|Hunting Ghosts (Spirit Avenue)]], [[wiki/quests/750-kill-monster-of-the-avenue-of-spirit|Kill monster of The avenue of spirit]], [[wiki/quests/1102-the-avenue-of-spirit-kill-monster|The Avenue of spirit : Kill monster]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4000004 | `voice/UV4000004.wav` |
| 2 | 0 | 4000004 | `voice/UV4000004.wav` |
| 3 | 0 | 4020004 | not in sound.csv |
| 4 | 0 | 4020004 | not in sound.csv |
| 5 | 0 | 4030004 | not in sound.csv |
| 6 | 0 | 4040004 | not in sound.csv |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 6.2 |
| f32@10c | 0.5 |
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
