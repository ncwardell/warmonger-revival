---
title: "Elite Skeleton Warrior"
type: "monster"
id: 702
status: "stub"
missing: ["level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 702", "client: Quest.cdb kill objectives (quests 101)", "video: [[gameplay/video-early-quests|Video notes: the first 20 levels]] §5, target frame at [31:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=1910s): HP 600, regen +12/tick (2% of max) (Elite Skeleton Warrior during quest 101 (kill group 10004 = 702/703))"]
name_key: "UnitName_702"
category: 1
class_mask: 1
kill_group: 10004
model: 41
model_name: "MOB_Skeleton_Elilte_01"
model_path: "character/npc/monster/mob_seleton_elite_01/mob_seleton_elite_01.mo"
scale: 1.1
radius: 1
sounds: [4070000, 4070000, 3060040, 3060040, 3060040, 4070003]
quest_targets:
  - {"quest": 101, "need": 10, "group": 10004}
quest_drops:
  - {"quest": 101, "item": 2572, "rate": 100, "need": 10}
spawn_fields: [99, 100, 101]
hp: 600
hp_regen: 12
---
<!-- generated:start -->
<!-- generated-keys: title=334e98 type=9bbc46 id=a08521 sources=d63d67 name_key=a51141 category=356a19 class_mask=356a19 kill_group=75186a model=761f22 model_name=a307db model_path=eb5090 scale=4491f8 radius=356a19 sounds=6dfede quest_targets=8fd759 quest_drops=29ce0c spawn_fields=0f349c hp=15aa0c hp_regen=7b5200 -->
|  |  |
|---|---|
| **Unit id** | `702` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10004` with [[wiki/monsters/703-elite-skeleton-archer\|Elite Skeleton Archer]] |
| **Model** | ObjectList `41` MOB_Skeleton_Elilte_01 (`character/npc/monster/mob_seleton_elite_01/mob_seleton_elite_01.mo`) |
| **Scale** | 1.1 (second scale / radius 1) |

*No image: the client has no 2-D monster art (only the 3-D model).*

### Server stats

None of these is in the client; they were server data. Fill them in the front matter with a source (`drops: [{"item": id, "rate": %, "count": [min, max]}]`, `spawns: [{"field": id, "x": .., "z": .., "count": n, "respawn_s": s}]`).

| field | value |
|---|---|
| hp | 600 |
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
| hp_regen | 12 |

### Quests

- [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]: collect 10 × [[wiki/items/2572-weak-elite-skeleton-bone|Weak Elite Skeleton bone]] (drops at 100% while the quest is active) in [[wiki/fields/99-corpse-incineration|Corpse incineration]], [[wiki/fields/100-corpse-incineration|Corpse incineration]], [[wiki/fields/101-corpse-incineration|Corpse incineration]] — via kill group `10004` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/99-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]
- [[wiki/fields/100-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]
- [[wiki/fields/101-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/101-all-sorts-of-fragile-bones|All sorts of Fragile bones]]

### Other units with this name

[[wiki/monsters/642-elite-skeleton-warrior|Elite Skeleton Warrior (642)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 2 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 3 | 0 | 3060040 | `effect/ES3060040.wav` |
| 4 | 0 | 3060040 | `effect/ES3060040.wav` |
| 5 | 0 | 3060040 | `effect/ES3060040.wav` |
| 6 | 0 | 4070003 | `Unit/UE4070003.wav` |

### Seen in

- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps at [24:12](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1452s): 22. Portal → Corpse incineration (field 99) 24:12. The player arrives beside a "Training Camp" return portal (gate 1500 at 306.03, 2254.17, *client*). Mobs: Sk…
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Monsters and damage: Skeleton Warrior / Archer, Elite Skeleton Warrior / Archer · 700 / 701, 702 / 703 · Corpse incineration (99) · groups 10003 / 10004; they hit for about 19
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen at [31:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=1910s) *(name match)*: Elite Skeleton Warrior · 600 · +12 · 31:50
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen *(name match)*: Kill messages ("X was destroyed") in quest order: Slime → Chepa Warrior / Chepa Archer (Training Ground circle, many killed for exp) → Bee, Cobra → Chepa Warri…

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
