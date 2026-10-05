---
title: "Fragile Elite Lizard Swordsman"
type: "monster"
id: 652
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 652", "client: Quest.cdb kill objectives (quests 104)"]
name_key: "UnitName_652"
category: 1
class_mask: 1
kill_group: 10006
model: 71
model_name: "MOB_Lizardman_01"
model_path: "character/npc/monster/mob_lizardman/mob_lizardman_01.mo"
scale: 2
radius: 1
sounds: [4070000, 4070000, 4070013, 4070013, 4070013]
quest_targets:
  - {"quest": 104, "need": 10, "group": 10006}
spawn_fields: [103, 105, 107]
---
<!-- generated:start -->
<!-- generated-keys: title=6c00f2 type=9bbc46 id=918fc6 sources=ccd4fa name_key=91179a category=356a19 class_mask=356a19 kill_group=e86188 model=d02560 model_name=39ab4b model_path=21b985 scale=da4b92 radius=356a19 sounds=904c2a quest_targets=a0851c spawn_fields=2d93e6 -->
|  |  |
|---|---|
| **Unit id** | `652` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10006` with [[wiki/monsters/653-fragile-elite-lizard-lancer\|Fragile Elite Lizard Lancer]] |
| **Model** | ObjectList `71` MOB_Lizardman_01 (`character/npc/monster/mob_lizardman/mob_lizardman_01.mo`) |
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
| 1 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 2 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 3 | 12 | 4070013 | `Unit/UE4070013.wav` |
| 4 | 12 | 4070013 | `Unit/UE4070013.wav` |
| 5 | 0 | 4070013 | `Unit/UE4070013.wav` |

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen *(name match)*: Kill messages ("X was destroyed") in quest order: Slime → Chepa Warrior / Chepa Archer (Training Ground circle, many killed for exp) → Bee, Cobra → Chepa Warri…

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
