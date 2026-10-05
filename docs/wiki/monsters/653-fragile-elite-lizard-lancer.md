---
title: "Fragile Elite Lizard Lancer"
type: "monster"
id: 653
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 653", "client: Quest.cdb kill objectives (quests 104)"]
name_key: "UnitName_653"
category: 1
class_mask: 1
kill_group: 10006
model: 72
model_name: "MOB_Lizardman_02"
model_path: "character/npc/monster/mob_lizardman/mob_lizardman_02.mo"
scale: 2
radius: 1
projectile: 808
sounds: [4070015, 4070015, 4070014, 4070014, 4070014]
quest_targets:
  - {"quest": 104, "need": 10, "group": 10006}
spawn_fields: [103, 105, 107]
---
<!-- generated:start -->
<!-- generated-keys: title=92529d type=9bbc46 id=e1c03d sources=29d62e name_key=1f35af category=356a19 class_mask=356a19 kill_group=e86188 model=c09763 model_name=f9e294 model_path=2c38fa scale=da4b92 radius=356a19 projectile=38afd2 sounds=364564 quest_targets=a0851c spawn_fields=2d93e6 -->
|  |  |
|---|---|
| **Unit id** | `653` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10006` with [[wiki/monsters/652-fragile-elite-lizard-swordsman\|Fragile Elite Lizard Swordsman]] |
| **Model** | ObjectList `72` MOB_Lizardman_02 (`character/npc/monster/mob_lizardman/mob_lizardman_02.mo`) |
| **Scale** | 2 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 808 (archers carry one; meaning *inferred*) |

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

- [[wiki/quests/104-delivering-punishment|Delivering Punishment]]: kill 10 in [[wiki/fields/103-place-for-scattered-troops|Place for Scattered troops]], [[wiki/fields/105-place-for-scattered-troops|Place for Scattered troops]], [[wiki/fields/107-place-for-scattered-troops|Place for Scattered troops]] — via kill group `10006` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/103-place-for-scattered-troops|Place for Scattered troops]] — quest map of [[wiki/quests/104-delivering-punishment|Delivering Punishment]]
- [[wiki/fields/105-place-for-scattered-troops|Place for Scattered troops]] — quest map of [[wiki/quests/104-delivering-punishment|Delivering Punishment]]
- [[wiki/fields/107-place-for-scattered-troops|Place for Scattered troops]] — quest map of [[wiki/quests/104-delivering-punishment|Delivering Punishment]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070015 | `Unit/UE4070015.wav` |
| 2 | 0 | 4070015 | `Unit/UE4070015.wav` |
| 3 | 12 | 4070014 | `Unit/UE4070014.wav` |
| 4 | 12 | 4070014 | `Unit/UE4070014.wav` |
| 5 | 0 | 4070014 | `Unit/UE4070014.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 3 |
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
