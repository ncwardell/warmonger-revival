---
title: "Ancient Ghost"
type: "monster"
id: 827
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 827", "docs: [[gameplay/dungeon-drops]] (boss of field 826)", "client: Quest.cdb kill objectives (quests 21)"]
name_key: "UnitName_827"
category: 1
class_mask: 1
model: 242
model_name: "MOB_GhostKing_01_02"
model_path: "character/npc/monster/npc_evil/mob_ghostking_02.mo"
scale: 1.5
radius: 1
projectile: 865
sounds: [4070058, 4070058, 4070059, 4070059, 4070059, 4070060]
boss_of: [826]
quest_targets:
  - {"quest": 21, "need": 3}
quest_drops:
  - {"quest": 21, "item": 2568, "rate": 70, "need": 3}
spawn_fields: [113, 826]
---
<!-- generated:start -->
<!-- generated-keys: title=1b5fce type=9bbc46 id=1d57cc sources=5ce207 name_key=cfe690 category=356a19 class_mask=356a19 model=851cd0 model_name=b71a5d model_path=16e067 scale=aa8f28 radius=356a19 projectile=81d51c sounds=c9a41e boss_of=721895 quest_targets=93cdb1 quest_drops=3c173d spawn_fields=7888b5 -->
|  |  |
|---|---|
| **Unit id** | `827` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `242` MOB_GhostKing_01_02 (`character/npc/monster/npc_evil/mob_ghostking_02.mo`) |
| **Scale** | 1.5 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 865 (archers carry one; meaning *inferred*) |
| **Boss of** | Field 826 |

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

- [[wiki/quests/21-group-ancient-ghosts|(Group) Ancient Ghosts]]: collect 3 × [[wiki/items/2568-essence-of-darkness|essence of Darkness]] (drops at 70% while the quest is active) in [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]]

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/113-the-avenue-of-spirit|The avenue of spirit]] — quest map of [[wiki/quests/21-group-ancient-ghosts|(Group) Ancient Ghosts]]
- Field 826 — boss ([[gameplay/dungeon-drops]])

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070058 | `Unit/UE4070058.wav` |
| 2 | 0 | 4070058 | `Unit/UE4070058.wav` |
| 3 | 925 | 4070059 | `Unit/UE4070059.wav` |
| 4 | 925 | 4070059 | `Unit/UE4070059.wav` |
| 5 | 0 | 4070059 | `Unit/UE4070059.wav` |
| 6 | 0 | 4070060 | `Unit/UE4070060.wav` |

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § Fortress (levels 12–20) at [65:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=3920s): 24. [Group] Ancient Ghosts (21, Freya, 65:20): obtain the essence of Darkness ×3 (Ancient Ghost 827, 70%) in The avenue of spirit (113). Panel: 900000 exp [990…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 8 |
| u8@90 | 1 |
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
