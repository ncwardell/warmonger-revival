---
title: "Skeleton Archer"
type: "monster"
id: 701
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 701", "client: Quest.cdb kill objectives (quests 101)"]
name_key: "UnitName_701"
category: 1
class_mask: 1
kill_group: 10003
model: 11
model_name: "MOB_Seleton02"
model_path: "character/npc/monster/mob_seleton02/mob_seleton02.mo"
scale: 0.8
radius: 0.8
projectile: 583
sounds: [4070113, 4070113, 4070014, 4070014, 4070014, 4070003]
quest_targets:
  - {"quest": 101, "need": 10, "group": 10003}
quest_drops:
  - {"quest": 101, "item": 2571, "rate": 100, "need": 10}
spawn_fields: [99, 100, 101]
---
<!-- generated:start -->
<!-- generated-keys: title=4c173c type=9bbc46 id=917098 sources=5c3571 name_key=478206 category=356a19 class_mask=356a19 kill_group=b27b41 model=17ba07 model_name=519469 model_path=c36c5c scale=480262 radius=480262 projectile=9c676e sounds=89c031 quest_targets=c290ae quest_drops=cee252 spawn_fields=0f349c -->
|  |  |
|---|---|
| **Unit id** | `701` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10003` with [[wiki/monsters/700-skeleton-warrior\|Skeleton Warrior]] |
| **Model** | ObjectList `11` MOB_Seleton02 (`character/npc/monster/mob_seleton02/mob_seleton02.mo`) |
| **Scale** | 0.8 (second scale / radius 0.8) |
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

- [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]: collect 10 × [[wiki/items/2571-weak-skeleton-bone|Weak Skeleton bone]] (drops at 100% while the quest is active) in [[wiki/fields/99-corpse-incineration|Corpse incineration]], [[wiki/fields/100-corpse-incineration|Corpse incineration]], [[wiki/fields/101-corpse-incineration|Corpse incineration]] — via kill group `10003` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/99-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]
- [[wiki/fields/100-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]
- [[wiki/fields/101-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]

### Other units with this name

[[wiki/monsters/641-skeleton-archer|Skeleton Archer (641)]]

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
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § Training Ground and Camp (levels 1–11) at [26:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=1590s), [36:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=2196s) *(name match)*: 12. Hunting Skeletons (107, the Scout, 26:30): kill the Skeleton Warrior Leader and the Skeleton Archer Leader (704/705), then report to Frei at 36:35. Reward:…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 2.7 |
| f32@10c | 1 |
<!-- generated:end -->

## Notes

- Lives in [[wiki/fields/99-corpse-incineration|Corpse incineration (99)]]; kill group 10003 for quest 101 (Weak Skeleton bone) (video + client, [[gameplay/video-tutorial-walkthrough]] step 22 at [24:12](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1452s), step 26).
- Skeletons hit the player (a low-level Guardian) for about 19; the player's basic hits did 109 damage to them (video, [[gameplay/video-tutorial-walkthrough]] § Monsters and damage).

## Behaviour

- Quest items drop at the `Quest.tsv` rate: every kill of a matching monster gave one while the quest was active (video, [[gameplay/video-early-quests]] §6).

## Sources

- [[gameplay/video-tutorial-walkthrough]] steps 22–26 and § Monsters and damage; [[gameplay/video-early-quests]] §2, §5

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
