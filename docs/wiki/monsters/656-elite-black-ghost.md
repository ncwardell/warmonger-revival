---
title: "Elite Black Ghost"
type: "monster"
id: 656
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 656", "client: Quest.cdb kill objectives (quests 778, 1027)"]
name_key: "UnitName_656"
category: 1
class_mask: 1
kill_group: 10030
model: 274
model_name: "NPC_Evil001"
model_path: "character/npc/monster/NPC_Evil/NPC_Evil001.mo"
scale: 2
radius: 1
sounds: [4000004, 4000004, 4000004, 4000004, 4000004, 4000004]
quest_targets:
  - {"quest": 778, "need": 8, "group": 10030}
  - {"quest": 1027, "need": 8, "group": 10030}
spawn_fields: [124]
---
<!-- generated:start -->
<!-- generated-keys: title=18c599 type=9bbc46 id=e30e49 sources=3e6350 name_key=61ea42 category=356a19 class_mask=356a19 kill_group=c52651 model=431bf3 model_name=07adc2 model_path=e26f4d scale=da4b92 radius=356a19 sounds=2db6a5 quest_targets=fbb5ad spawn_fields=181a14 -->
|  |  |
|---|---|
| **Unit id** | `656` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10030` with [[wiki/monsters/657-elite-red-ghost\|Elite Red Ghost]] |
| **Model** | ObjectList `274` NPC_Evil001 (`character/npc/monster/NPC_Evil/NPC_Evil001.mo`) |
| **Scale** | 2 (second scale / radius 1) |

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

- [[wiki/quests/778-ghost-soldier|Ghost soldier]]: kill 8 in [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] — via kill group `10030` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1027-ghost-fortress-hunting|Ghost Fortress : Hunting]]: kill 8 in [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] — via kill group `10030` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] — quest map of [[wiki/quests/778-ghost-soldier|Ghost soldier]], [[wiki/quests/1027-ghost-fortress-hunting|Ghost Fortress : Hunting]]

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

### Seen in

- [[gameplay/precept-shop|Precept shop and precept quests]] § 3. Example rolled quest (screenshot) *(name match)*: 2 · Kill Elite Ghost 0/10 · kill group 10030 = Elite Black Ghost 656, Elite Red Ghost 657 *client*

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 4.3 |
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
