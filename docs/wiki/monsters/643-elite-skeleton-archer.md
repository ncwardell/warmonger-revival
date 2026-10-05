---
title: "Elite Skeleton Archer"
type: "monster"
id: 643
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 643", "client: Quest.cdb kill objectives (quests 727, 1006)"]
name_key: "UnitName_643"
category: 1
class_mask: 1
kill_group: 10010
model: 43
model_name: "MOB_Skeleton_Elilte_02"
model_path: "character/npc/monster/mob_seleton_elite_02/mob_seleton_elite_02.mo"
scale: 1.1
radius: 1
projectile: 583
sounds: [4070113, 4070113, 4070014, 4070014, 4070014, 4070003]
quest_targets:
  - {"quest": 727, "need": 5, "group": 10010}
  - {"quest": 1006, "need": 5, "group": 10010}
quest_drops:
  - {"quest": 727, "item": 2557, "rate": 100, "need": 5}
  - {"quest": 1006, "item": 2657, "rate": 100, "need": 5}
spawn_fields: [121]
---
<!-- generated:start -->
<!-- generated-keys: title=57f240 type=9bbc46 id=dcd7d0 sources=880c2f name_key=a941a4 category=356a19 class_mask=356a19 kill_group=b66ddc model=0286dd model_name=843967 model_path=04ed34 scale=4491f8 radius=356a19 projectile=9c676e sounds=89c031 quest_targets=30542b quest_drops=24ab91 spawn_fields=a5a5cb -->
|  |  |
|---|---|
| **Unit id** | `643` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10010` with [[wiki/monsters/642-elite-skeleton-warrior\|Elite Skeleton Warrior]] |
| **Model** | ObjectList `43` MOB_Skeleton_Elilte_02 (`character/npc/monster/mob_seleton_elite_02/mob_seleton_elite_02.mo`) |
| **Scale** | 1.1 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 583 (archers carry one; meaning *inferred*) |

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

- [[wiki/quests/727-the-necessary-materials|The necessary materials]]: collect 5 × [[wiki/items/2557-elite-skeleton-bone|Elite Skeleton bone]] (drops at 100% while the quest is active) in [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] — via kill group `10010` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1006-skull-temple-hunting|Skull Temple : Hunting]]: collect 5 × [[wiki/items/2657-elite-skeleton-bone|Elite Skeleton bone]] (drops at 100% while the quest is active) in [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] — via kill group `10010` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] — quest map of [[wiki/quests/727-the-necessary-materials|The necessary materials]], [[wiki/quests/1006-skull-temple-hunting|Skull Temple : Hunting]]

### Other units with this name

[[wiki/monsters/703-elite-skeleton-archer|Elite Skeleton Archer (703)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070113 | `Unit/UE4070113.wav` |
| 2 | 0 | 4070113 | `Unit/UE4070113.wav` |
| 3 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 4 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 5 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 6 | 0 | 4070003 | `Unit/UE4070003.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 5.3 |
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
