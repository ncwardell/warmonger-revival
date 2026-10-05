---
title: "Reviatan Shadow"
type: "monster"
id: 678
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 678", "client: HeroData.cdb id 12 (hero transform of the same name)", "docs: [[gameplay/dungeon-drops]] (boss of field 126)", "docs: [[gameplay/maps-and-dungeons]] (boss of field 126)", "client: DungeonAdmission.cdb (rewards advertised by the dungeon, no rates)", "client: Quest.cdb kill objectives (quests 760, 1039)"]
name_key: "UnitName_678"
category: 6
class_mask: 1
kill_group: 10018
model: 74
model_name: "MOB_DemonLord_01"
model_path: "character/npc/monster/mob_demon/mob_demonlord_01.mo"
scale: 1.5
radius: 1
projectile: 853
sounds: [4070051, 4070051, 4070050, 4070050, 4070050, 4070052]
hero: 12
boss_of: [126]
dungeon_rewards:
  - {"field": 126, "items": [612, 613, 693, 694, 1935, 2707, 2757]}
quest_targets:
  - {"quest": 760, "need": 1, "group": 10018}
  - {"quest": 1039, "need": 1, "group": 10018}
spawn_fields: [126]
---
<!-- generated:start -->
<!-- generated-keys: title=245e76 type=9bbc46 id=b2029b sources=12917c name_key=f7953f category=c1dfd9 class_mask=356a19 kill_group=39b7a7 model=1f1362 model_name=1b7ed1 model_path=e1bf24 scale=aa8f28 radius=356a19 projectile=43d6ee sounds=bfd9b2 hero=7b5200 boss_of=d9b420 dungeon_rewards=c61337 quest_targets=fa745f spawn_fields=d9b420 -->
|  |  |
|---|---|
|  | ![Reviatan Shadow](../assets/monsters/678.png) |
| **Unit id** | `678` |
| **Category** | boss (inferred: every dungeon boss and quest bosses such as Tow Chief) (`category@8a` = 6) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10018` |
| **Model** | ObjectList `74` MOB_DemonLord_01 (`character/npc/monster/mob_demon/mob_demonlord_01.mo`) |
| **Scale** | 1.5 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 853 (archers carry one; meaning *inferred*) |
| **Hero transform** | Reviatan Shadow |
| **Boss of** | [[wiki/dungeons/126-lv-7-demon-hell\|(Lv 7) Demon Hell]] |

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

- [[wiki/quests/760-group-border-area-hard-mode|Group - Border Area Hard Mode]]: kill 1 in [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] — via kill group `10018` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1039-demon-hell-boss-hunting|Demon Hell : Boss Hunting]]: kill 1 in [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] — via kill group `10018` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] — boss ([[gameplay/dungeon-drops]], [[gameplay/maps-and-dungeons]]); quest map of [[wiki/quests/760-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/1039-demon-hell-boss-hunting|Demon Hell : Boss Hunting]]

### Dungeon rewards (advertised)

What the dungeon's entry window shows (`DungeonAdmission`). It is a list of possible rewards of the whole dungeon, not this boss's drop table, and has no rates.

- [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]]: [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/694-gem-stone-yellow|Gem Stone : Yellow]], [[wiki/items/1935-essence-of-light|Essence of Light]], [[wiki/items/2707-horn-of-leviathan|Horn of Leviathan]], [[wiki/items/2757-the-devil-commander-leviathan-s-sealed-weapon|The Devil commander Leviathan's Sealed Weapon]]

### Other units with this name

[[wiki/monsters/740-reviatan-shadow|Reviatan Shadow (740)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070051 | `Unit/UE4070051.wav` |
| 2 | 0 | 4070051 | `Unit/UE4070051.wav` |
| 3 | 977 | 4070050 | `Unit/UE4070050.wav` |
| 4 | 977 | 4070050 | `Unit/UE4070050.wav` |
| 5 | 0 | 4070050 | `Unit/UE4070050.wav` |
| 6 | 0 | 4070052 | `Unit/UE4070052.wav` |

### Seen in

- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 1. Per dungeon level: 7 · Hell of Demon → 126 "[Lv 7] Demon Hell" · Akasha/Reviathan → Reviatan Shadow 678 / 740, Commander Reviatan 739, Reviatan 972 · Diamond 810, Borage 826, Spa…
- [[gameplay/maps-and-dungeons|Maps and dungeons]] § 2. Border-area (normal/hard) dungeons: 7 · Demon Hell (*Hell of Demon*) · 126 · Reviatan Shadow (678/740; "Commander Reviatan" 739) · T2 · Diamond ×4, Spartium ×5, Borage ×3

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 9 |
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
