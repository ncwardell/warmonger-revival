---
title: "Reviatan"
type: "monster"
id: 972
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 972", "docs: [[gameplay/dungeon-drops]] (boss of field 126)", "client: DungeonAdmission.cdb (rewards advertised by the dungeon, no rates)"]
name_key: "UnitName_972"
category: 6
class_mask: 1
model: 74
model_name: "MOB_DemonLord_01"
model_path: "character/npc/monster/mob_demon/mob_demonlord_01.mo"
scale: 1.5
radius: 1
projectile: 853
sounds: [4070050, 4070050, 4070051, 4070051, 4070051, 4070052]
boss_of: [126]
dungeon_rewards:
  - {"field": 126, "items": [612, 613, 693, 694, 1935, 2707, 2757]}
spawn_fields: [126]
---
<!-- generated:start -->
<!-- generated-keys: title=ae9dbb type=9bbc46 id=5a14ec sources=21f93c name_key=d666ba category=c1dfd9 class_mask=356a19 model=1f1362 model_name=1b7ed1 model_path=e1bf24 scale=aa8f28 radius=356a19 projectile=43d6ee sounds=cc9343 boss_of=d9b420 dungeon_rewards=c61337 spawn_fields=d9b420 -->
|  |  |
|---|---|
| **Unit id** | `972` |
| **Category** | boss (inferred: every dungeon boss and quest bosses such as Tow Chief) (`category@8a` = 6) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `74` MOB_DemonLord_01 (`character/npc/monster/mob_demon/mob_demonlord_01.mo`) |
| **Scale** | 1.5 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 853 (archers carry one; meaning *inferred*) |
| **Boss of** | [[wiki/dungeons/126-lv-7-demon-hell\|(Lv 7) Demon Hell]] |

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

- [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] — boss ([[gameplay/dungeon-drops]])

### Dungeon rewards (advertised)

What the dungeon's entry window shows (`DungeonAdmission`). It is a list of possible rewards of the whole dungeon, not this boss's drop table, and has no rates.

- [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]]: [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/694-gem-stone-yellow|Gem Stone : Yellow]], [[wiki/items/1935-essence-of-light|Essence of Light]], [[wiki/items/2707-horn-of-leviathan|Horn of Leviathan]], [[wiki/items/2757-the-devil-commander-leviathan-s-sealed-weapon|The Devil commander Leviathan's Sealed Weapon]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070050 | `Unit/UE4070050.wav` |
| 2 | 0 | 4070050 | `Unit/UE4070050.wav` |
| 3 | 977 | 4070051 | `Unit/UE4070051.wav` |
| 4 | 977 | 4070051 | `Unit/UE4070051.wav` |
| 5 | 0 | 4070051 | `Unit/UE4070051.wav` |
| 6 | 0 | 4070052 | `Unit/UE4070052.wav` |

### Seen in

- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 1. Per dungeon level: 7 · Hell of Demon → 126 "[Lv 7] Demon Hell" · Akasha/Reviathan → Reviatan Shadow 678 / 740, Commander Reviatan 739, Reviatan 972 · Diamond 810, Borage 826, Spa…
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 2. Where the sheet disagrees with the client *(name match)*: Boss names · Deathhead, Death Knight, Akasha/Reviathan · King Deathhead, Dark Knight Skull, Reviatan (Lv 7) / Akasha (Lv 8) · client
- [[gameplay/sources|Sources and gaps]] § 9. What is still missing *(name match)*: 1 · Monster stats: HP, level, attack, armour, MR, move and attack speed per UnitDB id. The client has none (see spec/monsters). Only fragments are known: nexus…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@8c | 102 |
| u8@91 | 15 |
| f32@c0 | 9 |
| f32@10c | 0.5 |
<!-- generated:end -->

## Notes

- Boss of [[wiki/dungeons/126-lv-7-demon-hell|[Lv 7] Demon Hell (126)]] (guides + client ids, [[gameplay/maps-and-dungeons]] §2; [[gameplay/dungeon-drops]] §1) — "Reviatan", listed only by [[gameplay/dungeon-drops]]. Crush Online name: Akasha/Reviathan (Crush Online sheet, listed for both Lv 7 and Lv 8; the forum says Akasha / Leviathan); the client's rewards for this dungeon show Leviathan's horn and sealed weapon ([[gameplay/dungeon-drops]] §1–2; [[gameplay/crush-mechanics]] §9).
- That dungeon drops T2 named-set gear, already reinforced at a random level (+0 to +11 seen) (image + guide, [[gameplay/maps-and-dungeons]] §2).
- Other units with this boss's name: [[wiki/monsters/678-reviatan-shadow|678]], [[wiki/monsters/740-reviatan-shadow|740]], [[wiki/monsters/739-commander-reviatan|739]].
- The dungeons guide shows the Demon Hell boss as **two** identical figures (a multi-boss fight); the PvE text of the Remote Bomb TP skill ("attacks all bosses after attacking the middle boss") fits (image, [[gameplay/maps-and-dungeons]] §2).

## Behaviour

- Drops: the dungeon entry panel advertises this dungeon's essence, horn and sealed weapon (client, front matter `dungeon_rewards`; no rates). Crush Online players said every boss (dungeon or world map) could drop every essence (player, [[gameplay/crush-mechanics]] §9). Warmonger patch 0920 raised boss-material drop rates from dungeon bosses and fort guardians (notes, [[gameplay/patch-history]] § Numbers pass (October 2026)).
- The forum says a dungeon boss only exists while the land is monster-invaded (forum, [[gameplay/warmonger-forum]] §3); in hard mode the boss waits at the end (guide, [[gameplay/maps-and-dungeons]] §2).
- Crush Online patch 2016-12-15 let dungeon elites drop a scroll that summoned one extra boss, once per boss (this boss is on the list); the client's summon items 2585–2589 do not include one for it (staff + client, [[gameplay/crush-patch-notes]] § 2016-12-15).

## Sources

- [[gameplay/dungeon-drops]] §1–2, [[gameplay/maps-and-dungeons]] §2, [[gameplay/crush-mechanics]] §9, [[gameplay/warmonger-forum]] §3, [[gameplay/crush-patch-notes]] § 2016-12-15, [[gameplay/patch-history]]

## Open questions

- HP, level, damage, exp and drop rates: no source gives them. [[gameplay/sources]] §9 lists boss videos (Commander Reviatan solo, Komodo 5-man) that could give HP against damage numbers.
- The guides do not say which of this boss's unit ids is the normal-mode, hard-mode or field version.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
