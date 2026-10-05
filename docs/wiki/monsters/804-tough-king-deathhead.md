---
title: "Tough King Deathhead"
type: "monster"
id: 804
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 804", "docs: [[gameplay/dungeon-drops]] (boss of field 121)", "docs: [[gameplay/maps-and-dungeons]] (boss of field 121)", "client: DungeonAdmission.cdb (rewards advertised by the dungeon, no rates)"]
name_key: "UnitName_804"
category: 6
class_mask: 1
model: 35
model_name: "MOB_Seleton King_01"
model_path: "character/npc/monster/mob_seleton king/mob_seleton king_01.mo"
scale: 2.5
radius: 1
sounds: [4070017, 4070017, 4070018]
boss_of: [121]
dungeon_rewards:
  - {"field": 121, "items": [601, 693, 1930, 2701, 2751]}
spawn_fields: [121]
---
<!-- generated:start -->
<!-- generated-keys: title=666c0d type=9bbc46 id=43a784 sources=08ad82 name_key=23e3ac category=c1dfd9 class_mask=356a19 model=972a67 model_name=0cf010 model_path=6a4c49 scale=555a5c radius=356a19 sounds=10cd19 boss_of=a5a5cb dungeon_rewards=56688c spawn_fields=a5a5cb -->
|  |  |
|---|---|
| **Unit id** | `804` |
| **Category** | boss (inferred: every dungeon boss and quest bosses such as Tow Chief) (`category@8a` = 6) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `35` MOB_Seleton King_01 (`character/npc/monster/mob_seleton king/mob_seleton king_01.mo`) |
| **Scale** | 2.5 (second scale / radius 1) |
| **Boss of** | [[wiki/dungeons/121-lv-1-skull-temple\|(Lv 1) Skull Temple]] |

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

- [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] — boss ([[gameplay/dungeon-drops]], [[gameplay/maps-and-dungeons]])

### Dungeon rewards (advertised)

What the dungeon's entry window shows (`DungeonAdmission`). It is a list of possible rewards of the whole dungeon, not this boss's drop table, and has no rates.

- [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]]: [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1930-essence-of-darkness|essence of Darkness]], [[wiki/items/2701-deathhead-horn|DeathHead Horn]], [[wiki/items/2751-the-death-head-s-sealed-weapon|The Death Head's Sealed Weapon]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070017 | `Unit/UE4070017.wav` |
| 2 | 0 | 4070017 | `Unit/UE4070017.wav` |
| 6 | 0 | 4070018 | `Unit/UE4070018.wav` |

### Seen in

- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 1. Per dungeon level: 1 · Temple of the Skull → 121 "[Lv 1] Skull Temple" · Deathhead → King Deathhead 672; Tough King Deathhead 804; 1501 · Garnet 802, Red Bloodstone 812 · Blue Pa…

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
