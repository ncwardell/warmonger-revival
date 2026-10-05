---
title: "Chepa Archer"
type: "monster"
id: 546
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 546"]
name_key: "UnitName_546"
category: 8
class_mask: 1
model: 31
model_name: "MOB_Chepa02_0_1_0_00_00"
model_path: "character/npc/monster/mob_chepa/mob_chepa02.mo"
scale: 1.8
radius: 1
projectile: 662
sounds: [4070000, 4070000, 4070014, 4070014, 4070014, 4070016]
---
<!-- generated:start -->
<!-- generated-keys: title=99fa35 type=9bbc46 id=461742 sources=c44f0a name_key=90013c category=fe5dbb class_mask=356a19 model=632667 model_name=aae49c model_path=baa448 scale=93ec1d radius=356a19 projectile=091d03 sounds=8b4aa6 -->
|  |  |
|---|---|
| **Unit id** | `546` |
| **Category** | field monster (inferred: ogres, trolls, bears, phytons) (`category@8a` = 8) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `31` MOB_Chepa02_0_1_0_00_00 (`character/npc/monster/mob_chepa/mob_chepa02.mo`) |
| **Scale** | 1.8 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 662 (archers carry one; meaning *inferred*) |

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

### Other units with this name

[[wiki/monsters/547-chepa-archer|Chepa Archer (547)]], [[wiki/monsters/669-chepa-archer|Chepa Archer (669)]], [[wiki/monsters/707-chepa-archer|Chepa Archer (707)]], [[wiki/monsters/728-chepa-archer|Chepa Archer (728)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 2 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 3 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 4 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 5 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 6 | 0 | 4070016 | `Unit/UE4070016.wav` |

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § Training Camp (field 92) and back at [8:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=530s) *(name match)*: 13. 8:50 Lewellyn (Scroll Merchant, 315) offers side quest 100 "Hunting for Furs" (dialogue 644): 5 White Chepa Fur 2554 from Chepa Warrior 727 and 5 Black Che…
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 5. Other facts *(name match)*: Monsters by area: Training Ground: Slime 604, Bee 731, Cobra 732, Chepa Warrior 727, Chepa Archer 728, Chepa officers 710/711 (the officers fight inside a grou…
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen *(name match)*: Kill messages ("X was destroyed") in quest order: Slime → Chepa Warrior / Chepa Archer (Training Ground circle, many killed for exp) → Bee, Cobra → Chepa Warri…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@8c | 112 |
| u8@91 | 15 |
| f32@c0 | 2.7 |
| f32@10c | 1 |
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
