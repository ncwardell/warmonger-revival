---
title: "Skeleton Archer Officer"
type: "monster"
id: 705
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 705", "client: Quest.cdb kill objectives (quests 107)"]
name_key: "UnitName_705"
category: 1
class_mask: 1
model: 44
model_name: "MOB_Skeleton_Elilte_02_02"
model_path: "character/npc/monster/mob_seleton_elite_02/mob_seleton_elite_02_02.mo"
scale: 1.5
radius: 1
projectile: 583
sounds: [4070113, 4070113, 4070014, 4070014, 4070014, 4070003]
quest_targets:
  - {"quest": 107, "need": 1}
spawn_fields: [99, 100, 101]
---
<!-- generated:start -->
<!-- generated-keys: title=dcf0ba type=9bbc46 id=794bb3 sources=117ca7 name_key=22e00d category=356a19 class_mask=356a19 model=98fbc4 model_name=adcae0 model_path=f9cec0 scale=aa8f28 radius=356a19 projectile=9c676e sounds=89c031 quest_targets=6c3ee6 spawn_fields=0f349c -->
|  |  |
|---|---|
| **Unit id** | `705` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `44` MOB_Skeleton_Elilte_02_02 (`character/npc/monster/mob_seleton_elite_02/mob_seleton_elite_02_02.mo`) |
| **Scale** | 1.5 (second scale / radius 1) |
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

- [[wiki/quests/107-hunting-skeletons|Hunting Skeletons]]: kill 1 in [[wiki/fields/99-corpse-incineration|Corpse incineration]], [[wiki/fields/100-corpse-incineration|Corpse incineration]], [[wiki/fields/101-corpse-incineration|Corpse incineration]]

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/99-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/107-hunting-skeletons|Hunting Skeletons]]
- [[wiki/fields/100-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/107-hunting-skeletons|Hunting Skeletons]]
- [[wiki/fields/101-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/107-hunting-skeletons|Hunting Skeletons]]

### Other units with this name

[[wiki/monsters/687-skeleton-archer-officer|Skeleton Archer Officer (687)]], [[wiki/monsters/852-skeleton-archer-officer|Skeleton Archer Officer (852)]]

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

- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps at [28:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1680s), [28:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1720s): 24. Skeleton Warrior Officer (704) and Skeleton Archer Officer (705) in the south of field 99, guarded by elites 28:00–28:40. An officer's speech bubble shouts…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 5.3 |
| f32@10c | 0.5 |
<!-- generated:end -->

## Notes

- Stands in the south of [[wiki/fields/99-corpse-incineration|Corpse incineration (99)]], guarded by elite skeletons; target of quest 107 (video + client, [[gameplay/video-tutorial-walkthrough]] step 24 at [28:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1680s); [[gameplay/video-character-creation-and-tutorial]] step 20).
- An officer's speech bubble shouts "Kill them!!" (video, [[gameplay/video-tutorial-walkthrough]] step 24).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/video-tutorial-walkthrough]] step 24; [[gameplay/video-early-quests]] §2, §5; [[gameplay/video-character-creation-and-tutorial]] step 20

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
