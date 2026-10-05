---
title: "Golem"
type: "monster"
id: 618
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 618"]
name_key: "UnitName_618"
category: 8
class_mask: 1
model: 63
model_name: "MOB_Golem_Brimstone_01"
model_path: "character/npc/monster/mob_golem/mob_golem_01.mo"
scale: 1
radius: 1
sounds: [4070112, 4070112, 4070010, 4070010, 4070010, 4070119]
---
<!-- generated:start -->
<!-- generated-keys: title=ce691b type=9bbc46 id=ff6d1d sources=c156b0 name_key=c137eb category=fe5dbb class_mask=356a19 model=a17554 model_name=dde77f model_path=ed16ce scale=356a19 radius=356a19 sounds=f39c5f -->
|  |  |
|---|---|
| **Unit id** | `618` |
| **Category** | field monster (inferred: ogres, trolls, bears, phytons) (`category@8a` = 8) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `63` MOB_Golem_Brimstone_01 (`character/npc/monster/mob_golem/mob_golem_01.mo`) |
| **Scale** | 1 (second scale / radius 1) |

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

[[wiki/monsters/616-golem|Golem (616)]], [[wiki/monsters/628-golem|Golem (628)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070112 | `Unit/UE4070112.wav` |
| 2 | 0 | 4070112 | `Unit/UE4070112.wav` |
| 3 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 4 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 5 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 6 | 0 | 4070119 | `Unit/UE4070119.wav` |

### Seen in

- [[gameplay/consumables|Consumables and clickables]] § 1. Rules that apply to every clickable *(name match)*: 1150 · Transform · Golem, Demon, Slime, Jack

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@8c | 105 |
| u8@91 | 15 |
| f32@c0 | 4.3 |
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
