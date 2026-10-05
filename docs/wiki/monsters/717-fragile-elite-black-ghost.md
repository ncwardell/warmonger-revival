---
title: "Fragile Elite Black Ghost"
type: "monster"
id: 717
status: "partial"
missing: ["level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 717", "client: Quest.cdb kill objectives (quests 108, 750, 1102)", "video: [[gameplay/video-early-quests|Video notes: the first 20 levels]] §5, target frame at [83:15](https://www.youtube.com/watch?v=s04CSN16w1s&t=4995s): HP 2000, regen +40/tick (2% of max) (Fragile Elite Black / Red Ghost)"]
name_key: "UnitName_717"
category: 1
class_mask: 1
kill_group: 10008
model: 274
model_name: "NPC_Evil001"
model_path: "character/npc/monster/NPC_Evil/NPC_Evil001.mo"
scale: 2
radius: 1
sounds: [4000004, 4000004, 4000004, 4000004, 4000004, 4000004]
quest_targets:
  - {"quest": 108, "need": 10, "group": 10008}
  - {"quest": 750, "need": 50, "group": 10008}
  - {"quest": 1102, "need": 50, "group": 10008}
spawn_fields: [113]
hp: 2000
hp_regen: 40
---
<!-- generated:start -->
<!-- generated-keys: title=38f38c type=9bbc46 id=e1c1bf sources=82e350 name_key=eb4abb category=356a19 class_mask=356a19 kill_group=e3a530 model=431bf3 model_name=07adc2 model_path=e26f4d scale=da4b92 radius=356a19 sounds=2db6a5 quest_targets=935e48 spawn_fields=85c8ae hp=a4ac91 hp_regen=af3e13 -->
|  |  |
|---|---|
| **Unit id** | `717` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10008` with [[wiki/monsters/718-fragile-elite-red-ghost\|Fragile Elite Red Ghost]] |
| **Model** | ObjectList `274` NPC_Evil001 (`character/npc/monster/NPC_Evil/NPC_Evil001.mo`) |
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
| 3 | 0 | 4000004 | `voice/UV4000004.wav` |
| 4 | 0 | 4000004 | `voice/UV4000004.wav` |
| 5 | 0 | 4000004 | `voice/UV4000004.wav` |
| 6 | 0 | 4000004 | `voice/UV4000004.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 4.3 |
| f32@10c | 0.5 |
<!-- generated:end -->

## Notes

- Seen killed in The avenue of spirit (Abyss Lv 4, field 113) (video, [[gameplay/video-early-quests]] §1, §5).
- The target frame read HP 2000 with regeneration +40 (2% of max) at [83:15](https://www.youtube.com/watch?v=s04CSN16w1s&t=4995s) (video, [[gameplay/video-early-quests]] §5).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/video-early-quests]] §1, §5

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
