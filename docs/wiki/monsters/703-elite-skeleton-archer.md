---
title: "Elite Skeleton Archer"
type: "monster"
id: 703
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 703", "client: Quest.cdb kill objectives (quests 101)"]
name_key: "UnitName_703"
category: 1
class_mask: 1
kill_group: 10004
model: 43
model_name: "MOB_Skeleton_Elilte_02"
model_path: "character/npc/monster/mob_seleton_elite_02/mob_seleton_elite_02.mo"
scale: 1.1
radius: 1
projectile: 583
sounds: [4070113, 4070113, 4070014, 4070014, 4070014, 4070003]
quest_targets:
  - {"quest": 101, "need": 10, "group": 10004}
quest_drops:
  - {"quest": 101, "item": 2572, "rate": 100, "need": 10}
spawn_fields: [99, 100, 101]
---
<!-- generated:start -->
<!-- generated-keys: title=57f240 type=9bbc46 id=8fc1bb sources=1fd46b name_key=4a8651 category=356a19 class_mask=356a19 kill_group=75186a model=0286dd model_name=843967 model_path=04ed34 scale=4491f8 radius=356a19 projectile=9c676e sounds=89c031 quest_targets=8fd759 quest_drops=29ce0c spawn_fields=0f349c -->
|  |  |
|---|---|
| **Unit id** | `703` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10004` with [[wiki/monsters/702-elite-skeleton-warrior\|Elite Skeleton Warrior]] |
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

- [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]: collect 10 × [[wiki/items/2572-weak-elite-skeleton-bone|Weak Elite Skeleton bone]] (drops at 100% while the quest is active) in [[wiki/fields/99-corpse-incineration|Corpse incineration]], [[wiki/fields/100-corpse-incineration|Corpse incineration]], [[wiki/fields/101-corpse-incineration|Corpse incineration]] — via kill group `10004` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/99-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]
- [[wiki/fields/100-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]
- [[wiki/fields/101-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]

### Other units with this name

[[wiki/monsters/643-elite-skeleton-archer|Elite Skeleton Archer (643)]]

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

### Seen in

- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps at [24:12](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1452s): 22. Portal → Corpse incineration (field 99) 24:12. The player arrives beside a "Training Camp" return portal (gate 1500 at 306.03, 2254.17, *client*). Mobs: Sk…

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
