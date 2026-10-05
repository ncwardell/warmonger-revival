---
title: "War Chief Garon"
type: "monster"
id: 1223
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 1223", "client: HeroData.cdb id 11 (hero transform of the same name)", "docs: [[gameplay/dungeon-drops]] (boss of field 125)", "docs: [[gameplay/maps-and-dungeons]] (boss of field 125)", "client: DungeonAdmission.cdb (rewards advertised by the dungeon, no rates)"]
name_key: "UnitName_1223"
category: 6
class_mask: 1
model: 97
model_name: "MOB_Orc_Lord_01"
model_path: "character/npc/monster/mob_orc/mob_orc_lord_01.mo"
scale: 1.5
radius: 1
sounds: [4070074, 4070074, 4070004, 4070004, 4070004, 4070069]
hero: 11
boss_of: [125]
dungeon_rewards:
  - {"field": 125, "items": [602, 693, 1935, 2706, 2756]}
spawn_fields: [125]
---
<!-- generated:start -->
<!-- generated-keys: title=722f70 type=9bbc46 id=297beb sources=074442 name_key=3ea8aa category=c1dfd9 class_mask=356a19 model=812ed4 model_name=0a9fa7 model_path=d78802 scale=aa8f28 radius=356a19 sounds=3e1d7f hero=17ba07 boss_of=896837 dungeon_rewards=097645 spawn_fields=896837 -->
|  |  |
|---|---|
|  | ![War Chief Garon](wiki/assets/monsters/1223.png) |
| **Unit id** | `1223` |
| **Category** | boss (inferred: every dungeon boss and quest bosses such as Tow Chief) (`category@8a` = 6) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `97` MOB_Orc_Lord_01 (`character/npc/monster/mob_orc/mob_orc_lord_01.mo`) |
| **Scale** | 1.5 (second scale / radius 1) |
| **Hero transform** | War Chief Garon |
| **Boss of** | [[wiki/dungeons/125-lv-5-tow-canyon\|(Lv 5) Tow Canyon]] |

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

- [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]] — boss ([[gameplay/dungeon-drops]], [[gameplay/maps-and-dungeons]])

### Dungeon rewards (advertised)

What the dungeon's entry window shows (`DungeonAdmission`). It is a list of possible rewards of the whole dungeon, not this boss's drop table, and has no rates.

- [[wiki/dungeons/125-lv-5-tow-canyon|(Lv 5) Tow Canyon]]: [[wiki/items/602-blue-passion-piece-d|Blue Passion Piece (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1935-essence-of-light|Essence of Light]], [[wiki/items/2706-horn-of-garon|Horn of Garon]], [[wiki/items/2756-the-war-hammer-garon-s-sealed-weapon|The War hammer Garon's Sealed Weapon]]

### Other units with this name

[[wiki/monsters/677-war-chief-garon|War Chief Garon (677)]], [[wiki/monsters/822-war-chief-garon|War Chief Garon (822)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070074 | `Unit/UE4070074.wav` |
| 2 | 0 | 4070074 | `Unit/UE4070074.wav` |
| 3 | 926 | 4070004 | `Unit/UE4070004.wav` |
| 4 | 926 | 4070004 | `Unit/UE4070004.wav` |
| 5 | 0 | 4070004 | `Unit/UE4070004.wav` |
| 6 | 0 | 4070069 | `Unit/UE4070069.wav` |

### Seen in

- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 1. Per dungeon level: 6 *(client: 5)* · Canyon of Tow → 125 "[Lv 5] Tow Canyon" · War chief Garon → War Chief Garon 677; 822, 1223 · Emerald 806, Rosemary 822, Jasmine 824 · 602, 69…
- [[gameplay/maps-and-dungeons|Maps and dungeons]] § 2. Border-area (normal/hard) dungeons: 5 · Tow Canyon (*Canyon of Tow*) · 125 · War Chief Garon (677/822/1223) · T2 · Emerald ×4, Rosemary ×5, Jasmine ×3
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 9. Dungeons, bosses, farming *(name match)*: 6 · Canyon of Tow · War Chief Garon · Emerald, Rosemary, Jasmine
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 12. Crush vs Warmonger: differences that matter for the server *(name match)*: [t402]: https://web.archive.org/web/20161026230614/http://www.crush-game.com/forum/threads/war-chief-garon-great-summoner-spectre-quests.402/

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
