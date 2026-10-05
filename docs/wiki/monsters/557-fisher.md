---
title: "Fisher"
type: "monster"
id: 557
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 557"]
name_key: "UnitName_557"
category: 8
class_mask: 1
model: 70
model_name: "MOB_fisher Boss_01"
model_path: "character/npc/monster/mob_fisher/mob_fisher boss_01.mo"
scale: 1
radius: 1
projectile: 774
sounds: [4070035, 4070035, 4070036, 4070036, 4070036, 4070037]
---
<!-- generated:start -->
<!-- generated-keys: title=3c5b25 type=9bbc46 id=859371 sources=5fba71 name_key=695f92 category=fe5dbb class_mask=356a19 model=b7103c model_name=df608e model_path=213684 scale=356a19 radius=356a19 projectile=66c4d1 sounds=d8fe26 -->
|  |  |
|---|---|
| **Unit id** | `557` |
| **Category** | field monster (inferred: ogres, trolls, bears, phytons) (`category@8a` = 8) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `70` MOB_fisher Boss_01 (`character/npc/monster/mob_fisher/mob_fisher boss_01.mo`) |
| **Scale** | 1 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 774 (archers carry one; meaning *inferred*) |

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

[[wiki/monsters/556-fisher|Fisher (556)]], [[wiki/monsters/560-fisher|Fisher (560)]], [[wiki/monsters/644-fisher|Fisher (644)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070035 | `Unit/UE4070035.wav` |
| 2 | 0 | 4070035 | `Unit/UE4070035.wav` |
| 3 | 770 | 4070036 | `Unit/UE4070036.wav` |
| 4 | 770 | 4070036 | `Unit/UE4070036.wav` |
| 5 | 0 | 4070036 | `Unit/UE4070036.wav` |
| 6 | 0 | 4070037 | `Unit/UE4070037.wav` |

### Seen in

- [[gameplay/patch-history|Patch notes and other sources]] § Items *(name match)*: Boss sets (Death Head, Skull, Fisher, Komodo, Spector, Garon, Fame Knight, Fame Warrior) with 3 bonus steps (WM 0809); essences for them drop from fort guardia…
- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]] § 6. Boss and fame set bonuses *(name match)*: Fisher (3, 3021–) · AP 30 · AP 40, MR Pen 20 · AP 60, MR Pen 30

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 6.5 |
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
