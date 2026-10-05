---
title: "Dark Knight Skull"
type: "monster"
id: 1205
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 1205", "client: HeroData.cdb id 1 (hero transform of the same name)", "docs: [[gameplay/dungeon-drops]] (boss of field 128)", "docs: [[gameplay/maps-and-dungeons]] (boss of field 128)", "client: DungeonAdmission.cdb (rewards advertised by the dungeon, no rates)"]
name_key: "UnitName_1205"
category: 6
class_mask: 1
model: 48
model_name: "MOB_Seleton King_02"
model_path: "character/npc/monster/mob_seleton king/mob_seleton king_02.mo"
scale: 2.5
radius: 1
sounds: [4070017, 4070017, 4070018]
hero: 1
boss_of: [128]
dungeon_rewards:
  - {"field": 128, "items": [611, 693, 1930, 2702, 2752]}
spawn_fields: [128]
---
<!-- generated:start -->
<!-- generated-keys: title=118473 type=9bbc46 id=b74e9c sources=7f9639 name_key=ceb327 category=c1dfd9 class_mask=356a19 model=64e095 model_name=de18f7 model_path=f4640e scale=555a5c radius=356a19 sounds=10cd19 hero=356a19 boss_of=c9e1d0 dungeon_rewards=781ba1 spawn_fields=c9e1d0 -->
|  |  |
|---|---|
|  | ![Dark Knight Skull](wiki/assets/monsters/1205.png) |
| **Unit id** | `1205` |
| **Category** | boss (inferred: every dungeon boss and quest bosses such as Tow Chief) (`category@8a` = 6) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `48` MOB_Seleton King_02 (`character/npc/monster/mob_seleton king/mob_seleton king_02.mo`) |
| **Scale** | 2.5 (second scale / radius 1) |
| **Hero transform** | Dark Knight Skull |
| **Boss of** | [[wiki/dungeons/128-lv-2-skull-cemetery\|(Lv 2) Skull Cemetery]] |

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

- [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]] — boss ([[gameplay/dungeon-drops]], [[gameplay/maps-and-dungeons]])

### Dungeon rewards (advertised)

What the dungeon's entry window shows (`DungeonAdmission`). It is a list of possible rewards of the whole dungeon, not this boss's drop table, and has no rates.

- [[wiki/dungeons/128-lv-2-skull-cemetery|(Lv 2) Skull Cemetery]]: [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1930-essence-of-darkness|essence of Darkness]], [[wiki/items/2702-skull-horn|Skull Horn]], [[wiki/items/2752-the-dark-knight-s-sealed-weapon|The Dark Knight.'s Sealed Weapon]]

### Other units with this name

[[wiki/monsters/673-dark-knight-skull|Dark Knight Skull (673)]], [[wiki/monsters/809-dark-knight-skull|Dark Knight Skull (809)]], [[wiki/monsters/1504-dark-knight-skull|Dark Knight Skull (1504)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070017 | `Unit/UE4070017.wav` |
| 2 | 0 | 4070017 | `Unit/UE4070017.wav` |
| 6 | 0 | 4070018 | `Unit/UE4070018.wav` |

### Seen in

- [[gameplay/maps-and-dungeons|Maps and dungeons]] § 2. Border-area (normal/hard) dungeons: 2 · Skull Cemetery (*Cemetery of the Skull*) · 128 · Dark Knight Skull (673/809/1205) · T1 · Blue Bloodstone, Topaz, Rosemary, Jasmine ×2 each
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 5. Notable items and skills *(name match)*: Transform stones "Sacred Power" (Crusader Cherubim) / "Wrath of the Knight" (Dark Knight Skull) · 5 Essence of Light or Darkness + 5 Brilliant spell stones (10…
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 9. Dungeons, bosses, farming *(name match)*: 2 · Cemetery of the Skull · Death Knight (Dark Knight Skull) · Topaz, Blue Bloodstone, Rosemary, Jasmine
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 12. Crush vs Warmonger: differences that matter for the server *(name match)*: [t254]: https://web.archive.org/web/20161022145703/http://www.crush-game.com/forum/threads/crusader-cherubim-dark-knight-skull-skill-stones.254/
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 1. Per dungeon level *(name match)*: "Death Knight" (sheet) is "Dark Knight Skull" in the client. The client's sealed weapon is also "Dark Knight". *client*
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 2. Where the sheet disagrees with the client *(name match)*: Boss names · Deathhead, Death Knight, Akasha/Reviathan · King Deathhead, Dark Knight Skull, Reviatan (Lv 7) / Akasha (Lv 8) · client
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § Hero form (Dark Knight Skull) *(name match)*: Hero · Dark Knight Skull: the new R skill is Heaven and Earth 20006, which is weapon 69 (item 8000 "Dark knight Skull"; HeroData 1). Hero skills on that weapon…
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § Hero form (Dark Knight Skull) *(name match)*: Client values for Dark Knight Skull · HeroData stat1 1,204, stat2 756, hp 10,890, mp 3,010. The observed max is not base + these values (7,282 + 10,890 ≠ 16,21…

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
