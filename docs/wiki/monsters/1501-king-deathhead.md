---
title: "King Deathhead"
type: "monster"
id: 1501
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 1501", "client: HeroData.cdb id 7 (hero transform of the same name)", "docs: [[gameplay/dungeon-drops]] (boss of field 121)", "client: DungeonAdmission.cdb (rewards advertised by the dungeon, no rates)"]
name_key: "UnitName_1501"
category: 1
class_mask: 1
model: 35
model_name: "MOB_Seleton King_01"
model_path: "character/npc/monster/mob_seleton king/mob_seleton king_01.mo"
scale: 2.5
radius: 1
sounds: [4070017, 4070017, 4070018]
hero: 7
boss_of: [121]
dungeon_rewards:
  - {"field": 121, "items": [601, 693, 1930, 2701, 2751]}
spawn_fields: [121]
---
<!-- generated:start -->
<!-- generated-keys: title=07072a type=9bbc46 id=0e55c1 sources=f182e2 name_key=d9f287 category=356a19 class_mask=356a19 model=972a67 model_name=0cf010 model_path=6a4c49 scale=555a5c radius=356a19 sounds=10cd19 hero=902ba3 boss_of=a5a5cb dungeon_rewards=56688c spawn_fields=a5a5cb -->
|  |  |
|---|---|
|  | ![King Deathhead](../assets/monsters/1501.png) |
| **Unit id** | `1501` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `35` MOB_Seleton King_01 (`character/npc/monster/mob_seleton king/mob_seleton king_01.mo`) |
| **Scale** | 2.5 (second scale / radius 1) |
| **Hero transform** | King Deathhead |
| **Boss of** | [[wiki/dungeons/121-lv-1-skull-temple\|(Lv 1) Skull Temple]] |

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

- [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]] — boss ([[gameplay/dungeon-drops]])

### Dungeon rewards (advertised)

What the dungeon's entry window shows (`DungeonAdmission`). It is a list of possible rewards of the whole dungeon, not this boss's drop table, and has no rates.

- [[wiki/dungeons/121-lv-1-skull-temple|(Lv 1) Skull Temple]]: [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1930-essence-of-darkness|essence of Darkness]], [[wiki/items/2701-deathhead-horn|DeathHead Horn]], [[wiki/items/2751-the-death-head-s-sealed-weapon|The Death Head's Sealed Weapon]]

### Other units with this name

[[wiki/monsters/672-king-deathhead|King Deathhead (672)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070017 | `Unit/UE4070017.wav` |
| 2 | 0 | 4070017 | `Unit/UE4070017.wav` |
| 6 | 0 | 4070018 | `Unit/UE4070018.wav` |

### Seen in

- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 1. Per dungeon level: 1 · Temple of the Skull → 121 "[Lv 1] Skull Temple" · Deathhead → King Deathhead 672; Tough King Deathhead 804; 1501 · Garnet 802, Red Bloodstone 812 · Blue Pa…
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 2. Where the sheet disagrees with the client *(name match)*: Boss names · Deathhead, Death Knight, Akasha/Reviathan · King Deathhead, Dark Knight Skull, Reviatan (Lv 7) / Akasha (Lv 8) · client

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 6.5 |
| f32@10c | 0.5 |
<!-- generated:end -->

## Notes

- Boss of [[wiki/dungeons/121-lv-1-skull-temple|[Lv 1] Skull Temple (121)]] (guides + client ids, [[gameplay/maps-and-dungeons]] §2; [[gameplay/dungeon-drops]] §1) — listed only by [[gameplay/dungeon-drops]]. Crush Online name: Deathhead (Crush Online sheet, *Temple of the Skull*, Lv 1) ([[gameplay/dungeon-drops]] §1–2; [[gameplay/crush-mechanics]] §9).
- That dungeon drops T1 named-set gear, already reinforced at a random level (+0 to +11 seen) (image + guide, [[gameplay/maps-and-dungeons]] §2).
- Other units with this boss's name: [[wiki/monsters/672-king-deathhead|672]], [[wiki/monsters/804-tough-king-deathhead|804]].
- Forum: the Lv 1–2 bosses (Deathhead, Death Knight) could be soloed with base gear and potions (forum, [[gameplay/warmonger-forum]] §3). Essence of Darkness "drops from the Tier 1 dungeon boss" (Crush forum, [[gameplay/dungeon-drops]] §1); in Warmonger the T1/T2 boss was shielded unless the nation held more than one fort on the channel (forum, [[gameplay/warmonger-forum]] §3).
- Warmonger patch 0809 added a **Death Head** boss set (3 bonus steps); the essences for these sets drop from fort guardians (notes, [[gameplay/patch-history]] § Items).

## Behaviour

- Drops: the dungeon entry panel advertises this dungeon's essence, horn and sealed weapon (client, front matter `dungeon_rewards`; no rates). Crush Online players said every boss (dungeon or world map) could drop every essence (player, [[gameplay/crush-mechanics]] §9). Warmonger patch 0920 raised boss-material drop rates from dungeon bosses and fort guardians (notes, [[gameplay/patch-history]] § Numbers pass (October 2026)).
- The forum says a dungeon boss only exists while the land is monster-invaded (forum, [[gameplay/warmonger-forum]] §3); in hard mode the boss waits at the end (guide, [[gameplay/maps-and-dungeons]] §2).
- Crush Online patch 2016-12-15: elites in boundary-area dungeons dropped a scroll that summoned one extra boss, once per boss; this boss's scroll is [[wiki/items/2585-the-death-head-s-pipe|The Death Head's Pipe (2585)]] in the client (staff + client, [[gameplay/crush-patch-notes]] § 2016-12-15).

## Sources

- [[gameplay/dungeon-drops]] §1–2, [[gameplay/maps-and-dungeons]] §2, [[gameplay/crush-mechanics]] §9, [[gameplay/warmonger-forum]] §3, [[gameplay/crush-patch-notes]] § 2016-12-15, [[gameplay/patch-history]]

## Open questions

- HP, level, damage, exp and drop rates: no source gives them. [[gameplay/sources]] §9 lists boss videos (Commander Reviatan solo, Komodo 5-man) that could give HP against damage numbers.
- The guides do not say which of this boss's unit ids is the normal-mode, hard-mode or field version.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
