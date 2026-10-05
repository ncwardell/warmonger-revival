---
title: "Chepa Warrior"
type: "monster"
id: 544
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 544"]
name_key: "UnitName_544"
category: 8
class_mask: 1
model: 30
model_name: "MOB_Chepa01_0_1_0_00_00"
model_path: "character/npc/monster/mob_chepa/mob_chepa01.mo"
scale: 1.8
radius: 1
sounds: [4070000, 4070000, 4070013, 4070013, 4070013, 4070016]
---
<!-- generated:start -->
<!-- generated-keys: title=8fc8c1 type=9bbc46 id=b87bed sources=2468b7 name_key=a98695 category=fe5dbb class_mask=356a19 model=22d200 model_name=67408a model_path=207e1f scale=93ec1d radius=356a19 sounds=14185a -->
|  |  |
|---|---|
| **Unit id** | `544` |
| **Category** | field monster (inferred: ogres, trolls, bears, phytons) (`category@8a` = 8) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `30` MOB_Chepa01_0_1_0_00_00 (`character/npc/monster/mob_chepa/mob_chepa01.mo`) |
| **Scale** | 1.8 (second scale / radius 1) |

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

[[wiki/monsters/545-chepa-warrior|Chepa Warrior (545)]], [[wiki/monsters/668-chepa-warrior|Chepa Warrior (668)]], [[wiki/monsters/706-chepa-warrior|Chepa Warrior (706)]], [[wiki/monsters/727-chepa-warrior|Chepa Warrior (727)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 2 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 3 | 0 | 4070013 | `Unit/UE4070013.wav` |
| 4 | 0 | 4070013 | `Unit/UE4070013.wav` |
| 5 | 0 | 4070013 | `Unit/UE4070013.wav` |
| 6 | 0 | 4070016 | `Unit/UE4070016.wav` |

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 4. NPC positions (Erion copy) at [13:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=790s) *(name match)*: Chepa Warrior/Archer Officers 710/711 · — · 93 · north arena (not measured) · — · 13:10 · Dialogue 685 says "in the north"
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § Training Ground and Camp (levels 1–11) at [7:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=420s), [12:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=757s) *(name match)*: 3. The task at hand (3, Floyd), accepted at 7:00: 5 Bee Needle from Bees (731) and 5 Cobra/Snake Leather from Cobras (732). Turn in to Floyd at 12:35. Reward:…
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 5. Other facts *(name match)*: Monsters by area: Training Ground: Slime 604, Bee 731, Cobra 732, Chepa Warrior 727, Chepa Archer 728, Chepa officers 710/711 (the officers fight inside a grou…
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen *(name match)*: Kill messages ("X was destroyed") in quest order: Slime → Chepa Warrior / Chepa Archer (Training Ground circle, many killed for exp) → Bee, Cobra → Chepa Warri…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@8c | 112 |
| u8@91 | 15 |
| f32@c0 | 3.5 |
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
