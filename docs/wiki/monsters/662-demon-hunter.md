---
title: "Demon Hunter"
type: "monster"
id: 662
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 662", "client: Quest.cdb kill objectives (quests 35, 743, 1036)"]
name_key: "UnitName_662"
category: 1
class_mask: 1
kill_group: 10031
model: 95
model_name: "MOB_Demon_01"
model_path: "character/npc/monster/mob_demon/mob_demon_01.mo"
scale: 1.3
radius: 1
projectile: 853
sounds: [4070068, 4070068, 4070066, 4070066, 4070066]
quest_targets:
  - {"quest": 35, "need": 1, "group": 10031}
  - {"quest": 743, "need": 10, "group": 10031}
  - {"quest": 1036, "need": 10, "group": 10031}
quest_drops:
  - {"quest": 35, "item": 2582, "rate": 10, "need": 1}
  - {"quest": 743, "item": 2574, "rate": 70, "need": 10}
  - {"quest": 1036, "item": 2674, "rate": 70, "need": 10}
spawn_fields: [126]
---
<!-- generated:start -->
<!-- generated-keys: title=6973ac type=9bbc46 id=091d03 sources=97d604 name_key=9ce9e3 category=356a19 class_mask=356a19 kill_group=466b50 model=8e63fd model_name=b1dcd3 model_path=6bdcd6 scale=2afe7d radius=356a19 projectile=43d6ee sounds=bf9feb quest_targets=faf92b quest_drops=6d712f spawn_fields=d9b420 -->
|  |  |
|---|---|
| **Unit id** | `662` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10031` |
| **Model** | ObjectList `95` MOB_Demon_01 (`character/npc/monster/mob_demon/mob_demon_01.mo`) |
| **Scale** | 1.3 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 853 (archers carry one; meaning *inferred*) |

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

- [[wiki/quests/35-demon-hell|Demon Hell]]: collect 1 × [[wiki/items/2582-innocence-piece|Innocence Piece]] (drops at 10% while the quest is active) in [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] — via kill group `10031` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/743-demon-hell|Demon Hell]]: collect 10 × [[wiki/items/2574-unknown-crystal|Unknown Crystal]] (drops at 70% while the quest is active) in [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] — via kill group `10031` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1036-demon-hell-hunting|Demon Hell : Hunting]]: collect 10 × [[wiki/items/2674-unknown-crystal|Unknown Crystal]] (drops at 70% while the quest is active) in [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] — via kill group `10031` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] — quest map of [[wiki/quests/35-demon-hell|Demon Hell]], [[wiki/quests/743-demon-hell|Demon Hell]], [[wiki/quests/1036-demon-hell-hunting|Demon Hell : Hunting]]

### Other units with this name

[[wiki/monsters/679-demon-hunter|Demon Hunter (679)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070068 | `Unit/UE4070068.wav` |
| 2 | 0 | 4070068 | `Unit/UE4070068.wav` |
| 3 | 0 | 4070066 | `Unit/UE4070066.wav` |
| 4 | 0 | 4070066 | `Unit/UE4070066.wav` |
| 5 | 0 | 4070066 | `Unit/UE4070066.wav` |

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 6 |
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
