---
title: "Tough Elite Tow Sorcerer"
type: "monster"
id: 821
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 821", "docs: [[gameplay/dungeon-drops]] (boss of field 820)"]
name_key: "UnitName_821"
category: 3
class_mask: 1
model: 18
model_name: "MOB_Orc_Wizard_0_1_0_00_00"
model_path: "character/npc/monster/mob_orc/mob_orc_wizard.mo"
scale: 1.7
radius: 1
projectile: 642
sounds: [4070111, 4070111, 4070012, 4070012, 4070012, 4070011]
boss_of: [820]
spawn_fields: [820]
---
<!-- generated:start -->
<!-- generated-keys: title=20fc5a type=9bbc46 id=fbbf19 sources=f5e3aa name_key=45c146 category=77de68 class_mask=356a19 model=9e6a55 model_name=beb51d model_path=07c67e scale=58e6d3 radius=356a19 projectile=99316d sounds=ab3b33 boss_of=3fab9c spawn_fields=3fab9c -->
|  |  |
|---|---|
| **Unit id** | `821` |
| **Category** | elite / named variant (inferred) (`category@8a` = 3) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `18` MOB_Orc_Wizard_0_1_0_00_00 (`character/npc/monster/mob_orc/mob_orc_wizard.mo`) |
| **Scale** | 1.7 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 642 (archers carry one; meaning *inferred*) |
| **Boss of** | Field 820 |

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

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- Field 820 — boss ([[gameplay/dungeon-drops]])

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070111 | `Unit/UE4070111.wav` |
| 2 | 0 | 4070111 | `Unit/UE4070111.wav` |
| 3 | 926 | 4070012 | `Unit/UE4070012.wav` |
| 4 | 926 | 4070012 | `Unit/UE4070012.wav` |
| 5 | 0 | 4070012 | `Unit/UE4070012.wav` |
| 6 | 0 | 4070011 | `Unit/UE4070011.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 4 |
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
